# Agentic 금융 서비스 UI — 컴포넌트 인터랙션 → 넛지·행동유도 → 광고 (합성)

> **비전**: 인터넷은행의 Agentic AI 서비스는 *순수 텍스트*가 아니라 **대화 안에 GUI 컴포넌트(버튼·카드·위젯)를 섞어 내고, 사용자가 그걸 눌러 서비스가 실행**되는 형태가 된다.
> 그 위에 **① 서비스 실행 → ② 넛지·행동유도 → ③ 광고/커머스**를 어떻게 얹을지, 그리고 **다크패턴 경계**를 어떻게 지킬지를 CHI 2026 · DIS 2026 논문으로 뒷받침한다.
> 논문별 전체 설명·링크·PDF: [CHI26.md](CHI26.md) · [DIS26.md](DIS26.md)

## 3-레이어 모델

```
┌─ ③ 광고 · 커머스 ───────────────────────── 다크패턴 경계 ─┐
│   추천/스폰서 컴포넌트를 대화에 삽입, 충동구매 vs 합리적 소비   │
├─ ② 넛지 · 행동유도 ───────────────────────────────────────┤
│   버튼/카드/피드백으로 의사결정을 좋은 방향으로 유도(설득 ↔ 반발) │
├─ ① 메커니즘: 에이전트가 GUI 컴포넌트를 생성/실행 ──────────────┤
│   "텍스트만" 대신 버튼·위젯 렌더 → 누르면 서비스 수행            │
└──────────────────────────────────────────────────────────┘
        ↑ 가로지르는 축: 사용자 행동 · 신뢰/과의존 · 설명/통제
핵심: ①을 잘 만들수록 ②③를 담을 표면이 생긴다. 단, ③로 갈수록 다크패턴 위험↑ → 통제·설명 장치 필수.
```

## ① 메커니즘 — 에이전트가 GUI 컴포넌트를 생성/실행 (버튼 인터랙션)

| 코드 | 논문 | 무엇을 주나 |
|---|---|---|
| `CHI16` | **DuetUI** — Human-Agent Co-Generation of Task-Oriented Interfaces | 사용자가 에이전트와 **함께 task UI를 생성**하고 중간에 개입·override. 우리 서비스의 "버튼 누르면 실행" 인터랙션의 직접 레퍼런스 ★ |
| `CHI18` | **Improving UI Generation Models from Designer Feedback** (Apple) | LLM이 만든 컴포넌트가 **잘 디자인되게** 하는 학습/피드백 루프 |
| `CHI19` | **Characterizing Unintended Consequences of GUI Agents** | GUI를 자동 조작하는 에이전트의 **실사용 이슈·완화** (실패 모드 사전 파악) |
| `CHI20` 🇰🇷 | **Voice Computer-Using Agent for Online Shopping** (연세대) | 에이전트가 **GUI를 직접 조작**해 거래 수행 — 접근성 + 실행형 인터랙션 |
| `CHI01` 🇰🇷 | **Bridging Gulfs in UI Generation** (서울대) | 프롬프트→UI 생성의 **실행/평가 격차**를 의미 가이드로 메움 |
| `CHI03` | **Fit Matters: Format–Distance Alignment** | 응답을 **텍스트/컴포넌트/미디어 중 무엇으로** 줄지 인지상태에 정렬 |
| `CHI05` | **Interaction Methods in Generative AI Tools (Review 37)** | 생성형 AI 인터랙션·인터페이스 **디자인 패턴 카탈로그** |
| `DIS01` | **Hybrid GUI-LLM Interface Paradigm** | GUI 직접조작 + LLM을 결합한 **하이브리드 인터페이스** 원형 ★ |
| `DIS02` | **When Systems Take Initiative (mixed-initiative)** | 시스템이 **주도권을 갖는** 적응형 질의 — 버튼/제안 자동 제시 |
| `DIS03` | **Fairy Cursor** | 챗창이 아니라 **흐름 속**에서 돕는 임베디드 에이전트 형태 |
| `DIS04` 🇰🇷 | **IntentFlow** (KAIST) | **의도 전달** 동역학 — 사용자 의도→결과(컴포넌트) 명세 워크플로 |

## ② 넛지 · 행동유도 (컴포넌트 위에 얹는 설득)

