# -*- coding: utf-8 -*-
# RECEITAS PRONTAS PRA CASA (aba do site) — parse CRU e leve.
# Substitui as condições elaboradas antigas. Doses verbatim; só limpa artefatos.
import os, re

_src = os.path.join(_here, "sources", "receitas_casa.txt")
_raw = open(_src, encoding="utf-8").read() if os.path.exists(_src) else ""

def _n(s):
    s = (s or "").lower()
    for a,b in [("á","a"),("à","a"),("ã","a"),("â","a"),("é","e"),("ê","e"),("í","i"),
                ("ó","o"),("ô","o"),("õ","o"),("ú","u"),("ç","c")]:
        s = s.replace(a,b)
    return s

# ---- mapeamento título/cid -> bloco crânio-caudal ----
def _block_for(title, cid):
    t = _n(title); c = (cid or "").upper()
    def has(*ks): return any(_n(k) in t for k in ks)
    # infecciosas/sistêmicas primeiro (evita falso-positivo tipo 'pirose' em leptospirose)
    if has("dengue","arbovirose","sepse","anafilaxia","intoxica","febre maculosa","leptospirose",
           "escorpi","botrópico","jararaca","aranha","pep","violência sexual","picada"): return "GERAL"
    if has("ivas","resfriado","gripe","amigdalite","faringo","sinusite","otite","otalgia",
           "cerume","rinite","perfuração","tosse subaguda"): return "ORL"
    if has("conjuntivite","calázio","calazio","olho","ocular","neurite óptica","periorbit","herpes zoster oft"): return "OLHOS"
    if has("cefaleia","cefaléia","enxaqueca","tontura","vertigem","labirintite","neuralgia","paralisia de bell",
           "ramsay","avc","convuls","meningite","encefalopatia"): return "NEURO"
    if has("asma","bronquite","dpoc","pneumonia","coqueluche","influenza","srag","tosse","iam","infarto",
           "insuficiência cardíaca","edema agudo","bradicardia","taquiarritmia","dissec","tromboflebite",
           "trombose venosa","oclusão arterial","dor torácica","pressão","pa "): return "TORAX"
    if has("candidiase oral"): return "ABDOME"
    if has("geca","gastroenterite","disenteria","colite","reflux","drge","gastrite","epigastralgia","pirose",
           "hemorroida","hemorroid","constipacao","parasitose","enterobi","oxiur","xerostomia","soluco",
           "afta","colecistite","diverticulite","pancreatite","abdome","corpo estranho","colica biliar","hemorragia digestiva",
           "apendicite","dor de dente"): return "ABDOME"
    if has("hipergli","hipogli","hiperpotass","hipopotass","hiponatr","cetoacidose","hiperosmolar","rabdomi"): return "METAB"
    if has("anemia","epistaxe","neutropenia","falcêmica","falcemica","transfus"): return "HEMATO"
    if has("lombalgia","mialgia","dor cronica","gota","entorse","fasciite","osteoartrite","insuficiencia venosa"): return "MSK"
    if has("cistite","itu","pielonefrite","nefrolit","cólica nefrética","cólica menstrual","sangramento uterino",
           "vaginose","candidíase","tricomon","cervicite","sífilis","sifilis","gonorr","herpes genital","cancro",
           "linfogranuloma","climatério","atrofia urogenital","incontinência","mastite","balanite","escroto","orqui","bacteri"): return "GU"
    if has("alergia","urticária","abscesso","furúnculo","carbúnculo","hidradenite","disidrose","dermatite","tínea","tinea",
           "impetigo","escabiose","pediculose","herpes simples","herpes zoster","queimadura","erisipela","celulite","foliculite",
           "onicocriptose","unha encravada","feridas"): return "PELE"
    if has("abstinência"): return "PSIQ"
    if has("dengue","sepse","anafilaxia","intoxica","febre maculosa","leptospirose","escorpi","botrópico","jararaca",
           "aranha","pep","violência","acidente"): return "GERAL"
    return "GERAL"

_RED = re.compile(r"(sepse|anafilaxia|choque|pcr|iam|infarto|avc|dissec|edema agudo|meningite|convuls|"
                  r"cetoacidose|hiperosmolar|hemorragia digestiva|intoxica|pancreatite|colecistite|diverticulite|"
                  r"abdome agudo|oclusão arterial|trombose venosa|pielonefrite|apendicite|neutropenia|falcêmica|"
                  r"hiperpotass|hiponatr|taquiarritmia|bradicardia|edema agudo|encefalopatia|rabdomi)", re.I)
_YEL = re.compile(r"(sinusite|otite|amigdalite|faringo|dpoc|influenza|coqueluche|bronquite|dengue|leptospirose|"
                  r"febre maculosa|escorpi|botrópico|jararaca|aranha|cistite|itu|cólica|nefrolit|erisipela|celulite|"
                  r"herpes zoster|escabiose|gota|vertigem|tontura|epistaxe|transfus|sangramento|alergia|urticária|"
                  r"queimadura|abscesso|furúnculo|hidradenite|impetigo|pediculose|neuralgia|paralisia|ramsay|"
                  r"pressão|pa \(|elevação|mastite|orqui|cervicite|sífilis|gonorr|tricomon|cancro|linfogranuloma|pep)", re.I)
