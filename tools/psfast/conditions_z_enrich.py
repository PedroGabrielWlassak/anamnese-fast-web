# -*- coding: utf-8 -*-
# Enriquecimento (roda por último): Exame físico esperado + Disclaimer para os
# quadros frequentes. Conteúdo semiológico/orientação (NÃO dose) e EDITÁVEL no app.
# Aplica sobre CONDITIONS já criadas, por título canônico.

_SSVV = "SSVV: PA __/__ | FC __ | FR __ | SatO2 __% | Tax __°C."
_BEG  = "BEG, corado, hidratado, acianótico, anictérico, afebril."

_EXAME = {
"IVAS / Amigdalite / Resfriado":
 f"{_BEG}\n{_SSVV}\nOrofaringe: hiperemia leve, sem exsudato. Otoscopia: MT translúcida bilateral.\n"
 "AP: MV+ bilateral, sem RA, eupneico em ar ambiente. Sem linfonodomegalia cervical significativa.",
"Faringoamigdalite":
 f"{_BEG}\n{_SSVV}\nOrofaringe: amígdalas hiperemiadas e hipertrofiadas [± exsudato puntiforme]. "
 "Linfonodo cervical anterior [doloroso à palpação]. Sem trismo, sem sialorreia, sem abaulamento peritonsilar.\nAP: MV+ sem RA.",
"Amigdalite Aguda":
 f"{_BEG}\n{_SSVV}\nOrofaringe: amígdalas hiperemiadas com exsudato; úvula centrada, sem abaulamento. "
 "Adenopatia cervical anterior [dolorosa]. Sem trismo/sialorreia.",
"Sinusite Aguda":
 f"{_BEG}\n{_SSVV}\nFace: dor à palpação/percussão de seios [maxilar/frontal]. Rinoscopia: secreção [purulenta] em meato médio. "
 "Sem edema/eritema periorbitário, sem alteração visual. Neuro: sem déficits.",
"Otite Média Aguda":
 f"{_BEG}\n{_SSVV}\nOtoscopia [D/E]: MT abaulada, hiperemiada, opaca [± otorreia]. "
 "Região retroauricular sem edema/eritema. Mímica facial preservada.",
"Otite Externa":
 f"{_BEG}\n{_SSVV}\nOtoscopia [D/E]: dor à tração do tragus/pavilhão, edema e hiperemia do conduto [± secreção]. "
 "MT [visível/não visualizada]. Retroauricular livre.",
"Rinite Alérgica":
 f"{_BEG}\n{_SSVV}\nRinoscopia: mucosa nasal pálida/edemaciada, coriza hialina. Sem secreção purulenta. "
 "Orofaringe sem exsudato. AP: MV+ sem RA.",
"Alergia / Rinite Alérgica":
 f"{_BEG}\n{_SSVV}\nPele: [placas urticariformes / sem lesões]. Rinoscopia: mucosa pálida, coriza hialina. "
 "AP: MV+ sem sibilos. Sem edema de glote/lábios, sem estridor.",
"GECA / Gastroenterite (adulto)":
 f"{_BEG}, mucosas úmidas.\n{_SSVV}\nAbdome: RHA+ (aumentados), flácido, dor difusa leve à palpação, "
 "sem defesa/rigidez, DB negativa. Sem sinais de desidratação (turgor preservado, sem hipotensão postural).",
"Cefaleia":
 f"{_BEG}, orientado.\n{_SSVV}\nNeuro: Glasgow 15, pupilas isofotorreagentes, sem déficits focais, sem rigidez de nuca. "
 "Marcha e fala preservadas. Fundo de olho [sem papiledema, se avaliado].",
"Enxaqueca":
 f"{_BEG}, [fotofobia presente].\n{_SSVV}\nNeuro: Glasgow 15, sem déficits focais, sem rigidez de nuca, pupilas isofotorreagentes.",
"Lombalgia / Mialgia":
 f"{_BEG}\n{_SSVV}\nColuna lombar: dor à palpação de musculatura paravertebral, sem dor em linha média/processos espinhosos. "
 "Lasègue negativo bilateral. Força e sensibilidade de MMII preservadas. Reflexos simétricos. Sem alteração esfincteriana.",
"Cólica Menstrual ou Sangramento":
 f"{_BEG}\n{_SSVV}\nAbdome: dor à palpação em hipogástrio, sem defesa/DB. Sem massas palpáveis. "
 "[Especular/toque conforme indicação].",
"Cistite / ITU":
 f"{_BEG}, afebril.\n{_SSVV}\nAbdome: dor leve à palpação suprapúbica, sem defesa. "
 "Giordano NEGATIVO bilateral. Sem toxemia.",
"Pielonefrite":
 f"REG/BEG, [febril].\n{_SSVV}\nGiordano POSITIVO à [D/E]. Abdome sem sinais de irritação peritoneal. "
 "Avaliar toxemia/instabilidade (indicam internação).",
"Dengue":
 f"{_BEG}, hidratado.\n{_SSVV} (PA deitado e em pé).\nProva do laço: [negativa]. Pele: [exantema?], sem petéquias/sangramentos. "
 "Abdome: fígado não palpável, indolor. Sem hipotensão postural.",
"Conjuntivite":
 f"{_BEG}, afebril.\nOlho [D/E]: hiperemia conjuntival difusa, secreção [serosa/purulenta], sem edema palpebral importante. "
 "Córnea sem opacidades, reflexo fotomotor preservado, acuidade visual preservada. Olho contralateral sem alterações.",
"Alergia":
 f"{_BEG}\n{_SSVV}\nPele: lesões [urticariformes/eczematosas] em [localização], [com/sem] sinais de infecção secundária. "
 "Sem edema de lábios/glote, sem estridor, AP: MV+ sem sibilos.",
"Herpes Zoster":
 f"{_BEG}\n{_SSVV}\nPele: vesículas agrupadas sobre base eritematosa, distribuição em dermátomo [__], unilateral, sem ultrapassar linha média. "
 "[Avaliar acometimento oftálmico/ramo V1].",
"Herpes Simples":
 f"{_BEG}\nPele/mucosa: vesículas agrupadas em base eritematosa em [lábio/genital], [± úlceras rasas dolorosas]. "
 "Sem sinais de infecção bacteriana secundária.",
"Escabiose":
 f"{_BEG}\nPele: pápulas e escoriações pruriginosas em espaços interdigitais, punhos, axilas, cintura, região genital. "
 "Prurido de predomínio noturno. [Contactantes sintomáticos?].",
"Gota":
 f"{_BEG}, afebril.\n{_SSVV}\nArticulação [1ª MTF/joelho/tornozelo]: monoartrite com sinais flogísticos (edema, calor, rubor, dor intensa). "
 "Sem porta de entrada infecciosa evidente.",
"Vertigem / Labirintite / Tontura":
 f"{_BEG}\n{_SSVV}\nNeuro: Glasgow 15, sem déficits focais. HINTS: [head-impulse / nistagmo / skew]. "
 "Nistagmo [horizontal, unidirecional, esgotável]. Marcha [com desvio], Romberg [__]. Otoscopia normal.",
"Epigastralgia / Pirose":
 f"{_BEG}\n{_SSVV}\nAbdome: dor à palpação em epigástrio, sem defesa/DB, RHA+. Sem massas. "
 "Sem sinais de alarme (sem melena, sem massa, sem emagrecimento).",
"Doença do Refluxo Gastroesofágico":
 f"{_BEG}\n{_SSVV}\nAbdome: leve dor epigástrica, sem defesa, RHA+. Orofaringe sem alterações. "
 "Sem disfagia/odinofagia, sem sinais de alarme.",
"Gastrite / DRGE":
 f"{_BEG}\n{_SSVV}\nAbdome: dor à palpação em epigástrio, sem defesa/DB, RHA+. Sem massas nem visceromegalias.",
"Constipação":
 f"{_BEG}\n{_SSVV}\nAbdome: distendido, timpânico, RHA+, indolor ou dor leve difusa, sem defesa. "
 "Toque retal: [fezes endurecidas em ampola / ampola vazia], sem massas, sem sangue.",
"Elevação Importante da PA (sem LOA)":
 f"{_BEG}, assintomático.\nSSVV: PA __/__ (reaferir após 5–10 min de repouso) | FC __.\n"
 "Neuro: sem déficits focais, sem alteração visual. ACV: RCR 2T BNF, sem sopros. AP: MV+ sem RA (sem congestão). "
 "Sem edema, pulsos simétricos. Fundo de olho [se disponível].",
"Influenza":
 f"{_BEG}, [febril].\n{_SSVV}\nOrofaringe: hiperemia leve. AP: MV+ bilateral, sem RA, SatO2 preservada. "
 "Sem sinais de gravidade (sem dispneia, sem hipoxemia).",
"Pneumonia":
 f"REG/BEG, [febril, taquipneico?].\n{_SSVV}\nAP: estertores crepitantes em base [D/E], [± sopro tubário, ↑FTV]. "
 "SatO2 __%. CURB-65: C__ U__ R__ B__ (idade≥65)__ = __ pontos. [Confusão? FR≥30? PA<90/60?].",
"Bronquite":
 f"{_BEG}, afebril.\n{_SSVV}\nAP: MV+ bilateral, [roncos/sibilos esparsos], sem estertores crepitantes localizados. "
 "SatO2 preservada.",
"Nefrolitíase / Cólica Nefrética":
 f"[REG por dor], inquieto, sem posição antálgica.\n{_SSVV}\nGiordano [positivo à D/E]. Abdome flácido, "
 "dor em flanco/fossa lombar, sem irritação peritoneal. [Sem febre — se febre, pensar em pielonefrite obstrutiva].",
"Hemorroida":
 f"{_BEG}, afebril.\nRegião anal: [mamilo hemorroidário externo trombosado / plicoma], sem abscesso/celulite perianal. "
 "Toque retal: [conforme tolerância], sem massas, sem sangue vivo abundante.",
"Enjoo / Náuseas":
 f"{_BEG}, hidratado.\n{_SSVV}\nAbdome: flácido, indolor, RHA+, sem defesa. Sem sinais de desidratação. "
 "[Investigar causa: gestação, medicações, labiríntica, gastrointestinal].",
"Cólica Biliar":
 f"{_BEG}, afebril.\n{_SSVV}\nAbdome: dor em hipocôndrio direito/epigástrio, Murphy [negativo — se positivo, pensar colecistite], "
 "sem defesa/DB, RHA+. Sem icterícia.",
"Disenteria":
 f"{_BEG}, [febril].\n{_SSVV}\nAbdome: RHA+ aumentados, dor difusa, sem defesa/DB. Fezes com [sangue/muco]. "
 "Avaliar estado de hidratação.",
"Impetigo":
 f"{_BEG}, afebril.\nPele: lesões com crostas melicéricas [± bolhas] em [face/membros], sem celulite/abscesso associado. "
 "Sem sinais sistêmicos.",
"Abscesso Cutâneo":
 f"{_BEG}\n{_SSVV}\nPele: coleção flutuante, eritematosa, dolorosa em [localização], [com/sem] celulite perilesional. "
 "[Sem sinais sistêmicos / avaliar febre].",
"Náuseas e vômitos (gestante)":
 f"{_BEG}, hidratada.\n{_SSVV}\nAbdome gravídico, indolor, RHA+. Sem sinais de desidratação. "
 "[IG __ sem; avaliar cetose/hiperêmese se vômitos incoercíveis].",
"ITU / Cistite (gestante)":
 f"{_BEG}, afebril.\n{_SSVV}\nAbdome gravídico; dor suprapúbica leve. Giordano negativo bilateral. "
 "[Se Giordano+ ou febre → pielonefrite: internar].",
}

