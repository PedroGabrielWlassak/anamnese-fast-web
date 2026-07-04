# -*- coding: utf-8 -*-
# TÓRAX / CARDIO-PNEUMO

C(title="Tosse / SRAG", cid="", block="TORAX", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Vick 44E — 1 frasco
Tomar 15 ml de 8 em 8 horas se tosse persistente.
OU
Dropropizina 3mg/ml xarope 120 ml
Tomar 10 ml de 6 em 6 horas, por 3 dias.

Strepsils pastilhas — 1 caixa
Dissolver 1 pastilha na boca, 2 ou mais vezes ao dia, até alívio. Máximo 10/dia.

Oseltamivir 75mg — 10 comprimidos
Tomar 1 comprimido de 12 em 12 horas por 5 dias.

Loratadina 10mg — 7 comprimidos
Tomar 1 comprimido à noite por 7 dias."""}])

C(title="Bronquite", cid="J20", block="TORAX", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Beclometasona 200mcg
2 jatos de 12/12 horas por 7 dias ou até alívio dos sintomas.

Salbutamol 100mcg
2 jatos até de 4/4 horas, se crise.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas, se dor ou febre."""},
      {"dest":"casa","label":"Uso nasal","text":"""Lavagem nasal com soro fisiológico 0,9% — 1 frasco
Aplicar 1 seringa de 20ml em cada narina, 3x ao dia, até melhora.

Budesonida 64mcg spray nasal — 1 frasco
Aplicar 1 jato em cada narina de 12 em 12 horas por 10 dias."""}])

