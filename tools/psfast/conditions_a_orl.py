# -*- coding: utf-8 -*-
# ORL — verbatim das doses; artefatos limpos; flags marcadas.

C(title="IVAS / Resfriado / Gripe", cid="J06.9", block="ORL", sev="verde",
  anamnese=("PACIENTE REFERE [sintomas gripais] há [X] dias. Nega febre, nega dispneia, "
            "nega dor torácica, nega disfagia, nega vômitos e nega prostração. Sem outros sintomas associados."),
  nota=("Aumentar ingesta hídrica para melhorar expectoração. Anti-histamínico alternativo: "
        "Dexclorfeniramina 2mg 1 cp de 8/8h por 5 dias, ou Bilastina 20mg 1 cp VO pela manhã por 10 dias. "
        "ATB apenas se critério (Centor alto / bacteriana)."),
  rx=[
    {"dest":"casa","label":"Sintomáticos","text":"""Dipirona 500mg — 20 comprimidos
Tomar via oral 2 comprimidos de 6 em 6 horas se dor ou febre.
OU
Paracetamol 500mg — 20 comprimidos
Tomar 1 comprimido de 8 em 8 horas se dor ou febre.

Maleato de dexclorfeniramina 2mg/5ml
Tomar via oral 5 mL, 3x por dia, por 5 dias.

Cetoprofeno 100mg — 1 caixa
Tomar via oral 1 comprimido de 12 em 12 horas por 5 dias.
OU
Diclofenaco 50mg — 10 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 5 dias.
OU
Prednisona 20mg
Tomar 1 comprimido pela manhã, por 5 dias.

Strepsils pastilhas — 1 caixa
Dissolver 1 pastilha na boca, 2 ou mais vezes ao dia, até alívio. Máximo 10 pastilhas/dia.

Dropropizina 3mg/ml xarope 120 ml
Tomar 10 ml de 6 em 6 horas, por 3 dias.
OU
Acetilcisteína xarope 40 mg/mL
Tomar 15 mL antes de dormir, via oral, por 5 dias."""},
    {"dest":"casa","label":"Uso nasal","text":"""Lavagem nasal com soro fisiológico 0,9% — 1 frasco
Aplicar 1 seringa de 20ml em cada narina, 3x ao dia, até melhora.

Budesonida 64mcg spray nasal — 1 frasco
Aplicar 1 jato em cada narina de 12 em 12 horas por 10 dias."""},
    {"dest":"casa","label":"ATB (se indicado)","text":"""Amoxicilina 500mg — 30 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 10 dias.
OU
Amoxicilina + clavulanato 875+125mg — 20 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 10 dias.
OU
Azitromicina 500mg — 5 comprimidos
Tomar 1 comprimido 1x ao dia por 5 dias.
OU
Claritromicina 500mg — 20 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 10 dias.
OU
Levofloxacino 750mg — 10 comprimidos
Tomar 1 comprimido 1x ao dia por 10 dias.
OU
Clindamicina 300mg — 30 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 10 dias.
OU
Penicilina benzatina 1.200.000 UI — IM, dose única.

Hexomedine spray — 1 frasco
Aplicar 3 jatos de 4 em 4 horas na garganta se dor."""},
  ])

C(title="Amigdalite aguda", cid="J03", block="ORL", sev="amarela",
  nota="Viral na maioria → sintomático. Bacteriana (Centor/estrepto) → ATB abaixo.",
  rx=[
    {"dest":"casa","label":"ATB (se bacteriana)","text":"""Amoxicilina 500mg — 30 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 10 dias. (Completar os 10 dias mesmo com melhora. Buscar PS se reação adversa.)
OU
Amoxicilina + clavulanato 875+125mg — 20 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 10 dias.
OU
Clindamicina 300mg
Tomar 1 comprimido de 8 em 8 horas por 10 dias."""},
    {"dest":"casa","label":"Sintomáticos","text":"""Dipirona 500mg — 20 comprimidos
Tomar via oral 2 comprimidos de 6 em 6 horas se dor ou febre.

Maleato de dexclorfeniramina 2mg/5ml
Tomar via oral 5 mL, 2x por dia, por 5 dias.

Prednisona 20mg
Tomar 1 comprimido pela manhã, por 5 dias.

Strepsils pastilhas — 1 caixa
Dissolver 1 pastilha na boca, 2 ou mais vezes ao dia, até alívio. Máximo 10/dia."""},
    {"dest":"casa","label":"Uso nasal","text":"""Lavagem nasal com soro fisiológico 0,9% — 1 frasco
Aplicar 1 seringa de 20ml em cada narina, 3x ao dia, até melhora.

Budesonida 64mcg spray nasal — 1 frasco
Aplicar 1 jato em cada narina de 12 em 12 horas por 10 dias."""},
  ])

