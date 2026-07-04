# -*- coding: utf-8 -*-
# METAB + HEMATO + GERAL/CRÍTICO + PSIQ + BONUS

# ---------- METAB ----------
C(title="Hiperglicemia", cid="R73.9", block="METAB", sev="amarela",
  nota="Cuidado com CAD e EHH!",
  rx=[{"dest":"ps","label":"Insulina regular SC conforme glicemia capilar","text":"""Glicemia 150–250: 2 UI
Glicemia 250–300: 4 UI
Glicemia 300–350: 6 UI
Glicemia 350–400: 8 UI
Glicemia >400: 10 UI"""}])

C(title="Hipoglicemia", cid="E16.2", block="METAB", sev="amarela",
  rx=[{"dest":"ps","label":"","text":"""Glicose hipertônica 50%: 4 a 6 amp EV (começar com 4).
Sem acesso venoso (incomum): Glucagon 1mg IM.
Hepatopatas, etilistas, desnutridos: Tiamina 100mg EV."""}])

C(title="Hipopotassemia", cid="E87.6", block="METAB", sev="amarela",
  rx=[{"dest":"casa","label":"Leve","text":"""KCl xarope 6%
Tomar 15ml VO de 8/8 horas.
OU
Cloreto de potássio 600mg
Tomar 1 comprimido de 8/8 horas."""},
      {"dest":"ps","label":"Moderado/grave (K <3)","text":"""KCl 19,1% 15 ml (1,5 ampola) + SF 0,9% 1 litro — EV em BIC 250 ml/h por 4 horas."""}])

C(title="Hiperpotassemia", cid="E87.5", block="METAB", sev="vermelha",
  rx=[{"dest":"ps","label":"Se ECG alterado","text":"""Gluconato de cálcio 10% 10ml + SG5% 100ml EV em BIC em 2–3 min.
Insulina regular 10 UI + SG10% 500ml EV em BIC em 60 minutos.
OU nebulização com salbutamol: 10 gotas + 3ml SF — repetir até 3x.
OU Furosemida (20mg/2ml): 1 amp de 12/12h."""}])

C(title="Hiponatremia", cid="E87.1", block="METAB", sev="vermelha",
  rx=[{"dest":"ps","label":"Grave (<120) e aguda","text":"""SF 0,9% 445 ml + NaCl 20% 55ml — infundir em BI durante 12 horas.
Solicitar Na após."""}])

C(title="Cetoacidose diabética", cid="E14.1", block="METAB", sev="vermelha",
  nota=("Dextro, gasometria arterial, Urina I, Na, K, hemograma, ureia, creatinina, ECG. "
        "Glicemia capilar 1/1h (estável por 3h → 2/2h). Ureia/creatinina/Na/K de 2/2h até estabilização. Internar."),
  rx=[{"dest":"internacao","label":"Reposição volêmica / eletrólitos","text":"""Dieta zero. 15–20 ml/kg SF0,9% na primeira hora.
Após exames — Na normal-alto: NaCl 0,45% 250–500ml/h; Na baixo: NaCl 0,9% 250–500ml/h.
Quando glicemia = 200: soro glicosado 5% + NaCl 0,45% 150–250ml/h.
K <3,3: KCl 10% (1g/10ml) 10ml + NaCl 0,45% 100ml — 20–40 mEq/h até K >3,3 (NÃO dar insulina).
K entre 3,3 e 5,5: KCl 10% 10ml + NaCl 0,45% 100ml — 20–30 mEq em cada litro EV.
K >5,5: dosar novamente em 2 horas.
Se pH <6,9: bicarbonato de sódio 8,4% (1mEq/ml) 100ml + SF0,9% 400ml — correr em 2 horas."""},
      {"dest":"internacao","label":"Insulina","text":"""Grave: Insulina regular (100UI/ml) 1ml + 99ml SF0,9% (1 UI/ml) — 0,1 UI/kg em bolus; após 0,1 UI/kg/h EV em BI (titular). Quando glicemia = 200: 0,02–0,05 UI/kg/h.
Leve-moderado: Insulina regular 0,3 UI/kg SC dose única; após 0,2 UI/kg SC de 2/2h. Quando glicemia = 200: 0,1 UI/kg SC 2/2h.
Dipirona 1g EV 6/6h. Bromoprida 10mg EV 8/8h. O2 se necessário."""}])

