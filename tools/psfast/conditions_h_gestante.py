# -*- coding: utf-8 -*-
# GESTANTE (tab "GESTANTE") + BÔNUS (Exame físico, Conduta, Medicações AMA)
# Fonte: protectedtext/pgwlassak. Doses verbatim; grafias corrigidas.

# ---------- GESTANTE ----------
C(title="Hipertensão (gestante)", cid="O10", block="GEST", sev="amarela",
  rx=[{"dest":"casa","label":"Crônica / leve","text":"""Metildopa 250mg
Tomar 1 a 2 comprimidos VO até de 6/6h."""},
      {"dest":"ps","label":"Hipertensão aguda grave","text":"""Nifedipino 20mg — 1 cp VO de 30/30 min.
Hidralazina 5mg — 1 amp EV de 30/30 min."""},
      {"dest":"ps","label":"Crise hipertensiva / eclâmpsia (MgSO4)","text":"""MgSO4 8ml + SF 0,9% 92ml — correr em 20 min em BIC (300ml/h).
MgSO4 10ml + SG 5% 500ml — correr 100ml/h em BIC."""}])

C(title="Diabetes (gestante)", cid="O24", block="GEST", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Insulina (esquema conforme glicemia)."""}])

C(title="Anemia (gestante)", cid="O99.0", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Profilaxia: Sulfato ferroso 40mg + Ácido fólico 0,2mg/mL 60 gotas — até o 3º mês de puerpério.
Tratamento: ajustar sulfato ferroso conforme hemoglobina."""}])

C(title="Síndrome gripal (gestante)", cid="J06", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Beclometasona spray nasal — 2 jatos em cada narina de 12/12h.
OU Budesonida spray nasal — 2 jatos em cada narina de 12/12h.

Bromelin S — 10ml de 12/12h.

Loratadina 10mg — 1 cp VO 1x ao dia."""}])

C(title="Pneumonia / Sinusite / Amigdalite (gestante)", cid="J18 · J01 · J03", block="GEST", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Amoxicilina 500mg — 1 cp VO de 8/8h.
OU Amoxicilina + clavulanato (Clavulin) 875+125mg — 1 cp VO de 12/12h.
OU Azitromicina 500mg — 1 cp VO 1x ao dia por 5 dias."""}])

C(title="Broncoespasmo / Crise asmática (gestante)", cid="J45", block="GEST", sev="amarela",
  nota="Crises graves: considerar corticoide, porém avaliar se é PNAR e vai precisar de doppler — o corticoide anula a avaliação do ducto venoso.",
  rx=[{"dest":"casa","label":"","text":"""Salbutamol (spray/nebulização)."""}])

C(title="Náuseas e vômitos (gestante)", cid="O21", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Ondansetrona (Vonau, Zofran) 4mg — 1 cp VO de 8/8h.
OU Meclizina (Meclin) 25mg — 1 cp VO de 8/8h.
OU Metoclopramida (Plasil) 4mg — 1 cp/1 amp de 8/8h.
OU Dimenidrinato (Dramin) 40 gotas/1cp/1 amp de 8/8h.
OU Ranitidina 150mg — 1 cp VO de 8/8h."""}])

C(title="Epigastralgia (gestante)", cid="K21", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Simeco Plus (hidróxido de alumínio + hidróxido de magnésio + simeticona) — 10ml VO de 8/8h.
OU LuftaGastro Pro (alginato de sódio + bicarbonato de potássio) — 10ml VO de 8/8h.
OU Hidróxido de alumínio (Mylanta Plus) — 10ml VO de 8/8h."""}])

C(title="Dor abdominal (gestante)", cid="R10", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Escopolamina (Buscopan) 10mg — 1 cp VO de 8/8h.
OU Escopolamina + paracetamol (Buscoduo) 10+500mg — 1 cp VO de 8/8h.
OU Ranitidina 150mg — 1 cp VO de 8/8h."""}])

C(title="Constipação (gestante)", cid="K59.0", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Óleo mineral.
Lactulona — 10ml VO.
Tamarine — 1 cp VO à noite por 7 dias.
Bisacodil (Dulcolax) 5mg — 1 cp VO."""}])

C(title="Diarreia (gestante)", cid="A09", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Soro de reidratação oral.
Floratil 200mg — 1 cp VO de 8/8h por 3 dias.
Enterogermina — 5ml VO de 8/8h por 3 dias."""}])

C(title="Doença hemorroidária (gestante)", cid="O22.4", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Diosmina + hesperidina (Proctyl, Daflon) tópico — aplicar na região."""}])