C(title="Faringoamigdalite", cid="J03", block="ORL", sev="amarela",
  nota=("75% viral (dor de garganta, mialgia, febre baixa, tosse, coriza, sem adenopatia). "
        "20–40% bacteriana (hiperemia, tonsilas aumentadas, exsudato purulento, adenomegalia jugulodigástrica, "
        "leucocitose com desvio). ATB só se necessário. Na unidade: Profenid ou Decadron IM."),
  rx=[
    {"dest":"casa","label":"ATB (se necessário)","text":"""Amoxicilina 500mg — 30 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 10 dias.
OU
Amoxicilina + clavulanato 875+125mg — 20 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 10 dias."""},
    {"dest":"casa","label":"Sintomáticos","text":"""Dipirona 500mg — 20 comprimidos
Tomar via oral 2 comprimidos de 6 em 6 horas se dor ou febre.

Maleato de dexclorfeniramina 2mg/5ml
Tomar via oral 5 mL, 2x por dia, por 5 dias.

Prednisona 20mg
Tomar 1 comprimido pela manhã, por 5 dias.

Strepsils pastilhas — 1 caixa
Dissolver 1 pastilha na boca, 2 ou mais vezes ao dia, até alívio. Máximo 10/dia."""},
    {"dest":"casa","label":"Uso nasal","text":"""Lavagem nasal com soro fisiológico 0,9% — 1 frasco
Aplicar 1 seringa de 20ml em cada narina, 3x ao dia, até melhora.

Budesonida 64mcg spray nasal — 1 frasco
Aplicar 1 jato em cada narina de 12 em 12 horas por 10 dias."""},
    {"dest":"ps","label":"Na unidade (IM, se necessário)","text":"""Agora: Profenid OU Decadron IM.
Penicilina benzatina 1.200.000 UI — aplicar IM, dose única."""},
  ])

C(title="Sinusite aguda", cid="J01", block="ORL", sev="amarela",
  nota=("ATB se >10 dias, sinal de dupla piora, ou febre muito alta persistente + dor facial intensa."),
  flags=["Amox-clav 500+125mg descrita '8/8h por 10 dias' — seu manual antes citava 5–7 dias; conferir duração."],
  rx=[
    {"dest":"casa","label":"Sintomáticos + nasal","text":"""Prednisona 20mg
Tomar 1 comprimido pela manhã por 5 dias.

Dipirona 500mg
Tomar 1 a 2 comprimidos de 6 em 6 horas se dor ou febre.

Lavagem nasal com soro fisiológico 0,9% — 1 frasco
Aplicar 1 seringa de 20ml em cada narina, 3x ao dia, até melhora.

Budesonida 64mcg spray nasal — 1 frasco
Aplicar 1 jato em cada narina de 12 em 12 horas por 10 dias."""},
    {"dest":"casa","label":"ATB (se >10 dias / dupla piora)","text":"""Amoxicilina + clavulanato 500+125mg — 30 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 10 dias.
OU
Levofloxacino 750mg
Tomar 1 comprimido 1x ao dia por 5–7 dias."""},
  ])

C(title="Tosse subaguda pós-viral", cid="R05.2", block="ORL", sev="verde",
  rx=[
    {"dest":"casa","label":"","text":"""Dropropizina 3mg/ml xarope 120 ml
Tomar 10 ml de 6 em 6 horas, por 3 dias.

Budesonida 50mcg nasal
Aplicar 1 jato em cada narina de 12 em 12 horas por 5 dias."""},
  ])