C(title="Coqueluche", cid="A37", block="TORAX", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Azitromicina 500mg — 5 comprimidos
Tomar 1 comprimido 1x ao dia por 5 dias.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas, se dor ou febre.

Bromoprida 10mg
Tomar 1 comprimido de 8/8 horas, se náusea ou vômito."""}])

C(title="Influenza / Gripe", cid="J11", block="TORAX", sev="amarela",
  nota="Oseltamivir: corrigir para função renal.",
  rx=[{"dest":"casa","label":"Antiviral","text":"""Oseltamivir 75mg
Tomar 1 comprimido de 12/12 horas por 5 dias."""},
      {"dest":"casa","label":"Sintomáticos","text":"""Dipirona 500mg — 20 comprimidos
Tomar via oral 2 comprimidos de 6 em 6 horas se dor ou febre.

Maleato de dexclorfeniramina 2mg/5ml
Tomar via oral 5 mL, 3x por dia, por 5 dias.

Cetoprofeno 100mg — 1 caixa
Tomar 1 comprimido de 12 em 12 horas por 5 dias.
OU
Prednisona 20mg
Tomar 1 comprimido pela manhã, por 5 dias.

Strepsils pastilhas — 1 caixa
Dissolver 1 pastilha na boca, 2 ou mais vezes ao dia, até alívio. Máximo 10/dia.

Acetilcisteína xarope 40 mg/mL
Tomar 15 mL antes de dormir, via oral, por 5 dias."""},
      {"dest":"casa","label":"Uso nasal","text":"""Lavagem nasal com soro fisiológico 0,9% — 1 frasco
Aplicar 1 seringa de 20ml em cada narina, 3x ao dia, até melhora.

Budesonida 64mcg spray nasal — 1 frasco
Aplicar 1 jato em cada narina de 12 em 12 horas por 10 dias."""}])

C(title="Pneumonia", cid="J18", block="TORAX", sev="vermelha",
  nota=("Solicitar Rx e laboratório. Internação se SatO2 <92%. CURB-65: 0–1 ambulatorial; "
        "≥2 considerar internação; ≥3 grave. Nebulização com SF 0,9%."),
  rx=[{"dest":"casa","label":"Ambulatorial","text":"""Amoxicilina + clavulanato 875/125mg — 20 comprimidos
Tomar 1 comprimido de 12/12 horas por 10 dias.
OU
Levofloxacino 500mg — 7 comprimidos
Tomar 1 comprimido 1x ao dia por 7 dias.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas, se dor ou febre.

Bromoprida 10mg
Tomar 1 comprimido de 8/8 horas, se náusea ou vômito."""},
      {"dest":"internacao","label":"Internação / paciente grave (PSI/PORT)","text":"""Solicitar: Rx tórax; hemograma, ureia, creatinina, eletrólitos. Avaliar necessidade de internação.
Levofloxacino 750mg: 1 amp 1x/dia
OU
Ceftriaxona 2g 1x/dia + Azitromicina 500mg 1x/dia EV
OU
Clavulin + Azitromicina 500mg 1x/dia EV
Glicemia capilar 4/4h. Se HGT <60: glicose hipertônica 50%. Insulina regular SOS."""}])

C(title="Asma — manutenção (GINA 2026)", cid="J45", block="TORAX", sev="amarela",
  nota=("CONCEITO-CHAVE: NÃO usar SABA (salbutamol) isolado como alívio. Todo paciente deve ter "
        "corticoide inalatório (CI). SABA sozinho = mais crises. Enxaguar a boca após CI (evita candidíase). "
        "STEP 5: encaminhar especialista (fenotipagem, LAMA, biológicos)."),
  rx=[{"dest":"casa","label":"Track 1 (preferido) — CI-formoterol","text":"""STEP 1–2: Budesonida + formoterol 200/6 mcg — inalar 1 cápsula/dose SE NECESSÁRIO (alívio anti-inflamatório).
STEP 3 (MART): Budesonida + formoterol 200/6 mcg — 1 dose de 12/12h (manutenção) + 1 dose SE NECESSÁRIO (mesma bombinha).
STEP 4 (MART): Budesonida + formoterol 200/6 mcg — 2 doses de 12/12h (manutenção) + 1 dose SE NECESSÁRIO (máx ~12 doses/dia)."""},
      {"dest":"casa","label":"Track 2 (alternativo) — só se Track 1 indisponível","text":"""STEP 1: CI dose baixa SEMPRE que usar o SABA.
STEP 2: CI dose baixa DIÁRIO (ex.: Budesonida 200mcg 1 dose 12/12h) + Salbutamol 100mcg 1–2 jatos SE NECESSÁRIO.
STEP 3: CI-LABA (formoterol/budesonida ou salmeterol/fluticasona) 12/12h + SABA SOS.
STEP 4: CI-LABA dose MÉDIA 12/12h + SABA SOS.

Add-on (qualquer step, se controle insuficiente): Montelucaste 10mg à noite."""}])

C(title="Crise de asma (exacerbação)", cid="J45", block="TORAX", sev="vermelha",
  alarmes="Fala entrecortada, uso de musculatura acessória, SatO2 <92%, sonolência/confusão, tórax silencioso → grave.",
  nota=("GINA 2026: PREFERIR salbutamol. Fenoterol passou a NÃO recomendado (risco cardiovascular/mortalidade). "
        "MgSO4 nebulizado sem benefício (usar EV)."),
  rx=[{"dest":"ps","label":"Na unidade","text":"""O2 se Sat <94% (meta 93–95%).
Salbutamol 100mcg: 4–10 jatos com espaçador de 20/20 min por 1 hora
+ Brometo de ipratrópio 20mcg: 4–8 jatos de 20/20 min por 1 hora.
OU nebulização: Salbutamol 10–20 gotas + ipratrópio 30–40 gotas + SF 0,9% 3ml.
Corticoide sistêmico precoce (até 1h): Prednisona 40–50mg VO OU Hidrocortisona 200mg EV.
Reavaliar após 1ª hora; se não melhorar, repetir broncodilatador."""},
      {"dest":"ps","label":"Crise grave / sem resposta","text":"""Sulfato de magnésio 2g EV + SF 0,9% 100–250ml — correr em 20 min (dose única).
Gasometria, considerar VNI, contato com retaguarda/UTI."""},
      {"dest":"casa","label":"Para casa","text":"""Prednisona 40mg/dia por 5–7 dias (criança 3–5 dias).

Formoterol + budesonida 6/200 mcg
Manutenção: inalar 1 cápsula de 12/12h (enxaguar a boca após).
Alívio: se falta de ar/sintomas, inalar 1 cápsula extra. Não ultrapassar ~12 doses/dia (manutenção + alívio).
Encaminhar para acompanhamento."""}])

C(title="DPOC exacerbado", cid="J44", block="TORAX", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Amoxicilina + clavulanato 500+125mg — 30 comprimidos
Tomar 1 comprimido de 8/8 horas por 10 dias.

Prednisona 20mg
Tomar 2 comprimidos 1x ao dia por 7 dias.

Inalatório de 6/6h por 5 dias: Salbutamol 10 gotas + ipratrópio 20 gotas + SF 0,9% 2ml.
OU spray: Salbutamol 100mcg 2 jatos de 6/6h + Ipratrópio 20mcg 2 jatos de 6/6h."""},
      {"dest":"ps","label":"Na unidade","text":"""Nebulização: Fenoterol 10 gotas + ipratrópio 30 gotas + SF 0,9% 3ml de 20/20 min por 1 hora.
Prednisona 40mg VO OU Hidrocortisona 300mg EV.
Cateter nasal 2–3L (meta 88–92%)."""}])