| 코드 | 논문 | 무엇을 주나 |
|---|---|---|
| `CHI10` | **The Bots of Persuasion** | CA의 **언어적 성격 표현**이 의사결정에 주는 영향 — 설득 톤 설계 |
| `CHI15` | **Dynamic Compensation (Financial Losses)** | **손실회피**를 자극하는 동적 보상 → 참여·책임감↑ (행동경제 넛지) |
| `CHI09` | **BuyMate (Live Commerce)** | 충동구매 유발 패턴 vs **합리적 소비로 유도하는 AI 개입** |
| `DIS13` 🇰🇷 | **MindStock** (KAIST) | 투자앱 인지편향을 **원칙기반 피드백**으로 자기성찰 유도 |
| `CHI06` | **Behavioral Indicators of Overreliance** | 넛지가 **과의존**으로 흐르는지 감지하는 행동지표 (역효과 감시) |

## ③ 광고 · 커머스 (+ 다크패턴 경계)

| 코드 | 논문 | 무엇을 주나 |
|---|---|---|
| `CHI02` | **Deception at Scale — 1K LLM-Generated E-Commerce Components** | LLM이 만든 **커머스 UI 컴포넌트의 다크패턴** 실태·요인·완화 — 광고/판매 컴포넌트 생성 시 직접 경고 ★ |
| `CHI17` | **Dark Patterns Meet GUI Agents** | **에이전트가 조작적 인터페이스에 취약** + 인간 감독 역할 — ①↔③ 브리지 ★ |
| `DIS09` | **Is it Dark? (Livestream E-commerce)** | 다크패턴을 사용자 **행동전략·해석**으로 재조명 |
| `DIS10` | **Revealed or Reinforced (Assistive Tech × Dark Patterns)** | 보조기술이 다크패턴 경험을 **드러내거나 강화** |
| `DIS11` | **Rushed by Discomfort (VR Privacy Deceptive Design)** | 몰입형 **프라이버시 다크패턴**에 대한 사용자 반응 |

## 가로지르는 축 — 사용자 행동 · 신뢰 · 설명/통제

| 코드 | 논문 | 축 |
|---|---|---|
| `CHI07` | Do People Appropriately Rely on AI-Advice? (Review) | AI 조언 **의존**의 적절성 |
| `CHI04` | Rethinking User Empowerment in AI Recommender | 추천의 **투명·통제** 인터페이스 |
| `CHI13` 🇰🇷 | Clarifying or Complicating? XAI in E-Commerce (서울대) | **AI 설명**이 구매 의사결정에 실제 도움이 되는가 |
| `CHI08` | Multimodal Conversational Search (Gemini Live류) | 통합 대화검색 **사용 행동** |

## 은행 AX팀 설계 함의 (요약)

| 설계 질문 | 근거 논문 | 적용 포인트 |
|---|---|---|
| 텍스트 vs 컴포넌트, 무엇으로 응답? | `CHI03` `CHI05` | 사용자 인지상태·과업에 따라 버튼/카드/텍스트 선택 |
| 버튼-액션 실행 인터랙션을 어떻게? | `CHI16` `DIS01` `DIS02` | 에이전트-사용자 공동생성 + mixed-initiative, 항상 override 가능 |
| 생성된 컴포넌트 품질 보장 | `CHI18` | 디자이너 피드백 루프로 컴포넌트 일관성 확보 |
| 넛지를 넣되 반발 최소화 | `CHI10` `CHI15` `DIS13` | 손실회피·원칙기반 피드백, 설득 톤 조절 |
| 광고/추천을 넣되 신뢰 유지 | `CHI02` `CHI17` `CHI09` `DIS09` | 다크패턴 회피, 스폰서 표시·통제권 제공 |
| 과의존·오작동 방지 | `CHI06` `CHI07` `CHI19` `CHI04` | 과의존 지표 모니터링 + 설명·통제·인간 감독 |

## 읽는 순서 추천
1. **`CHI16` DuetUI** → 우리가 만들 "컴포넌트 공동생성·버튼 실행" 인터랙션의 골격
2. **`DIS01` Hybrid GUI-LLM** → GUI+LLM 결합 패러다임
3. **`CHI02` Deception at Scale** + **`CHI17` Dark Patterns Meet GUI Agents** → ③ 광고/커머스 컴포넌트의 윤리 가드레일
4. **`CHI15` Dynamic Compensation** + **`DIS13` MindStock** → ② 금융 넛지 설계
5. **`CHI06`/`CHI07`/`CHI04`** → 신뢰·과의존·통제 안전장치