C(title="Estado hiperglicêmico hiperosmolar", cid="E14", block="METAB", sev="vermelha",
  nota="Dextro, gasometria arterial, Urina I, Na, K, hemograma, ureia, creatinina, ECG. Glicemia capilar 1/1h. Ureia/creatinina/Na/K de 2/2h. Internar.",
  rx=[{"dest":"internacao","label":"","text":"""Dieta zero. SF0,9% 15–20 ml/kg na primeira hora.
Após exames — Na normal-alto: NaCl 0,45% 150–250 ml/h.
Quando glicemia = 300: solução glicosada 5% 150ml + SF 150ml — infundir 150 ml/h.
K <3,3: KCl 10% (1g/10ml) 10ml + NaCl 0,45% 100ml — 20–40 mEq/h até K >3,3 (NÃO dar insulina).
K entre 3,3 e 5,5: KCl 10% 10ml + NaCl 0,45% 100ml — 20–30 mEq por litro EV.
Insulina regular (100UI/ml) 1ml + 99ml SF0,9% — 0,1 UI/kg bolus; após 0,1 UI/kg/h EV em BI. Quando glicemia = 300: 0,5 a 1,0 UI/h EV.
Dipirona 1g EV 6/6h. Bromoprida 10mg EV 8/8h."""}])

C(title="Rabdomiólise", cid="M62", block="METAB", sev="amarela",
  nota=("Hemograma, ureia, creatinina, fósforo, K, Ca, TGO, TGP, GGT, glicose, ácido úrico, gasometria venosa, CPK, Urina I, ECG. "
        "CPK <3000 sem disfunção renal: hidratação + CPK diário. CPK >5000 e lesão renal: internação, SF/Ringer, "
        "monitorar débito urinário, corrigir distúrbios (hipercalemia, hipocalcemia, hiperfosfatemia)."))

