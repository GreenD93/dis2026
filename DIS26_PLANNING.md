# DIS 2026 참석 계획 (DIS26_PLANNING)

> **ACM Designing Interactive Systems Conference 2026** · Singapore (NUS) · **2026-06-13~17** · 시간=현지(SGT)
> 출처: https://programs.sigchi.org/dis/2026

## 0. 이 정리의 관점 — 인터넷은행 AX팀

> 통합 신규 인터페이스(Orchestration)·Agentic AI를 만드는 입장에서, **(Ⅰ) 통합/에이전트 인터페이스 · (Ⅱ) AI 페르소나(정체성 설계 + 합성 페르소나) · (Ⅲ) Agentic 금융서비스 고객 행동 · (Ⅳ) 인터페이스로 사기·기만 방어** 4갈래(연관성 기준 병합)로 DIS 논문을 정리한다.
> 표기: 🇰🇷 한국 기관 저자 · 📄 PDF 확보(`DIS26/`) · 🔗 공식 프로그램(논문집은 학회 후 ACM DL 공개)

## 1. 학회 일정 골격

| 날짜 | 내용 |
|---|---|
| 6/13(토)–14(일) | 워크숍 · Doctoral Consortium · (14일 18:00 Welcome Reception) |
| **6/15(월)** | 본 학회 1일차 — 세션 09:30·11:00·14:00·16:10 |
| **6/16(화)** | 본 학회 2일차 — 세션 09:00·11:00·14:00·16:10 |
| **6/17(수)** | 본 학회 3일차 — 세션 09:00·11:00·14:00 · Closing Keynote |

> 휴식: 커피 10:30–11:00 / 점심 12:30–14:00 / 커피 15:30–16:10

## 2. 소주제별 추천 논문 (17편 · 연관성 기준 4섹션)

### Ⅰ. 통합 신규 인터페이스 · Orchestration · Agentic AI
*ChatGPT/Gemini류 통합 인터페이스가 텍스트를 넘어 GUI·에이전트·의도를 다루는 형태*

#### DIS01 · A Hybrid GUI-LLM Interface Paradigm for 3D Scene Customisation
- 🕘 **6/15(월) 11:00–12:30** · 📍 LT 50 (Stephen Riady Centre Lv1) · 세션 *AI-Augmented Creative Interfaces* (Papers)
- 👤 Isaac Valadez (Vrije Universiteit Brussel); Irving Avina (Mad Monkeys) 외 1인
- 💡 GUI 직접조작 + LLM 프롬프트를 결합한 **하이브리드 인터페이스(LCS)** — 비전문가용 3D 씬 편집. ★통합 신규 인터페이스 원형.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257037) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS02 · When Systems Take Initiative: A Design Framework for Adaptive, Mixed-initiative Database Querying
- 🕘 **6/15(월) 16:10–17:40** · 📍 Auditorium 1 (Town Plaza Lv1) · 세션 *Agency and Explanation in AI Systems* (Papers)
- 👤 Longfei Chen (ShanghaiTech University); Shenghan Gao (ShanghaiTech University) 외 5인
- 💡 시스템이 주도권을 갖는 **적응형 mixed-initiative 질의** — Orchestration이 사용자 의도를 보조(GUI↔자연어 전환).
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257198) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS03 · Exploring Fairy Cursor as a Form of AI Agent for In-the-Flow Assistance: Design Opportunities and Challenges
- 🕘 **6/15(월) 16:10–17:40** · 📍 Auditorium 1 (Town Plaza Lv1) · 세션 *Agency and Explanation in AI Systems* (Papers)
- 👤 Yining Cao (University of California, San Diego); James Hollan (UC San Diego) 외 1인
- 💡 챗창이 아니라 **커서에 붙어** 흐름 속에서 돕는 임베디드 에이전트 — 통합 서비스 안의 에이전트 형태.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257119) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS04 · 🇰🇷 📄 IntentFlow: Investigating Fluid Dynamics of Intent Communication in Generative AI
- 🕘 **6/17(수) 09:00–10:30** · 📍 LT 52 (Stephen Riady Centre Lv2) · 세션 *Robots, LLMs, and Intent* (Papers)
- 👤 Yoonsu Kim (KAIST); Kihoon Son (KAIST) 외 3인
- 💡 생성형 AI의 **의도 전달(intent communication) 동역학** — 의도→결과 명세 워크플로. (KAIST, Juho Kim 랩)
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257035) · [arXiv](https://arxiv.org/abs/2507.22134) · 📄 `DIS26/DIS04_*.pdf`

#### DIS05 · Who Did What? Designing Avatars for Explainable Multi-Agent Systems in Knowledge Work
- 🕘 **6/15(월) 16:10–17:40** · 📍 Auditorium 1 (Town Plaza Lv1) · 세션 *Agency and Explanation in AI Systems* (Papers)
- 👤 Simon Rapp (WIN); Martin Feick (Karlsruhe Institute of Technology (KIT)) 외 2인
- 💡 멀티에이전트 결과를 **아바타로 설명·투명화** — '누가 무엇을 했나' 가시화로 Orchestration 신뢰 확보.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257236) · ⏳ 논문집 미공개(학회 후 ACM DL)

