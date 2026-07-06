# -*- coding: utf-8 -*-
# RECEITAS PRONTAS PRA CASA (aba do site) — parse cru e leve.
# Doses VERBATIM. Limpa apenas artefatos/typos de grafia; corrige CID errado óbvio.
import os, re

_src = os.path.join(_here, "sources", "receitas_casa.txt")
_raw = open(_src, encoding="utf-8").read() if os.path.exists(_src) else ""

def _n(s):
    s = (s or "").lower()
    for a, b in [("á","a"),("à","a"),("ã","a"),("â","a"),("é","e"),("ê","e"),
                 ("í","i"),("ó","o"),("ô","o"),("õ","o"),("ú","u"),("ç","c")]:
        s = s.replace(a, b)
    return s

# ---- typos de grafia (NUNCA dose) — aplicados linha a linha ----
_TYPOS = [
    ("BUSCOPAM","BUSCOPAN"),("Buscopam","Buscopan"),
    ("ONDANSENTRONA","ONDANSETRONA"),("Ondansentrona","Ondansetrona"),
    ("AOD IA","AO DIA"),("8/H8","8/8"),("TOMAR O1 ","TOMAR 01 "),
    ("HIDROXIDIDO","HIDRÓXIDO"),("REFECIÇÕES","REFEIÇÕES"),
    ("HIDROCORTICONA","HIDROCORTISONA"),
    ("OFTAMOLÓGICO","OFTALMOLÓGICO"),("OFTAMOLOGICO","OFTALMOLOGICO"),
    ("COIDEÍNA","CODEÍNA"),
    ("AMIGLDALITE","AMIGDALITE"),("Amigldalite","Amigdalite"),
    ("agua+sábado","água + sabão"),("clorezidina","clorexidina"),
    ("ACETILCEFUROXIMA","AXETILCEFUROXIMA"),("Acetilcefuroxima","Axetilcefuroxima"),
    ("TRIGÊMIO","TRIGÊMEO"),("Trigêmio","Trigêmeo"),
    ("SUBGAGUDA","SUBAGUDA"),("Subgaguda","Subaguda"),
    ("não melhorara","não melhorar"),
    ("Pulmãoj81","Pulmão"),("PULMÃOJ81","PULMÃO"),
    (" se 6 em 6 horas"," de 6 em 6 horas"),
    ("DIARRÉIA","DIARREIA"),
]
def _fixline(s):
    for a, b in _TYPOS:
        s = s.replace(a, b)
    return s

# ---- blocos crânio-caudal ----
def _block_for(title, cid):
    t = _n(title)
    def has(*ks): return any(_n(k) in t for k in ks)
    if has("dengue","arbovirose","sepse","anafilaxia","intoxica","febre maculosa","leptospirose",
           "escorpi","botropico","jararaca","aranha","pep","violencia sexual","picada",
           "desprotegida","intubacao"): return "GERAL"
    if has("ivas","resfriado","gripe","amigdalite","faringo","sinusite","otite","otalgia",
           "cerume","rinite","perfuracao","tosse subaguda"): return "ORL"
    if has("conjuntivite","calazio","olho","ocular","neurite optica","periorbit","zoster ocular"): return "OLHOS"
    if has("cefaleia","enxaqueca","tontura","vertigem","labirintite","neuralgia","paralisia de bell",
           "ramsay","avc","convuls","meningite","encefalopatia"): return "NEURO"
    if has("asma","bronquite","dpoc","pneumonia","coqueluche","influenza","srag","tosse","iam","infarto",
           "insuficiencia cardiaca","edema agudo","bradicardia","taquiarritmia","dissec","tromboflebite",
           "trombose venosa","oclusao arterial","dor toracica","elevacao importante da pa"): return "TORAX"
    if has("candidiase oral"): return "ABDOME"
    if has("geca","gastroenterite","disenteria","colite","reflux","drge","gastrite","epigastralgia","pirose",
           "hemorroid","constipacao","parasitose","enterobi","oxiur","xerostomia","soluco",
           "afta","colecistite","diverticulite","pancreatite","abdome","corpo estranho","colica biliar",
           "hemorragia digestiva","apendicite","dor de dente"): return "ABDOME"
    if has("hipergli","hipogli","hiperpotass","hipopotass","hiponatr","cetoacidose","hiperosmolar","rabdomi"): return "METAB"
    if has("anemia","epistaxe","neutropenia","falcemica","transfus"): return "HEMATO"
    if has("lombalgia","mialgia","dor cronica","gota","entorse","fasciite","osteoartrite","insuficiencia venosa"): return "MSK"
    if has("cistite","itu","infeccao urinaria","pielonefrite","nefrolit","colica nefretica","colica menstrual",
           "sangramento uterino","vaginose","candidiase","tricomon","cervicite","sifilis","gonorr",
           "herpes genital","cancro","linfogranuloma","climaterio","atrofia urogenital","incontinencia",
           "mastite","balanite","escroto","orqui","bacteri"): return "GU"
    if has("alergia","urticaria","abscesso","furunculo","carbunculo","hidradenite","disidrose","dermatite",
           "tinea","impetigo","escabiose","pediculose","herpes simples","herpes zoster","queimadura",
           "erisipela","celulite","foliculite","onicocriptose","unha encravada","feridas","drenagem"): return "PELE"
    if has("abstinencia"): return "PSIQ"
    return "GERAL"

