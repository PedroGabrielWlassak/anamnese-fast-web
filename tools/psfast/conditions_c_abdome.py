# -*- coding: utf-8 -*-
# ABDOME / GASTRO

C(title="GECA / Gastroenterite (adulto)", cid="A09", block="ABDOME", sev="verde",
  anamnese=("PACIENTE REFERE DIARREIA HÁ [X] DIA(S). Nega febre, nega sangue nas fezes, nega vômitos persistentes, "
            "nega incapacidade de ingerir líquidos, nega redução da diurese, nega tontura, nega síncope, "
            "nega dor abdominal intensa, nega distensão abdominal e nega prostração importante.\n"
            "#Medicamentos de uso contínuo: nega  #Comorbidades: nega  #Alergias: nega  #Gestação: [avaliar]"),
  exame=("Bom estado geral, corado, hidratado, acianótico, anictérico, afebril.\n"
         "Abdome discretamente distendido, plano, dor discreta à palpação difusa, sem defesa ou rigidez."),
  nota="Zinco (criança): <5 anos 20mg/dia por 10 dias; <6 meses 10mg/dia por 10 dias.",
  rx=[{"dest":"casa","label":"","text":"""Soro de hidratação oral — 4 sachês
Diluir 1 sachê em 1L de água filtrada e tomar 1 copo a cada evacuação. Armazenar em geladeira, descartar no dia seguinte. Manter até melhora completa.

Dipirona 500mg — 20 comprimidos
Tomar 1 comprimido de 6/6 horas se dor ou febre.

Buscopan composto — 1 caixa
Tomar 1 comprimido de 6/6 horas se dor ou cólica.

Metoclopramida 10mg — 10 comprimidos
Tomar 1 comprimido de 8/8 horas se náusea ou vômito.
OU
Ondansetrona 4mg sublingual — 1 caixa
Deixar 1 a 2 comprimidos abaixo da língua até dissolver, de 8/8 horas se náusea ou vômito.

Floratil — 1 caixa
Tomar 1 comprimido de 12/12 horas por 3 dias.

Racecadotrila 100mg
Tomar 1 comprimido de 8/8 horas até cessar a diarreia (até 3–5 dias), associado a hidratação oral.

Simeticona gotas — 1 frasco
Tomar 50 gotas de 8/8 horas se gases."""},
      {"dest":"casa","label":"Se epigastralgia","text":"""Omeprazol 20mg — 28 comprimidos
Tomar 1 comprimido 1x ao dia, em jejum, aguardar 30 min para alimentar, por 14 dias."""},
      {"dest":"casa","label":"Se precisar de ATB","text":"""Ciprofloxacino 500mg — 6 comprimidos
Tomar 1 comprimido de 12/12 horas por 3 dias.
OU
Sulfametoxazol-trimetoprima 800/160mg
Tomar 1 comprimido de 12/12 horas por 3 a 5 dias."""}])

