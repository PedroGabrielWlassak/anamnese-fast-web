# -*- coding: utf-8 -*-
# NEURO + OLHOS

# ---------- NEURO ----------
C(title="Cefaleia", cid="R51", block="NEURO", sev="verde",
  anamnese=("Paciente refere cefaleia há [X]. Nega início súbito da dor, nega pico de intensidade em segundos, "
            "nega pior cefaleia da vida, nega trauma craniano recente, nega febre, nega rigidez de nuca, "
            "nega vômitos persistentes, nega síncope, nega convulsões, nega alteração visual, nega diplopia, "
            "nega alteração da fala, nega confusão mental, nega fraqueza, nega parestesias, nega desequilíbrio, "
            "nega dificuldade para deambular, nega uso de anticoagulantes, nega mudança do padrão habitual."),
  exame=("Bom estado geral, corado, hidratado, acianótico, anictérico, afebril.\n"
         "Neuro: Glasgow 15, sem sinais meníngeos, sem déficits focais."),
  rx=[{"dest":"casa","label":"","text":"""Dipirona 500mg — 40 comprimidos
Tomar 2 comprimidos de 6/6 horas se dor, por 5 dias.

Naproxeno 550mg — 10 comprimidos
Tomar 1 comprimido de 12/12 horas se dor (até 5 dias).
OU
Cetoprofeno 100mg — 1 caixa
Tomar 1 comprimido de 12/12 horas se dor (até 5 dias).

Ondansetrona 4mg — 1 caixa
Tomar 1 comprimido de 8/8h se náusea/vômito.

Sumatriptano 50mg — 1 caixa
Tomar 1 comprimido ao iniciar sintomas de enxaqueca para abortar a crise (pode repetir se necessário)."""}])

C(title="Enxaqueca", cid="G43", block="NEURO", sev="amarela",
  nota="Evitar opioides. Profilaxia: Propranolol 40mg 2 cp 1x/dia OU Metoprolol 25mg 4 cp 1x/dia OU Amitriptilina 25mg 1 cp 1x/dia OU Ácido valproico 250mg 1 cp 3x/dia.",
  rx=[{"dest":"casa","label":"Crise (uso oral)","text":"""Sumatriptano 50mg
Tomar 1 a 2 comprimidos, dose única, se crise de enxaqueca.
OU
Naproxeno 500mg
Tomar 1 comprimido de 12/12 horas por 3 dias.
OU
Ibuprofeno 400mg
Tomar 1 comprimido de 12/12 horas por 3 dias."""},
      {"dest":"ps","label":"Na unidade","text":"""Crise leve: Dipirona 1 amp EV OU Profenid 1 amp EV.
Crise moderada: Clorpromazina 1 amp EV e/ou Dramin 1 amp EV ou Bromoprida 1 amp EV.
Estado migranoso: Dexametasona 1 amp EV lento. Evitar opioides."""}])