def _sev_for(title):
    if _RED.search(title): return "vermelha"
    if _YEL.search(title): return "amarela"
    return "verde"

# ---- CID: normaliza "J069"->J06.9, "R101"->R10.1; mantém "J03","H66" ----
def _fmt_cid(code):
    m = re.match(r"^([A-Z])(\d{2})(\d)$", code)
    if m: return f"{m.group(1)}{m.group(2)}.{m.group(3)}"
    return code

def _parse_header(h):
    s = h.strip().strip("#").strip()
    s = re.sub(r"_{2,}", " ", s).strip()
    s = re.sub(r"#{2,}", " ", s).strip()
    s = re.sub(r"\(\s*REVER\s*\)", "", s, flags=re.I).strip()
    s = re.sub(r"\(?\s*Bia\s*\)?", " ", s)
    s = re.sub(r"\bBEATRIZ\b", " ", s, flags=re.I)
    # captura CIDs
    cids = re.findall(r"\b([A-Z]\d{2}(?:\.\d{1,2})?\d?)\b", s)
    cids = [_fmt_cid(c) for c in cids]
    # remove só o token "CID"/"CID:" isolado (NÃO 'cid' dentro de palavras: acidente, acidose)
    s = re.sub(r"\(?\s*\bCID\b[:\s]*", " ", s)
    s = re.sub(r"\b[A-Z]\d{2}(?:\.\d{1,2})?\d?\b", " ", s)
    s = s.replace("(", " ").replace(")", " ")
    s = re.sub(r"\s+", " ", s).strip(" -:·/")
    # Title case suave (mantém siglas curtas)
    title = _titlecase(s)
    cid = " · ".join(dict.fromkeys(cids)) if cids else ""
    return title, cid

_KEEP_UP = {"IVAS","SUS","AMA","DRGE","GECA","SRAG","DPOC","IAM","AVC","TVP","PA","HDA","PEP","ITU","SUA","MG","O2","AE","AVCH","AVCI"}
_LOWER = {"de","do","da","dos","das","em","e","ou","para","com","no","na","por","a","o","ao","à"}
def _titlecase(s):
    words = s.split()
    out = []
    for idx, w in enumerate(words):
        wu = re.sub(r"[^A-Za-zÀ-ÿ]", "", w).upper()
        wl = re.sub(r"[^A-Za-zÀ-ÿ]", "", w).lower()
        if wu in _KEEP_UP:
            out.append(w.upper())
        elif wl in _LOWER and idx > 0:
            out.append(wl)
        elif w.isupper() and len(w) > 2:
            out.append(w.capitalize())
        else:
            out.append(w)
    return " ".join(out).strip()

# ---- split em condições pelos cabeçalhos ----
_HDR = re.compile(r"^(?:_{3,}.*?_{3,}.*|#{2,}.*?#{2,}.*|#{2,}\s+.+)$")
def _is_header(line):
    s = line.strip()
    if re.match(r"^_{3,}.*[A-Za-zÀ-ÿ].*_{3,}", s): return True
    if re.match(r"^#{2,}\s*[A-Za-zÀ-ÿ].*", s): return True
    return False

# marcadores de destino/seção (viram rótulos de grupo)
_DEST = [
    (re.compile(r"\b(internaç|hospitalar|uti|paciente grave)\b", re.I), "internacao"),
    (re.compile(r"\b(aqui|agora na unidade|na unidade|sala|im\b|im\s*\(|ev\b|nebuliz|parenteral|agora:)\b", re.I), "ps"),
]
def _dest_of(label):
    for rx, d in _DEST:
        if rx.search(label): return d
    return "casa"

_DOSEISH = re.compile(r"\d+\s*(mg|mcg|ml|g|ui|comprimido|cp|amp|frasco|gotas?|jato|caixa|env|sach|pastilha|milh|000)", re.I)
def _is_section_label(s):
    """Linha curta em CAIXA ALTA ou terminando em ':' que rotula um grupo (não é droga)."""
    if not s: return False
    if len(s) > 70: return False
    if re.match(r"^\d+\s*[\).]", s): return False           # item numerado
    if _DOSEISH.search(s): return False                     # tem dose -> é medicamento, não rótulo
    up = s.upper()
    if s.endswith(":"): return True
    if re.search(r"\b(USO ORAL|USO NASAL|USO T[ÓO]PICO|USO OFTALM|USO VAGINAL|USO OTOL[ÓO]GICO|USO LOCAL|"
                 r"USO EXTERNO|SE PRECISAR DE ATB|SE NECESS[ÁA]RIO ATB|SE BACTERIANA|ATB|AMBULATORIAL|"
                 r"CASA|AQUI|AGORA|NA UNIDADE|IM\b|IM \(|INTERNA[ÇC][ÃA]O|2[ªa] LINHA|CRISE|PROFILAXIA|"
                 r"CUIDADOS|ORIENTA[ÇC][ÕO]ES|CONDUTA|OBSERVA)", up):
        return True
    return False