C(title="IAM — infarto agudo do miocárdio", cid="I21.9", block="TORAX", sev="vermelha",
  nota="ECG, troponina, CK-MB. Jejum. MOV + cateter nasal se Sat <90%. SF 0,5ml/kg/h. Encaminhar/internar UTI.",
  rx=[{"dest":"ps","label":"","text":"""AAS 300mg VO mastigado.
Clopidogrel 75mg: 4 comprimidos VO (ou 1 comprimido se ≥75 anos).
Dipirona (500mg/ml): 1g EV 6/6h.
Dinitrato de isossorbida 5mg: 1 comprimido sublingual — repetir a cada 5 min se necessário (checar contraindicações!).
Morfina (10mg/ml): 1 amp + 9ml AD — fazer 2 a 5 ml, repetir a cada 5 min se necessário."""}])

C(title="Insuficiência cardíaca (perfis)", cid="I50", block="TORAX", sev="vermelha",
  rx=[{"dest":"ps","label":"Perfil B","text":"""Dieta zero até compensação. Restrição hídrica. VNI. Se Sat <90%: máscara O2.
Furosemida (20mg/2ml): 1mg/kg EV.
Hidralazina 25 a 100mg VO 8/8h OU Nitroprussiato (50mg/2ml): 1 amp + 248ml SG 5% EV em BIC, iniciar 10ml/h."""},
      {"dest":"ps","label":"Perfil C","text":"""Dieta zero. Restrição hídrica.
Furosemida (20mg/2ml): 1mg/kg EV.
Nitroprussiato (50mg/2ml): 1 amp + 248ml SG 5% EV, iniciar 10ml/h.
Se hipotensão: Noradrenalina (1mg/ml) 20ml + 80ml SG5% EV em BIC, iniciar 1ml/h. Encaminhar."""},
      {"dest":"ps","label":"Perfil D","text":"""Dieta oral conforme aceitação.
SF 0,9% 20ml/kg em 24h. Encaminhar."""}])