### Ⅱ. AI 페르소나 — 정체성 설계 + 합성 페르소나(고객 이해)
*에이전트 정체성·캐릭터를 설계하고, 실사용자 없이 LLM 페르소나로 고객을 모사·평가*

#### DIS16 · 🇰🇷 Designing Artificial Identity: The Identity Design Framework and Research Agenda
- 🕘 **6/17(수) 11:00–12:30** · 📍 LT 52 (Stephen Riady Centre Lv2) · 세션 *Robots in Social and Professional Roles* (Papers)
- 👤 Karla Bransky (The Australian National University); Penny Sweetser (The Australian National University) 외 13인
- 💡 **AI/에이전트 정체성(Artificial Identity) 설계 프레임워크**와 연구 어젠다 — 페르소나·정체성 설계의 정통 레퍼런스. ★★ (SNU·ETRI)
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257056) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS17 · Designing Character-Bound In-Public Companions: Interactional Insights from ACG Practices
- 🕘 **6/16(화) 11:00–12:30** · 📍 LT 51 (Stephen Riady Centre Lv1) · 세션 *Social XR and Virtual Companionship* (Papers)
- 👤 Yijie Guo (Tsinghua University); Ruhan Wang (Tsinghua University) 외 9인
- 💡 ACG(애니·만화·게임) 실천에서 길어낸 **캐릭터-바운드 공개 동반자**의 인터랙션 인사이트 — 캐릭터 페르소나 설계.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257118) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS12 · 📄 Understanding Down Syndrome Stereotypes in LLM-Based Personas
- 🕘 **6/16(화) 11:00–12:30** · 📍 LT 52 (Stephen Riady Centre Lv2) · 세션 *LLMs for Learning and Neurodiversity* (Papers)
- 👤 Chantelle Wu (Northeastern University); Mengxu Pan (Northeastern University) 외 8인
- 💡 **LLM+RAG로 사용자 페르소나 모델링**(Persona-L) + 고정관념 리스크 — 합성 페르소나로 고객 이해(주의점). ★
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257253) · [arXiv](https://arxiv.org/abs/2512.02275) · 📄 `DIS26/DIS12_*.pdf`

#### DIS13 · StreetDesignAI: Broadening Designer Perspectives Through Multi-Persona Evaluation of Cycling Infrastructure
- 🕘 **6/15(월) 11:00–12:30** · 📍 LT 51 (Stephen Riady Centre Lv1) · 세션 *Designing AI Concepts and Values* (Papers)
- 👤 Ziyi Wang (University of Maryland, College Park); Yilong Dai (the University of Alabama) 외 6인
- 💡 **다중 페르소나**로 디자이너 관점 확장(자전거 인프라 평가) — 현장조사 없이 다관점 고객 시뮬레이션.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257240) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS14 · PrivacyMotiv: Vulnerability-Centered Persona Journeys for Empathic Privacy Reviews in UX Design
- 🕘 **6/15(월) 11:00–12:30** · 📍 LT 51 (Stephen Riady Centre Lv1) · 세션 *Designing AI Concepts and Values* (Papers)
- 👤 Zeya Chen (Northeastern Univeristy); Jianing Wen (Northeastern University) 외 3인
- 💡 **취약성 중심 페르소나 저니**로 공감적 프라이버시 리뷰 — 현장조사 없이 사용자 입장을 대리 체험. ★
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257081) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS15 · 📄 ConSearcher: Supporting Conversational Information Seeking in Online Communities with Member Personas
- 🕘 **6/16(화) 11:00–12:30** · 📍 LT 52 (Stephen Riady Centre Lv2) · 세션 *LLMs for Learning and Neurodiversity* (Papers)
- 👤 Shiwei Wu (Sun Yat-sen University); Xinyue Chen (Sun Yat-sen University) 외 6인
- 💡 온라인 커뮤니티 **멤버 페르소나**로 대화형 정보탐색 — 실제 사용자 군집을 페르소나로 모사.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257070) · [arXiv](https://arxiv.org/abs/2603.19747) · 📄 `DIS26/DIS15_*.pdf`

### Ⅲ. Agentic AI 금융 서비스에서의 고객 행동
*투자·뱅킹·거래에서 사용자가 실제로 어떻게 의사결정/행동하는가*

#### DIS06 · 🇰🇷 MindStock: Investigating How Principle-Anchored Feedback Supports Self-Reflection in Mobile Investment
- 🕘 **6/16(화) 16:10–17:40** · 📍 Auditorium 1 (Town Plaza Lv1) · 세션 *Aging, Culture, and Domestic Technology* (Papers)
- 👤 Sooyohn Nam (KAIST); Yeohyun Jung (KAIST) 외 3인
- 💡 모바일 투자앱 인지편향을 **원칙기반 피드백**으로 자기성찰 유도 — **금융 의사결정 행동변화**. ★ (KAIST/UNIST)
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257127) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS07 · Who Gets Left Out of Digital Banking in Later Life? Barriers and Opportunitiesin Hong Kong's Silver Population
- 🕘 **6/16(화) 16:10–17:40** · 📍 Auditorium 1 (Town Plaza Lv1) · 세션 *Aging, Culture, and Domestic Technology* (Papers)
- 👤 Clarence Cheung (Hong Kong University of Science and Technology); Jianan Liu (Hong Kong Polytechnic University) 외 6인
- 💡 고령층의 **디지털뱅킹 사용 장벽·기회**(홍콩) — Agentic 금융서비스가 놓치는 고객층의 실제 행동/포용. ★
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257161) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS08 · 📄 Bonik Somiti: A Social-market Tool for Safe, Accountable, and Harmonious Informal E-Market Ecosystem in Bangladesh
- 🕘 **6/15(월) 16:10–17:40** · 📍 LT 52 (Stephen Riady Centre Lv2) · 세션 *AI, Civic Participation, and Journalism* (Papers)
- 👤 A.T.M Mizanur Rahman (University of Illinois Urbana-Champaign); Sharifa Sultana (University of Illinois Urbana-Champaign)
- 💡 비공식 전자상거래 생태계를 위한 **안전·책임 소셜마켓 도구** — 신뢰 기반 금융거래 행동 설계.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257147) · [arXiv](https://arxiv.org/abs/2602.12650) · 📄 `DIS26/DIS08_*.pdf`

### Ⅳ. 인터페이스 디자인으로 사기·기만(deception/fraud) 방어
*다크패턴·기만을 사용자가 어떻게 겪고, 인터페이스로 어떻게 막을까*

#### DIS09 · Is it Dark? Understanding Dark Pattern Influence through User Behavioral Strategies and Interpretations in Livestream E-commerce
- 🕘 **6/17(수) 09:00–10:30** · 📍 Auditorium 2 (Stephen Riady Centre Lv1) · 세션 *Power, Privacy, and Participation* (Papers)
- 👤 Yue Qin (The Hong Kong University of Science and Technology (Guangzhou)); Tengjia Zuo (The Hong Kong University of Science and Technology (Guangzhou)) 외 1인
- 💡 라이브커머스 **다크패턴**을 사용자 **행동전략·해석**으로 재조명 — 기만 인지/방어 인터페이스. ★
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257068) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS10 · Revealed or Reinforced: How Assistive Technologies Shape the Experience with Dark Patterns for Blind and Low-Vision Users
- 🕘 **6/17(수) 11:00–12:30** · 📍 LT 50 (Stephen Riady Centre Lv1) · 세션 *Accessibility Across Vision and Print* (Papers)
- 👤 Agata Stanczyk (Ruhr University Bochum); Mindy Tran (Max Planck Institute for Security and Privacy) 외 3인
- 💡 **보조기술(스크린리더 등)**이 다크패턴 경험을 드러내거나 오히려 강화 — 접근성 × 기만 방어.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257053) · ⏳ 논문집 미공개(학회 후 ACM DL)