_NOTE_LABELS = re.compile(r"^(CUIDADOS|ORIENTA[ÇC][ÕO]ES|CONDUTA|OBSERVA|NOTA|OBS)\b", re.I)
def _is_anamnese(s):
    return bool(re.match(r"^(PACIENTE REFERE|Paciente refere|Nega |#|⚫|RESUMO)", s))

def _clean(txt):
    txt = re.sub(r"\bpressss\b", "", txt, flags=re.I)
    txt = re.sub(r"\(?\s*Bia\s*\)?", "", txt)
    txt = txt.replace("BEATRIZ", "").replace("Beatriz", "")
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()

def _process_condition(header, body):
    title, cid = _parse_header(header)
    if not title: return None
    block = _block_for(title, cid)
    sev = _sev_for(title)
    lines = body.split("\n")

    nota_parts = []
    # grupos: lista de (dest, label, [linhas])
    groups = []
    cur = {"dest":"casa","label":"","lines":[]}
    groups.append(cur)
    seen_drug = False

    i = 0
    while i < len(lines):
        raw = lines[i]; s = raw.strip()
        if not s:
            cur["lines"].append("")
            i += 1; continue
        # anamnese / notas de topo (antes de qualquer droga)
        if not seen_drug and _is_anamnese(s):
            nota_parts.append(s); i += 1; continue
        if _NOTE_LABELS.match(s):
            # nota: absorve até próxima label/droga
            note_buf = [re.sub(r"^(CUIDADOS|ORIENTA[ÇC][ÕO]ES|CONDUTA|OBSERVA[ÇC][ÕO]ES?|OBS|NOTA)\s*:?\s*", "", s, flags=re.I)]
            i += 1
            while i < len(lines):
                n = lines[i].strip()
                if not n: break
                if _is_section_label(n) or re.match(r"^\d+\s*[\).]", n): break
                note_buf.append(n); i += 1
            nota_parts.append(" ".join(x for x in note_buf if x).strip())
            continue
        if _is_section_label(s):
            lbl = s.strip().strip("*").strip(":").strip("-").strip()
            d = _dest_of(lbl)
            # rótulos "USO ORAL/NASAL" viram casa sem poluir
            if re.match(r"^(USO ORAL|USO NASAL|USO T[ÓO]PICO|USO OFTALM|USO VAGINAL|USO OTOL|USO LOCAL|USO EXTERNO|CASA)$", lbl, re.I):
                lbl_clean = ""
            else:
                lbl_clean = lbl
            cur = {"dest":d,"label":lbl_clean,"lines":[]}
            groups.append(cur)
            i += 1; continue
        # linha comum (droga/posologia)
        seen_drug = True
        cur["lines"].append(s)
        i += 1

    # monta rx
    rx = []
    for g in groups:
        text = _clean("\n".join(g["lines"]))
        if not text: continue
        rx.append({"dest":g["dest"], "label":g["label"], "text":text})
    nota = _clean("\n".join(p for p in nota_parts if p))
    return dict(title=title, cid=cid, block=block, sev=sev, nota=nota, rx=rx)

# sub-seções que NÃO são condições próprias -> mesclar no card anterior
_SUBSEC = re.compile(r"^(se emergencia|ajuste d|conduta|exames solicitar|opcao|op\.)", re.I)
def _is_junk(title):
    tn = _n(title).strip()
    if not tn or tn.isdigit() or len(tn) < 3: return True
    return False
def _is_subsection(title):
    return bool(_SUBSEC.match(_n(title).strip()))

# ---- executa ----
if _raw:
    _lines = _raw.split("\n")
    _idx = [i for i,l in enumerate(_lines) if _is_header(l)]
    _idx.append(len(_lines))
    _conds = []
    for k in range(len(_idx)-1):
        h = _lines[_idx[k]]
        body = "\n".join(_lines[_idx[k]+1:_idx[k+1]])
        if not re.search(r"[A-Za-zÀ-ÿ]", h): continue
        cond = _process_condition(h, body)
        if not cond or not cond["rx"]: continue
        if _is_junk(cond["title"]):
            continue
        if _is_subsection(cond["title"]) and _conds:
            # mescla rx no card anterior (ex.: opções de anti-HTN da Elevação da PA)
            _conds[-1]["rx"].extend(cond["rx"])
            continue
        _conds.append(cond)

    # dedup: mesmo título normalizado + bloco -> junta rx e nota
    _bykey = {}
    _order = []
    for c in _conds:
        key = (c["block"], _n(c["title"]).strip())
        if key in _bykey:
            base = _bykey[key]
            base["rx"].extend(c["rx"])
            if c["nota"] and c["nota"] not in base["nota"]:
                base["nota"] = (base["nota"] + " " + c["nota"]).strip()
        else:
            _bykey[key] = c; _order.append(c)

    for c in _order:
        C(title=c["title"], cid=c["cid"], block=c["block"], sev=c["sev"],
          nota=c["nota"], rx=c["rx"])