C(title="Cefaleia pós-raqui", cid="O74.5", block="NEURO", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Dipirona + mucato de isometepteno + cafeína 300/30/30mg
Tomar 2 comprimidos de 6/6 horas por 3 dias.
OU
Paracetamol + cafeína 500/65mg
Tomar 2 comprimidos de 6/6h por 3 dias.

Refratário: Amitriptilina 25mg — 1 comprimido à noite por 3 noites."""},
      {"dest":"ps","label":"Refratário (na unidade)","text":"""Ringer lactato 2500ml EV em 24h."""}])

C(title="Cefaleia tensional", cid="R51", block="NEURO", sev="verde",
  nota="Profilaxia: Amitriptilina 10mg 1 a 5 cp à noite.",
  rx=[{"dest":"casa","label":"","text":"""Paracetamol 750mg
Tomar 1 comprimido de 6/6 horas se dor.
E/OU
Diclofenaco 50mg
Tomar 1 comprimido de 6/6 horas."""}])

C(title="Vertigem / Labirintite / Tontura", cid="R42", block="NEURO", sev="amarela",
  nota="Excluir AVC: score HINTS.",
  rx=[{"dest":"casa","label":"Sintomático","text":"""Dramin B6
Tomar 1 comprimido de 6/6h se náuseas ou vômitos.

Labirin 8mg — 1 caixa
Tomar 1 comprimido de 8/8h.
OU
Meclin 50mg
Tomar 1 comprimido de 12/12 horas por 5 dias.

Cinarizina 25mg
Tomar 1 comprimido de 8/8 horas por até 5 dias."""},
      {"dest":"casa","label":"Neurite vestibular","text":"""Prednisona 20mg — 1 caixa
Tomar 3 comprimidos pela manhã por 5 dias (corticoterapia com desmame: 60mg/dia 5 dias, reduzir 10mg/dia até o 9º, 5mg no 10º).

Crônica: Flunarizina 10mg — 1 comprimido à noite por 5 dias."""},
      {"dest":"ps","label":"Agora (na unidade)","text":"""SF 0,9% 100ml + Dramin 1 amp EV.
Sem melhora: Metoclopramida 10mg EV.
Sem melhora: Diazepam 1 amp EV."""}])

C(title="Neuralgia do trigêmeo", cid="G50.9", block="NEURO", sev="amarela",
  nota="Encaminhar neurologista.",
  rx=[{"dest":"casa","label":"","text":"""Carbamazepina 200mg
Tomar 1 comprimido de 12/12 horas.
E/OU
Gabapentina 300mg
Tomar 1 comprimido de 8/8 horas."""}])

C(title="Paralisia de Bell", cid="G51.0", block="NEURO", sev="amarela",
  nota="Hemograma, PCR (excluir infecções). Encaminhar neurologista.",
  rx=[{"dest":"casa","label":"Oral","text":"""Prednisona 20mg
Tomar 3 a 4 comprimidos 1x ao dia por 5–7 dias.
OU
Prednisolona 20mg
Tomar 3 comprimidos 1x ao dia por 5 dias."""},
      {"dest":"casa","label":"Oftálmico","text":"""Carmelose sódica
Pingar 1 gota no olho afetado sempre que necessário."""}])

C(title="Síndrome de Ramsay Hunt", cid="B02.2", block="NEURO", sev="amarela",
  nota="Casos graves (vertigem, zumbido, perda auditiva) → internar. Encaminhar neurologista.",
  rx=[{"dest":"casa","label":"Oral","text":"""Valaciclovir 1g
Tomar 1 comprimido de 8/8 horas por 7–10 dias.
OU
Aciclovir 400mg
Tomar 1 comprimido de 4/4 horas por 10 dias.

Dipirona 1g
Tomar 1 comprimido de 6/6 horas se dor ou febre."""},
      {"dest":"casa","label":"Oftálmico","text":"""Carmelose sódica
Pingar 1 gota no olho afetado sempre que necessário."""}])

C(title="Neuralgia pós-herpética", cid="G53.0", block="NEURO", sev="amarela",
  nota="Após aplicar o creme pode 'queimar' por alguns minutos.",
  rx=[{"dest":"casa","label":"Tópico","text":"""Capsaicina creme 0,075%
Aplicar na região 2–3x ao dia."""},
      {"dest":"casa","label":"Oral","text":"""Gabapentina 300mg
Tomar 1 a 6 comprimidos 1x ao dia.
OU
Amitriptilina 25mg
Tomar 1 a 3 comprimidos 1x ao dia."""}])

C(title="Meningite bacteriana", cid="G00.9", block="NEURO", sev="vermelha",
  nota=("Hemograma, ureia, creatinina, coagulograma, hemocultura, lactato, glicose, líquor, TC (s/n). "
        "Profilaxia de contactantes (meningococo): Ciprofloxacino 500mg VO dose única OU Rifampicina 600mg 12/12h por 2 dias."),
  rx=[{"dest":"internacao","label":"","text":"""Ringer lactato ou SF 0,9% 20ml/kg EV.
Ceftriaxona 2g EV 12/12 horas por 7–14 dias
OU Meropenem 2g EV de 8/8 horas por 10–14 dias (suspeita pseudomonas/enterobactéria).
Se >50 anos: + Ampicilina 2g EV de 4/4 horas.
Dexametasona 0,15ml/kg EV de 6/6 horas por 2 dias (começar 30 min antes do ATB).
Dipirona (500mg/ml) 1g EV 6/6 horas.
Metoclopramida (10mg/2ml) 1 amp + AD EV 8/8 horas OU Bromoprida (10mg/2ml) 1 amp EV 8/8h.
Omeprazol (40mg/10ml) 20–40mg EV/VO 1x ao dia pela manhã."""}])

C(title="Crise convulsiva", cid="R56", block="NEURO", sev="vermelha",
  nota="Procurar focos: TC crânio, eletrólitos, hemograma, PCR, Urina I. Avaliação Neurologia. Considerar IOT se não houver melhora.",
  rx=[{"dest":"ps","label":"","text":"""MOV. Se HGT <60: glicose hipertônica 50%.
Diazepam 10mg EV — repetir no máximo 2x. Se sem acesso: Midazolam 15mg IM.
Não melhorou: Fenitoína 1 amp + 250ml de SF 0,9% EV em BIC — correr em 30 minutos."""}])

C(title="AVC isquêmico", cid="I63 · I64", block="NEURO", sev="vermelha",
  nota=("Dextro, hemograma, coagulograma, βhCG, ECG, TC crânio sem contraste. Controle PA: manter ≤220x120; "
        "iniciar trombólise apenas se ≤185x110 (manter <180x110). Nitroprussiato (25mg/ml) 50mg + 250ml SG5% (=200mcg/ml) "
        "iniciar 0,5 mcg/kg/min. Internação UTI."),
  rx=[{"dest":"ps","label":"","text":"""Dieta zero. SF 0,9% ou Ringer lactato 20–30 ml/kg/dia.
Insulina regular 2–4 UI SC (manter glicemia 140–180).
Dipirona 1g EV de 4/4 horas.
Metoclopramida 10mg EV 8/8 horas.
Omeprazol 20–40mg VO/EV pela manhã. O2 se Sat <94%."""},
      {"dest":"ps","label":"Trombólise (<4,5h) — checar contraindicações","text":"""Alteplase (50mg/ml) 0,9 mg/kg (máx 90mg): 10% da dose em bolus, restante em infusão lenta em 1 hora — acesso periférico.
AAS 100mg: 2 comprimidos ao dia (se trombólise, aguardar 24h para iniciar).
Heparina não fracionada 5000 SC 8/8h OU Enoxaparina 40mg SC 24/24h (se trombólise, aguardar 24h)."""}])

C(title="AVC hemorrágico", cid="I61 · I62", block="NEURO", sev="vermelha",
  nota=("Dextro, hemograma, coagulograma, βhCG, ECG, TC crânio sem contraste. Manter PAS=140 (intraparenquimatosa) "
        "ou <160 (subaracnoide): Nitroprussiato (25mg/ml) 50mg + 250ml SG5% (=200mcg/ml) iniciar 0,5 mcg/kg/min. "
        "Suspender/reverter antiagregantes e anticoagulantes. Internação UTI + neurocirurgia."),
  rx=[{"dest":"ps","label":"","text":"""Dieta zero. SF 0,9% ou Ringer lactato 20–30 ml/kg/dia.
Dipirona 1g EV de 4/4 horas.
Metoclopramida 10mg EV 8/8 horas.
Omeprazol 20–40mg VO/EV pela manhã.
Crise convulsiva: Difenil-hidantoína (50mg/ml) ataque 15 mg/kg EV; manutenção 100mg EV de 8/8h.
Subaracnoide: Nimodipina 60mg 4/4 horas por 21 dias."""}])

C(title="Ataque isquêmico transitório", cid="G45", block="NEURO", sev="amarela",
  nota="ECG, USG cervical, Angio-TC/RNM, eco transtorácico. Calcular ABCD2.",
  rx=[{"dest":"casa","label":"ABCD2 <4","text":"""AAS 100mg
Tomar 2 comprimidos ao dia."""},
      {"dest":"internacao","label":"ABCD2 ≥4","text":"""Internação.
AAS 100mg: 2 comprimidos dose de ataque, seguido de 1 comprimido/dia.
Clopidogrel 75mg: 4 comprimidos dose de ataque, seguido de 1 comprimido ao dia (por 21 dias).
Dipirona 1g EV de 4/4 horas. Metoclopramida 10mg EV 8/8 horas. Omeprazol 20–40mg VO/EV pela manhã."""}])

C(title="Encefalopatia hipertensiva", cid="I67.4", block="NEURO", sev="vermelha",
  nota="Excluir IAM, AVC, dissecção de aorta, trauma. ECG, Rx tórax, Urina I, creatinina, eletrólitos, marcadores cardíacos (s/n), TC crânio (s/n).",
  rx=[{"dest":"ps","label":"","text":"""Dieta zero. Ringer lactato 20ml/kg EV em 24 horas se necessário.
Abaixar 15% da PA na 1ª hora: Nitroprussiato de sódio 1 amp (50mg/2ml) + 250ml SG5% — iniciar infusão 5–10ml/hora.
Dipirona 1g EV de 6/6 horas se dor.
Bromoprida 10mg EV de 8/8 horas se náusea/vômito.
Omeprazol 40mg EV 1x pela manhã."""}])

# ---------- OLHOS ----------
C(title="Conjuntivite", cid="H10", block="OLHOS", sev="verde",
  exame="Olho [D/E] com hiperemia conjuntival discreta, sem secreção purulenta evidente. Sem edema periorbitário importante.",
  rx=[{"dest":"casa","label":"Uso oftalmológico","text":"""Tobramicina 0,3% solução oftálmica — 1 frasco
Aplicar 1 gota no olho acometido, de 6/6 horas, por 7 dias.

Colírio lubrificante (Systane, Lacrifilm ou Lacrima)
Pingar 1 gota no olho afetado de 4/4 horas.

Soro fisiológico 0,9%
Aplicar compressa gelada com soro fisiológico 4x ao dia no olho afetado."""},
      {"dest":"casa","label":"Uso oral","text":"""Loratadina 10mg — 7 comprimidos
Tomar 1 comprimido à noite por até 7 noites.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas se dor."""}])

C(title="Calázio", cid="H00.1", block="OLHOS", sev="verde",
  rx=[{"dest":"casa","label":"Uso oftalmológico","text":"""Tobramicina 0,3% pomada
Aplicar 1 cm da pomada 2x ao dia por 5 dias.

Compressas mornas por 10 minutos 4x ao dia com massagem suave sobre a lesão."""}])

C(title="Celulite periorbitária / pré-septal", cid="H05", block="OLHOS", sev="amarela",
  nota="Compressas quentes na área inflamada 3x ao dia. Excluir celulite septal (TC).",
  rx=[{"dest":"casa","label":"","text":"""Amoxicilina + clavulanato 500mg — 30 comprimidos
Tomar 1 comprimido de 8/8 horas por 10 dias.
OU
Moxifloxacino 400mg — 10 comprimidos
Tomar 1 comprimido 1x ao dia por 10 dias."""}])

C(title="Queimadura ocular (abrasão / química)", cid="T26", block="OLHOS", sev="amarela",
  nota="Lavar olho com SF 0,9% 1 litro. Colírio anestésico. Avaliação oftalmo.")

C(title="Neurite óptica", cid="H46", block="OLHOS", sev="amarela",
  nota="Solicitar hemograma, ureia, creatinina, Na, K e TC de crânio sem contraste. Avaliação oftalmo e neurologista.",
  rx=[{"dest":"internacao","label":"Na internação","text":"""Dieta oral branda.
Metilprednisolona 1g + SF 400ml EV — infundir em 30–60 minutos, por 3–5 dias.
Dipirona 1–2g EV de 6/6 horas.
Metoclopramida 10mg EV + AD, de 8/8 horas, se náusea ou vômito.
Omeprazol 20–40mg VO/EV de 24/24 horas, pela manhã."""}])

C(title="Herpes zoster oftálmico", cid="B02.3", block="OLHOS", sev="amarela",
  nota="Compressas geladas; deixar a pele seca.",
  rx=[{"dest":"casa","label":"","text":"""Aciclovir 400mg
Tomar 2 comprimidos de 4/4 horas por 7 dias.

Prednisona 20mg
Tomar 2 comprimidos 1x ao dia."""}])
