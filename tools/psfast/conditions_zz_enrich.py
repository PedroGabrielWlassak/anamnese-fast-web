# -*- coding: utf-8 -*-
# Enriquecimento parte 2 (roda por último): EF esperado + Disclaimer para os
# demais quadros clínicos. Semiologia/orientação (NUNCA dose), 100% editável.
_S = "SSVV: PA __/__ | FC __ | FR __ | SatO2 __% | Tax __°C."
_B = "BEG, corado, hidratado, acianótico, anictérico, afebril."
_BG = "BEG, corada, hidratada, acianótica, anictérica, afebril."
_OBS = ("Obstétrico: BCF __ bpm | AU __ cm | tônus uterino normal | "
        "dinâmica ausente | sem perdas vaginais | movimentação fetal presente.")

_EX2 = {
# ===================== GERAL / CRÍTICO =====================
"Anafilaxia":
 f"REG/MEG, ansioso.\n{_S}\nPele: urticária/angioedema, edema de lábios/face. VAS: [estridor, edema de glote]. "
 "AP: sibilos difusos, tiragem. ACV: taquicardia, [hipotensão]. Nível de consciência [__].",
"Ataque Isquemico Transitório":
 f"{_B} (assintomático no momento — déficit já resolvido).\n{_S}\nNeuro: Glasgow 15, SEM déficits focais no exame atual. "
 "ACV: RCR, avaliar sopro carotídeo, ritmo (FA?). Calcular ABCD2.",
"Febre Maculosa":
 f"REG, febril, toxemiado.\n{_S}\nPele: exantema maculopapular em punhos/tornozelos com progressão centrípeta (inclui palmas/plantas). "
 "Mialgia intensa. [História de carrapato/área rural]. Avaliar sinais de gravidade (petéquias, alteração neurológica).",
"Intoxicação Exógena":
 f"[Nível de consciência __], Glasgow __.\n{_S}\nPupilas [mióticas/midriáticas]. Pele [seca/sudoreica]. "
 "Toxíndrome: [colinérgica/anticolinérgica/opioide/simpaticomimética]. Odor [__]. Avaliar ABCDE.",
"Intubação Orotraqueal (70 kg)":
 f"Paciente com indicação de via aérea definitiva.\n{_S}\nGlasgow __, esforço respiratório [__], SatO2 __%. "
 "Preditores de VA difícil (LEMON/Mallampati). Pré-oxigenação, monitorização, material checado.",
"Leptospirose":
 f"REG, febril.\n{_S}\nMialgia intensa (panturrilhas), sufusão conjuntival. [Icterícia rubínica]. "
 "Avaliar oligúria/LRA, sinais hemorrágicos, comprometimento pulmonar (síndrome de Weil).",
"Picada de Aranha-Marrom":
 f"{_B}\n{_S}\nLesão: placa marmórea com halo isquêmico central em [local], dor local. "
 "Avaliar forma cutânea vs cutâneo-visceral (hemólise: icterícia, colúria, oligúria).",
"Picada de Escorpião (Acidente Escorpiônico)":
 f"[BEG/agitado por dor].\n{_S}\nLocal da picada: dor intensa, [parestesia]. "
 "Avaliar sinais sistêmicos (sudorese, sialorreia, vômitos, taquicardia, taquipneia) → moderado/grave.",
"Picada de Jararaca (Acidente Botrópico)":
 f"[BEG].\n{_S}\nLocal: edema, dor, equimose, [bolhas/necrose]. Sangramento local/gengivorragia. "
 "Avaliar tempo de coagulação, sinais de gravidade (sangramento sistêmico, oligúria, hipotensão).",
"Relação Desprotegida / Violência Sexual (PEP)":
 f"{_B}\n{_S}\nExame conforme protocolo de violência sexual (preservação de evidências se aplicável). "
 "Genital/anal: [lesões?]. Definir janela para PEP (<72h) e contracepção de emergência.",
"Sepse":
 f"REG/MEG, toxemiado.\n{_S}\nNível de consciência [rebaixado?]. Perfusão: TEC __s, extremidades [frias/quentes], livedo. "
 "Buscar foco (pulmonar/urinário/abdominal/pele/SNC). qSOFA: FR≥22 __ | PAS≤100 __ | alteração do sensório __.",
# ===================== NEURO =====================
"AVC Hemorrágico (AVCH)":
 f"[Rebaixamento], Glasgow __.\n{_S}\nNeuro: déficit focal [__], [rigidez de nuca se HSA], pupilas [__]. "
 "NIHSS __. Cefaleia súbita intensa/vômitos. PA habitualmente elevada.",
"AVC Isquêmico (AVCI)":
 f"[Alerta/rebaixado], Glasgow __.\n{_S}\nNeuro: déficit focal — [hemiparesia/disartria/desvio de rima/afasia/hemianopsia]. "
 "NIHSS __. Definir tempo de início (última vez visto bem) para janela de trombólise.",
"Cefaleia Pós-Raqui":
 f"{_B}\n{_S}\nCefaleia POSTURAL (piora ao sentar/levantar, alivia deitado), após raqui/punção. "
 "Neuro: sem déficits focais, sem rigidez de nuca. [± zumbido, fotofobia].",
"Cefaleia Tensional":
 f"{_B}, orientado.\n{_S}\nDor em aperto/pressão bilateral, leve-moderada, sem náusea. "
 "Neuro: sem déficits, sem rigidez de nuca. Tensão em musculatura cervical/trapézios.",
"Crise Convulsiva":
 f"Pós-ictal: sonolento, [confuso], Glasgow em recuperação.\n{_S}\nSem sinais de trauma cranioencefálico. "
 "Neuro: [Todd?], sem rigidez de nuca. Glicemia capilar __. Avaliar mordedura de língua/liberação esfincteriana.",
"Encefalopatia Hipertensiva":
 f"[Confuso/rebaixado], Glasgow __.\nSSVV: PA muito elevada __/__ | FC __.\nNeuro: cefaleia, [alteração visual], "
 "sem déficit focal fixo (diagnóstico de exclusão — afastar AVC). Fundo de olho: [papiledema/exsudatos].",
"Meningite Bacteriana":
 f"REG/MEG, toxemiado, febril.\n{_S}\nRigidez de nuca, Kernig/Brudzinski [positivos]. Glasgow __. "
 "[Petéquias/púrpura = meningococcemia]. Fotofobia. Avaliar sinais de HIC.",
"Neuralgia do Trigêmeo":
 f"{_B}\nDor paroxística, em choque, no território do trigêmeo (V2/V3), desencadeada por gatilhos (falar/mastigar/tocar). "
 "Neuro: SEM déficit sensitivo/motor entre as crises (se déficit → investigar causa secundária).",
"Neuralgia Pós Herpética":
 f"{_B}\nDor neuropática (queimação/choque) no dermátomo de zoster prévio, com [alodínia]. "
 "Pele: cicatrizes/hiperpigmentação da erupção prévia, sem lesões ativas.",
"Paralisia de Bell":
 f"{_B}\nParalisia facial periférica: acomete fronte (não enruga testa), sinal de Bell, apagamento do sulco nasolabial. "
 "Otoscopia normal (afastar Ramsay Hunt/otite). Restante do exame neurológico normal.",
"Síndrome de Ramsay Hunt":
 f"{_B}\nParalisia facial periférica + vesículas em conduto auditivo/pavilhão/orofaringe (zoster ótico). "
 "[Otalgia, hipoacusia, vertigem, zumbido]. Otoscopia: vesículas no CAE.",
# ===================== OLHOS =====================
"Celulite Periorbitária / Pré-Septal":
 f"{_B}, [febril].\nOlho [D/E]: edema e eritema palpebral, SEM proptose, SEM dor à motricidade ocular, "
 "SEM oftalmoplegia, acuidade e reflexos preservados (se presentes → orbitária/pós-septal = emergência).",
"Herpes Zoster Ocular":
 f"{_B}\nVesículas em dermátomo V1 (fronte/pálpebra), sinal de Hutchinson (ponta do nariz). "
 "Olho: hiperemia, [dor, fotofobia]. Avaliar acuidade visual e córnea (fluoresceína).",
"Neurite Óptica":
 f"{_B}\nOlho [D/E]: baixa de acuidade visual subaguda, dor à motricidade ocular, discromatopsia. "
 "Defeito pupilar aferente relativo (DPAR). Fundo de olho: [papilite ou normal].",
# ===================== ORL =====================
"Cerume":
 f"{_B}\nOtoscopia [D/E]: rolha de cerume ocluindo o conduto, MT não visualizada. "
 "Sem sinais de otite externa/média associada.",
"Otalgia":
 f"{_B}\n{_S}\nOtoscopia: [normal — considerar causa referida: ATM, dental, faríngea]. "
 "Palpação de ATM e cervical. Orofaringe.",
"Perfuração Membrana Timpânica":
 f"{_B}\nOtoscopia [D/E]: perfuração da MT [central/marginal], [± otorreia]. "
 "Avaliar história de trauma/otite/barotrauma. Acuidade auditiva grosseira.",
"Tosse Subaguda Pós-Viral":
 f"{_B}, afebril.\n{_S}\nOrofaringe: [gotejamento pós-nasal]. AP: MV+ sem RA, SatO2 preservada. "
 "Tosse há 3–8 semanas após IVAS, sem sinais de gravidade.",
# ===================== TÓRAX =====================
"Asma — Manutenção Gina 2026":
 f"{_B}, eupneico (fora de crise).\n{_S}\nAP: MV+ bilateral, [sibilos esparsos ou ausentes]. "
 "Avaliar controle (sintomas diurnos, despertares, uso de resgate, limitação). Técnica inalatória.",
"Bradicardia Instável":
 f"[Rebaixado/sudoreico].\nSSVV: FC < 50 __ | PA __/__ (hipotensão?) | SatO2 __%.\n"
 "Sinais de má perfusão/instabilidade (5D: dor torácica, dispneia, ↓consciência, desmaio, ↓PA). ECG: [tipo de bloqueio].",
"Coqueluche":
 f"{_B}, afebril ou febre baixa.\n{_S}\nParoxismos de tosse com guincho inspiratório/vômito pós-tosse. "
 "AP: geralmente limpo entre acessos. [Contactante/vacinação].",
"Crise de Asma — Exacerbação":
 f"[REG/MEG], [taquipneico], fala [frases/palavras].\n{_S}\nAP: sibilos difusos, tiragem, uso de acessória, "
 "[tórax silencioso = gravíssimo]. SatO2 __%. FR __. Nível de consciência.",
"Dissecção Aguda de Aorta":
 f"MEG, dor torácica/dorsal intensa 'rasgando'.\nSSVV: PA __/__ (assimetria entre MMSS?), FC __.\n"
 "Pulsos assimétricos/déficit de pulso. [Sopro de insuficiência aórtica]. Avaliar déficit neurológico/isquemia.",
"Dor Torácica — Abordagem Rápida":
 f"[BEG/MEG].\n{_S}\nACV: RCR 2T, [sopros, B3/B4], turgência jugular. AP: MV+ [estertores/abolido]. "
 "Reprodutível à palpação? Pulsos simétricos? ECG em ≤10 min. Buscar as 6 causas fatais.",
"DPOC Exacerbado":
 f"[REG], [taquipneico], tórax em tonel.\n{_S}\nAP: MV↓ difuso, sibilos/roncos, expiração prolongada. "
 "SatO2 __% (meta 88–92%). Uso de musculatura acessória, cianose, edema (cor pulmonale).",
"Edema Agudo de Pulmão":
 f"MEG, dispneia intensa, ortopneia, sudoreico.\n{_S}\nAP: estertores crepitantes bilaterais até ápices, [sibilos]. "
 "ACV: taquicardia, B3, turgência jugular. SatO2 baixa. Extremidades [frias].",
"IAM — Infarto Agudo do Miocárdio":
 f"[BEG/MEG], sudoreico, ansioso.\n{_S}\nDor precordial em aperto, irradiação [MSE/mandíbula], >20 min. "
 "ACV: RCR 2T, [B3/B4, sopro, atrito]. AP: [estertores = Killip]. ECG em ≤10 min.",
"Insuficiência Cardíaca":
 f"[REG], [dispneico].\n{_S}\nACV: turgência jugular, B3, [sopros]. AP: estertores crepitantes bibasais. "
 "Edema de MMII, [hepatomegalia, ascite]. Perfil hemodinâmico (quente/frio × seco/congesto).",
"Oclusão Arterial Aguda":
 f"{_B}, dor intensa no membro.\n{_S}\nMembro [__]: 6 P — dor, palidez, ausência de pulso, parestesia, "
 "paralisia, poiquilotermia (frio). TEC alargado. Comparar com contralateral. Tempo de isquemia.",
"Taquiarritmias":
 f"[BEG/instável], palpitações.\nSSVV: FC __ (>100) | PA __/__ | SatO2 __%.\n"
 "Avaliar instabilidade (dor torácica, dispneia, ↓consciência, hipotensão). ECG: QRS [estreito/largo], R-R [regular/irregular].",
"Tosse e SRAG":
 f"[REG], [dispneico].\n{_S}\nAP: MV+ [estertores], SatO2 __%. Avaliar sinais de gravidade "
 "(FR≥24, SatO2<95%, esforço, piora do estado geral). Definir se preenche critério de SRAG.",
"Tromboflebite Superficial":
 f"{_B}, afebril.\n{_S}\nMembro: cordão venoso endurecido, eritematoso, doloroso ao longo de trajeto de veia superficial, "
 "SEM edema importante de todo o membro (avaliar extensão e proximidade da junção safeno-femoral).",
"Trombose Venosa":
 f"{_B}\n{_S}\nMembro [__]: edema assimétrico, dor à palpação da panturrilha, [empastamento, ↑temperatura, "
 "dilatação venosa superficial]. Homans de baixo valor. Calcular escore de Wells.",
# ===================== ABDOME =====================
"Abdome Agudo Obstrutivo":
 f"[REG/MEG], [desidratado].\n{_S}\nAbdome distendido, timpânico, RHA [aumentados/metálicos ou abolidos], "
 "dor difusa, [parada de eliminação de gases/fezes], vômitos. Toque retal: ampola [vazia]. Cicatrizes prévias.",
"Apendicite Aguda — Score de Alvarado":
 f"{_B}, [febril].\n{_S}\nAbdome: dor em FID (McBurney), Blumberg [+], [Rovsing, psoas, obturador]. "
 "Defesa localizada. Alvarado: __ pontos. βhCG em mulher fértil.",
"Candidiase Oral":
 f"{_B}\nCavidade oral: placas brancas removíveis (aspecto de leite coalhado) em mucosa jugal/língua/palato, "
 "com base eritematosa. Avaliar fatores predisponentes (ATB, corticoide inalatório, imunossupressão, DM).",
"Colecistite Aguda":
 f"[REG], febril.\n{_S}\nAbdome: dor em HD, sinal de MURPHY POSITIVO, [defesa localizada]. RHA+. "
 "[Icterícia leve]. Avaliar sinais de colangite (tríade de Charcot).",
"Colite Pseudomembranosa":
 f"[REG], [febril].\n{_S}\nAbdome: distendido, dor difusa, RHA+. Diarreia volumosa (uso recente de ATB). "
 "Avaliar desidratação e sinais de gravidade (megacólon: distensão importante, toxemia).",
"Diverticulite Aguda":
 f"{_B}, [febril].\n{_S}\nAbdome: dor em FIE, [defesa/Blumberg localizado em FIE], massa palpável dolorosa? "
 "RHA+/↓. Avaliar sinais de complicação (peritonite difusa, sepse).",
"Enterobíase / Oxiurose":
 f"{_B}\nRegião perianal: [escoriações por prurido]. Prurido anal de predomínio noturno. "
 "Restante do exame sem alterações. [Contactantes/creche].",
"Hemorragia Digestiva Alta":
 f"[REG/MEG, palidez].\n{_S} (avaliar hipotensão postural).\nToque retal: MELENA. [Hematêmese/borra de café]. "
 "Estigmas de hepatopatia? Avaliar repercussão hemodinâmica e classificar (Blatchford).",
"Pancreatite Aguda":
 f"[REG/MEG].\n{_S}\nAbdome: dor epigástrica intensa em faixa/irradiação dorsal, [distensão], RHA↓. "
 "[Sinais de Cullen/Grey-Turner = grave]. Avaliar SIRS/gravidade.",
"Parasitose":
 f"{_B}\n{_S}\nAbdome: flácido, RHA+, [dor difusa leve]. Avaliar palidez (anemia), prurido anal. "
 "Geralmente exame pobre; contexto epidemiológico.",
"Soluço":
 f"{_B}\n{_S}\nSoluço persistente. Exame geralmente normal — investigar causa (refluxo, irritação diafragmática, "
 "SNC, distúrbio metabólico) se >48h/refratário.",
"Xerostomia":
 f"{_B}\nCavidade oral: mucosa seca, saliva escassa/espessa, [candidíase associada, cáries]. "
 "Avaliar medicações xerostomizantes e doenças associadas (Sjögren, DM).",
# ===================== METAB =====================
"Cetoacidose Diabética":
 f"[REG/MEG], desidratado, [rebaixado].\n{_S}\nRitmo de Kussmaul, hálito cetônico. Mucosas secas, TEC alargado. "
 "Glicemia capilar __ (>250). Buscar fator precipitante (infecção, má adesão). Cetonúria/cetonemia.",
"Estado Hiperglicêmico Hiperosmolar":
 f"[Rebaixado], desidratação grave.\n{_S}\nMucosas muito secas, TEC alargado, [hipotensão]. Glicemia capilar __ (muito alta, >600). "
 "Sem Kussmaul/cetose importante. Nível de consciência ∝ osmolaridade. Buscar precipitante.",
"Hiperglicemia":
 f"{_B}\n{_S}\nGlicemia capilar __. Avaliar sintomas (poliúria, polidipsia), sinais de desidratação, "
 "cetose (afastar CAD/EHH). Buscar infecção/fator descompensador.",
"Hiperpotassemia":
 f"{_B} (sintomas inespecíficos).\n{_S}\nAvaliar fraqueza muscular, [arritmia]. ECG obrigatório: onda T apiculada, "
 "alargamento de QRS, ↓onda P. K sérico __. Buscar causa (LRA, drogas, rabdomiólise).",
"Hipoglicemia":
 f"[Sudoreico/rebaixado/agitado].\n{_S}\nGlicemia capilar __ (<70). Sinais adrenérgicos (tremor, sudorese, taquicardia) "
 "e neuroglicopênicos (confusão, déficit focal transitório, ↓consciência). Buscar causa (jejum, insulina/hipoglicemiante).",
"Hiponatremia":
 f"[Variável conforme gravidade/velocidade].\n{_S}\nAvaliar volemia (hipo/eu/hipervolêmica): mucosas, TEC, edema, turgência. "
 "Neuro: [confusão, cefaleia, convulsão se grave/aguda]. Na sérico __.",
"Hipopotassemia":
 f"{_B}\n{_S}\nFraqueza muscular, [cãibras], [íleo]. ECG: onda U, achatamento de T, [ESV]. "
 "K sérico __. Buscar causa (perdas GI, diuréticos).",
"Rabdomiólise":
 f"{_B}\n{_S}\nMialgia, fraqueza, urina escura (mioglobinúria — 'cor de coca-cola'). [Edema/dor muscular localizada]. "
 "Buscar causa (trauma/imobilização, exercício, drogas, convulsão). CPK __.",
# ===================== HEMATO =====================
"Anemia Ferropriva":
 f"{_B}\n{_S}\nPalidez cutâneo-mucosa, [coiloníquia, queilite angular]. ACV: [sopro sistólico funcional]. "
 "Investigar fonte de perda (menstrual, digestiva). Hb __.",
"Anemia Megaloblástica":
 f"{_B}\n{_S}\nPalidez, [glossite, icterícia leve]. Neuro (B12): [parestesias, ↓propriocepção, marcha atáxica]. "
 "Investigar dieta/absorção. Hb/VCM __.",
"Crise Álgica Falcêmica":
 f"[REG por dor].\n{_S}\nDor óssea/articular difusa, [priapismo]. Avaliar sinais de complicação: "
 "síndrome torácica aguda (dor torácica, hipoxemia, infiltrado), sequestro, febre/infecção, AVC.",
"Epistaxe":
 f"{_B}\nSSVV: PA __/__ | FC __ (avaliar HAS/repercussão).\nRinoscopia: sangramento [anterior — Kiesselbach / posterior]. "
 "Avaliar uso de anticoagulante/antiagregante, coagulopatia. Estimar volume.",
"Neutropenia Febril":
 f"[REG/MEG], febril.\n{_S}\nBuscar foco minucioso (cavidade oral, pele/cateter, perianal — evitar toque retal, "
 "pulmonar, urinário). Sinais de sepse. Quimioterapia recente. Calcular MASCC.",
"Transfusão de Hemoderivados":
 f"{_B}\n{_S}\nAvaliar indicação e alvo (Hb/plaquetas/coagulação). Durante: monitorar febre, calafrio, dispneia, "
 "urticária, dor lombar, hipotensão (reação transfusional). Checar compatibilidade/identificação.",
# ===================== MSK =====================
"Dor Crônica":
 f"{_B}\n{_S}\nExame do sítio doloroso: [articular/miofascial/neuropático]. Amplitude de movimento, pontos-gatilho, "
 "sinais neurológicos. Escala de dor __/10. Impacto funcional. Sem sinais de alarme (bandeiras vermelhas).",
"Entorse do Tornozelo":
 f"{_B}\nTornozelo [D/E]: edema e dor em [maléolo lateral/ligamento talofibular anterior], equimose. "
 "Carga [possível/impossível]. Critérios de Ottawa (dor em maléolo posterior/base do 5º meta/navicular).",
"Fasciíte Plantar":
 f"{_B}\nPé [D/E]: dor à palpação da inserção da fáscia plantar no calcâneo, pior aos primeiros passos matinais. "
 "Dorsiflexão dos pododáctilos reproduz dor. Sem sinais inflamatórios sistêmicos.",
"Insuficiência Venosa Crônica":
 f"{_B}\n{_S}\nMMII: varizes, edema vespertino, dermatite ocre, [lipodermatosclerose, úlcera maleolar medial]. "
 "Pulsos distais presentes (afastar componente arterial). Sem sinais de TVP aguda.",
"Osteoartrite":
 f"{_B}\nArticulação [joelho/mãos/quadril]: dor mecânica, crepitação, [nódulos de Heberden/Bouchard], "
 "limitação de ADM, [derrame leve]. Sem sinais inflamatórios exuberantes/febre.",
# ===================== GU =====================
"Atrofia Urogenital":
 f"{_BG}\nExame genital: mucosa vaginal pálida, fina, ressecada, [perda de rugosidade, petéquias]. "
 "Contexto de pós-menopausa. Sintomas de secura/dispareunia/urinários.",
"Bacteriúria Assintomática":
 f"{_B}, ASSINTOMÁTICO.\n{_S}\nSem disúria/polaciúria/dor lombar. Giordano negativo. "
 "Urocultura positiva sem sintomas. (Tratar apenas gestante/pré-procedimento urológico.)",
"Balanite":
 f"{_B}\nGlande/prepúcio: eritema, edema, [secreção, placas esbranquiçadas se candidiásica]. "
 "Avaliar fimose/higiene, DM. Sem úlcera (se úlcera → investigar IST).",
"Cancro Mole":
 f"{_B}\nGenital: úlcera(s) DOLOROSA(S), fundo sujo/purulento, bordas irregulares e amolecidas. "
 "Adenopatia inguinal dolorosa [bubão, fistulizado]. (vs cancro duro da sífilis: indolor.)",
"Candidíase":
 f"{_BG}\nExame especular: corrimento branco grumoso ('leite talhado'), aderido, hiperemia/edema vulvovaginal, prurido. "
 "pH vaginal normal (<4,5). Sem odor de peixe.",
"Cervicite":
 f"{_BG}\nEspecular: colo hiperemiado, friável, com secreção mucopurulenta no orifício. "
 "Dor à mobilização do colo? (afastar DIP). Coletar para gonococo/clamídia.",
"Climatério Sintomas Vasomotores":
 f"{_BG}\n{_S}\nExame geral sem alterações agudas. Contexto de peri/pós-menopausa (fogachos, sudorese, insônia). "
 "Avaliar sinais de atrofia urogenital associada. PA/IMC.",
"Gonorreia":
 f"{_B}\nGenital: [secreção uretral purulenta abundante / corrimento cervical mucopurulento]. "
 "Disúria. Avaliar acometimento faríngeo/anal e coinfecção por clamídia.",
"Herpes Genital":
 f"{_B}\nGenital: vesículas agrupadas e/ou úlceras rasas DOLOROSAS em base eritematosa, [adenopatia inguinal dolorosa]. "
 "Primoinfecção: mais extenso + sintomas sistêmicos.",
"Incontinência Urinária":
 f"{_B}\n{_S}\nAvaliar tipo (esforço/urgência/mista): teste de esforço, [prolapso genital], resíduo pós-miccional. "
 "Toque: tônus/força do assoalho pélvico. Afastar ITU/causa reversível.",
"Linfogranuloma Venéreo":
 f"{_B}\nGenital: úlcera/pápula transitória (pode passar despercebida) seguida de adenopatia inguinal dolorosa "
 "(bubão), [sinal do sulco]. Avaliar forma anorretal (proctite) em contexto de risco.",
"Mastite":
 f"{_BG}, [febril].\n{_S}\nMama [D/E]: área de eritema, calor, dor e endurecimento (geralmente lactante). "
 "Avaliar flutuação (abscesso), fissura mamilar, adenopatia axilar.",
"Orquiepididimite":
 f"{_B}, [febril].\n{_S}\nBolsa escrotal [D/E]: dor e edema de epidídimo/testículo, [hiperemia], "
 "Prehn positivo (alívio com elevação), reflexo cremastérico presente (afastar torção — Prehn neg/cremastérico ausente).",
"Sangramento Uterino Anormal":
 f"{_BG}, [palidez se sangramento importante].\n{_S} (avaliar repercussão/hipotensão).\n"
 "Especular: origem do sangramento, volume, [coágulos]. βhCG. Avaliar anemia sintomática.",
"Sífilis":
 f"{_B}\nPrimária: cancro DURO — úlcera única, indolor, base endurecida, adenopatia indolor. "
 "Secundária: roséola/lesões palmoplantares, condiloma plano. Solicitar VDRL/teste treponêmico.",
"Tricomoníase":
 f"{_BG}\nEspecular: corrimento amarelo-esverdeado bolhoso, abundante, colo 'em framboesa', pH >4,5, "
 "prurido/ardor vulvar. Teste de aminas [+]. IST — tratar parceria.",
"Vaginose":
 f"{_BG}\nEspecular: corrimento branco-acinzentado homogêneo, aderente, odor de peixe (teste de aminas +), "
 "pH >4,5, SEM inflamação exuberante. Critérios de Amsel.",
# ===================== PELE =====================
"Dermatite de Contato":
 f"{_B}\nPele: eritema, vesículas, [descamação/liquenificação se crônica] com distribuição na área de contato "
 "(padrão geográfico/linear). Prurido. Identificar agente (níquel, cosmético, planta).",
"Dermatite Perioral":
 f"{_B}\nFace: pápulas e pústulas eritematosas perorais, poupando a borda vermelha dos lábios (zona clara). "
 "História de corticoide tópico facial. Sem comedões (vs acne).",
"Drenagem Abscesso":
 f"{_B}, [afebril].\n{_S}\nColeção flutuante, eritematosa e dolorosa em [local], [ponto de drenagem]. "
 "Avaliar celulite perilesional e sinais sistêmicos. Sensibilidade/perfusão distais preservadas.",
"Erisipela / Celulite":
 f"{_B}, [febril].\n{_S}\nPele [membro/face]: placa eritematosa, quente, dolorosa, [bordas nítidas na erisipela / "
 "difusas na celulite], [bolhas, linfangite, adenopatia]. Identificar porta de entrada (micose interdigital, ferida).",
"Furunculo / Carbunculo":
 f"{_B}\nPele: nódulo(s) foliculares eritematosos e dolorosos com [ponto de pus central], "
 "carbúnculo = confluência de vários. Avaliar celulite associada e sinais sistêmicos. DM?",
"Hidradenite Supurativa":
 f"{_B}\nÁreas intertriginosas (axila/inguinal/inframamária): nódulos dolorosos recidivantes, abscessos, "
 "[fístulas, cicatrizes em ponte, comedões duplos]. Estadiar (Hurley I–III).",
"Pediculose":
 f"{_B}\nCouro cabeludo (ou púbis): lêndeas aderidas à haste do cabelo, [piolhos vivos], escoriações por prurido, "
 "[adenopatia cervical posterior]. Contactantes.",
"Queimadura":
 f"{_B}\n{_S}\nQueimadura em [local]: profundidade [1º/2º superficial/2º profundo/3º], SCQ estimada __% (regra dos 9). "
 "Avaliar vias aéreas (fuligem, rouquidão), áreas nobres (face/mãos/pés/períneo), circunferencial.",
"Queimadura Elétrica":
 f"{_B}\n{_S}\nMarcas de entrada/saída da corrente em [locais]. Lesão tecidual pode ser MUITO maior que a aparente. "
 "ECG/monitorização (arritmia), avaliar mioglobinúria/rabdomiólise, síndrome compartimental.",
"Tínea Capitis":
 f"{_B}\nCouro cabeludo: placa(s) de alopecia com descamação, [cabelos tonsurados, pontos pretos], "
 "[querion = placa inflamatória dolorosa]. Adenopatia cervical/occipital. Luz de Wood se disponível.",
# ===================== PSIQ =====================
"Abstinência Alcoólica":
 f"[Ansioso/agitado, tremor].\n{_S}\nTremor de extremidades, sudorese, taquicardia, HAS. "
 "Avaliar gravidade (CIWA-Ar): alucinações, convulsão, desorientação (delirium tremens). Glicemia/hidratação.",
# ===================== GESTANTE =====================
"Anemia (gestante)":
 f"{_BG}\n{_S}\nPalidez cutâneo-mucosa. {_OBS}\nHb __ (ajustar meta na gestação).",
"Ansiedade / Depressão (gestante)":
 f"{_BG}\n{_S}\nHumor/afeto [__], ansiedade, [insônia]. Avaliar risco (ideação, funcionalidade). {_OBS}",
"Broncoespasmo / Crise asmática (gestante)":
 f"[REG], [taquipneica].\n{_S}\nAP: sibilos difusos, SatO2 __% (manter ≥95% — feto é sensível à hipóxia). {_OBS}",
"Candidíase (gestante)":
 f"{_BG}\nEspecular: corrimento branco grumoso aderido, prurido/hiperemia vulvovaginal, pH normal. {_OBS}",
"Clamídia / Gonorreia (gestante)":
 f"{_BG}\nEspecular: colo friável com secreção mucopurulenta. {_OBS}\nRastrear/tratar parceria; risco de transmissão perinatal.",
"Constipação (gestante)":
 f"{_BG}\nAbdome gravídico, RHA+, [distensão leve], indolor. Toque retal se necessário. {_OBS}",
"Diabetes (gestante)":
 f"{_BG}\n{_S}\nGlicemia capilar __. Avaliar controle glicêmico. {_OBS}",
"Diarreia (gestante)":
 f"{_BG}, hidratada.\n{_S}\nAbdome gravídico, RHA+ aumentados, dor difusa leve, sem defesa. {_OBS}",
"Doença hemorroidária (gestante)":
 f"{_BG}\nRegião anal: mamilos hemorroidários [externos/trombosados], sem abscesso/celulite. {_OBS}",
"Dor (gestante)":
 f"{_BG}\n{_S}\nExame do sítio doloroso [__]. {_OBS}\nEvitar AINE (sobretudo 3º trimestre).",
"Dor abdominal (gestante)":
 f"{_BG}\n{_S}\nAbdome gravídico: localizar dor, RHA, defesa/DB. {_OBS}\n"
 "🚩 Diferenciar de causas obstétricas (DPP, TPP, pré-eclâmpsia) e cirúrgicas (apendicite).",
"Epigastralgia (gestante)":
 f"{_BG}\n{_S}\nAbdome: dor epigástrica. {_OBS}\n🚩 Se 3º trim + HAS/cefaleia/escotomas → afastar pré-eclâmpsia/HELLP (dor em HD/epigástrio).",
"Epilepsia (gestante)":
 f"{_BG}\n{_S}\nPós-ictal se crise recente. Neuro: [déficit?]. {_OBS}\n"
 "🚩 Crise no 3º trim/periparto com HAS → afastar eclâmpsia.",
"Hipertensão (gestante)":
 f"{_BG}\nSSVV: PA __/__ (repetir), FC __.\nEdema [__], reflexos [normo/hiperativos], [clônus]. {_OBS}\n"
 "🚩 Sinais de pré-eclâmpsia grave: cefaleia, escotomas, dor em HD/epigástrio, hiper-reflexia.",
"Pielonefrite (gestante)":
 f"REG, febril.\n{_S}\nGiordano POSITIVO à [D/E]. {_OBS}\n"
 "Alto risco de trabalho de parto prematuro/sepse → internar.",
"Pneumonia / Sinusite / Amigdalite (gestante)":
 f"{_BG}, [febril].\n{_S}\nFoco: [AP com estertores / orofaringe com exsudato / dor em seios da face]. SatO2 __%. {_OBS}",
"Prurido (gestante)":
 f"{_BG}\nPele: [lesões urticariformes / sem lesões]. {_OBS}\n"
 "🚩 Prurido palmoplantar sem lesões no 3º trim → afastar colestase gravídica (dosar ácidos biliares/TGO/TGP).",
"Síndrome gripal (gestante)":
 f"{_BG}, [febril].\n{_S}\nOrofaringe hiperemiada, coriza. AP: MV+ sem RA, SatO2 preservada. {_OBS}\n"
 "Gestante é grupo de risco para influenza — baixo limiar para oseltamivir.",
"Tricomoníase (gestante)":
 f"{_BG}\nEspecular: corrimento amarelo-esverdeado bolhoso, colo 'em framboesa', pH >4,5, teste de aminas +. {_OBS}",
"Vaginose (gestante)":
 f"{_BG}\nEspecular: corrimento acinzentado homogêneo, odor de peixe (aminas +), pH >4,5. {_OBS}\n"
 "Associada a parto prematuro — tratar.",
}

