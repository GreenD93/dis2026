# DIS 2026 · CHI 2026 논문 큐레이션

> 인터넷은행 AI개발자(AI Orchestration · AI Persona · AI Transformation) 관점에서, **DIS 2026 / CHI 2026** 채택 논문 중 통합형 채팅 인터페이스 · 액션칩 · UI 컴포넌트 · 넛지/광고 · 금융 사용자 행동에 관련된 논문을 골라 정리한 저장소.
>
> 데이터 출처: **SIGCHI 공식 프로그램** (`programs.sigchi.org/{dis,chi}/2026`) — 실제 채택 논문·세션·시간표. 더미 없음.

## 📁 문서 구성

| 파일 | 내용 |
|---|---|
| **[CHI26.md](CHI26.md)** | CHI 2026 관심 논문 **25편** · 5개 소주제 · 인용수·관련도 순위 |
| **[DIS26.md](DIS26.md)** | DIS 2026 참석 계획 · 17편 · 요일별 세션·장소·시간 · 🇰🇷 한국인 저자 이메일 |
| **[AGENTIC_UI_NUDGE_ADS.md](AGENTIC_UI_NUDGE_ADS.md)** | ⭐ 합성: 컴포넌트 인터랙션 → 넛지·행동유도 → 광고 **3-레이어 모델** + 은행 AX 설계 함의 |
| **[INDEX.md](INDEX.md)** | 두 학회 요약 · 소주제 매핑 · PDF 출처 메모 |
| `papers/CHI26/` · `papers/DIS26/` | 논문 PDF (로컬 전용, **git 비포함** — `.gitignore`) |
| `scripts/` | 생성 파이프라인(프로그램 크롤·인용수 조회·키워드 점수·PDF 다운로드) |

> ⚠️ **PDF는 저작권상 git 미포함**. 학회 프로그램 페이지·ACM DL·arXiv 링크를 통해 직접 받아 `papers/CHI26/` 또는 `papers/DIS26/` 아래 배치.

## 🎯 큐레이션 관점

**통합형 채팅 인터페이스(ChatGPT/Gemini/Claude류)** 가 단순 텍스트가 아니라 **GUI 컴포넌트(버튼·카드·액션칩)** 를 섞어 내고 사용자가 눌러 서비스를 실행하는 인터랙션 — 그 디자인·사용자 행동, 위에 얹는 넛지·광고, AI 페르소나 설계, 금융 의사결정.

| | DIS 2026 (Task1) | CHI 2026 (Task2) |
|---|---|---|
| 개최 | 🇸🇬 Singapore (NUS) · **6/13–17** (현재 진행) | 🇪🇸 Barcelona · **4/13–17** (완료) |
| 선정 | **17편** (4 소주제) + 한국인 저자 발표 별도 | **25편** (5 소주제) |
| PDF | 4/17 (arXiv) — 학회 후 ACM DL 보강 가능 | 25/25 확보 |

---

## 🟦 CHI 2026 — 25편 INDEX

> 📑 상세: [CHI26.md](CHI26.md) · 🔗 = ACM DOI · 🇰🇷 = 한국 기관 저자 · ★ 관련도(★★★ 비전 핵심 · ★★ 강함 · ★ 관련) · 인용 = Semantic Scholar 기준

### Ⅰ. Agentic UI 메커니즘 — 에이전트가 GUI 컴포넌트를 생성·실행 (8편)