C(title="Edema agudo de pulmão", cid="J81", block="TORAX", sev="vermelha",
  rx=[{"dest":"ps","label":"","text":"""Dieta zero (até melhora de dispneia). VNI.
Furosemida 20mg/2ml: 1mg/kg.
Morfina 10mg/ml (não para todos): 3 a 5 ml EV → 1 amp + 9ml SF.
Tridil (em cardiopatia isquêmica) ou Niprid (mais usado): 1 amp + 240ml SG 5% EV BIC (paciente 70kg começar 10ml/h).
SVD (quantificar diurese). Glicemia capilar 2/2h. Se HGT <60: glicose hipertônica 50%. Insulina regular SOS.
Monitorização. Cabeceira elevada."""}])

C(title="Bradicardia instável", cid="R00.1", block="TORAX", sev="vermelha",
  rx=[{"dest":"ps","label":"","text":"""MOV, dextro.
Atropina 1mg EV bolus — repetir a cada 3–5 minutos (máx 3mg).
Sem resposta: Dopamina 5 amp + 200ml SG — iniciar 20ml/h
OU Epinefrina (1mg) 10 amp + 90ml SG — iniciar 6ml/h (se responder, reduzir para 3ml/h).
Sem resposta: Fentanil (50mcg/ml) 2ml + 8ml SF — fazer 20 a 30 mcg OU Morfina 4 a 5 mg.
Marca-passo transcutâneo: ligar função MP, modo fixo, FC 60, iniciar estimulação (energia 40, aumentar 10 em 10).
Transferir paciente."""}])

C(title="Taquiarritmias", cid="I49", block="TORAX", sev="vermelha",
  flags=["Torsades: 'SULFATO DE MG 22 EV EM 15 MIN' — provável 2 g (typo). Conferir."],
  rx=[{"dest":"ps","label":"Paciente instável — cardioversão","text":"""Flutter atrial: cardioversão sincronizada 50J.
Fibrilação atrial: cardioversão sincronizada 120J.
Taquicardia supraventricular: cardioversão sincronizada 50J.
TV monomórfica: cardioversão sincronizada 100J.
TV polimórfica: cardioversão sincronizada 200J.
Torsades de pointes: desfibrilação 200J bifásico + sulfato de Mg 2g EV em 15 min.
Cardioversão: monitorizar, acesso venoso; Fentanil (100mcg/2ml) 1 amp + 8ml AD — 2ml EV bolus; Etomidato (20mg/10ml) ½ amp EV bolus; ventilar com ambu; sincronizar, carga adequada, gel nas pás."""},
      {"dest":"ps","label":"Paciente estável","text":"""MOV, dextro.
Taquicardia supraventricular: manobra vagal e/ou Adenosina 6mg/12mg EV bolus + flush 10ml SF.
Fibrilação atrial: Amiodarona 300mg + 250ml SG5% em 30 min. Manutenção: Amiodarona 900mg em 250ml SG5% em 24h.
OU Metoprolol 5mg EV em 5 min (1mg/min) — repetir a cada 15 min se necessário (máx 15mg).
OU Diltiazem 0,25mg/kg EV em infusão lenta.
Flutter atrial: Amiodarona 300mg + 150ml SG5% em 30 min. Manutenção igual.
OU Metoprolol 5mg EV.
TV monomórfica/polimórfica: Amiodarona 150mg EV em 10 min. Manutenção: 1mg/min (6h), 0,5mg/min (18h).
Torsades de pointes: sulfato de Mg 2g EV em 15 min."""}])

C(title="Dissecção aguda de aorta", cid="I71", block="TORAX", sev="vermelha",
  nota="ECG, Rx tórax, hemograma, lactato, ureia, creatinina, TGO, TGP. Monitorização em leito de emergência. Cateter O2 2L/min se Sat <92% ou dispneia. Cabeceira elevada. Sinais vitais 1/1h.",
  rx=[{"dest":"ps","label":"","text":"""Dieta zero. Ringer lactato 500ml EV, s/n.
Morfina (10mg/ml): 1 amp + 9ml AD — fazer 4ml.
Deixar FC <60 e PAS entre 100 e 120: Metoprolol 5mg bolus EV — repetir de 10/10 min s/n (máx 20mg).
Se não melhorar: Niprid (50mg/2ml) 1 amp + 250ml SG5% EV em BIC, começar 2ml/h (titular)."""}])