_RED = re.compile(r"(sepse|anafilaxia|choque|pcr|iam|infarto|avc|dissec|edema agudo|meningite|convuls|"
                  r"cetoacidose|hiperosmolar|hemorragia digestiva|intoxica|pancreatite|colecistite|diverticulite|"
                  r"abdome agudo|oclus[ãa]o arterial|trombose venosa|pielonefrite|apendicite|neutropenia|falc[êe]mica|"
                  r"hiperpotass|hiponatr|taquiarritmia|bradicardia|encefalopatia|rabdomi|pneumonia|intuba)", re.I)
_YEL = re.compile(r"(sinusite|otite|amigdalite|faringo|dpoc|influenza|coqueluche|bronquite|dengue|leptospirose|"
                  r"febre maculosa|escorpi|botr[óo]pico|jararaca|aranha|cistite|itu\b|c[óo]lica|nefrolit|erisipela|celulite|"
                  r"herpes zoster|escabiose|gota|vertigem|tontura|epistaxe|transfus|sangramento|alergia|urtic[áa]ria|"
                  r"queimadura|abscesso|fur[úu]nculo|hidradenite|impetigo|pediculose|neuralgia|paralisia|ramsay|"
                  r"eleva[çc][ãa]o|mastite|orqui|cervicite|s[íi]filis|gonorr|tricomon|cancro|linfogranuloma|pep|desprotegida)", re.I)
def _sev_for(title):
    if _RED.search(title): return "vermelha"
    if _YEL.search(title): return "amarela"
    return "verde"

def _fmt_cid(code):
    m = re.match(r"^([A-Z])(\d{2})(\d)$", code)
    if m: return f"{m.group(1)}{m.group(2)}.{m.group(3)}"
    return code

_KEEP_UP = {"IVAS","SUS","AMA","DRGE","GECA","SRAG","DPOC","IAM","AVC","TVP","PA","HDA","PEP","ITU","SUA","MG","O2","AE","AVCH","AVCI"}
_LOWER = {"de","do","da","dos","das","em","e","ou","para","com","no","na","por","a","o","ao","à"}
def _titlecase(s):
    out = []
    for idx, w in enumerate(s.split()):
        wu = re.sub(r"[^A-Za-zÀ-ÿ]", "", w).upper()
        wl = re.sub(r"[^A-Za-zÀ-ÿ]", "", w).lower()
        if wu in _KEEP_UP: out.append(w.upper())
        elif wl in _LOWER and idx > 0: out.append(wl)
        elif w.isupper() and len(w) > 2: out.append(w.capitalize())
        else: out.append(w)
    return " ".join(out).strip()

def _parse_header(h):
    s = _fixline(h.strip().strip("#").strip())
    s = re.sub(r"_{2,}", " ", s).strip()
    s = re.sub(r"#{2,}", " ", s).strip()
    s = re.sub(r"\(\s*REVER\s*\)", "", s, flags=re.I).strip()
    s = re.sub(r"\(?\s*Bia\s*\)?", " ", s)
    s = re.sub(r"\bBEATRIZ\b", " ", s, flags=re.I)
    cids = [_fmt_cid(c) for c in re.findall(r"\b([A-Z]\d{2}(?:\.\d{1,2})?\d?)\b", s)]
    s = re.sub(r"\(?\s*\bCID\b[:\s]*", " ", s)
    s = re.sub(r"\b[A-Z]\d{2}(?:\.\d{1,2})?\d?\b", " ", s)
    s = s.replace("(", " ").replace(")", " ")
    s = re.sub(r"\s+", " ", s).strip(" -:·/")
    return _titlecase(s), (" · ".join(dict.fromkeys(cids)) if cids else "")