# ---------- HEMATO ----------
C(title="Anemia ferropriva", cid="D50.9", block="HEMATO", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Sulfato ferroso (200mg ferro elementar)
Tomar 1 comprimido 1x ao dia, 30 minutos antes ou 60 minutos após as refeições. De preferência com suco de laranja."""}])

C(title="Anemia megaloblástica", cid="D51", block="HEMATO", sev="verde",
  rx=[{"dest":"casa","label":"Vitamina B12","text":"""Cianocobalamina 2500 mcg/ml
Aplicar 5000 mcg IM a cada 7 dias por 4 semanas; após, 5000 mcg IM a cada 30 dias por 2 meses.
OU
Cianocobalamina 1000mcg
Tomar 1 comprimido 1x ao dia."""},
      {"dest":"casa","label":"Ácido fólico","text":"""Ácido fólico 5mg
Tomar 1 comprimido 1x ao dia."""}])

C(title="Epistaxe", cid="R04.0", block="HEMATO", sev="amarela",
  nota=("Avaliar sinais de trauma → ABCD, imagem. Avaliar uso de AAS/Clopidogrel/Marevan e HAS descontrolada. "
        "Manter paciente sentado com cabeça levemente fletida. Tampão anterior: gaze + pinça Kelly + 1 amp adrenalina "
        "(ou ácido tranexâmico 50mg/ml 5–10ml) + xylocaína gel. Se não melhorar: ácido tranexâmico 1 amp + 250ml SF 0,9% "
        "correr em 10–30 min. Observação e encaminhar especialista."))

C(title="Neutropenia febril", cid="D72.9", block="HEMATO", sev="vermelha",
  nota="Hemograma, função renal, eletrólitos, função hepática, PCR, lactato, hemocultura. MASCC score para definir local de tratamento.",
  rx=[{"dest":"casa","label":"Ambulatorial","text":"""Amoxicilina + clavulanato 875/125mg
Tomar 1 comprimido de 12/12 horas.

Ciprofloxacino 500mg
Tomar 1 comprimido de 12/12 horas.
OU
Levofloxacino 500mg
Tomar 1 comprimido 1x ao dia."""},
      {"dest":"internacao","label":"Internação","text":"""Cefepime 2g 8/8 horas
OU Meropenem 1g 8/8 horas
OU Tazocin 4,5g 6/6 horas.
Se infecção cutânea: acrescentar Vancomicina 2g 8/8 horas.
Se diarreia por Clostridium: Vancomicina 500mg VO."""}])

C(title="Crise álgica falcêmica", cid="D57", block="HEMATO", sev="vermelha",
  nota="Síndrome torácica aguda: SF 0,9% 2 a 3L/24h; se Sat <90%: O2; Ceftriaxona 2g 1x/dia EV + Azitromicina 500mg 1x/dia VO.",
  rx=[{"dest":"ps","label":"","text":"""SF 0,9% 500ml (3 a 5L/24h).
Leve: Dipirona 1g EV.
Moderada: Tramadol 100mg + 100ml SF 0,9% + Bromoprida EV lento.
Intensa: Morfina (2mg/2ml) 2ml, repetir em 5 min se não melhorar."""}])

C(title="Transfusão de hemoderivados", cid="", block="HEMATO", sev="amarela",
  rx=[{"dest":"ps","label":"Hemácias","text":"""Concentrado de hemácias (1 unidade aumenta 1 Hb e 3% Ht) — nos primeiros 30 min, 15 gotas/min (média 1–2 horas).
Dipirona 500mg – 1g EV de 6/6 horas.
Metoclopramida 10mg/2ml – 1 amp EV.
Se histórico de reação alérgica: Difenidramina 50mg/ml – 10–50mg IM profunda ou EV em 5–30 min OU Prometazina 25mg/ml – 1 amp IM.
Dosar Hb/Ht em 1–2 horas."""},
      {"dest":"ps","label":"Plaquetas","text":"""Concentrado de plaquetas (50–60ml/bolsa) – 1 unidade/10kg – infundir em 30 minutos.
Dipirona 500mg – 1g EV de 6/6 horas.
Metoclopramida 10mg/2ml – 1 amp EV."""}])

# ---------- GERAL / CRÍTICO ----------
C(title="Sepse", cid="A41", block="GERAL", sev="vermelha",
  nota="Suspeita: SOFA e NEWS — hemograma, creatinina, bilirrubina. Ao internar: hemocultura e urocultura.",
  rx=[{"dest":"ps","label":"Alta suspeição","text":"""Gasometria, lactato e culturas. Antibiótico: ligar CCIH do hospital.
Cristaloide 30ml/kg em 3h — alíquotas de 500ml.
Se necessário: Noradrenalina (1mg/ml) 20ml + 80ml SG 5% EV em BIC (começar 10ml/h).
Dipirona (500mg/ml): 1–2g 6/6h.
Bromoprida (10mg/2ml): 10mg EV 8/8h.
Omeprazol (40mg/ml): 20–40mg EV/VO pela manhã."""}])

C(title="Anafilaxia", cid="T78", block="GERAL", sev="vermelha",
  rx=[{"dest":"ps","label":"","text":"""Adrenalina (1mg/ml): 0,3–0,5 mg IM — repetir 5/5 min por mais 2x se necessário.
Sala de emergência. MOV. Dieta zero. Ringer lactato 500ml EV.
Hidrocortisona (100mg/frasco): 300mg + SF 0,9% 10 ml.
Se broncoespasmo: nebulização Salbutamol (5mg/ml) 10–20 gotas + 3ml SF 0,9%."""},
      {"dest":"ps","label":"Refratariedade","text":"""Adrenalina 0,1ml + 9ml SF EV em bolus.
Adrenalina 10 amp + 90ml SG5% em BIC — começar 4ml/hora em acesso central."""}])

C(title="Intoxicação exógena", cid="Y19.9", block="GERAL", sev="vermelha",
  nota="MOV (O2 se Sat <94%), ABCD, ligar Ceatox 0800 014 8110. Hemograma, EAS, função renal, Na, K, Ca, Mg, gasometria arterial, ECG.",
  rx=[{"dest":"ps","label":"Descontaminação / antídotos","text":"""Carvão ativado 1g/kg (máx 50g) — até 2 horas da ingestão, VO ou SNE. Manter: 50g 4/4 horas.
AAS/tricíclicos/fenobarbital: Bicarbonato de sódio 1–2 mEq/kg (ampola 8,4%, 1ml=1mEq) EV bolus; após 150ml de bicarbonato + 1L SG5% contínuo 100–200ml/h.
Organofosforados/carbamatos: Atropina 2mg EV a cada 5 min até sumir roncos.
Opioides: Naloxona 0,4mg EV, repetir a cada 3 min aumentando a dose (0,8/2/4/6).
Benzodiazepínicos: Flumazenil 0,1mg EV bolus.
Cocaína/anfetamina/crack: Diazepam EV.
Paracetamol: N-acetilcisteína 140mg/kg; manter 17 doses de 70mg/kg 4/4 horas."""}])

C(title="Dengue / Arbovirose", cid="A90", block="GERAL", sev="amarela",
  alarmes=("Sinais de alarme (surgem na DEFERVESCÊNCIA, 3º–6º dia): dor abdominal intensa e contínua, vômitos persistentes, "
           "sangramento de mucosas, letargia/irritabilidade, hipotensão postural/lipotimia, hepatomegalia dolorosa, "
           "Ht subindo com plaquetas caindo."),
  nota=("Colher NS1 em até 5 dias de sintomas (de preferência no 3º). EVITAR AINE e AAS (risco de sangramento) — "
        "usar dipirona/paracetamol. Paciente em uso de AAS: hemograma diário; suspender se plaquetas <30.000. "
        "Repouso e aumento de ingestão de líquidos."),
  rx=[{"dest":"casa","label":"Sem alarme","text":"""Soro de reidratação oral — 4 envelopes
Diluir 1 envelope em 1 litro de água e beber durante o dia. Beber mais 3 litros de outros líquidos.

Dipirona 1g
Tomar 1 comprimido de 6/6 horas se dor ou febre.
OU
Paracetamol 500mg
Tomar 1 comprimido de 6/6 horas se dor ou febre.

Desloratadina 5mg
Tomar 1 comprimido 1x ao dia se coceira.

Dramin B6
Tomar 1 comprimido de 8/8 horas se náusea, vômito ou tontura.
OU Ondansetrona 8mg — 1 comprimido de 8/8h se náusea/vômito por 5 dias."""},
      {"dest":"ps","label":"Grupo C/D","text":"""Hemograma, albumina, transaminases, PCR. Se necessário: Rx tórax, USG abdominal.
10ml/kg SF0,9% EV. Reavaliar. Mais 10ml/kg SF0,9% EV."""}])

C(title="Febre maculosa", cid="A77", block="GERAL", sev="amarela",
  flags=["'Dipirona 50mg 6/6h' no bloco oral — provável 500mg (typo)."],
  nota="Solicitar hemograma, Na, K, creatinina, TGP, TGO.",
  rx=[{"dest":"casa","label":"","text":"""Doxiciclina 100mg
Tomar 1 comprimido de 12/12 horas por 7 dias (ou até 7 dias após parar a febre).

Dipirona 500mg
Tomar 1 comprimido de 6/6h se dor ou febre.

Dramin B6
Tomar 1 comprimido de 8/8h se náusea ou vômito."""},
      {"dest":"internacao","label":"Se internação","text":"""SF 0,9% 30ml/kg EV em 24h.
Doxiciclina 100mg EV de 12/12 horas (manter por 3 dias após término da febre).
Dipirona 1g EV 4/4h se dor ou febre.
Bromoprida 10mg/2ml EV de 8/8h se náusea ou vômito."""}])

C(title="Leptospirose", cid="A27", block="GERAL", sev="amarela",
  nota="Hemograma, ureia, creatinina, Na, K, TGO, TGP, bilirrubina, VHS, PCR, Urina I, CPK, sorologia. Repouso, hidratação, evitar aspirina.",
  rx=[{"dest":"casa","label":"","text":"""Doxiciclina 100mg — 14 comprimidos
Tomar 1 comprimido de 12/12 horas por 7 dias.

Dipirona 500mg
Tomar 1 a 2 comprimidos de 6/6 horas se dor ou febre.

Bromoprida 10mg
Tomar 1 comprimido de 8/8 horas se náusea ou vômito."""}])

C(title="Acidente escorpiônico", cid="T63", block="GERAL", sev="amarela",
  nota="Leve: infiltração de anestésico sem vasoconstrictor, observação 4h, compressa morna. Limpar com água e sabão.",
  rx=[{"dest":"ps","label":"Moderado / grave","text":"""Moderado: monitorização; soro antiescorpiônico (5ml) 3 amp EV (ou antiaracnídico 3 amp EV); observação 24h.
Grave: soro antiescorpiônico (5ml) 6 amp EV (ou antiaracnídico 6 amp EV); internação."""}])

C(title="Acidente botrópico (jararaca)", cid="T63", block="GERAL", sev="vermelha",
  nota="Manter diurese 30–40 ml/hora; elevação do membro. Complicações: fasciotomia / desbridamento / drenagem.",
  rx=[{"dest":"ps","label":"","text":"""Soro antibotrópico (5mg/ml):
Leve: 2–4 amp EV
Moderado: 4–8 amp EV
Grave: 12 amp EV.
Se infecção secundária: Cloranfenicol 50–100 mg/kg/dia VO/EV 6/6 horas.
Dipirona 1g EV 6/6 horas."""}])

C(title="Acidente por aranha marrom", cid="T63", block="GERAL", sev="amarela",
  rx=[{"dest":"ps","label":"","text":"""Leve–moderado: Prednisona 20mg — 2 comprimidos pela manhã por 5 dias.
Grave: 5 amp SAAr EV (em até 36h da picada) + Prednisona 20mg 2 cp/manhã por 5 dias.
Muito grave: 10 amp SAAr EV + Prednisona 20mg 2 cp/manhã por 5–7 dias."""}])

C(title="Relação sexual desprotegida / Violência sexual (PEP)", cid="Z20.2", block="GERAL", sev="vermelha",
  nota="Teste rápido HIV, sífilis, hepatite B e C. Checar vacina hepatite B. PEP até 72 horas.",
  rx=[{"dest":"ps","label":"","text":"""Tenofovir/Lamivudina 300mg + 300mg — 1 comprimido ao dia por 28 dias.
Dolutegravir 50mg — 1 comprimido ao dia por 28 dias.
Levonorgestrel 1,5mg (até 72 horas) — 1 comprimido VO.
Penicilina G benzatina 2.400.000 UI IM — 1.200.000 em cada glúteo.
Ceftriaxona 500mg IM.
Azitromicina 500mg — 2 comprimidos VO.
Metronidazol 400mg — 5 comprimidos VO."""}])

C(title="Dor de dente", cid="K08.8", block="GERAL", sev="verde",
  anamnese=("PACIENTE REFERE DOR DE DENTE HÁ [X] DIA(S). Nega febre ou outros sintomas sistêmicos. "
            "Informo que não há dentista na unidade e oriento buscar UPA com suporte odontológico."),
  exame=("Bom estado geral, corado, hidratado, acianótico, anictérico, afebril.\n"
         "Sem edema, hiperemia ou alterações visíveis. Cavidade oral sem secreção purulenta evidente."),
  nota="Orientar retorno se febre, edema local, trismo ou piora da dor.",
  rx=[{"dest":"casa","label":"","text":"""Dipirona 500mg — 20 comprimidos
Tomar via oral 2 comprimidos de 6 em 6 horas se dor ou febre.

Diclofenaco 50mg — 10 comprimidos
Tomar 1 comprimido de 8 em 8 horas por 5 dias."""}])

# ---------- PSIQ ----------
C(title="Abstinência alcoólica", cid="F10.3", block="PSIQ", sev="vermelha",
  nota="Hemograma, glicemia, ureia, creatinina, TGO, TGP, amilase, lipase.",
  rx=[{"dest":"ps","label":"","text":"""Diazepam 10mg — 1 comprimido a cada hora até melhora (máx 40mg/dia).
OU Lorazepam 2mg — 1 comprimido a cada hora até melhora (máx 10mg/dia).
E Tiamina 100–250mg EV/IM 1x/dia por 3 dias.
Se hipoglicemia (fazer tiamina antes): Glicose hipertônica 50% 4 amp EV.
Delirium tremens: Diazepam 5–10mg EV a cada 5–10 min (máx 20mg/dia).
Refratário: Fenobarbital 130–260mg EV a cada 15 min até melhora (máx 15 mg/kg/dia)."""}])

# ---------- BONUS ----------
C(title="Templates — anamnese / EF / evolução", cid="", block="BONUS", sev="amarela",
  nota="Esqueleto universal: copiar e editar. Sempre documentar SSVV na alta, alarmes pesquisados e negativos, orientação de retorno compreendida.",
  rx=[{"dest":"outro","label":"Anamnese direcionada","text":"""QP: [queixa] há [tempo].
HDA: [início, evolução, intensidade, fatores de melhora/piora, sintomas associados].
Nega: [sinais de alarme da queixa].
APP: [comorbidades, medicações de uso, alergias]."""},
      {"dest":"outro","label":"Exame físico direcionado","text":"""BEG, [afebril/febril], corado, hidratado, acianótico, anictérico.
SSVV: PA __/__ | FC __ | FR __ | SatO2 __% | Tax __°C.
Direcionado: [achados relevantes à queixa]."""},
      {"dest":"outro","label":"Exame físico completo","text":"""BEG, corado, hidratado, acianótico, anictérico, afebril.
Neuro: Glasgow 15, pupilas isofotorreagentes, sem déficits focais, sem sinais meníngeos.
ACV: 2 BRNF, sem sopros audíveis.
AR: MV+ bilateralmente, sem ruídos adventícios.
Abdome: flácido, indolor à palpação, RHA+, sem visceromegalias ou massas.
Membros: sem edema, sem dor à palpação, sem sinais de TVP, TEC <3s, pulsos amplos e simétricos.
Orofaringe sem alterações. Otoscopia: MT translúcida, sem abaulamentos."""},
      {"dest":"outro","label":"Evolução / conduta","text":"""# [Diagnóstico / hipótese]
HDA: [resumo]. Nega [alarmes pesquisados].
EF: [SSVV + direcionado].
Conduta: Prescrevo sintomáticos na unidade. Prescrevo sintomáticos para domicílio.
Oriento sinais de alarme e retorno se necessário. Compreendeu. Alta em BEG."""}])

C(title="Exames laboratoriais", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"outro","label":"ISTs","text":"""HBsAg · Anti-HCV · Anti-HIV 1 e 2 · Anti-HBc total · Anti-HBs · anticorpos anti-gonococo IgM e IgG · Chlamydia trachomatis IgM e IgG · VDRL."""},
      {"dest":"outro","label":"Rotina","text":"""Hemograma · ureia · creatinina · Na · K · TGO · TGP · glicemia de jejum · triglicérides · colesterol total e frações · 25-OH vitamina D · vitamina B12 · TSH · T4 livre · ferritina.
>50 anos: sangue oculto nas fezes e mamografia. Mulheres >65a / homens >70a / fatores de risco: densitometria óssea. DM: hemoglobina glicada."""}])

C(title="Bulário rápido por sintoma", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"outro","label":"Expectorante","text":"""Ambroxol xarope sem açúcar — 5ml 3x ao dia por 5 dias.
Acetilcisteína 600mg — 1x à noite por 5 noites (ou xarope 40mg/ml 15ml à noite; ou envelope 600mg/5g à noite).
Vick 44E xarope — 15ml de 6/6 horas."""},
      {"dest":"outro","label":"Tosse seca / antitussígeno","text":"""Seki xarope — 10ml 3x ao dia por 5 dias.
OU Cloperastina 3,54mg/ml — 10ml 3x ao dia por 5 dias.
Dropropizina 3mg/ml — 10ml 4x ao dia."""},
      {"dest":"outro","label":"Dor de garganta","text":"""Strepsils/Flogoral pastilha — 1 pastilha sempre que necessário.
Cloridrato de benzidamina pastilha — 1 pastilha VO de até 3/3 horas se dor de garganta."""},
      {"dest":"outro","label":"Resfriado (combinados)","text":"""Coristina D / Cimegripe / Resfenol (paracetamol, clorfeniramina, fenilefrina) — 1 cp de 6/6 horas.
Neolefrin (fenilefrina, carbinoxamina, paracetamol) — 1 cp de 8/8 horas.
Benegripe (dipirona, clorfeniramina, cafeína) — 3x ao dia.
Decongex Plus — 10 a 15ml 3x ao dia."""},
      {"dest":"outro","label":"AINE + protetor / pomada","text":"""Nivux — 1 cp de 12/12 horas por 3 dias.
Trok-N pomada — aplicar fina camada sobre lesão 1–2x por dia, por 7–10 dias."""}])

C(title="Intubação orotraqueal (70 kg)", cid="", block="BONUS", sev="vermelha",
  rx=[{"dest":"ps","label":"Sequência rápida","text":"""MOV. Preparo: checar aspirador; materiais (laringoscópio 3 ou 4, tubo 7 ou 7,5, ambu, guedel, seringa 20ml) e drogas; posicionar.
Pré-oxigenação: máscara não reinalante ou bolsa-válvula 10 a 12 L/min por 3 a 5 minutos.
Analgesia: Fentanil (2mg/ml – 10ml): 3 a 4ml EV em bolus lento.
Hipnótico: Etomidato (10ml): 10ml EV (0,2 a 0,4 mg/kg) OU Quetamina (10ml): 3–4ml OU Propofol (20ml): 10–15ml OU Midazolam (10ml): 3–4ml.
Bloqueador neuromuscular: Succinilcolina (10mg/ml): misturar o pó em 10ml SF, aspirar tudo (1 a 1,5mg/kg) OU Rocurônio (5ml): 7ml EV.
IOT: checar ausculta.
Ventilador: Modo VCV, FiO2 100%, PEEP 6 a 10, FR 16, Tinsp 1,0, VC (4–6 ml/kg predito) ≈ 420 ml.
Sedação em BIC: Fentanil 4 amp + 500ml SF a 10 ml/h E Midazolam 4 amp + 500ml SF a 10 ml/h."""}])

C(title="Drenagem de abscesso", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"outro","label":"","text":"""Separar material. Clorexidina alcoólico. Campo operatório.
Anestesia local (agulha marrom ou preta, mais finas).
Incisão pequena com lâmina 11 + Kelly para ampliar se necessário. Drenagem.
Colocar gaze dentro da loja se não houver drenagem espontânea.
Curativo: gaze + micropore."""}])

C(title="Prescrição de Ceftriaxona", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"outro","label":"","text":"""Ceftriaxona 2g + 100ml SF 0,9% EV 1x ao dia — correr em 30 minutos.
Duração: ___  Data de início: ___"""}])

C(title="Internação — prescrição padrão", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"internacao","label":"Modelo","text":"""Dieta.
SF 0,9% 500ml EV, ACM.
Soro glicofisiológico 500ml EV, ACM.
Dipirona 1g 6/6h, se dor ou febre.
Tramal 100mg 6/6h, a critério médico.
Metoclopramida 8/8h, se náusea ou vômito.
Omeprazol 40mg VO/EV 1x ao dia.
Lactulose 667mg/ml 10ml de 12/12h, se constipação.
Enoxaparina 40mg SC 24/24h.
Controle dos sinais vitais 6/6h. Cabeceira elevada 30°.
Se DM ou NPO: dextro; insulina regular conforme dextro; glicose 50% se hipoglicemia.
Exames laboratoriais e de imagem. Se quadro infeccioso: urocultura e hemocultura."""}])
