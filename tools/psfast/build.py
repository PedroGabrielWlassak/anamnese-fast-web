#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PS Fast — gerador único.
Fonte da verdade = lista CONDITIONS (doses verbatim do material do usuário).
Emite: recursos/ps-fast.md, recursos/data-prescricoes.js e recursos/ps-fast.pdf
Limpa artefatos de formatação; NÃO altera doses; marca flags para revisão.
"""
import re, json, os, html

OUT = "/Users/pedrowlassak/Documents/Anamnese Fast Web/recursos"

# ---- Blocos crânio-caudal (ordem + rótulo) ----
BLOCKS = [
    ("GERAL",  "🚨 Geral / Crítico",     "Sintomáticos · Sepse · Anafilaxia · Intoxicação · Arboviroses · Acidentes · Procedimentos"),
    ("NEURO",  "🧠 Cabeça / Neuro",       "Cefaleia · Enxaqueca · AVC · Convulsão · Meningite · Vertigem · Neuralgias"),
    ("OLHOS",  "👁 Olhos",                "Conjuntivite · Calázio · Celulite periorbitária · Neurite · Herpes ocular"),
    ("ORL",    "👂 Otorrino",             "IVAS · Amigdalite · Sinusite · Otite · Otalgia · Rinite · Cerume"),
    ("TORAX",  "🫁 Tórax / Cardio-Pneumo","Asma · DPOC · Pneumonia · IAM · ICC · EAP · Arritmias · TVP · Dor torácica · Elevação PA"),
    ("ABDOME", "🫃 Abdome / Gastro",      "GECA · DRGE · Hemorroida · Cólica biliar · Pancreatite · Apendicite · HDA"),
    ("METAB",  "🩸 Renal / Endócrino / Metabólico","Hiper/hipoglicemia · Distúrbios HE · CAD · EHH · Rabdomiólise"),
    ("HEMATO", "💉 Hematologia",          "Anemias · Epistaxe · Neutropenia febril · Crise falcêmica · Transfusão"),
    ("MSK",    "🦴 MSK / Reumato / Orto", "Lombalgia · Gota · Entorse · Fasciíte · Osteoartrite · IVC"),
    ("GU",     "🌸 Genitourinário / Gineco","Cistite · Pielonefrite · Cólica nefrética · SUA · Vaginites · ISTs · Climatério"),
    ("PELE",   "🧴 Pele",                 "Alergia · Abscesso · Tínea · Escabiose · Herpes · Queimadura · Erisipela · Feridas"),
    ("PSIQ",   "🧠 Psiquiatria",          "Abstinência alcoólica"),
    ("GEST",   "🤰 Gestante",             "Prescrições por sistema na gestação · o que NÃO usar"),
    ("BONUS",  "📝 Modelos / Bônus",      "Templates · Exame físico · Conduta · Medicações IM/EV · Bulário · IOT · Internação"),
    ("FARM",   "💊 Formulário SUS",       "Medicamentos disponíveis na rede (A–Z) e onde retirar"),
]
BLOCK_ORDER = {b[0]: i for i, b in enumerate(BLOCKS)}
DEST_ORDER = {"ps": 0, "casa": 1, "internacao": 2, "outro": 3}
DEST_LABEL = {"ps": "💉 PS / Sala", "casa": "🏠 Casa", "internacao": "🏥 Internação", "outro": "📄 Modelo"}

def slug(s):
    s = s.lower()
    for a, b in [("á","a"),("à","a"),("ã","a"),("â","a"),("é","e"),("ê","e"),
                 ("í","i"),("ó","o"),("ô","o"),("õ","o"),("ú","u"),("ç","c")]:
        s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:70]

def scenarios_from_text(text):
    """Divide um bloco de texto em cenários (separados por 'OU' / linha em branco).
    Cada cenário = linhas juntas com \\n. Não altera conteúdo."""
    text = text.strip("\n")
    if not text.strip():
        return []
    # normaliza separador OU isolado
    chunks = re.split(r"\n\s*OU\s*\n", text)
    scen = []
    for ch in chunks:
        lines = [ln.rstrip() for ln in ch.split("\n")]
        # remove linhas vazias das pontas
        while lines and not lines[0].strip(): lines.pop(0)
        while lines and not lines[-1].strip(): lines.pop()
        if not lines: continue
        model = "\n".join(l.strip() for l in lines if l.strip())
        scen.append({"header": "", "alternatives": [], "model_full": model,
                     "model_meds": model, "n_items": len([l for l in lines if l.strip()])})
    return scen

CONDITIONS = []
def C(**kw):
    CONDITIONS.append(kw)

# ============================================================
# CONDITIONS incluídas em arquivos separados (conditions_*.py)
# via exec para manter o build.py enxuto.
# ============================================================
import glob
_here = os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(os.path.join(_here, "conditions_*.py"))):
    with open(f, encoding="utf-8") as fh:
        code = fh.read()
    exec(compile(code, f, "exec"), globals())

# ============================================================
# BUILD TOPICS
# ============================================================
def build_topics():
    topics = []
    for c in CONDITIONS:
        rx = []
        for r in c.get("rx", []):
            scen = scenarios_from_text(r["text"])
            if not scen and not r.get("label"):
                continue
            rx.append({"title": r.get("label") or {"ps":"Prescrição — PS","casa":"Prescrição — Casa",
                        "internacao":"Prescrição — Internação","outro":"Modelo"}[r["dest"]],
                       "dest": r["dest"], "page": None, "explanation": "", "scenarios": scen})
        tid = f'{c["block"].lower()}-{slug(c["title"])}'
        topics.append({
            "id": tid, "title": c["title"], "cid": c.get("cid",""),
            "block": c["block"], "severity": c.get("sev","verde"),
            "source": "psfast", "page": None,
            "summary": c.get("nota",""), "explanation": c.get("nota",""),
            "alarmes": c.get("alarmes",""), "anamnese": c.get("anamnese",""),
            "exame": c.get("exame",""), "retorno": c.get("retorno",""),
            "flags": c.get("flags",[]),
            "rx": rx,
        })
    topics.sort(key=lambda t: (BLOCK_ORDER.get(t["block"],99), t["title"].lower()))
    return topics

def group_blocks(topics):
    by = {}; grouped = []
    for b in BLOCKS:
        by[b[0]] = {"id": b[0], "title": b[1], "subtitle": b[2], "topics": []}
        grouped.append(by[b[0]])
    for t in topics:
        by[t["block"]]["topics"].append(t)
    return [g for g in grouped if g["topics"]]

def emit_js(grouped, topics):
    counts = {
        "total": len(topics),
        "vermelha": sum(1 for t in topics if t["severity"]=="vermelha"),
        "amarela": sum(1 for t in topics if t["severity"]=="amarela"),
        "verde": sum(1 for t in topics if t["severity"]=="verde"),
        "with_model": sum(1 for t in topics if any(r["scenarios"] for r in t["rx"])),
    }
    data = {"title":"Prescrição PS Fast","source":"PS Fast · material próprio",
            "pdf":"recursos/ps-fast.pdf","blocks":grouped,"counts":counts}
    with open(os.path.join(OUT,"data-prescricoes.js"),"w",encoding="utf-8") as f:
        f.write("window.PRESCRICOES=")
        json.dump(data, f, ensure_ascii=False, separators=(",",":"))
        f.write(";")
    return counts

def emit_md(grouped):
    L = ["# Prescrição PS Fast",
         "",
         "> Receitas prontas para PS / APS. **Lembrar: alergias · AINE → rim · corticoide → HAS e DM.**",
         "> Doses são ponto de partida adulto — validar peso, função renal/hepática, gestação e protocolo local.",
         ""]
    for g in grouped:
        L.append(f"\n## {g['title']}\n")
        for t in g["topics"]:
            L.append(f"### {t['title']}" + (f"  ·  CID {t['cid']}" if t['cid'] else ""))
            if t["alarmes"]: L.append(f"\n🚩 **Alarme:** {t['alarmes']}")
            if t["anamnese"]:
                L.append("\n**📋 Anamnese**\n```\n"+t["anamnese"]+"\n```")
            if t["exame"]:
                L.append("\n**🩺 Exame físico**\n```\n"+t["exame"]+"\n```")
            for r in sorted(t["rx"], key=lambda x: DEST_ORDER.get(x["dest"],3)):
                L.append(f"\n**{DEST_LABEL.get(r['dest'],'')} — {r['title']}**")
                for i, s in enumerate(r["scenarios"]):
                    if i>0: L.append("\n_OU_")
                    L.append("```\n"+s["model_full"]+"\n```")
            if t["summary"]: L.append(f"\n💡 {t['summary']}")
            for fl in t["flags"]:
                L.append(f"\n<!-- FLAG: {fl} -->")
            L.append("")
    with open(os.path.join(OUT,"ps-fast.md"),"w",encoding="utf-8") as f:
        f.write("\n".join(L)+"\n")

def emit_pdf(grouped):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.lib import colors
        from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                        Preformatted, Table, TableStyle, PageBreak)
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    except ImportError:
        print("reportlab ausente — pulando PDF"); return False
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontSize=15, spaceAfter=6, textColor=colors.HexColor("#0d6b6b"))
    h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=12, spaceBefore=8, spaceAfter=3, textColor=colors.HexColor("#0a8f8f"))
    hcond = ParagraphStyle("hc", parent=styles["Heading3"], fontSize=10.5, spaceBefore=8, spaceAfter=2, textColor=colors.HexColor("#111827"))
    alarm = ParagraphStyle("al", parent=styles["Normal"], fontSize=8, textColor=colors.HexColor("#b91c1c"), spaceAfter=2, leading=10)
    desth = ParagraphStyle("dh", parent=styles["Normal"], fontSize=8, textColor=colors.HexColor("#b45309"), spaceBefore=3, spaceAfter=1, leading=10)
    mono = ParagraphStyle("mono", parent=styles["Code"], fontSize=8, leading=10, textColor=colors.HexColor("#0f172a"))
    note = ParagraphStyle("nt", parent=styles["Normal"], fontSize=7.5, textColor=colors.HexColor("#475569"), leading=9, spaceBefore=2)
    intro = ParagraphStyle("in", parent=styles["Normal"], fontSize=8, textColor=colors.HexColor("#475569"), leading=10)

    doc = SimpleDocTemplate(os.path.join(OUT,"ps-fast.pdf"), pagesize=A4,
                            leftMargin=14*mm, rightMargin=14*mm, topMargin=12*mm, bottomMargin=12*mm,
                            title="Prescrição PS Fast")
    el = [Paragraph("Prescrição PS Fast", h1),
          Paragraph("Receitas prontas para PS / APS. Lembrar: alergias · AINE → rim · corticoide → HAS e DM. "
                    "Doses = ponto de partida adulto; validar peso, função renal/hepática, gestação e protocolo local.", intro),
          Spacer(1, 4)]
    def esc(s): return html.escape(s).replace("\n","<br/>")
    for g in grouped:
        el.append(Paragraph(g["title"], h2))
        for t in g["topics"]:
            block = [Paragraph(esc(t["title"]) + (f' &nbsp;·&nbsp; <font size=7 color="#64748b">CID {esc(t["cid"])}</font>' if t["cid"] else ""), hcond)]
            if t["alarmes"]:
                block.append(Paragraph("🚩 " + esc(t["alarmes"]), alarm))
            if t["anamnese"]:
                block.append(Paragraph("<b>Anamnese</b>", desth))
                block.append(Preformatted(t["anamnese"], mono))
            if t["exame"]:
                block.append(Paragraph("<b>Exame físico</b>", desth))
                block.append(Preformatted(t["exame"], mono))
            for r in sorted(t["rx"], key=lambda x: DEST_ORDER.get(x["dest"],3)):
                block.append(Paragraph(esc(DEST_LABEL.get(r["dest"],"")) + " — " + esc(r["title"]), desth))
                for i, s in enumerate(r["scenarios"]):
                    prefix = "OU  " if i>0 else ""
                    block.append(Preformatted(prefix + s["model_full"], mono))
            if t["summary"]:
                block.append(Paragraph("💡 " + esc(t["summary"]), note))
            el.append(Table([[block]], colWidths=[182*mm],
                       style=TableStyle([("BOX",(0,0),(-1,-1),0.4,colors.HexColor("#e2e8f0")),
                                         ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
                                         ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),6),
                                         ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#ffffff"))])))
            el.append(Spacer(1,3))
    doc.build(el)
    return True

if __name__ == "__main__":
    topics = build_topics()
    grouped = group_blocks(topics)
    counts = emit_js(grouped, topics)
    emit_md(grouped)
    pdf_ok = emit_pdf(grouped)
    print(f"Condições: {counts['total']}  (🔴{counts['vermelha']} 🟡{counts['amarela']} 🟢{counts['verde']})  modelo:{counts['with_model']}")
    for g in grouped:
        print(f"  {g['title']}: {len(g['topics'])}")
    print("PDF:", "ok" if pdf_ok else "FALHOU")
    # flag report
    nfl = sum(len(t.get('flags',[])) for t in topics)
    print(f"Flags: {nfl}")