C(title="Trombose venosa profunda", cid="I82", block="TORAX", sev="vermelha",
  nota="Hemograma, ureia, creatinina, Na, K, TGO, TGP, USG doppler venoso. Manter membros elevados, repouso relativo. Alta hospitalar quando INR entre 2 e 3.",
  rx=[{"dest":"internacao","label":"Internação","text":"""Dieta sem restrições.
Enoxaparina 1mg/kg (máx 100mg) SC 12/12 horas.
OU se clearance <30: Heparina não fracionada 25000 UI/5ml — fazer 5ml + SF 0,9% 245ml (100U/ml); ataque 80U/kg; manutenção 18U/kg/hora EV em BI por pelo menos 5 dias.
E Varfarina 5mg VO 1x ao dia. Controle TAP/INR.
Dipirona 1g 6/6h. Bromoprida 10mg EV 8/8h. Cetoprofeno 1 amp EV 12/12h."""},
      {"dest":"casa","label":"Ambulatorial","text":"""Rivaroxabana 15mg
Tomar 1 comprimido de 12/12 horas por 3 semanas.
Depois: Rivaroxabana 20mg — 1 comprimido 1x ao dia por 3 meses.

Dipirona 1g
Tomar 1 comprimido de 6/6 horas se dor.

Deocil SL 10mg
Tomar 1 comprimido de 12/12 horas se dor intensa.
OU Varfarina 5mg — 1 comprimido às 18h. Controle INR a cada 15 dias."""}])

C(title="Tromboflebite superficial", cid="I80", block="TORAX", sev="amarela",
  nota="Avaliar risco (Whitebook). Orientações: compressa morna ou fria 3x/dia até melhora, elevação dos membros, meias compressivas.",
  rx=[{"dest":"casa","label":"Baixo / intermediário risco","text":"""Ibuprofeno 400mg
Tomar 1 comprimido de 8/8 horas.
OU
Diclofenaco 50mg
Tomar 1 comprimido de 8/8 horas.

Risco intermediário, por 45 dias: Enoxaparina 40mg/0,4ml SC 24/24h por 45 dias OU Rivaroxabana 10mg 1x ao dia por 45 dias."""},
      {"dest":"casa","label":"Alto risco (fatores TEV/TVP)","text":"""Ibuprofeno 400mg
Tomar 1 comprimido de 8/8 horas.
OU
Diclofenaco 50mg
Tomar 1 comprimido de 8/8 horas.

Por 3 meses: Enoxaparina 1mg/kg SC 12/12h OU Rivaroxabana 15mg 12/12h por 21 dias, após Rivaroxabana 20mg 1x ao dia."""}])

C(title="Oclusão arterial aguda", cid="I74.3", block="TORAX", sev="vermelha",
  nota="Hemograma, ureia, creatinina, Na, K, coagulograma / USG doppler arterial urgente. Não aguardar exames para iniciar tratamento.",
  rx=[{"dest":"ps","label":"","text":"""Enoxaparina 1mg/kg 12/12h.
Aquecimento passivo do membro.
Contato com cirurgião vascular."""}])

C(title="Dor torácica — abordagem rápida", cid="R07", block="TORAX", sev="vermelha",
  alarmes=("6 causas que matam: SCA/IAM · Dissecção de aorta (dor rasgando, assimetria de pulso/PA) · "
           "TEP (dispneia súbita, taquicardia, dor pleurítica) · Pneumotórax hipertensivo (MV abolido, desvio traqueia, turgência) · "
           "Tamponamento (hipotensão + turgência + bulhas abafadas) · Ruptura de esôfago (vômito + dor + enfisema subcutâneo)."),
  nota=("Passo 1: ECG em até 10 min + MOV. Passo 2: pensar nas 6 causas antes de 'musculoesquelético'. "
        "Score HEART estratifica SCA: 0–3 baixo (alta com troponina seriada negativa), 4–6 moderado (internar/observar), "
        "≥7 alto (invasiva precoce/transferir). Solicitar ECG seriado (1 normal não exclui), troponina seriada (0h/1h ou 0h/3h), "
        "Rx tórax, hemograma, eletrólitos, função renal, glicemia; D-dímero se suspeita TEP + Wells baixo, Angio-TC se D-dímero+. "
        "Se SCA confirmada/suspeita → protocolo IAM e internar/transferir."))