| # | 코드 | 인용 | ★ | 논문 | 비고 |
|---|---|---|---|---|---|
| 1 | CHI18 | 4 | ★★ | [Improving User Interface Generation Models from Designer Feedback](https://doi.org/10.1145/3772318.3791567) | Apple — UI 생성 모델 |
| 2 | CHI04 | 2 | ★★ | [Rethinking User Empowerment in AI Recommender System](https://doi.org/10.1145/3772318.3791914) | in-chat 추천 투명·통제 |
| 3 | CHI16 | 1 | ★★★ | [DuetUI: Bidirectional Context Loop for Human-Agent Co-Generation of Task-Oriented Interfaces](https://doi.org/10.1145/3772318.3790441) | **메커니즘 ★** |
| 4 | CHI01 | 1 | ★★ | [Bridging Gulfs in UI Generation through Semantic Guidance](https://doi.org/10.1145/3772318.3791966) | 🇰🇷 SNU |
| 5 | CHI05 | 1 | ★★ | [Interaction Methods in Generative AI Image Tools](https://doi.org/10.1145/3772318.3790307) | 37개 도구 리뷰 |
| 6 | CHI03 | 1 | ★★ | [Fit Matters: Format–Distance Alignment for Conversational Search](https://doi.org/10.1145/3772318.3790317) | NUS · 리치 응답 설계 |
| 7 | CHI19 | 0 | ★ | [Characterizing Unintended Consequences of GUI Agents for Web Browsing](https://doi.org/10.1145/3772318.3790696) | Tsinghua · 실사용 이슈 |
| 8 | CHI20 | 0 | ★ | [Toward Independent Online Shopping of the Visually Impaired Through Voice-based CUA](https://doi.org/10.1145/3772318.3791681) | 🇰🇷 Yonsei |

### Ⅱ. AI 페르소나·정체성 설계 (5편)

| # | 코드 | 인용 | ★ | 논문 | 비고 |
|---|---|---|---|---|---|
| 1 | CHI21 | 7 | ★★★ | [Creating and Evaluating Personas Using Generative AI: Scoping Review of 81 Articles](https://doi.org/10.1145/3772318.3790608) | **페르소나 방법론 지도 ★** |
| 2 | CHI22 | 6 | ★★★ | [Vibe Check: LLM CA Personality & Alignment on User Perceptions in Goal-Oriented Tasks](https://doi.org/10.1145/3772318.3790388) | 성격 설계 ★ |
| 3 | CHI24 | 4 | ★★ | [AI-exhibited Personality Traits Shape Human Self-concept through Conversations](https://doi.org/10.1145/3772318.3790654) | 페르소나 윤리 리스크 |
| 4 | CHI25 | 1 | ★★ | [It Seems to Understand My Heart: Persona-Driven Persuasive AI Agent (Aging-in-Place, SG)](https://doi.org/10.1145/3772318.3791422) | Dual-Persona 설득 |
| 5 | CHI23 | 0 | ★ | [PCGEF: Diagnosing Subjective Alignment in Persona-Conditioned Generation](https://doi.org/10.1145/3772318.3791402) | Sony AI |

### Ⅲ. 넛지·설득·광고·커머스 (+ 다크패턴 경계) (5편)

| # | 코드 | 인용 | ★ | 논문 | 비고 |
|---|---|---|---|---|---|
| 1 | CHI17 | 9 | ★★★ | [Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces](https://doi.org/10.1145/3772318.3791568) | **메커니즘×다크패턴 ★** |
| 2 | CHI02 | 1 | ★★★ | [Deception at Scale: Deceptive Designs in 1K LLM-Generated E-Commerce Components](https://doi.org/10.1145/3772318.3791063) | UCSD · UI+광고 윤리 |
| 3 | CHI10 | 1 | ★★ | [The Bots of Persuasion: CA Linguistic Personality on User Decisions](https://doi.org/10.1145/3772318.3791407) | TU Delft |
| 4 | CHI09 | 0 | ★★ | [BuyMate: AI Interventions for Rational Consumption in Live Commerce](https://doi.org/10.1145/3772318.3790928) | Tsinghua · 충동구매 |
| 5 | CHI15 | 0 | ★★ | [Dynamic Compensation: Sensitivity to Financial Losses in Crowd-sourced Studies](https://doi.org/10.1145/3772318.3791660) | 손실회피 넛지 |

### Ⅳ. 금융 × AI 인터페이스 — 금융활동·의사결정 (4편)

| # | 코드 | 인용 | ★ | 논문 | 비고 |
|---|---|---|---|---|---|
| 1 | CHI13 | 0 | ★★ | [Clarifying or Complicating? Older Adults' Engagement with Real-World XAI in E-Commerce](https://doi.org/10.1145/3772318.3791908) | 🇰🇷 SNU · XAI |
| 2 | CHI14 | 0 | ★★ | [ScamPilot: LLM Conversations to Protect Against Online Scams](https://doi.org/10.1145/3772318.3791313) | 사기 예방접종 |
| 3 | CHI11 | 0 | ★★ | [Supporting Money Management among Adults with Down Syndrome](https://doi.org/10.1145/3772318.3791299) | 포용 금융 UX |
| 4 | CHI12 | 0 | ★★ | [Navigating Financial Lives: How Autistic Adults Adapt Financial Technologies](https://doi.org/10.1145/3772318.3791131) | 금융앱 접근성 |

### Ⅴ. 사용자 행동·신뢰·과의존 (3편)

| # | 코드 | 인용 | ★ | 논문 | 비고 |
|---|---|---|---|---|---|
| 1 | CHI07 | 6 | ★★★ | [Do People Appropriately Rely on AI-Advice? Analytical Review of HCI Research](https://doi.org/10.1145/3772318.3791467) | 의존 적절성 리뷰 |
| 2 | CHI06 | 2 | ★★ | [Behavioral Indicators of Overreliance During Interaction with Conversational LMs](https://doi.org/10.1145/3772318.3790332) | 과의존 행동지표 ★ |
| 3 | CHI08 | 0 | ★ | [Spatiotemporal-Aware Multimodal Conversational Search in Outdoor Urban Space](https://doi.org/10.1145/3772318.3790541) | 🇰🇷 Yonsei · Gemini Live류 |

---

## 🟩 DIS 2026 — 17편 INDEX

> 📑 상세: [DIS26.md](DIS26.md) · 🔗 = SIGCHI 프로그램 · 🇰🇷 = 한국 기관 저자 · 📄 = arXiv PDF 확보 · ⏳ = 학회 후 ACM DL

### Ⅰ. 통합 신규 인터페이스 · Orchestration · Agentic AI (5편)

| # | 코드 | 일시(SGT) · 장소 | 논문 | 비고 |
|---|---|---|---|---|
| 1 | DIS01 | 6/15(월) 11:00 · LT 50 | [A Hybrid GUI-LLM Interface Paradigm for 3D Scene Customisation](https://programs.sigchi.org/dis/2026/program/content/257037) | 하이브리드 LCS — 통합 인터페이스 원형 |
| 2 | DIS02 | 6/15(월) 16:10 · Aud. 1 | [When Systems Take Initiative: Adaptive Mixed-Initiative Database Querying](https://programs.sigchi.org/dis/2026/program/content/257198) | GUI↔자연어 전환 |
| 3 | DIS03 | 6/15(월) 16:10 · Aud. 1 | [Fairy Cursor: AI Agent for In-the-Flow Assistance](https://programs.sigchi.org/dis/2026/program/content/257119) | 커서 임베디드 에이전트 |
| 4 | DIS04 | 6/17(수) 09:00 · LT 52 | [IntentFlow: Fluid Dynamics of Intent Communication in Generative AI](https://programs.sigchi.org/dis/2026/program/content/257035) | 🇰🇷 KAIST Juho Kim · 📄 [arXiv](https://arxiv.org/abs/2507.22134) |
| 5 | DIS05 | 6/15(월) 16:10 · Aud. 1 | [Who Did What? Avatars for Explainable Multi-Agent Systems in Knowledge Work](https://programs.sigchi.org/dis/2026/program/content/257236) | Orchestration 신뢰 |

### Ⅱ. AI 페르소나 — 정체성 설계 + 합성 페르소나(고객 이해) (6편)

| # | 코드 | 일시(SGT) · 장소 | 논문 | 비고 |
|---|---|---|---|---|
| 1 | DIS16 | 6/17(수) 11:00 · LT 52 | [Designing Artificial Identity: Framework and Research Agenda](https://programs.sigchi.org/dis/2026/program/content/257056) | 🇰🇷 SNU·ETRI · **정통 레퍼런스 ★★** |
| 2 | DIS17 | 6/16(화) 11:00 · LT 51 | [Designing Character-Bound In-Public Companions: ACG Practices](https://programs.sigchi.org/dis/2026/program/content/257118) | 캐릭터 페르소나 |
| 3 | DIS12 | 6/16(화) 11:00 · LT 52 | [Understanding Down Syndrome Stereotypes in LLM-Based Personas](https://programs.sigchi.org/dis/2026/program/content/257253) | Persona-L · 📄 [arXiv](https://arxiv.org/abs/2512.02275) ★ |
| 4 | DIS13 | 6/15(월) 11:00 · LT 51 | [StreetDesignAI: Multi-Persona Evaluation of Cycling Infrastructure](https://programs.sigchi.org/dis/2026/program/content/257240) | 다중 페르소나 |
| 5 | DIS14 | 6/15(월) 11:00 · LT 51 | [PrivacyMotiv: Vulnerability-Centered Persona Journeys for Privacy UX](https://programs.sigchi.org/dis/2026/program/content/257081) | 취약성 중심 ★ |
| 6 | DIS15 | 6/16(화) 11:00 · LT 52 | [ConSearcher: Conversational Information Seeking with Member Personas](https://programs.sigchi.org/dis/2026/program/content/257070) | 📄 [arXiv](https://arxiv.org/abs/2603.19747) |

### Ⅲ. Agentic AI 금융 서비스에서의 고객 행동 (3편)

| # | 코드 | 일시(SGT) · 장소 | 논문 | 비고 |
|---|---|---|---|---|
| 1 | DIS06 | 6/16(화) 16:10 · Aud. 1 | [MindStock: Principle-Anchored Feedback for Self-Reflection in Mobile Investment](https://programs.sigchi.org/dis/2026/program/content/257127) | 🇰🇷 KAIST/UNIST · **금융 의사결정 ★** |
| 2 | DIS07 | 6/16(화) 16:10 · Aud. 1 | [Who Gets Left Out of Digital Banking in Later Life? HK Silver Population](https://programs.sigchi.org/dis/2026/program/content/257161) | 디지털뱅킹 포용 ★ |
| 3 | DIS08 | 6/15(월) 16:10 · LT 52 | [Bonik Somiti: Social-Market Tool for Informal E-Market (Bangladesh)](https://programs.sigchi.org/dis/2026/program/content/257147) | 📄 [arXiv](https://arxiv.org/abs/2602.12650) |

### Ⅳ. 인터페이스 디자인으로 사기·기만(deception/fraud) 방어 (3편)

| # | 코드 | 일시(SGT) · 장소 | 논문 | 비고 |
|---|---|---|---|---|
| 1 | DIS09 | 6/17(수) 09:00 · Aud. 2 | [Is it Dark? Dark Pattern Influence in Livestream E-commerce](https://programs.sigchi.org/dis/2026/program/content/257068) | 행동전략·해석 ★ |
| 2 | DIS10 | 6/17(수) 11:00 · LT 50 | [Revealed or Reinforced: Assistive Tech & Dark Patterns for Blind/LV Users](https://programs.sigchi.org/dis/2026/program/content/257053) | 접근성×기만 |
| 3 | DIS11 | 6/15(월) 11:00 · LT 52 | [Rushed by Discomfort, Trapped by Immersion: VR Privacy Deceptive Design](https://programs.sigchi.org/dis/2026/program/content/257114) | VR/AR 다크패턴 |

---

## 📥 PDF 다운로드 가이드

저작권상 PDF는 git에 포함하지 않습니다. 각자 받아 `papers/CHI26/CHI{nn}_*.pdf`, `papers/DIS26/DIS{nn}_*.pdf` 형식으로 배치하면 [CHI26.md](CHI26.md) · [DIS26.md](DIS26.md) 의 `📄 papers/...` 참조가 해석됩니다.

- **ACM DL** (DOI 링크 — 브라우저에서 열람): 위 표의 [DOI](https://doi.org/) 링크
- **arXiv 프리프린트**: 위 표에 📄 [arXiv] 표시된 항목
- **SIGCHI 프로그램** (논문 메타·DOI·세션): [`programs.sigchi.org/chi/2026`](https://programs.sigchi.org/chi/2026) · [`programs.sigchi.org/dis/2026`](https://programs.sigchi.org/dis/2026)
- **자동 다운로드 스크립트**: `scripts/download_pdfs.py` (일부 ACM 링크는 Cloudflare 봇 차단 → 브라우저 수동 받기 권장)