# ---- renomeações/merges canônicos (título exato pós-parse) -> (novo título, cid override) ----
_TITLE_FIX = {
    "IVAS SUS Amigdalite Resfriado": ("IVAS / Amigdalite / Resfriado", None),
    "Alergia e Rinite Alérgica alergia": ("Alergia / Rinite Alérgica", None),
    "Gastrite/drge": ("Gastrite / DRGE", None),
    "Enjoo / Nauseas": ("Enjoo / Náuseas", None),
    "Otite Media Aguda": ("Otite Média Aguda", None),
    "Otite Média": ("Otite Média Aguda", None),
    "Otite Externa Aguda": ("Otite Externa", None),
    "Cistite": ("Cistite / ITU", None),
    "Infecção Urinária": ("Cistite / ITU", None),
    "Tontura": ("Vertigem / Labirintite / Tontura", None),
    "Vertigem // Labirintite// Tontura": ("Vertigem / Labirintite / Tontura", None),
    "GECA em Adulto": ("GECA / Gastroenterite (adulto)", None),
    "Gastroenterite // Náuseas e Vômitos": ("GECA / Gastroenterite (adulto)", None),
    "Nefrolitiase - Colica Nefretica": ("Nefrolitíase / Cólica Nefrética", None),
    "Hipoglicemia 16.2": ("Hipoglicemia", "E16.2"),
    "Herpes Zoster": (None, "B02"),
    "Cefaléia Pós Raqui": ("Cefaleia Pós-Raqui", None),
    "Cefaléia Tensional": ("Cefaleia Tensional", None),
    "Picada Escorpião Acidente Escorpiônico": ("Picada de Escorpião (Acidente Escorpiônico)", None),
    "Picada Jararaca Acidente Botrópico": ("Picada de Jararaca (Acidente Botrópico)", None),
    "Picada Aranha Marrom": ("Picada de Aranha-Marrom", None),
    "Acidente Vascular Encefálico Isquemico AVCI": ("AVC Isquêmico (AVCI)", None),
    "Acidente Vascular Encefálico Hemorragico AVCH": ("AVC Hemorrágico (AVCH)", None),
    "Edema Agudo de Pulmão": (None, "J81"),
    "IAM Infarto Agudo do Miocardio": ("IAM — Infarto Agudo do Miocárdio", None),
    "Bacteriúria Assintomáticas": ("Bacteriúria Assintomática", None),
    "Hidradenite Supurativa L 732": ("Hidradenite Supurativa", "L73.2"),
    "Tosse Subaguda Pós Viral": ("Tosse Subaguda Pós-Viral", None),
    "Gonorréia": ("Gonorreia", None),
    "Abstinência Alcoolica": ("Abstinência Alcoólica", None),
    "Insuficiencia Cardiaca": ("Insuficiência Cardíaca", None),
    "Insuficiencia Venosa Cronica": ("Insuficiência Venosa Crônica", None),
    "Fasciite Plantar": ("Fasciíte Plantar", None),
    "Anemia Megaloblastica": ("Anemia Megaloblástica", None),
    "Crise Algica Falcemica": ("Crise Álgica Falcêmica", None),
    "Neurite Optica": ("Neurite Óptica", None),
    "Calazio": ("Calázio", None),
    "Celulite Periorbitaria / Pré Septal": ("Celulite Periorbitária / Pré-Septal", None),
    "Herpes genital": ("Herpes Genital", None),
    "Cancro mole": ("Cancro Mole", None),
    "Parasitose AE": ("Parasitose", None),
    "Erisipela ou Celulite": ("Erisipela / Celulite", None),
    "Intubação Orotraqueal Paciente 70kg": ("Intubação Orotraqueal (70 kg)", None),
    "Elevação Importante da PA": ("Elevação Importante da PA (sem LOA)", None),
    "Relação Sexual Desprotegida/ Violência Sexual": ("Relação Desprotegida / Violência Sexual (PEP)", None),
    "Lombalgia // Mialgia": ("Lombalgia / Mialgia", None),
    "Enterobiase/ Oxiurose": ("Enterobíase / Oxiurose", None),
    "Hemorróida": ("Hemorroida", None),
    "Queimadura Ocular – Abrasão, Química": ("Queimadura Ocular (Abrasão / Química)", None),
}

