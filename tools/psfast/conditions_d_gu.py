# -*- coding: utf-8 -*-
# GENITOURINÁRIO / GINECO / ISTs

C(title="Cistite / ITU não complicada", cid="N30 · N39", block="GU", sev="amarela",
  flags=["Duração da Nitrofurantoína: bloco 'Cistite' diz 6/6h por 5 dias; bloco 'Infecção urinária N39' dizia 7 dias. Padronizar."],
  rx=[{"dest":"casa","label":"1ª linha","text":"""Nitrofurantoína 100mg — 20 comprimidos
Tomar 1 comprimido de 6/6 horas por 5 dias.
OU
Fosfomicina 3g — 1 envelope
Diluir em ½ copo e tomar em dose única antes de dormir.
OU
Cefalexina 500mg — 20 comprimidos
Tomar 1 comprimido de 6/6 horas por 5 dias."""},
      {"dest":"casa","label":"2ª linha","text":"""Ciprofloxacino 500mg — 20 comprimidos
Tomar 1 comprimido de 12/12 horas por 5 dias.
OU
Amoxicilina + clavulanato 500/125mg
Tomar 1 comprimido de 8/8 horas por 7 dias."""},
      {"dest":"casa","label":"Sintomáticos","text":"""Pyridium 100–200mg
Tomar 1 comprimido de 8/8 (a 12/12) horas, após as refeições, por no máximo 2 dias (urina fica laranja).

Dipirona 500mg — 40 comprimidos
Tomar 2 comprimidos de 6/6 horas se dor ou febre por 5 dias.
OU
Paracetamol 750mg — 20 comprimidos
Tomar 1 comprimido de 6/6 horas se dor ou febre."""}])

C(title="Bacteriúria assintomática", cid="N39", block="GU", sev="verde",
  nota="Tratar apenas em situações específicas (gestante, pré-procedimento urológico).",
  rx=[{"dest":"casa","label":"","text":"""Nitrofurantoína 100mg
Tomar 1 comprimido de 12/12 horas por 5–7 dias.
OU
Amoxicilina 500mg
Tomar 1 comprimido de 8/8 horas por 5–7 dias.
OU
Fosfomicina 3g
Tomar 1x, dose única."""}])

C(title="Pielonefrite", cid="N11", block="GU", sev="vermelha",
  nota=("Hemograma, ureia, creatinina, Urina I, urocultura, antibiograma, Na, K; se disponível USG vias urinárias e hemocultura. "
        "Ambulatorial: retornar em 48–72h para reavaliação. Internação se sepse, complicação, comorbidade significativa, "
        "não aceitação oral, não controle dos sintomas, gestação."),
  rx=[{"dest":"ps","label":"Na unidade","text":"""SF 250ml + 1 amp Dipirona."""},
      {"dest":"casa","label":"Ambulatorial","text":"""Levofloxacino 750mg
Tomar 1 comprimido ao dia por 7 dias.
OU
Ciprofloxacino 500mg
Tomar 1 comprimido de 12/12 horas por 7 dias.

Dipirona 500mg
Tomar 1 a 2 comprimidos de 6/6 horas se dor.

Bromoprida 10mg
Tomar 1 comprimido de 8/8 horas se náusea ou vômito."""},
      {"dest":"internacao","label":"Internação","text":"""SF 30–40ml/kg em 24h.
Dipirona 1g 6/6 horas se dor.
Bromoprida 10mg EV 8/8 horas se náusea ou vômito.
Ciprofloxacino 400mg EV 12/12 horas
OU
Ceftriaxona 2g EV 24/24h."""}])

C(title="Nefrolitíase / Cólica nefrética", cid="N23", block="GU", sev="amarela",
  nota="Hemograma, ureia, creatinina, Urina I, TC sem contraste de abdome. Tansulosina para cálculos <1cm SEM infecção. Encaminhar urologista. Internação: febre, rim único, função renal limítrofe, gestante, imunossuprimidos.",
  rx=[{"dest":"casa","label":"Uso oral","text":"""Buscopan composto
Tomar 1 comprimido de 6/6h se dor.

Cetoprofeno 100mg
Tomar 1 comprimido de 12/12h por 5 dias.

Bromoprida 10mg
Tomar 1 comprimido 8/8h se náusea ou vômito.

Tansulosina 0,4mg
Tomar 1 comprimido 1x ao dia por 4–6 semanas."""},
      {"dest":"ps","label":"Agora","text":"""Dieta zero. SF 0,9% 500ml EV.
Buscopan composto EV. Cetoprofeno EV.
Sem melhora: Tramadol 100mg + SF 0,9% 100ml EV lento; Bromoprida 10mg EV."""}])