C(title="Otalgia", cid="H92.0", block="ORL", sev="verde",
  rx=[
    {"dest":"casa","label":"","text":"""Dipirona 500mg
Tomar 1 a 2 comprimidos de 6 em 6 horas se dor ou febre.

Oto-Xilodase
Aplicar 5 gotas no ouvido afetado, 3x ao dia por 7 dias."""},
  ])

C(title="Otite média aguda", cid="H66 · H65", block="ORL", sev="amarela",
  nota=("ATB se <6m, otorreia, OMA bilateral <24m, toxemia, otalgia >48h, T>39°C ou incerteza de reavaliação. "
        "Amoxicilina: <2a → 10 dias; >2a → 7 dias. Na unidade: Dipirona + Decadron IM."),
  rx=[
    {"dest":"casa","label":"ATB","text":"""Amoxicilina 500mg — 21 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 7 dias.
OU
Amoxicilina + clavulanato 875+125mg — 20 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 10 dias.
OU
Axetilcefuroxima 500mg — 20 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 10 dias.
OU
Azitromicina 500mg — VO dose única, seguida de 250mg de 24/24h do 2º ao 5º dia."""},
    {"dest":"casa","label":"OMC simples agudizada","text":"""Ciprofloxacino + hidrocortisona (Otociriax) — 1 frasco
Aplicar 3 gotas no ouvido acometido de 12 em 12 horas por 7 dias.

Ciprofloxacino 500mg — 20 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 10 dias.

Prednisona 20mg — 10 comprimidos
Tomar 2 comprimidos pela manhã por até 5 dias.

Proteção auricular + encaminhar ORL."""},
  ])

C(title="Otite externa aguda", cid="H60", block="ORL", sev="amarela",
  nota="Otite necrotizante (ambulatorial): Ciprofloxacino 500mg 1 cp 12/12h por 4 semanas. Na unidade: Dipirona + Decadron IM.",
  rx=[
    {"dest":"casa","label":"Tópico + analgesia","text":"""Ciprofloxacino + hidrocortisona (Otociriax) — 1 frasco
Aplicar 3 gotas no ouvido acometido de 12 em 12 horas por 7 dias.

Ibuprofeno 600mg
Tomar 1 comprimido de 8 em 8 horas por 5 dias."""},
    {"dest":"casa","label":"Otite externa fúngica","text":"""Clotrimazol 1% — 1 frasco
Aplicar 3–4 gotas no ouvido acometido de 8 em 8 horas até resolução."""},
  ])

C(title="Cerume", cid="H61.2", block="ORL", sev="verde",
  rx=[
    {"dest":"casa","label":"","text":"""Cerumin
Aplicar 5 gotas no ouvido afetado 3x ao dia por 5 dias.

Dipirona 500mg
Tomar 1 comprimido de 6 em 6 horas se dor."""},
  ])

C(title="Perfuração de membrana timpânica", cid="H72", block="ORL", sev="amarela",
  nota="NÃO molhar o ouvido. Retorno com otorrino em 10 dias.",
  rx=[
    {"dest":"casa","label":"","text":"""Levofloxacino 500mg
Tomar 1 comprimido 1x ao dia por 10 dias.

Prednisona 20mg
Tomar 1 comprimido 1x ao dia por 5 dias."""},
  ])

C(title="Rinite alérgica", cid="J30", block="ORL", sev="verde",
  rx=[
    {"dest":"casa","label":"Anti-histamínico","text":"""Dexclorfeniramina 2mg
Tomar 1 comprimido de 8 em 8 horas por 7 dias.
OU
Loratadina 10mg
Tomar 1 comprimido 1x à noite por 7 dias.
OU
Hidroxizina 25mg
Tomar 1 comprimido 1x à noite por 7 dias."""},
    {"dest":"casa","label":"Uso nasal","text":"""Lavagem nasal com soro fisiológico 0,9% — 1 frasco
Aplicar 1 seringa de 20ml em cada narina, 3x ao dia, até melhora.

Budesonida 64mcg spray nasal — 1 frasco
Aplicar 1 jato em cada narina de 12 em 12 horas por 10 dias."""},
  ])