# ---- cabeçalhos de condição ----
def _is_header(line):
    s = line.strip()
    if re.match(r"^_{3,}.*[A-Za-zÀ-ÿ].*_{3,}", s): return True
    if re.match(r"^#{2,}\s*[A-Za-zÀ-ÿ].*", s): return True
    return False

# ---- destino (PS / casa / internação) ----
def _dest_of(label):
    ln = _n(label)
    if any(k in ln for k in ("interna", "hospitalar", "uti", "paciente grave")): return "internacao"
    if any(k in ln for k in ("na unidade", "agora", "aqui", "sala", "nebuliz",
                             "parenteral", "refratar", "sem melhora")): return "ps"
    if re.search(r"\b(im|ev)\b", ln): return "ps"
    return "casa"

_DOSEISH = re.compile(r"\d+\s*(mg|mcg|ml|g\b|ui|comprimido|cp\b|cps\b|amp|frasco|gotas?|jato|caixa|env|sach|pastilha|milh|colher|000)", re.I)
_VERBS = re.compile(r"^(TOMAR|APLICAR|USAR|FAZER|DILUIR|INALAR|PASSAR|PINGAR|SENTAR|LAVAR|DISSOLVER|DEIXAR|MASTIGAR|BEBER)\b", re.I)

def _is_section_label(s):
    if not s: return False
    if len(s) > 70: return False
    if s.startswith("-"): return False
    if re.match(r"^\d+\s*[\).]", s): return False
    if _DOSEISH.search(s): return False
    if _VERBS.match(s): return False
    up = s.upper()
    if s.endswith(":"): return True
    if re.search(r"\b(USO ORAL|USO NASAL|USO T[ÓO]PICO|USO OFTALM|USO VAGINAL|USO OTOL[ÓO]GICO|USO LOCAL|"
                 r"USO EXTERNO|SE PRECISAR DE ATB|SE NECESS[ÁA]RIO ATB|SE BACTERIANA|AMBULATORIAL|"
                 r"CASA|AQUI|AGORA|NA UNIDADE|INTERNA[ÇC][ÃA]O|2[ªa] LINHA|CRISE|PROFILAXIA|"
                 r"CUIDADOS|ORIENTA[ÇC][ÕO]ES|CONDUTA|OBSERVA|SEM MELHORA)\b", up):
        return True
    if re.match(r"^IM\b", up): return True
    return False

_NOTE_LABELS = re.compile(r"^(CUIDADOS|ORIENTA[ÇC][ÕO]ES|CONDUTA|OBSERVA|NOTA|OBS)\b", re.I)
_NARR_START = re.compile(r"^(PACIENTE REFERE|Paciente refere|Nega |#|⚫|RESUMO|Excluir|Colher|Score|Bom estado|Olho |Neuro:|Abdome |Coluna |CURB|75%|20-40%|O exame|Exame f[íi]sico|ATB indicado|> ATEN|USO DE ATB|Meta:|N[ÃA]O usar|⚠)", )

def _clean(txt):
    txt = re.sub(r"\bpressss\b", "", txt, flags=re.I)
    txt = re.sub(r"\(?\s*Bia\s*\)?", "", txt)
    txt = txt.replace("BEATRIZ", "").replace("Beatriz", "")
    # remove linhas-separador (____ ---- ====)
    lines = [ln for ln in txt.split("\n") if not re.fullmatch(r"[\s_\-–—=\.]{4,}", ln.strip() or "x") or ln.strip()==""]
    lines = [ln for ln in lines if not re.fullmatch(r"[_\-–—=\.]{4,}", ln.strip())]
    txt = "\n".join(lines)
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()

def _looks_rx(text):
    """Grupo tem cara de prescrição (dose ou via)?"""
    if _DOSEISH.search(text): return True
    if re.search(r"\b(EV|IM|VO|SC|SL)\b", text): return True
    return False