C(title="Candidíase (gestante)", cid="B37", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Miconazol creme vaginal — 1 tubete por noite, por 7 noites.
Se candidíase de repetição/importante: Fluconazol 150mg VO dose única."""}])

C(title="Vaginose (gestante)", cid="N76", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Metronidazol vaginal — 1 dosador 1x à noite por 5 dias."""}])

C(title="Tricomoníase (gestante)", cid="A59", block="GEST", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Metronidazol 250mg — 2 cp de 12/12h por 7 dias.
OU Metronidazol 250mg — 8 cp VO dose única."""}])

C(title="Clamídia / Gonorreia (gestante)", cid="A54 · A56", block="GEST", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Azitromicina 500mg — 2 cp VO dose única
+ Ceftriaxona 250mg IM dose única."""}])

C(title="ITU / Cistite (gestante)", cid="O23", block="GEST", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""<36 semanas: Nitrofurantoína 100mg — 1 cp VO de 6/6h por 5 dias.
>36 semanas: Cefalexina 500mg — 1 cp VO de 6/6h por 7 dias.
Amoxicilina ou Amoxicilina + clavulanato — de 8/8h por 4–7 dias."""}])

C(title="Pielonefrite (gestante)", cid="O23", block="GEST", sev="vermelha",
  rx=[{"dest":"internacao","label":"","text":"""Cefuroxima 750mg EV de 8/8h — até ficar afebril e trocar por VO, completando 10–14 dias.
OU Cefepima 2g EV de 8/8h ou de 12/12h."""}])

C(title="Dor (gestante)", cid="R52", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Paracetamol 500mg VO de 4/4h (pode associar Prednisona 5mg VO de 12/12h se dor intensa).
Miosan 5mg à noite por 3 dias, se cefaleia intensa."""},
      {"dest":"ps","label":"Dor intensa (na unidade)","text":"""Dipirona 500mg EV se dor intensa.
Decadron 1 amp IM se dor intensa.
Tramal 1 amp EV se dor refratária."""}])

C(title="Prurido (gestante)", cid="L29", block="GEST", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Levocetirizina (Zina) 5mg — 1 cp VO.
OU Loratadina 10mg — 1 cp VO.
OU Hidroxizina (Hixizine) 25mg — 1 cp VO.
OU Fexofenadina (Allegra) 120mg — 1 cp VO."""}])

C(title="Ansiedade / Depressão (gestante)", cid="F41", block="GEST", sev="amarela",
  nota="Insônia: Neozine 40mg/ml 5 gotas VO à noite.",
  rx=[{"dest":"casa","label":"Manutenção","text":"""Sertralina 50mg — 1 cp VO 1x ao dia."""},
      {"dest":"ps","label":"Crise de ansiedade","text":"""Neozine 40mg/ml — 5 gotas VO.
Prometazina — 1 amp IM.
Diazepam 5mg — 1 cp VO se na maternidade e refratária a outras medidas."""}])

C(title="Epilepsia (gestante)", cid="G40", block="GEST", sev="amarela",
  nota="Manter medicação usual, desde que NÃO seja Valproato de Sódio. Aumentar o esquema de ácido fólico no 1º trimestre.",
  rx=[{"dest":"ps","label":"Crise refratária","text":"""Diazepam 5mg — 1 cp VO se na maternidade e refratária a outras medidas."""}])

C(title="⛔ NÃO usar em gestante", cid="", block="GEST", sev="vermelha",
  alarmes="NÃO prescrever em gestantes: AINEs · Sulfametoxazol + trimetoprima · Valproato de sódio (epilepsia).",
  nota="Lista de contraindicações frequentes. Sempre checar categoria de risco na gestação antes de prescrever.")

# ---------- BÔNUS (novos) ----------
C(title="Exame físico — frases direcionadas", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"outro","label":"Geral (resumido)","text":"""Bom estado geral, corado, hidratado, acianótico, anictérico, afebril.
Murmúrios vesiculares presentes bilateralmente, sem ruídos adventícios, eupneico em ar ambiente.
BRNF 2T, sem sopros, pulsos cheios, TEC <2s.
Abdome flácido, plano, indolor à palpação.
Membros: sem edema, sem dor à palpação, sem sinais de TVP, TEC <3s, pulsos amplos e simétricos.
Neuro: Glasgow 15, sem sinais meníngeos, sem déficits focais."""},
      {"dest":"outro","label":"ORL / Pescoço / Oroscopia","text":"""Oroscopia: sem evidências de hiperemia, adenomegalias, abaulamentos patológicos, placas ou exsudatos.
Pescoço: traqueia centrada, musculatura tópica, sem alterações cutâneas à inspeção, ausência de massas ou tumorações à palpação.
Orofaringe sem alterações à inspeção, sem linfonodomegalia cervical.
Orofaringe com discreta hiperemia e edema, sem exsudato. Ausência de linfonodomegalia cervical palpável.
Orofaringe com amígdalas hiperemiadas e hipertrofiadas, com exsudato puntiforme esbranquiçado. Sem linfonodomegalia cervical palpável."""},
      {"dest":"outro","label":"Otoscopia","text":"""Otoscopia normal: coloração perolácea, íntegra, triângulo luminoso de Politzer presente, impressão do cabo do martelo, sem secreção.
Otite média aguda: MT hiperemiada, abaulada, perfuração puntiforme com saída de secreção purulenta.
OD: MT com discreta opacidade, sem abaulamento, sem perfuração.
Cerume: massa marrom/amarelada em forma de rolha, pode impossibilitar a visualização da MT.
Otite externa: MT normal, secreção e edema no conduto auditivo externo."""},
      {"dest":"outro","label":"Oftalmo / Ombro / Coluna / Toque retal","text":"""Olho esquerdo: hiperemia conjuntival difusa, secreção serosa/aquosa discreta, sem secreção purulenta, sem edema palpebral importante, córnea sem opacidades, reflexo fotomotor preservado. Olho direito sem alterações.
Ombro: sem sinais flogísticos, discreta limitação por dor, sem deformidades, neurovascular distal preservado.
Coluna lombar discretamente dolorosa à palpação paravertebral, sem deformidades, mobilidade preservada, sem déficits neurológicos em MMII.
Cervicalgia com contratura muscular, dor à palpação e limitação de mobilidade, sem déficits neurológicos.
Anoperíneo/toque retal: pele e mucosa íntegras, esfíncter normotenso, sem tumorações, fezes em ampola retal pastosas, sem melena em dedo de luva."""},
      {"dest":"outro","label":"Resumo — antecedentes","text":"""#Medicamentos de uso contínuo: nega
#Comorbidades prévias: nega
#Alergias: nega alergias medicamentosas conhecidas.
#Tabagista:
#Gestante:"""}])

C(title="Conduta / Alta", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"outro","label":"","text":"""Medicação na unidade + conduta para casa.
Orientações gerais. Oriento sinais de alarme. Prescrevo sintomáticos.
Explico o uso correto das medicações. Oriento retorno caso haja sinal de alarme ou piora.
Converso com o paciente e esclareço dúvidas. Explico a conduta aplicada; o paciente aceita, entende e concorda.
Alta médica."""}])

