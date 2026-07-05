# -*- coding: utf-8 -*-
# FORMULÁRIO SUS (tab "SUS medicamentos") — lista A–Z de disponibilidade na rede.
# Gerado da fonte sources/sus_medicamentos.txt; um card por letra.
import os, re

_src = os.path.join(_here, "sources", "sus_medicamentos.txt")
if os.path.exists(_src):
    _raw = open(_src, encoding="utf-8").read()
    _lines = _raw.split("\n")
    # Detecta cabeçalhos de letra: linha isolada com 1-2 chars entre linhas de "===="
    _letters = {}
    _cur = None
    i = 0
    while i < len(_lines):
        ln = _lines[i].strip()
        if re.fullmatch(r"=+", ln) and i+2 < len(_lines) and re.fullmatch(r"=+", _lines[i+2].strip()):
            _cur = _lines[i+1].strip().upper()
            _letters.setdefault(_cur, [])
            i += 3
            continue
        if _cur is not None and ln and not re.fullmatch(r"=+", ln):
            _letters[_cur].append(_lines[i].rstrip())
        i += 1

    def _condense(entries):
        """Junta cada medicamento com sua nota de disponibilidade em 1 linha."""
        out = []
        buf = []
        def flush():
            if not buf: return
            name = buf[0].strip()
            avail = " · ".join(x.strip() for x in buf[1:] if x.strip())
            avail = avail.replace("medicamento disponível", "disp.")
            out.append(name + (f"  — {avail}" if avail else ""))
        for ln in entries:
            s = ln.strip()
            if not s:
                continue
            low = s.lower()
            if low.startswith("medicamento disponível") or low.startswith("exclusivamente") or low.startswith("necess"):
                buf.append(s)
            else:
                flush(); buf = [s]
        flush()
        return out

    for letter in sorted(_letters.keys()):
        items = _condense(_letters[letter])
        if not items:
            continue
        text = "\n".join(items)
        C(title=f"Formulário SUS — {letter}", cid="", block="FARM", sev="verde",
          nota=f"{len(items)} itens. Consulta de disponibilidade na rede (não é prescrição).",
          rx=[{"dest":"outro","label":f"Medicamentos ({letter})","text":text}])