C(title="Cólica menstrual / SUA", cid="N94", block="GU", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Dipirona 500mg — 40 comprimidos
Tomar 2 comprimidos de 6/6 horas se dor ou febre por 5 dias.
OU
Paracetamol 500mg — 40 comprimidos
Tomar 1 comprimido de 6/6 horas se dor ou febre por 5 dias.

Buscopan composto — 1 caixa
Tomar 1 comprimido de 6/6 horas se dor ou cólica.

Diclofenaco 50mg — 10 comprimidos
Tomar 1 comprimido de 8/8 horas por 5 dias.

Ácido mefenâmico 500mg — 1 caixa
Tomar 1 comprimido de 8/8 horas se cólica intensa.
OU
Ácido tranexâmico 250mg — 36 comprimidos
Tomar 4 comprimidos, 3 vezes ao dia, por 3 dias."""}])

C(title="Vaginose bacteriana", cid="N76", block="GU", sev="amarela",
  nota="Evitar roupas justas/sintéticas; não usar perfumes na vulva; evitar duchas; dormir sem calcinha; usar sabonete íntimo.",
  rx=[{"dest":"casa","label":"Uso oral","text":"""Metronidazol 250mg — 28 comprimidos
Tomar 2 comprimidos de 12/12h por 7 dias."""},
      {"dest":"casa","label":"Uso vaginal","text":"""Metronidazol ginecológico 100mg/g
1 aplicador intravaginal por 5 noites."""}])

C(title="Candidíase vaginal", cid="B37", block="GU", sev="verde",
  nota="NÃO dar fluconazol para gestante!",
  rx=[{"dest":"casa","label":"Uso vaginal","text":"""Miconazol creme 2%
1 aplicador intravaginal à noite por 7 noites."""},
      {"dest":"casa","label":"Uso oral","text":"""Fluconazol 150mg
Tomar 1 comprimido, dose única.

Recorrente: Fluconazol 150mg 1 cp a cada 3 dias por 3 doses; depois 1 cp por semana por 6 meses."""}])

C(title="Tricomoníase", cid="A59", block="GU", sev="amarela",
  nota="Não beber álcool. Tratar parceria.",
  rx=[{"dest":"casa","label":"Uso oral","text":"""Metronidazol 400mg
Tomar 5 comprimidos, dose única.
OU
Metronidazol 250mg
Tomar 2 comprimidos de 12/12 horas por 7 dias."""},
      {"dest":"casa","label":"Uso intravaginal","text":"""Metronidazol geleia vaginal 100mg/g — 1 bisnaga
Aplicar 1 aplicador cheio dentro da vagina, à noite ao deitar, por 7 noites."""}])

C(title="Cervicite", cid="N72", block="GU", sev="amarela",
  rx=[{"dest":"ps","label":"","text":"""Ceftriaxona 250mg IM dose única."""},
      {"dest":"casa","label":"","text":"""Azitromicina 1g
Tomar 1 comprimido, dose única."""}])

C(title="Sífilis", cid="A53.9", block="GU", sev="amarela",
  nota="Solicitar teste rápido HIV, HBsAg/Anti-HBs/Anti-HBc, Anti-HCV, VDRL e FTA-Abs.",
  rx=[{"dest":"casa","label":"Recente","text":"""Penicilina G benzatina 2.400.000 UI
Aplicar 1.200.000 UI IM em cada glúteo, dose única.
OU
Doxiciclina 100mg
Tomar 1 comprimido de 12/12 horas por 15 dias."""},
      {"dest":"casa","label":"Tardia","text":"""Penicilina G benzatina 2.400.000 UI
Aplicar 1.200.000 UI IM em cada glúteo, 1x/semana por 3 semanas.
OU
Doxiciclina 100mg
Tomar 1 comprimido de 12/12 horas por 30 dias."""}])

C(title="Gonorreia (+ clamídia)", cid="A54", block="GU", sev="amarela",
  rx=[{"dest":"ps","label":"","text":"""Ceftriaxona 500mg IM dose única agora."""},
      {"dest":"casa","label":"","text":"""Doxiciclina 100mg
Tomar 1 comprimido de 12/12 horas por 7 dias.
OU (gestante)
Azitromicina 500mg
Tomar 2 comprimidos, dose única."""}])

C(title="Herpes genital", cid="A60", block="GU", sev="amarela",
  nota="Profilaxia (se >6 episódios/ano): Aciclovir 200mg 1 cp de 12/12h.",
  rx=[{"dest":"casa","label":"","text":"""Aciclovir 200mg — 50 comprimidos
Tomar 1 comprimido de 4/4h (exceto 1 dose noturna) por 10 dias. Horário sugerido: 06:00 / 10:00 / 14:00 / 18:00 / 22:00.
OU
Aciclovir 400mg
Tomar 1 comprimido de 8/8 horas por 5–7 dias.

Dipirona 1g
Tomar 1 comprimido de 6/6 horas se dor ou febre."""}])

C(title="Cancro mole", cid="A57", block="GU", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Azitromicina 500mg — 2 comprimidos
Tomar 2 comprimidos VO em dose única."""}])