C(title="Disenteria", cid="A09", block="ABDOME", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Ciprofloxacino 500mg
Tomar 1 comprimido de 12/12 horas por 3–5 dias.
OU
Azitromicina 1g
Tomar 1 comprimido, dose única.
OU
Azitromicina 500mg
Tomar 1 comprimido 1x ao dia por 3–5 dias.

Albendazol 400mg
Tomar 1 comprimido 1x ao dia por 3 dias (associar se indicado)."""}])

C(title="Colite pseudomembranosa", cid="A04.7", block="ABDOME", sev="amarela",
  nota="Hemograma, ureia, creatinina, Na, K, albumina.",
  rx=[{"dest":"casa","label":"","text":"""Metronidazol 250mg
Tomar 2 comprimidos de 8/8 horas por 10 dias.
OU
Vancomicina 125mg
Tomar 1 comprimido de 6/6 horas por 10 dias."""}])

C(title="DRGE / Gastrite", cid="K21 · K29", block="ABDOME", sev="verde",
  nota="Manter tratamento 4–8 semanas; não comer antes de deitar; evitar refeições volumosas; cessar tabagismo; evitar café/chocolate/álcool.",
  rx=[{"dest":"casa","label":"IBP","text":"""Omeprazol 20mg — 28 comprimidos
Tomar 2 comprimidos 1x ao dia, em jejum (30 min antes da refeição), por 14 dias.
OU
Pantoprazol 20mg
Tomar 1 a 2 comprimidos pela manhã.
OU
Dexlansoprazol (Dexilant) 30mg
Tomar 1 comprimido pela manhã, por 30 dias."""},
      {"dest":"casa","label":"Procinético / antiácido","text":"""Domperidona 10mg
Tomar 1 comprimido de 8/8 horas.
OU
Bromoprida 10mg
Tomar 1 comprimido de 8/8 horas.

Hidróxido de magnésio 60mg/ml
Tomar 5–10 ml VO 1 hora após as refeições e ao deitar.

Pepsamar (hidróxido de alumínio) 230mg — 1 caixa
Mastigar 2 comprimidos ao sentir azia intensa."""}])

C(title="Epigastralgia / Pirose", cid="R10.1 · K29", block="ABDOME", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Hidróxido de alumínio
Tomar 15 ml 3x ao dia, 15 minutos antes das principais refeições.
OU
Hidróxido de alumínio + hidróxido de magnésio + simeticona
Tomar 10 ml 4x ao dia, 1 hora antes das refeições.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas se dor.

Omeprazol 20mg
Tomar 1 comprimido 1x ao dia, pela manhã, por 10 dias.

Buscopan composto
Tomar 1 comprimido de 8/8 horas se dor.

Ondansetrona 4mg
Tomar 1 comprimido de 8/8 horas se náusea."""}])

C(title="Hemorroida", cid="I84", block="ABDOME", sev="verde",
  nota="Banho de assento: água morna por 15 min, 2x ao dia.",
  rx=[{"dest":"casa","label":"Uso oral","text":"""Plantago ovata (Metamucil/Fibermais/Muvinlax)
Tomar 1 a 3 sachês, diluídos em 200 ml de água.

Lactulose
Tomar 15 ml de 8/8 horas.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas se dor.

Cetoprofeno 100mg
Tomar 1 comprimido de 12/12 horas por 3–5 dias."""},
      {"dest":"casa","label":"Uso externo","text":"""Xyloproct pomada
Aplicar fina camada várias vezes ao dia na área afetada (ou usar o aplicador).
OU
Hidrocortisona creme 10mg/g
Aplicar fina camada na região afetada 2 a 3 vezes por dia, por no máximo 2 semanas."""}])

C(title="Constipação", cid="K59.0", block="ABDOME", sev="verde",
  nota="Se intensa: clister glicerinado 500ml agora.",
  rx=[{"dest":"casa","label":"1ª linha","text":"""Plantago ovata Forssk — 1 caixa
Diluir 1 envelope em 1 copo de água, 1x ao dia até melhora (pode repetir de 8/8h).
OU
Policarbofila cálcica 625mg
Tomar 1 comprimido de 12/12 horas, junto com as refeições.
OU
Óleo mineral
Tomar 1 colher de sopa (20 ml) de 12/12 horas.
OU
Lactulose 667 mg/mL — 1 frasco
Tomar 15 ml 1x ao dia até melhora (máx 60 ml/dia)."""},
      {"dest":"casa","label":"Se não melhorar","text":"""Polietilenoglicol 4000
Tomar 10g diluídos em água ou suco 1x ao dia.
OU
Hidróxido de magnésio 1200mg/15ml
Tomar 30 ml 1x ao dia.
OU
Bisacodil 5mg — 1 caixa
Tomar 1 comprimido 1x ao dia (ou 12/12h se resistência a outras medidas)."""}])

C(title="Parasitose", cid="B80", block="ABDOME", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Albendazol 200mg
Tomar 2 comprimidos, dose única."""}])

C(title="Enterobíase / Oxiurose", cid="B80", block="ABDOME", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Albendazol 400mg
Tomar (10mg/kg – máximo 400mg) 1x ao dia por 3 dias.

Dipirona 1g
Tomar 1 comprimido de 6/6 horas se dor ou febre.

Hidroxizina 25mg
Tomar 1 comprimido de 8/8 horas se coceira."""}])

C(title="Xerostomia", cid="R68.2", block="ABDOME", sev="verde",
  nota="Consumir acerola, limão, maçãs, peras; umedecer a cavidade oral com água filtrada ou gelo.",
  rx=[{"dest":"casa","label":"","text":"""Goma de mascar sem açúcar.

Pilocarpina 4% (40mg/ml)
Aplicar 3 gotas 3x ao dia, durante ou após as refeições.

Saliva artificial (Kin-Hidrat)
Usar conforme necessidade.

Dexpantenol
Aplicar nos lábios 2–3x ao dia."""}])