C(title="Medicações na unidade (IM / EV)", cid="", block="BONUS", sev="amarela",
  rx=[{"dest":"ps","label":"Analgésicos / AINE / corticoide","text":"""Cetoprofeno 50mg/mL (2mL) — aplicar 1 amp IM agora.
Dipirona sódica 500mg/mL (2mL) — aplicar 1 amp IM agora.
Dexametasona 4mg/mL — aplicar 1 amp IM agora.
Diclofenaco sódico 25mg/mL (3mL) — aplicar 1 amp IM agora."""},
      {"dest":"ps","label":"Sintomáticos (náusea / vômito / gástrico)","text":"""Ondansetrona 2mg/mL — aplicar 1 amp IM agora.
Bromoprida 5mg/mL (2mL) — aplicar 1 amp IM agora.
Metoclopramida 5mg/mL (2mL) — aplicar 1 amp IM agora.
Dimenidrinato + piridoxina 50+50mg/mL (1mL) [Dramin B6] — aplicar 1 amp IM profundo agora.
Omeprazol 40mg (pó liofilizado) — diluir em 10mL do diluente próprio e fazer EV lento agora."""},
      {"dest":"ps","label":"Antiespasmódicos","text":"""Escopolamina simples 20mg/mL (1mL) [Buscopan] — aplicar 1 amp IM agora.
Escopolamina + dipirona [Buscopan composto] — aplicar 1 amp IM agora."""},
      {"dest":"ps","label":"Opioides (dor forte / refratária)","text":"""Tramadol 50mg (1mL): 1 amp + SF 0,9% 100mL EV, correr lento em 20 minutos.
Morfina 10mg/mL (1mL) EV diluída: diluir 1 amp (1mL) + 9mL AD (=1mg/mL); aplicar ___ mL (___ mg) EV lento agora (ex: 2 a 3 mL).
Morfina 10mg/mL (1mL) IM pura: aplicar ___ mL IM profundo agora (0,3 a 0,5 mL para analgesia)."""},
      {"dest":"ps","label":"Outros","text":"""Prometazina 25mg/mL (2mL) [Fenergan] — aplicar 1 amp IM profundo agora.
Benzilpenicilina benzatina 1.200.000 UI [Benzetacil] — diluir com 4mL AD, aplicar 1 F/A IM profundo agora."""}])