def _process_condition(header, body):
    title, cid = _parse_header(header)
    if not title: return None
    lines = [_fixline(l) for l in body.split("\n")]

    nota_parts = []
    groups = []
    cur = {"dest": "casa", "label": "", "lines": []}
    groups.append(cur)
    seen_drug = False

    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            cur["lines"].append(""); i += 1; continue
        if _NOTE_LABELS.match(s):
            buf = [re.sub(r"^(CUIDADOS|ORIENTA[ÇC][ÕO]ES|CONDUTA|OBSERVA[ÇC][ÕO]ES?|OBS|NOTA)\s*:?\s*", "", s, flags=re.I)]
            i += 1
            while i < len(lines):
                n = lines[i].strip()
                if not n: break
                if _is_section_label(n) or re.match(r"^\d+\s*[\).]", n): break
                buf.append(n); i += 1
            nota_parts.append(" ".join(x for x in buf if x).strip())
            continue
        # narrativa pré-droga (anamnese/EF/contexto) -> nota
        if not seen_drug and not _DOSEISH.search(s) and not re.match(r"^\d+\s*[\).]", s):
            if _NARR_START.match(s) or (len(s.split()) >= 4 and re.search(r"[a-zà-ÿ]", s)):
                nota_parts.append(s); i += 1; continue
        if _is_section_label(s):
            lbl = s.strip().strip("*").strip(":").strip("-").strip()
            if re.match(r"^(USO ORAL|USO NASAL|USO T[ÓO]PICO|USO OFTALM\w*|USO VAGINAL|USO OTOL\w*|USO LOCAL|USO EXTERNO|CASA)$", lbl, re.I):
                lbl_clean = ""
            else:
                lbl_clean = lbl
            cur = {"dest": _dest_of(lbl), "label": lbl_clean, "lines": []}
            groups.append(cur)
            i += 1; continue
        seen_drug = True
        cur["lines"].append(s)
        i += 1

    rx = []
    for g in groups:
        text = _clean("\n".join(g["lines"]))
        if not text and g["label"]:
            text = g["label"]; g["label"] = ""
        if not text: continue
        # narrativa pós-droga sem dose/via -> nota
        if not _looks_rx(text) and len(text) < 420:
            nota_parts.append(text.replace("\n", " ").strip()); continue
        dest = g["dest"]
        # sniff de conteúdo: EV/IM/amp dominante -> ps
        if dest == "casa":
            ev = len(re.findall(r"\b(EV|IM|BIC|amp(?:ola)?s?)\b", text, re.I))
            vo = len(re.findall(r"\b(tomar|vo\b|comprimid|via oral|mastigar|dissolver)\b", text, re.I))
            if ev > vo and ev >= 1: dest = "ps"
        rx.append({"dest": dest, "label": g["label"], "text": text})
    nota = _clean("\n".join(p for p in nota_parts if p))
    return dict(title=title, cid=cid, nota=nota, rx=rx)

def _is_junk(title):
    tn = _n(title).strip()
    return (not tn) or tn.isdigit() or len(tn) < 3

_SUBSEC = re.compile(r"^(se emergencia|ajuste d|conduta|exames solicitar|opcao|op\.)", re.I)
def _is_subsection(title):
    return bool(_SUBSEC.match(_n(title).strip()))

# ---- executa ----
if _raw:
    _lines = _raw.split("\n")
    _idx = [i for i, l in enumerate(_lines) if _is_header(l)]
    _idx.append(len(_lines))
    _conds = []
    for k in range(len(_idx) - 1):
        h = _lines[_idx[k]]
        body = "\n".join(_lines[_idx[k] + 1:_idx[k + 1]])
        if not re.search(r"[A-Za-zÀ-ÿ]", h): continue
        cond = _process_condition(h, body)
        if not cond or not cond["rx"]: continue
        if _is_junk(cond["title"]): continue
        if _is_subsection(cond["title"]) and _conds:
            _conds[-1]["rx"].extend(cond["rx"])
            if cond["nota"]:
                _conds[-1]["nota"] = (_conds[-1]["nota"] + "\n" + cond["nota"]).strip()
            continue
        # renome/canonical
        fix = _TITLE_FIX.get(cond["title"])
        if fix:
            if fix[0]: cond["title"] = fix[0]
            if fix[1]: cond["cid"] = fix[1]
        _conds.append(cond)

    # dedup por título normalizado (merge rx, cids e notas)
    _bykey = {}; _order = []
    for c in _conds:
        key = _n(c["title"]).strip()
        if key in _bykey:
            base = _bykey[key]
            base["rx"].extend(c["rx"])
            if c["cid"]:
                parts = [p for p in (base["cid"].split(" · ") if base["cid"] else []) if p]
                for p in c["cid"].split(" · "):
                    if p and p not in parts: parts.append(p)
                base["cid"] = " · ".join(parts)
            if c["nota"] and c["nota"] not in base["nota"]:
                base["nota"] = (base["nota"] + "\n" + c["nota"]).strip()
        else:
            _bykey[key] = c; _order.append(c)

    for c in _order:
        blk = _block_for(c["title"], c["cid"])
        C(title=c["title"], cid=c["cid"], block=blk, sev=_sev_for(c["title"]),
          nota=c["nota"], rx=c["rx"])