C(title="Soluço", cid="R06.6", block="ABDOME", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Clorpromazina 25mg
Tomar 1 a 2 comprimidos de 12/12 horas por 5 a 10 dias.
OU
Gabapentina 300mg
Tomar ½ comprimido de 8/8 horas por 5 a 10 dias.
OU
Bromoprida 10mg
Tomar 1 comprimido de 8/8 horas por 5 a 10 dias.
OU
Baclofeno 10mg
Tomar 1 comprimido de 12/12 horas por 5 a 10 dias."""}])

C(title="Candidíase oral", cid="B37", block="ABDOME", sev="verde",
  rx=[{"dest":"casa","label":"Uso tópico","text":"""Nistatina 100.000 UI/ml
Tomar 1 a 6 ml 4x ao dia por 7–14 dias. Bochechar e manter por vários minutos na cavidade oral antes de engolir."""}])

C(title="Afta", cid="K12.0", block="ABDOME", sev="verde",
  rx=[{"dest":"casa","label":"Uso local","text":"""Omcilon-A (triancinolona)
Aplicar pequena quantidade sobre a lesão 3x ao dia por 7 dias."""}])

C(title="Colecistite aguda", cid="K81", block="ABDOME", sev="vermelha",
  nota="Hemograma, PCR, Na, K, ureia, creatinina, TGO, TGP, bilirrubina total e frações, FA, gama GT, amilase, lipase, USG abdome superior. Sinais vitais 6/6h.",
  rx=[{"dest":"ps","label":"","text":"""Dieta zero. Ringer lactato 500ml EV.
Dipirona 1g EV 6/6h.
Cetoprofeno 100mg EV 12/12h.
Bromoprida 10mg EV 8/8h.
Ceftriaxona 2g EV 24/24h.
Metronidazol 500mg EV 8/8h."""}])

C(title="Diverticulite aguda", cid="K57", block="ABDOME", sev="vermelha",
  nota="Hemograma, PCR, Na, K, ureia, creatinina, TC abdome com contraste. Dieta sem resíduos (leve, sem sementes).",
  rx=[{"dest":"casa","label":"Não complicada","text":"""Ciprofloxacino 500mg
Tomar 1 comprimido de 12/12 horas por 7 dias.

Metronidazol 250mg
Tomar 2 comprimidos de 8/8 horas por 7 dias.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas se dor."""},
      {"dest":"ps","label":"Complicada","text":"""Dieta zero. Ringer lactato 500ml EV.
Ceftriaxona 2g EV 24/24h.
Metronidazol 500mg EV 8/8h.
Dipirona 1g EV 6/6h SN. Bromoprida 10mg EV 8/8h SN. Sinais vitais 6/6h."""}])

C(title="Pancreatite aguda", cid="K85", block="ABDOME", sev="vermelha",
  nota="Hemograma, FA, gama GT, TGO, TGP, bilirrubinas, amilase, lipase, PCR, glicemia, Na, K, USG abdominal e/ou TC abdome. SVD (quantificar diurese, ideal >0,5ml/kg/h). Sinais vitais 6/6h.",
  rx=[{"dest":"ps","label":"","text":"""Dieta zero (até melhora clínica).
Ringer lactato 1000ml EV agora.
Ringer lactato 500ml + 7 amp (10ml) glicose hipertônica 50% + 1 amp (10ml) KCl 8/8 horas.
Dipirona 1g EV 6/6 horas.
Cetoprofeno 100mg EV 12/12h.
Morfina 2mg/ml: 2–4ml 4/4h se necessário.
Ondansetrona 4mg/ml 8/8h EV."""}])

C(title="Abdome agudo obstrutivo", cid="K56.6", block="ABDOME", sev="vermelha",
  nota="Rx abdome agudo (tórax AP, abdome deitado e em pé), hemograma, PCR, ureia, creatinina, Na, K. Aguardar 24–36h ou chamar cirurgia. Se repercussão sistêmica (febre, taquicardia, leucocitose, prostração): chamar cirurgia.",
  rx=[{"dest":"ps","label":"Brida / aderência","text":"""Dieta zero. Sonda nasogástrica aberta.
Dipirona 2g EV 4/4h.
Tramal 100mg + Bromoprida 10mg EV, se necessário.
Luftal 125mg 4/4h VO ou SNG.
500ml SF 0,9% + 5 amp SG 50% + 1 amp NaCl 20% + 1 amp KCl 19,1% 6/6h.
Sinais vitais."""}])

C(title="Ingesta de corpo estranho", cid="T18.9", block="ABDOME", sev="amarela",
  nota=("Rx abdome (deitado e em pé) e tórax. Objeto perfurocortante/pilhas/bateria/grandes, objeto no esôfago, "
        "paciente sintomático → EDA + avaliação cirurgia. Outros: orientar sinais de alarme, retorno em 24–48h para novo Rx."))

C(title="Cólica biliar", cid="K80", block="ABDOME", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Dipirona 500mg — 40 comprimidos
Tomar 2 comprimidos de 6/6 horas se dor ou febre por 5 dias.
OU
Paracetamol 750mg — 40 comprimidos
Tomar 1 comprimido de 6/6 horas se dor ou febre por 5 dias.

Buscopan composto — 1 caixa
Tomar 1 comprimido de 6/6 horas se dor ou cólica.

Diclofenaco 50mg — 10 comprimidos
Tomar 1 comprimido de 12/12 horas se dor intensa por até 5 dias.

Tramadol 50mg — 12 comprimidos
Tomar 1 comprimido de 8/8 horas se dor muito intensa e resistente.

Ondansetrona 8mg sublingual — 1 caixa
Deixar 1 comprimido abaixo da língua até absorção, de 8/8 horas se náusea ou vômito.
OU
Metoclopramida 10mg — 10 comprimidos
Tomar 1 comprimido de 8/8 horas se náusea ou vômito."""}])