C(title="Elevação importante da PA (sem LOA)", cid="I16.0", block="TORAX", sev="amarela",
  anamnese=("PACIENTE REFERE CEFALEIA/TONTURA HÁ [X]. Nega déficit neurológico focal, nega dor torácica, "
            "nega dispneia, nega alteração visual, nega disfagia, nega vômitos, nega oligúria. "
            "PA: ___x___ mmHg. FC: ___. Sem sinais de lesão de órgão-alvo."),
  alarmes=("Reclassifica p/ EMERGÊNCIA (I16.1) se LOA: dor torácica, dispneia, déficit neurológico, "
           "alteração visual, dor dorsal/abdominal (dissecção), gestante. Checar antes de medicar: aderência aos remédios hoje? "
           "Uso de cocaína/anfetamina/AINE/descongestionante/AO? Dor/ansiedade reativa? Glicemia capilar (descartar hipo)? ECG."),
  nota=("Meta: redução GRADUAL em 24–48h. NÃO forçar queda rápida. NÃO usar nifedipino sublingual (queda abrupta = isquemia). "
        "Emergência (I16.1) → UTI + anti-hipertensivo EV + monitorização; reduzir no máx 25% da PAM na 1ª hora "
        "(exceção dissecção). Nitroprussiato EV (EAP/encefalopatia), Nitroglicerina EV (SCA/IC), Labetalol/Nicardipino EV "
        "(AVC hemorrágico, PAS<140), Nitroprussiato+Esmolol (dissecção, PAS<120 em 20min), Hidralazina EV+MgSO4 (eclâmpsia), "
        "Fentolamina EV (feocromocitoma). CID: I10 essencial · I16.0 sem LOA · I16.1 emergência · I16.9 não especificada."),
  rx=[{"dest":"ps","label":"Conduta — sem LOA","text":"""Captopril 25mg — 2 comprimidos
Tomar 1 comprimido agora. Repetir em 60 min se PA ainda ≥180/110 mmHg.
OU
Clonidina 0,1mg — 2 comprimidos
Tomar 1 comprimido agora. Repetir em 60 min se necessário. (Preferir em ansiedade/hiperatividade simpática; risco de rebote se uso crônico suspenso.)

Dipirona 1g (500mg/comp) — 4 comprimidos
Tomar 2 comprimidos VO agora se cefaleia ou dor.
OU Dipirona 500mg/ml solução oral — 40 gotas VO agora se cefaleia ou dor."""},
      {"dest":"casa","label":"Ajuste do esquema crônico","text":"""IECA: Enalapril 10mg — 1 cp de 12/12h (ou Enalapril 20mg 12/12h) OU Captopril 25mg — 1 cp de 8/8h.
BRA: Losartana 50mg — 1 cp 1x/dia (ou 100mg 1x/dia).
BCC: Anlodipino 5mg — 1 cp 1x/dia (ou 10mg 1x/dia).
Diurético: Hidroclorotiazida 25mg — 1 cp pela manhã (ou Clortalidona 25mg pela manhã).

Retorno ao ambulatório/UBS em até 7 dias. Aumentar ingesta hídrica. Dieta hipossódica.
Retornar IMEDIATAMENTE se déficit neurológico, dor no peito, falta de ar, alteração visual, piora da cefaleia."""}])