_DI2 = {
"Anafilaxia":
 "EMERGÊNCIA. 1ª linha = ADRENALINA IM (vasto lateral) — não retardar. MOV, decúbito, O2, expansão. Corticoide/anti-H1 são adjuvantes. Observar (reação bifásica).",
"Ataque Isquemico Transitório":
 "Déficit neurológico transitório totalmente resolvido. Risco alto de AVC nas 48h → estratificar (ABCD2), antiagregar e investigar (imagem, carótidas, ECG/FA). 🚩 Se déficit persiste = AVC.",
"Febre Maculosa":
 "EMERGÊNCIA infecciosa — iniciar DOXICICLINA na SUSPEITA (não aguardar confirmação). 🚩 Letal se atrasar. Contexto: febre + mialgia + exantema (palmas/plantas) + carrapato/área rural.",
"Intoxicação Exógena":
 "ABCDE primeiro. Ligar CEATOX 0800-014-8110. Identificar toxíndrome e antídoto. 🚩 Rebaixamento, arritmia, convulsão, instabilidade → suporte + PS.",
"Intubação Orotraqueal (70 kg)":
 "Procedimento de sala. Sequência rápida: preparo (aspirador/material/drogas), pré-oxigenação, indução + BNM, IOT, confirmar (ausculta/capnografia), fixar + ventilador + sedação.",
"Leptospirose":
 "Antibiótico + suporte; hidratação. 🚩 Internar: icterícia, oligúria/LRA, sangramento, comprometimento pulmonar (Weil) — pode ser fatal. Evitar AINE/AAS.",
"Picada de Aranha-Marrom":
 "Loxoscelismo: forma cutânea (placa marmórea/necrose) vs cutâneo-visceral (hemólise). 🚩 Hemólise (icterícia, colúria, oligúria) → soro específico + internação.",
"Picada de Escorpião (Acidente Escorpiônico)":
 "Maioria leve (só analgesia local). 🚩 Moderado/grave (sudorese, vômitos, sialorreia, taquicardia/taquipneia, EAP) — sobretudo criança → soroterapia + observação/UTI.",
"Picada de Jararaca (Acidente Botrópico)":
 "Acidente botrópico: síndrome local + distúrbio de coagulação. Classificar (leve/moderado/grave) define nº de ampolas de soro. Monitorar TC/sangramento e função renal.",
"Relação Desprotegida / Violência Sexual (PEP)":
 "PEP para HIV é URGENTE (idealmente <2h, até 72h). Incluir contracepção de emergência, profilaxia de ISTs, hepatite B, sorologias e notificação/acolhimento se violência.",
"Sepse":
 "Pacote da 1ª hora: culturas + lactato, ATB de amplo espectro precoce, cristaloide 30 ml/kg. 🚩 Choque séptico (hipotensão refratária/lactato alto) → vasopressor + UTI.",
"AVC Hemorrágico (AVCH)":
 "EMERGÊNCIA — TC de crânio imediata. Controle pressórico, reverter anticoagulação, neurocirurgia. NÃO antiagregar. UTI. 🚩 Rebaixamento/HIC.",
"AVC Isquêmico (AVCI)":
 "TEMPO É CÉREBRO — TC + avaliar janela de trombólise (≤4,5h) / trombectomia. Definir última vez visto bem. Não baixar PA agressivamente (exceto pré-trombólise). Glicemia.",
"Cefaleia Pós-Raqui":
 "Cefaleia postural pós-punção. Conservador (repouso, hidratação, cafeína, analgesia). 🚩 Refratária → blood patch. Afastar febre/rigidez (meningite).",
"Cefaleia Tensional":
 "Analgésico simples/AINE; evitar uso abusivo (cefaleia por rebote). Profilaxia (amitriptilina) se frequente. 🚩 Reavaliar se muda o padrão (SNOOP).",
"Crise Convulsiva":
 "Proteger, glicemia capilar, benzodiazepínico se crise >5 min/repetida. Investigar causa (glicemia, eletrólitos, TC, infecção, abstinência). 🚩 Estado de mal → PS.",
"Encefalopatia Hipertensiva":
 "Emergência hipertensiva — diagnóstico de exclusão (afastar AVC/HSA). Reduzir PA de forma CONTROLADA e EV (≤25% da PAM na 1ª h) em UTI. Reversível se tratada.",
"Meningite Bacteriana":
 "EMERGÊNCIA — ATB empírico PRECOCE (+ dexametasona antes/junto), não atrasar por exames. Isolar se meningococo + quimioprofilaxia de contactantes. 🚩 Púrpura/sepse.",
"Neuralgia do Trigêmeo":
 "1ª linha carbamazepina; encaminhar neuro. 🚩 Início <40a, déficit sensitivo ou bilateral → investigar causa secundária (RM).",
"Neuralgia Pós Herpética":
 "Dor neuropática após zoster — gabapentina/amitriptilina/capsaicina; tratamento antiviral precoce do zoster reduz o risco. Manejo de dor crônica.",
"Paralisia de Bell":
 "Paralisia facial periférica idiopática — corticoide precoce (<72h) melhora prognóstico; proteção ocular. 🚩 Se central (poupa fronte) ou outros déficits → investigar AVC.",
"Síndrome de Ramsay Hunt":
 "Zoster do gânglio geniculado — antiviral + corticoide precoces (melhor recuperação facial). Proteção ocular. 🚩 Vertigem/hipoacusia intensas → internar/ORL.",
"Celulite Periorbitária / Pré-Septal":
 "Pré-septal (sem proptose/oftalmoplegia/dor à motricidade) → ATB VO + reavaliação. 🚩 Sinais orbitários (proptose, dor ao mover, ↓visão, oftalmoplegia) = pós-septal = TC + PS/EV.",
"Herpes Zoster Ocular":
 "Antiviral sistêmico precoce + oftalmo urgente. 🚩 Sinal de Hutchinson (ponta do nariz), ↓acuidade, comprometimento corneano.",
"Neurite Óptica":
 "Baixa visual + dor à motricidade + DPAR. Investigar (RM, afastar EM). Encaminhar oftalmo/neuro. 🚩 Bilateral/atípica → causa alternativa.",
"Cerume":
 "Cerume impactado sintomático → cerumenolítico ± lavagem. 🚩 Não irrigar se suspeita/história de perfuração de MT ou otite.",
"Otalgia":
 "Otoscopia normal → pensar em dor REFERIDA (ATM, dental, faríngea, cervical). Tratar a causa. 🚩 Otalgia + fatores de risco (tabagista, adulto, unilateral persistente) → afastar neoplasia/ORL.",
"Perfuração Membrana Timpânica":
 "Maioria fecha espontaneamente. Manter ouvido SECO, evitar gotas ototóxicas; analgesia. Retorno ORL. 🚩 Vertigem intensa/perda auditiva importante/paralisia facial.",
"Tosse Subaguda Pós-Viral":
 "Tosse 3–8 semanas pós-IVAS, autolimitada — considerar gotejamento pós-nasal/hiper-reatividade. ATB não indicado. 🚩 Reavaliar se >8 sem, hemoptise, emagrecimento, dispneia.",
"Asma — Manutenção Gina 2026":
 "NÃO usar SABA isolado — todo paciente precisa de corticoide inalatório (CI-formoterol preferido). Ajustar step pelo controle, checar técnica/adesão. Enxaguar boca após CI.",
"Bradicardia Instável":
 "Instável (hipotensão, ↓consciência, dor torácica, dispneia) → atropina; se refratária, marca-passo transcutâneo/drogas. Buscar causa (drogas, IAM, hipercalemia, hipóxia). PS/monitor.",
"Coqueluche":
 "Macrolídeo (reduz transmissão) + isolamento respiratório; notificar. 🚩 Lactente (apneia/cianose) → internar. Quimioprofilaxia de contactantes.",
"Crise de Asma — Exacerbação":
 "SABA + ipratrópio + corticoide sistêmico precoce; O2 alvo 93–95%. Reavaliar em 1h. 🚩 Grave/sem resposta (tórax silencioso, ↓consciência, SatO2 baixa) → MgSO4 EV + UTI.",
"Dissecção Aguda de Aorta":
 "EMERGÊNCIA — dor 'rasgando' + assimetria de pulso/PA. Controle rápido de FC e PA (betabloqueio antes de vasodilatador). Angio-TC. Cirurgia (tipo A). Não anticoagular.",
"Dor Torácica — Abordagem Rápida":
 "ECG em ≤10 min + troponina seriada. Afastar as 6 causas fatais (SCA, dissecção, TEP, pneumotórax hipertensivo, tamponamento, ruptura de esôfago) antes de rotular como musculoesquelético.",
"DPOC Exacerbado":
 "Broncodilatador + corticoide sistêmico + ATB (se ↑purulência/volume ou VNI). O2 alvo 88–92% (cuidado com hipercapnia). 🚩 Rebaixamento/acidose → VNI/UTI.",
"Edema Agudo de Pulmão":
 "EMERGÊNCIA — sentar, O2/VNI, diurético, vasodilatador (se PA permite), tratar causa (SCA, crise HTN, arritmia). 🚩 Hipotensão/choque → cuidado com vasodilatador, UTI.",
"IAM — Infarto Agudo do Miocárdio":
 "ECG ≤10 min. COM supra → reperfusão (angioplastia/trombólise) IMEDIATA. AAS + 2º antiagregante, analgesia, monitor. 🚩 Killip alto/instabilidade → UTI.",
"Insuficiência Cardíaca":
 "Descompensada → diurético + vasodilatador conforme perfil (quente-congesto o mais comum). Buscar fator descompensador. 🚩 Frio-congesto/choque → inotrópico/UTI.",
"Oclusão Arterial Aguda":
 "EMERGÊNCIA (janela ~6h) — anticoagular JÁ, não aguardar exames, contato imediato com cirurgia vascular. 🚩 Paralisia/anestesia = isquemia avançada.",
"Taquiarritmias":
 "Instável (hipotensão/↓consciência/dor torácica/dispneia) → cardioversão sincronizada. Estável → conforme QRS/RR (vagal/adenosina, controle de FC, antiarrítmico). Tratar causa.",
"Tosse e SRAG":
 "Sintomático; oseltamivir se influenza/grupo de risco. 🚩 SRAG (dispneia, SatO2<95%, FR≥24, piora do estado geral, ↓PA) → O2 + PS/internação + notificar.",
"Tromboflebite Superficial":
 "AINE + medidas locais; anticoagular se extensa/próxima da junção safeno-femoral ou alto risco. 🚩 Avaliar TVP associada (doppler) se dúvida.",
"Trombose Venosa":
 "Confirmar (Wells + doppler/D-dímero) e anticoagular. 🚩 Sinais de TEP (dispneia, dor torácica, taquicardia, hipóxia) → avaliar/estratificar urgente.",
"Abdome Agudo Obstrutivo":
 "Dieta zero, SNG, hidratação, correção hidroeletrolítica + avaliação CIRÚRGICA. 🚩 Sinais de estrangulamento/perfuração (febre, taquicardia, defesa, acidose) → cirurgia urgente.",
"Apendicite Aguda — Score de Alvarado":
 "Alvarado guia (não substitui clínica): baixo → observar; intermediário → imagem; alto → cirurgia. βhCG em mulher fértil (afastar ectópica). Analgesia NÃO mascara. 🚩 Peritonite.",
"Candidiase Oral":
 "Antifúngico tópico (nistatina) ou sistêmico. Corrigir predisponente (higiene, corticoide inalatório → enxaguar). 🚩 Extensa/recorrente/disfagia → investigar imunossupressão (HIV, esofagite).",
"Colecistite Aguda":
 "Murphy+ + febre → internação, dieta zero, hidratação, ATB, analgesia + avaliação cirúrgica (colecistectomia). 🚩 Colangite (Charcot/Reynolds) = emergência.",
"Colite Pseudomembranosa":
 "C. difficile (uso recente de ATB) → suspender o ATB culpado + tratar (metronidazol/vancomicina VO). 🚩 Megacólon tóxico/toxemia/↑lactato → cirurgia/UTI.",
"Diverticulite Aguda":
 "Não complicada (sem complicação em imagem) → ATB + dieta conforme tolerância, ambulatorial em selecionados. 🚩 Complicada (abscesso/perfuração/peritonite/sepse) → internação/cirurgia.",
"Enterobíase / Oxiurose":
 "Antiparasitário (dose única + repetir em 2 semanas) — tratar toda a família. Higiene (unhas curtas, roupas de cama). Benigno.",
"Hemorragia Digestiva Alta":
 "Estabilizar (2 acessos, cristaloide, transfusão por meta), IBP EV, avaliar hemodinâmica → EDA. Se varicosa: ATB + terlipressina. 🚩 Instabilidade → UTI.",
"Pancreatite Aguda":
 "Diagnóstico (2 de 3: dor típica, lipase ↑3x, imagem). Hidratação vigorosa + analgesia + dieta zero inicial. Buscar etiologia (biliar/álcool). 🚩 Sinais de gravidade/necrose → UTI.",
"Parasitose":
 "Antiparasitário conforme agente; medidas de higiene/saneamento. Benigno. 🚩 Anemia importante, obstrução (áscaris), síndrome de Löffler.",
"Soluço":
 "Agudo é benigno (medidas físicas). Persistente (>48h) → investigar causa (refluxo, irritação diafragmática/frênica, SNC, metabólico) + tratamento medicamentoso.",
"Xerostomia":
 "Medidas locais (hidratação, saliva artificial, sialogogo) + tratar candidíase/cáries. Revisar medicações. 🚩 Xeroftalmia associada → investigar Sjögren.",
"Cetoacidose Diabética":
 "EMERGÊNCIA — hidratação vigorosa + insulina EV + reposição de K (NÃO iniciar insulina se K<3,3) + tratar precipitante. Monitorar glicemia/K/gaso. UTI/internação.",
"Estado Hiperglicêmico Hiperosmolar":
 "EMERGÊNCIA — desidratação intensa; reposição volêmica cuidadosa + insulina + K + tratar precipitante. Mortalidade alta. Corrigir osmolaridade devagar. UTI.",
"Hiperglicemia":
 "Assintomática sem cetose → ajustar tratamento/orientar + seguimento. 🚩 Cetose/desidratação/rebaixamento → afastar CAD/EHH (gaso, cetona, osmolaridade).",
"Hiperpotassemia":
 "ECG obrigatório. 🚩 Alterações no ECG ou K muito alto = EMERGÊNCIA — gluconato de cálcio (estabiliza membrana) + insulina+glicose/β2 (shift) + remover K (diurético/diálise).",
"Hipoglicemia":
 "Corrigir JÁ (glicose oral se consciente / glicose hipertônica EV se rebaixado); em etilista/desnutrido dar tiamina antes. Observar recorrência (sulfonilureia/insulina longa). Buscar causa.",
"Hiponatremia":
 "Corrigir conforme volemia, sintomas e velocidade. 🚩 Sintomática grave (convulsão/coma) → salina hipertônica com cautela. NÃO corrigir rápido (risco de mielinólise).",
"Hipopotassemia":
 "Repor K (VO se leve, EV se grave/sintomático/ECG alterado) — corrigir também Mg. Monitor se EV. Buscar/tratar causa (perdas, diurético).",
"Rabdomiólise":
 "Hidratação EV vigorosa (prevenir LRA) + monitorar CPK/K/função renal + tratar causa. 🚩 LRA, hipercalemia, síndrome compartimental → internar.",
"Anemia Ferropriva":
 "Repor ferro (VO, longe de refeição/com vitamina C) + INVESTIGAR a fonte de perda (sempre — sobretudo digestiva em homem/pós-menopausa). Reavaliar Hb.",
"Anemia Megaloblástica":
 "Repor B12/ácido fólico conforme deficiência (B12 preferir IM se má absorção). Investigar causa. 🚩 Sintomas neurológicos (B12) — repor B12 antes de folato isolado.",
"Crise Álgica Falcêmica":
 "Analgesia PRECOCE e adequada (opioide se intensa) + hidratação + O2 se hipoxemia. Buscar desencadeante/infecção. 🚩 Síndrome torácica aguda, sequestro, AVC, priapismo, febre → internar.",
"Epistaxe":
 "Compressão + medidas locais (vasoconstrictor/cautério/tampão anterior). Controlar PA e revisar anticoagulação. 🚩 Posterior/refratária/repercussão → tampão posterior + ORL/internação.",
"Neutropenia Febril":
 "EMERGÊNCIA oncológica — ATB de amplo espectro na 1ª hora (após culturas), não atrasar. Estratificar (MASCC) para VO/ambulatorial vs internação. Evitar toque retal.",
"Transfusão de Hemoderivados":
 "Transfundir por indicação/meta (não só pelo número). Checar identificação/compatibilidade. 🚩 Reação (febre, dispneia, dor lombar, hipotensão, urticária) → PARAR e manejar.",
"Dor Crônica":
 "Abordagem multimodal (não-farmacológico + analgésico por mecanismo). Opioide com cautela/critério. 🚩 Bandeiras vermelhas (febre, emagrecimento, déficit, dor noturna/em repouso) → investigar.",
"Entorse do Tornozelo":
 "PRICE + analgesia + carga/mobilização precoce conforme dor. Aplicar critérios de Ottawa para decidir radiografia. Reabilitação previne recidiva.",
"Fasciíte Plantar":
 "Autolimitada — alongamento, palmilha/calçado, controle de peso, AINE curto. Melhora em semanas-meses. 🚩 Dor atípica/noturna/sistêmica → reavaliar.",
"Insuficiência Venosa Crônica":
 "Base = compressão elástica + elevação + atividade + cuidado com a pele. Venotônico adjuvante. 🚩 Úlcera (tratar) e sinais de TVP aguda / componente arterial (checar pulsos antes de comprimir).",
"Osteoartrite":
 "Não-farmacológico é a base (exercício, perda de peso) + analgésico/AINE (tópico preferível em idoso). 🚩 Sinais inflamatórios exuberantes/febre/derrame → afastar artrite séptica/cristal.",
"Atrofia Urogenital":
 "Estrogênio vaginal (baixa dose) ± hidratante/lubrificante. Checar contraindicações (história de câncer hormônio-dependente).",
"Bacteriúria Assintomática":
 "NÃO tratar de rotina (só GESTANTE ou pré-procedimento urológico invasivo). Evitar uso desnecessário de ATB.",
"Balanite":
 "Higiene + tópico conforme causa (candidiásica/irritativa/bacteriana). Rastrear DM se recorrente. 🚩 Úlcera → investigar IST.",
"Cancro Mole":
 "Úlcera dolorosa + bubão inguinal — ATB (azitromicina/ceftriaxona). Rastrear outras ISTs/HIV, tratar parceria. Notificar.",
"Candidíase":
 "Antifúngico tópico ou fluconazol VO (NÃO fluconazol em gestante). Recorrente → esquema de manutenção + investigar fator (DM, imunossupressão).",
"Cervicite":
 "Tratar empiricamente gonococo + clamídia (ceftriaxona + azitro/doxi), tratar parceria, rastrear ISTs. 🚩 Dor à mobilização do colo/dor pélvica → DIP.",
"Climatério Sintomas Vasomotores":
 "Medidas comportamentais; fitoterápico/não-hormonal ou terapia hormonal conforme perfil de risco (checar contraindicações). Avaliar saúde óssea/cardiovascular.",
"Gonorreia":
 "Ceftriaxona IM + cobertura de clamídia; tratar parceria, rastrear ISTs, notificar. 🚩 Doença gonocócica disseminada/DIP/artrite.",
"Herpes Genital":
 "Antiviral (mais eficaz se precoce); analgesia. Orientar transmissão/recorrência. Profilaxia supressiva se recorrências frequentes. Rastrear ISTs.",
"Incontinência Urinária":
 "Fisioterapia do assoalho pélvico + medidas comportamentais 1ª linha; anticolinérgico (urgência) conforme tipo. Afastar/ tratar ITU e causas reversíveis.",
"Linfogranuloma Venéreo":
 "Doxiciclina 21 dias; tratar parceria, rastrear ISTs, notificar. 🚩 Forma anorretal (proctite) em contexto de risco.",
"Mastite":
 "Manter esvaziamento/amamentação + analgesia + ATB (cobrir S. aureus). 🚩 Flutuação = abscesso (drenagem/USG). Corrigir pega/fissura.",
"Orquiepididimite":
 "ATB conforme faixa/risco (jovem: gonococo/clamídia; idoso: gram-negativo) + analgesia + suspensório. 🚩 EMERGÊNCIA: afastar TORÇÃO testicular (dor súbita, Prehn neg, cremastérico ausente) → USG/cirurgia.",
"Sangramento Uterino Anormal":
 "Estabilizar se agudo (antifibrinolítico/hormonal); βhCG sempre. Investigar causa (PALM-COEIN). 🚩 Instabilidade/anemia sintomática → PS.",
"Sífilis":
 "Penicilina benzatina (esquema conforme fase); tratar parceria, rastrear ISTs/HIV, notificar e acompanhar VDRL. Gestante: penicilina (dessensibilizar se alérgica).",
"Tricomoníase":
 "Metronidazol (evitar álcool) — IST: tratar parceria e rastrear outras ISTs. Associada a complicações na gestação.",
"Vaginose":
 "Metronidazol (VO ou vaginal); não é IST clássica mas tratar parceria não é rotina. Medidas de higiene. Associada a parto prematuro na gestante.",
"Dermatite de Contato":
 "Afastar o agente + corticoide tópico ± anti-histamínico para prurido. Corticoide oral se extensa. Identificar/evitar o desencadeante previne recidiva.",
"Dermatite Perioral":
 "SUSPENDER corticoide tópico facial (piora/perpetua) + tópico (metronidazol/clindamicina) ou tetraciclina VO nos casos moderados. Evitar cosméticos oclusivos.",
"Drenagem Abscesso":
 "Tratamento = INCISÃO E DRENAGEM. ATB só se celulite associada, sistêmico, imunossupressão ou localização de risco. Compressa quente, retorno para reavaliação.",
"Erisipela / Celulite":
 "ATB (cobrir estrepto/estafilo) + elevação + tratar PORTA DE ENTRADA (micose interdigital, ferida). 🚩 Sinais sistêmicos/rápida progressão/dor desproporcional (fasciíte) → internar/EV.",
"Furunculo / Carbunculo":
 "Compressa quente ± drenagem se flutuante; ATB (cobrir S. aureus) se carbúnculo, celulite, face ou sistêmico. Furunculose de repetição → descolonização.",
"Hidradenite Supurativa":
 "Crônica recidivante — medidas gerais (perda de peso, cessar tabagismo, higiene), tópico/ATB nas crises, encaminhar dermato (estadiar Hurley). Drenar abscesso doloroso.",
"Pediculose":
 "Pediculicida tópico (permetrina) + repetir em 7 dias + retirar lêndeas; tratar contactantes. Ivermectina VO se refratário.",
"Queimadura":
 "Resfriar (água corrente), analgesia, curativo. Estimar SCQ/profundidade. 🚩 Internar/referência: >10% SCQ 2º grau, face/mãos/pés/períneo, 3º grau, via aérea, elétrica, circunferencial.",
"Queimadura Elétrica":
 "Lesão interna >> externa. ECG/monitor (arritmia), hidratação + vigiar mioglobinúria/rabdomiólise e síndrome compartimental. Baixo limiar para internar/referência.",
"Tínea Capitis":
 "Exige antifúngico SISTÊMICO (tópico não cura) — griseofulvina/terbinafina. 🚩 Querion (placa inflamatória) → antifúngico oral ± corticoide, evitar cicatriz/alopecia definitiva.",
"Abstinência Alcoólica":
 "Benzodiazepínico guiado por gravidade (CIWA) + TIAMINA (antes da glicose) + hidratação. 🚩 Delirium tremens/convulsão → PS/UTI. Rastrear comorbidades.",
"Anemia (gestante)":
 "Suplementar ferro + ácido fólico; ajustar conforme Hb. Investigar se anemia importante/refratária. Impacto materno-fetal.",
"Ansiedade / Depressão (gestante)":
 "Preferir medidas não-farmacológicas; se medicar, escolher fármaco seguro na gestação (ex.: sertralina) com apoio especializado. 🚩 Ideação suicida → avaliação urgente.",
"Broncoespasmo / Crise asmática (gestante)":
 "Tratar a crise como na não-gestante (SABA + corticoide) — hipóxia materna é pior para o feto que a medicação. Manter SatO2 ≥95%. Avaliar necessidade de doppler (PNAR).",
"Candidíase (gestante)":
 "Tratamento TÓPICO (evitar fluconazol oral). Comum na gestação; tratar se sintomática.",
"Clamídia / Gonorreia (gestante)":
 "Tratar (ceftriaxona + azitromicina) — risco de transmissão perinatal (conjuntivite/pneumonia neonatal). Tratar parceria e rastrear ISTs.",
"Constipação (gestante)":
 "Fibras/hidratação + laxativo seguro (fibras, lactulose, PEG); evitar estimulantes contínuos. Comum pelo efeito da progesterona/ferro.",
"Diabetes (gestante)":
 "Controle glicêmico rígido (dieta + insulina se necessário; evitar a maioria dos orais). Seguimento pré-natal de alto risco. 🚩 Descompensação.",
"Diarreia (gestante)":
 "Hidratação é a base; sintomáticos seguros. Evitar medicações contraindicadas. 🚩 Desidratação, sangue/febre alta, TPP → avaliar.",
"Doença hemorroidária (gestante)":
 "Medidas locais + fibras/hidratação (constipação piora). Tópicos seguros. 🚩 Trombose muito dolorosa/sangramento importante.",
"Dor (gestante)":
 "Paracetamol é o analgésico de escolha. EVITAR AINE (sobretudo 3º trimestre — fechamento do ducto arterioso/oligoâmnio). Opioide só com critério.",
"Dor abdominal (gestante)":
 "🚩 Sempre afastar causas obstétricas (DPP, trabalho de parto prematuro, pré-eclâmpsia) e cirúrgicas (apendicite — apresentação atípica). βhCG/USG obstétrico. Baixo limiar para avaliar.",
"Epigastralgia (gestante)":
 "Antiácido/medidas posturais; comum por refluxo gestacional. 🚩 3º trim + HAS + dor em HD/epigástrio + cefaleia/escotomas → PRÉ-ECLÂMPSIA/HELLP — avaliar urgente.",
"Epilepsia (gestante)":
 "Manter a medicação de controle (NÃO suspender; evitar valproato) + reforçar ácido fólico. 🚩 Crise no periparto com HAS/proteinúria → ECLÂMPSIA (sulfato de magnésio) — emergência.",
"Hipertensão (gestante)":
 "Anti-hipertensivo seguro (metildopa/nifedipino/hidralazina). 🚩 Pré-eclâmpsia grave (PA≥160/110, cefaleia, escotomas, dor epigástrica, plaquetopenia) → sulfato de magnésio + PS obstétrico.",
"Pielonefrite (gestante)":
 "Sempre INTERNAR (risco de sepse e trabalho de parto prematuro) — ATB EV + hidratação + monitorização materno-fetal.",
"Pneumonia / Sinusite / Amigdalite (gestante)":
 "Tratar com ATB seguro na gestação (betalactâmico/macrolídeo). 🚩 Pneumonia com hipoxemia/gravidade → internar (gestante tolera menos a hipóxia).",
"Prurido (gestante)":
 "Anti-histamínico seguro + hidratante. 🚩 Prurido palmoplantar sem lesões no 3º trim → COLESTASE gravídica (dosar ácidos biliares/transaminases) — risco fetal, encaminhar.",
"Síndrome gripal (gestante)":
 "Gestante é GRUPO DE RISCO para influenza → baixo limiar para oseltamivir; sintomáticos seguros. 🚩 Dispneia/SatO2 baixa → SRAG, internar.",
"Tricomoníase (gestante)":
 "Metronidazol (evitar álcool); IST — tratar parceria. Associada a parto prematuro/RPMO.",
"Vaginose (gestante)":
 "Tratar (metronidazol) — associada a parto prematuro e RPMO. Rastrear/tratar se sintomática.",
}

# aplica
for _c in CONDITIONS:
    _t = _c.get("title")
    if _t in _EX2 and not _c.get("exame"):
        _c["exame"] = _EX2[_t]
    if _t in _DI2 and not _c.get("disclaimer"):
        _c["disclaimer"] = _DI2[_t]