C(title="Hemorragia digestiva alta", cid="K92.2", block="ABDOME", sev="vermelha",
  nota="Monitorização. Concentrado de hemácias se Hb <7. Noradrenalina 4 amp + 254ml SG5% EV em BIC — iniciar 5–10ml/h (alvo PAM <65) se necessário. SVD (meta 0,5ml/kg/h). Solicitar EDA e UTI.",
  rx=[{"dest":"ps","label":"","text":"""Dieta zero. Ringer lactato 500ml EV agora (20–30ml/kg de ressuscitação)."""},
      {"dest":"ps","label":"HDA varicosa","text":"""Ceftriaxona 2g EV agora.
Terlipressina 2mg EV agora."""},
      {"dest":"ps","label":"HDA não varicosa","text":"""Omeprazol 40mg EV agora (manter de 12/12 horas)."""}])

C(title="Apendicite aguda (Alvarado)", cid="K35", block="ABDOME", sev="vermelha",
  alarmes="Dor que MIGRA para FID, anorexia, náusea/vômito, febre. Mulher jovem com dor em FID → sempre pensar em causa ginecológica (ectópica, cisto roto, DIP) e pedir beta-hCG.",
  nota=("Score de Alvarado (MANTRELS, 0–10): Migração 1 · Anorexia 1 · Náusea/vômito 1 · Dor à palpação FID 2 · "
        "Descompressão dolorosa 1 · Temperatura ≥37,3°C 1 · Leucocitose >10.000 2 · Desvio à esquerda 1. "
        "≤4 improvável (alta com retorno); 5–6 observação+imagem; 7–8 imagem+cirurgia; ≥9 cirurgia direta. "
        "Solicitar hemograma, PCR, Urina I, beta-hCG (toda mulher fértil), USG (jovens magros/crianças/gestantes) ou TC com contraste. "
        "Analgesia NÃO mascara o diagnóstico — pode/deve dar."),
  rx=[{"dest":"ps","label":"Conduta na unidade","text":"""Dieta zero. SF 0,9% ou Ringer lactato EV.
Dipirona 1g EV 6/6h se dor.
Ondansetrona 4mg EV 8/8h se náusea/vômito.
Se cirurgia indicada / suspeita perfuração → ATB pré-op: Ceftriaxona 2g EV 1x ao dia + Metronidazol 500mg EV 8/8h.
Avaliação/contato cirurgia geral."""}])