_DISC = {
"IVAS / Amigdalite / Resfriado":
 "Viral na maioria → sintomático, SEM antibiótico. Reavaliar se dispneia, SatO2 baixa, febre >5 dias ou bifásica (piora após melhora), toxemia.",
"Faringoamigdalite":
 "75% viral. Pensar em bacteriana (estrepto) por Centor/McIsaac (febre, exsudato, adenopatia anterior dolorosa, ausência de tosse). "
 "🚩 PS/drenagem: trismo, sialorreia, voz 'batata quente', abaulamento peritonsilar, dispneia/estridor.",
"Amigdalite Aguda":
 "Bacteriana (estrepto) → ATB abaixo. 🚩 Complicação supurativa (abscesso peritonsilar): trismo, sialorreia, desvio de úvula → PS.",
"Sinusite Aguda":
 "Viral na maioria. ATB só se >10 dias sem melhora, dupla piora, ou febre alta + secreção purulenta + dor facial por 3–4 dias. "
 "🚩 Emergência: edema/eritema periorbitário, alteração visual, sinais neurológicos.",
"Otite Média Aguda":
 "Analgesia é o pilar. ATB se otorreia, toxemia/quadro grave ou falha; adulto pouco sintomático pode só observar. "
 "🚩 Mastoidite (edema retroauricular, protrusão do pavilhão), paralisia facial → PS.",
"Otite Externa":
 "Tópico + analgesia; evitar molhar o ouvido. 🚩 Otite necrotizante (diabético/imunossuprimido com dor desproporcional) → referência.",
"Rinite Alérgica":
 "Corticoide nasal é a base; anti-histamínico conforme sintomas. Orientar controle ambiental. Não requer ATB.",
"Alergia / Rinite Alérgica":
 "🚩 Sinais de anafilaxia (edema de glote/lábios, estridor, dispneia, hipotensão, dor abdominal) → adrenalina IM + PS imediato.",
"GECA / Gastroenterite (adulto)":
 "Hidratação (oral se tolera; EV se desidratação/vômitos). ATB NÃO de rotina. 🚩 Reavaliar/PS: desidratação, disenteria (sangue+febre alta), "
 "vômitos incoercíveis, abdome cirúrgico, gestante/idoso/imunossuprimido.",
"Cefaleia":
 "Primária (tensional/enxaqueca) → sintomático. 🚩 SNOOP → neuroimagem: início súbito/'pior da vida', déficit focal, febre+rigidez de nuca, "
 ">50a nova, progressiva, imunossupressão/câncer, papiledema, piora com Valsalva.",
"Enxaqueca":
 "Analgésico/AINE + antiemético, ambiente calmo e escuro. Evitar opioides. 🚩 Se sinais de alarme (SNOOP) → investigar.",
"Lombalgia / Mialgia":
 "Sem bandeira: sintomático + manter atividade; SEM imagem de rotina. 🚩 Bandeiras vermelhas: déficit motor progressivo, "
 "retenção/incontinência, anestesia em sela (cauda equina), febre, perda de peso/câncer, trauma, dor noturna, 1º episódio >50a.",
"Cólica Menstrual ou Sangramento":
 "AINE é a base da dismenorreia; antifibrinolítico se sangramento aumentado. 🚩 Instabilidade/anemia sintomática ou gestação (afastar ectópica) → PS.",
"Cistite / ITU":
 "ITU baixa não complicada (mulher não gestante). 🚩 Tratar como complicada/pielonefrite se: febre, Giordano+, toxemia, gestante, homem, sonda, imunossuprimido. "
 "Fenazopiridina (Pyridium) por no máximo 48h.",
"Pielonefrite":
 "Tolera VO e sem critério de gravidade → ATB VO ambulatorial + reavaliação em 48–72h. 🚩 Internar: sepse/toxemia, vômitos incoercíveis, "
 "gestante, obstrução, comorbidade descompensada.",
"Dengue":
 "EVITAR AINE e AAS (sangramento) — usar dipirona/paracetamol. Hidratação por peso. 🚩 Sinais de alarme (surgem na defervescência, 3º–6º dia): "
 "dor abdominal intensa, vômitos persistentes, sangramento de mucosa, letargia, lipotimia, hepatomegalia dolorosa, Ht↑ com plaquetas↓ → hidratação EV/observação.",
"Conjuntivite":
 "Maioria viral/alérgica (autolimitada). ATB tópico se bacteriana (secreção purulenta). 🚩 Encaminhar oftalmo: dor intensa, baixa de acuidade visual, "
 "fotofobia importante, hiperemia ciliar, uso de lente de contato, trauma.",
"Alergia":
 "Anti-histamínico ± corticoide conforme extensão. 🚩 Anafilaxia (edema de glote, estridor, dispneia, hipotensão) → adrenalina IM + PS.",
"Herpes Zoster":
 "Antiviral idealmente nas primeiras 72h + analgesia. 🚩 Zoster oftálmico (V1/ponta do nariz — sinal de Hutchinson) → antiviral + oftalmo urgente.",
"Herpes Simples":
 "Antiviral abrevia o quadro (melhor benefício se precoce). Orientar sobre recorrência e transmissão.",
"Escabiose":
 "Tratar o paciente E todos os contactantes/domicílio ao mesmo tempo; trocar/expor roupas de cama e corpo. Repetir o esquema em 7 dias.",
"Gota":
 "Crise: AINE OU corticoide OU colchicina (quanto mais precoce, melhor). NÃO iniciar/ajustar alopurinol durante a crise aguda. "
 "🚩 Afastar artrite séptica se monoartrite febril/porta de entrada.",
"Vertigem / Labirintite / Tontura":
 "🚩 EXCLUIR AVC (HINTS): nistagmo que muda de direção, head-impulse normal, skew deviation, déficit focal, cefaleia/instabilidade → central, PS/neuroimagem. "
 "Periférica → sintomático + manobras (se VPPB).",
"Epigastralgia / Pirose":
 "IBP + antiácido; medidas comportamentais. 🚩 Sinais de alarme (endoscopia/investigar): disfagia, emagrecimento, anemia, melena, vômitos persistentes, massa, idade >45–50a de início recente.",
"Doença do Refluxo Gastroesofágico":
 "IBP 4–8 semanas + medidas comportamentais (não deitar após comer, elevar cabeceira, evitar cafeína/álcool/tabagismo). 🚩 Sinais de alarme → EDA.",
"Gastrite / DRGE":
 "IBP em jejum + antiácido para alívio. Investigar/erradicar H. pylori conforme contexto. 🚩 Sinais de alarme → EDA.",
"Constipação":
 "Fibras/hidratação + laxativo osmótico como base; estimulante/enema se refratário. 🚩 Alarme (colonoscopia): sangramento, emagrecimento, "
 "mudança recente do hábito >50a, anemia, história familiar.",
"Elevação Importante da PA (sem LOA)":
 "Sem lesão de órgão-alvo → redução GRADUAL em 24–48h; NÃO usar nifedipino SL. Reafira a PA após repouso; ajustar/retomar anti-HTN VO + seguimento. "
 "🚩 Emergência (LOA): dor torácica, dispneia, déficit neurológico, alteração visual, dor dorsal (dissecção), gestante → PS/UTI + EV.",
"Influenza":
 "Oseltamivir com maior benefício nas primeiras 48h (priorizar grupos de risco); corrigir por função renal. "
 "🚩 Sinais de gravidade (dispneia, SatO2<95%, piora do estado geral, descompensação de comorbidade) → SRAG/PS.",
"Pneumonia":
 "Definir local pelo CURB-65/PSI + SatO2. 🚩 Internar: SatO2<92%, CURB-65≥2, instabilidade, comorbidade descompensada. "
 "Ambulatorial só se baixo risco e seguimento garantido.",
"Bronquite":
 "Habitualmente viral e autolimitada → sintomático; ATB NÃO de rotina. 🚩 Reavaliar se febre alta persistente, dispneia, SatO2 baixa (afastar pneumonia).",
"Nefrolitíase / Cólica Nefrética":
 "Analgesia (AINE/dipirona) + hidratação; tansulosina só para cálculo <1 cm SEM infecção. 🚩 Internar/urologia: febre (pielonefrite obstrutiva), "
 "rim único, LRA, gestante, imunossuprimido, dor refratária.",
"Hemorroida":
 "Fibra/hidratação + medidas locais (banho de assento, tópico). 🚩 Avaliar/cirurgia: trombose muito dolorosa (<72h drenável), sangramento importante, "
 "abscesso/celulite perianal, dúvida diagnóstica.",
"Enjoo / Náuseas":
 "Antiemético conforme causa. Sempre investigar a etiologia (gestação em mulher fértil, medicações, causa central/labiríntica, abdome agudo).",
"Cólica Biliar":
 "Analgesia + antiespasmódico; orientar dieta e seguimento (USG/eletiva). 🚩 Colecistite (Murphy+, febre, dor mantida >6h), colangite (tríade de Charcot) "
 "ou icterícia → PS/internação.",
"Disenteria":
 "Diarreia com sangue/muco + febre → considerar ATB (Cipro/Azitro) + hidratação. 🚩 Toxemia, desidratação grave, imunossuprimido → PS.",
"Impetigo":
 "Tópico (localizado) ou VO (extenso/sistêmico/falha). Higiene local + afastar de creche/escola até melhora. Evitar coçar (autoinoculação).",
"Abscesso Cutâneo":
 "Base do tratamento é DRENAGEM; ATB se celulite associada, sinais sistêmicos, imunossuprimido ou localização de risco. Compressa quente.",
"Náuseas e vômitos (gestante)":
 "Preferir antieméticos seguros na gestação. 🚩 Hiperêmese (vômitos incoercíveis, cetose, perda de peso, distúrbio hidroeletrolítico) → hidratação EV.",
"ITU / Cistite (gestante)":
 "Tratar sempre (inclui bacteriúria assintomática); escolher ATB seguro conforme IG. 🚩 Febre/Giordano+ = pielonefrite → internar (risco de trabalho de parto prematuro).",
}

_applied_ex = 0; _applied_di = 0
for _c in CONDITIONS:
    _t = _c.get("title")
    if _t in _EXAME and not _c.get("exame"):
        _c["exame"] = _EXAME[_t]; _applied_ex += 1
    if _t in _DISC:
        _c["disclaimer"] = _DISC[_t]; _applied_di += 1