C(title="Linfogranuloma venéreo", cid="A55", block="GU", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Doxiciclina 100mg — 42 comprimidos
Tomar 1 comprimido de 12/12 horas por 21 dias."""}])

C(title="Climatério (sintomas vasomotores)", cid="N95.1", block="GU", sev="verde",
  rx=[{"dest":"casa","label":"","text":"""Isoflavona de soja 200mg — 1 caixa
Tomar 1 comprimido VO de 24/24h por 30 dias."""}])

C(title="Atrofia urogenital", cid="N90", block="GU", sev="verde",
  nota="Checar contraindicações.",
  rx=[{"dest":"casa","label":"Uso vaginal","text":"""Estradiol 10mcg/comprimido
Aplicar 1 comprimido via vaginal 2x na semana.
OU
Promestrieno creme vaginal 10mg
Aplicar à noite por 30 noites."""}])

C(title="Sangramento uterino anormal", cid="N93", block="GU", sev="amarela",
  flags=["'Ringer lactato 500- 2000L EV' no bloco agudo — 'L' provável typo de 'ml' (500–2000 ml)."],
  rx=[{"dest":"ps","label":"Sangramento agudo","text":"""Dieta branda. Ringer lactato 500–2000 ml EV correr rápido.
Monitorização. Glicemia capilar. Glicose hipertônica 50% 20ml EV se HGT <70. Repouso no leito.
Ácido tranexâmico 10mg/kg EV (dose máxima 600mg/dose) agora.
OU Ácido tranexâmico 1,5g VO de 8/8 horas por 5 dias."""},
      {"dest":"casa","label":"Sangramento crônico","text":"""Levonorgestrel + etinilestradiol 0,15mg/0,03mg
Tomar 1 comprimido de 12/12 horas por 7 dias. Depois, 1 comprimido por dia por 21 dias.
OU inserir DIU de levonorgestrel.
OU
Ibuprofeno 600mg
Tomar 1 comprimido de 8/8 horas por 5 dias.
OU
Ácido tranexâmico 500mg
Tomar 1 comprimido de 8/8 horas por 4 dias."""}])

C(title="Incontinência urinária", cid="R32", block="GU", sev="verde",
  nota="Tratar constipação/DPOC/ICC/DM; evitar cafeína e álcool; fisioterapia pélvica.",
  rx=[{"dest":"casa","label":"","text":"""Oxibutinina 5mg
Tomar 1 comprimido de 8/8 horas.
OU
Imipramina 10mg
Tomar 1 comprimido ao dia."""}])

C(title="Mastite", cid="", block="GU", sev="amarela",
  rx=[{"dest":"casa","label":"","text":"""Cefalexina 500mg
Tomar 1 comprimido de 6/6 horas por 10 a 14 dias.
OU
Amoxicilina 500mg
Tomar 1 comprimido de 8/8 horas por 10 a 14 dias."""}])

C(title="Balanite", cid="N51.2", block="GU", sev="verde",
  rx=[{"dest":"casa","label":"Tópico","text":"""Nitrato de miconazol creme 2%
Aplicar nas lesões 2x ao dia.

Hidrocortisona 1% creme
Aplicar nas lesões 2x ao dia."""},
      {"dest":"casa","label":"Oral","text":"""Fluconazol 150mg
Tomar 1 comprimido, dose única.

Dipirona 500mg
Tomar 1 comprimido de 6/6 horas se dor.

Desloratadina 5mg
Tomar 1 comprimido 1x ao dia se coceira."""}])

C(title="Escroto agudo", cid="N51.1", block="GU", sev="amarela",
  nota="Hemograma, PCR, Urina I, urocultura, USG doppler bolsa escrotal. Encaminhar urologia/cirurgia.")

C(title="Orquiepididimite", cid="N45", block="GU", sev="amarela",
  nota="Suspensório escrotal por 10 dias; evitar esforço físico; encaminhar urologista.",
  rx=[{"dest":"ps","label":"Agora","text":"""Ceftriaxona (250mg/2ml) 1 amp EV."""},
      {"dest":"casa","label":"Jovem","text":"""Doxiciclina 100mg
Tomar 1 comprimido de 12/12 horas por 10 dias.

Dipirona 500mg
Tomar 1 a 2 comprimidos de 6/6 horas se dor.

Ibuprofeno 600mg
Tomar 1 comprimido de 8/8 horas por 3 dias."""},
      {"dest":"casa","label":"Idoso","text":"""Levofloxacino 500mg
Tomar 1 comprimido de 24/24 horas por 10 dias.

Dipirona 500mg
Tomar 1 a 2 comprimidos de 6/6 horas se dor.

Ibuprofeno 600mg
Tomar 1 comprimido de 8/8 horas por 3 dias."""}])