#### DIS11 · Rushed by Discomfort, Trapped by Immersion: Users’ Experiences and Responses to Privacy Deceptive Design in Commercial VR Applications 
- 🕘 **6/15(월) 11:00–12:30** · 📍 LT 52 (Stephen Riady Centre Lv2) · 세션 *Intimate Data, Consent, and Harm* (Papers)
- 👤 Hilda Hadan (University of Waterloo); Michaela Valiquette (Carleton University ) 외 2인
- 💡 **몰입형(VR/AR) 프라이버시 다크패턴**에 대한 사용자 경험·대응 — 기만 설계에 맞선 인터페이스 디자인.
- 🔗 [프로그램](https://programs.sigchi.org/dis/2026/program/content/257114) · ⏳ 논문집 미공개(학회 후 ACM DL)

## 3. 날짜별 동선 (시간 충돌 확인용)

| 시간(SGT) | 코드 | 논문 | 장소 |
|---|---|---|---|
| 6/15(월) 11:00–12:30 | DIS01 | A Hybrid GUI-LLM Interface Paradigm for 3D Scene C | LT 50 (Stephen Riady Centre Lv1) |
| 6/15(월) 11:00–12:30 | DIS11 | Rushed by Discomfort, Trapped by Immersion: Users’ | LT 52 (Stephen Riady Centre Lv2) |
| 6/15(월) 11:00–12:30 | DIS13 | StreetDesignAI: Broadening Designer Perspectives T | LT 51 (Stephen Riady Centre Lv1) |
| 6/15(월) 11:00–12:30 | DIS14 | PrivacyMotiv: Vulnerability-Centered Persona Journ | LT 51 (Stephen Riady Centre Lv1) |
| 6/15(월) 16:10–17:40 | DIS02 | When Systems Take Initiative: A Design Framework f | Auditorium 1 (Town Plaza Lv1) |
| 6/15(월) 16:10–17:40 | DIS03 | Exploring Fairy Cursor as a Form of AI Agent for I | Auditorium 1 (Town Plaza Lv1) |
| 6/15(월) 16:10–17:40 | DIS05 | Who Did What? Designing Avatars for Explainable Mu | Auditorium 1 (Town Plaza Lv1) |
| 6/15(월) 16:10–17:40 | DIS08 | Bonik Somiti: A Social-market Tool for Safe, Accou | LT 52 (Stephen Riady Centre Lv2) |
| 6/16(화) 11:00–12:30 | DIS12 | Understanding Down Syndrome Stereotypes in LLM-Bas | LT 52 (Stephen Riady Centre Lv2) |
| 6/16(화) 11:00–12:30 | DIS15 | ConSearcher: Supporting Conversational Information | LT 52 (Stephen Riady Centre Lv2) |
| 6/16(화) 11:00–12:30 | DIS17 | Designing Character-Bound In-Public Companions: In | LT 51 (Stephen Riady Centre Lv1) |
| 6/16(화) 16:10–17:40 | DIS06 | MindStock: Investigating How Principle-Anchored Fe | Auditorium 1 (Town Plaza Lv1) |
| 6/16(화) 16:10–17:40 | DIS07 | Who Gets Left Out of Digital Banking in Later Life | Auditorium 1 (Town Plaza Lv1) |
| 6/17(수) 09:00–10:30 | DIS04 | IntentFlow: Investigating Fluid Dynamics of Intent | LT 52 (Stephen Riady Centre Lv2) |
| 6/17(수) 09:00–10:30 | DIS09 | Is it Dark? Understanding Dark Pattern Influence t | Auditorium 2 (Stephen Riady Centre Lv1) |
| 6/17(수) 11:00–12:30 | DIS10 | Revealed or Reinforced: How Assistive Technologies | LT 50 (Stephen Riady Centre Lv1) |
| 6/17(수) 11:00–12:30 | DIS16 | Designing Artificial Identity: The Identity Design | LT 52 (Stephen Riady Centre Lv2) |

## 4. 🇰🇷 한국 기관 / 한국인 저자 참여 (별도)

> "한국대학교(고려대)" 단독 발표는 없음. 추천 17편 중 한국 소속 + 그 외 주요 한국 발표.

| 시간(SGT) | 논문 | 한국 소속 | 세션 |
|---|---|---|---|
| 6/17(수) 11:00 | **DIS16** Designing Artificial Identity: The Identity  | Seoul National University | Robots in Social and Professional Roles |
| 6/16(화) 16:10 | **DIS06** MindStock: Investigating How Principle-Ancho | KAIST | Aging, Culture, and Domestic Technology |
| 6/17(수) 09:00 | **DIS04** IntentFlow: Investigating Fluid Dynamics of  | KAIST | Robots, LLMs, and Intent |
| 월 18:30 | Comforting an Emotion-Mirroring Robot (PWiP) | Hongik Univ. | Provocations & WiP |
| 월 18:30 | Transparent AI-Mediated Language Support (PWiP) | Seoul National Univ. | Provocations & WiP |
| 화 09:00 | Co-designing Haptics for Deaf/HoH Music Education | KAIST · ETRI | Haptics and Sensory Interaction |
| 화 09:00 | Augmentiary: LLM Interpretive Feedback for Journaling | UNIST | AI in Education and Reflection |
| 화 11:00 | ComiXR: Comic Layouts in XR | KAIST | Social XR and Virtual Companionship |
| 화 14:00 | Value-Sensitive AI for Prayer | Yonsei (공저) | AI Support for Reflection and Writing |
| 화 14:00 | Group Conversational Agents: A Review | NAVER AI Lab (공저) | Conversational Agents in Everyday Life |
| 화 16:10 | When XR Comes Home | Sogang Univ. | Aging, Culture, and Domestic Technology |
| 수 11:00 | Designing Artificial Identity (framework) | ETRI (공저) | Robots in Social & Professional Roles |
| 수 14:00 | Who Sets the Norm? ADHD Relationships | KAIST | Algorithmic Intimacy and Identity |
| 수 14:00 | Is This the Real Me? Algorithmic Self-Portraits | UNIST | Algorithmic Intimacy and Identity |
| 일 09:00 | (워크숍) AI, Sensemaking & Decision-Making in Crisis | SeoulTech | WS15 |

🔗 굵은 `DISxx`는 추천 17편 포함.

## 5. PDF 안내

DIS 2026 논문집은 학회 개최(6/13–17)에 맞춰 ACM DL 공개. 현재는 **arXiv 프리프린트가 있는 4편**(DIS04·08·12·15)만 `DIS26/`에 확보 — 나머지는 개최 후 보강 가능.
