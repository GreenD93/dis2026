import json,datetime,glob,os
F=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'final.json')))
import os as _os; BASE=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
def has_pdf(folder,code):
    return bool(glob.glob(f"{BASE}/{folder}/{code}_*.pdf"))
def plink(conf,i): return f"https://programs.sigchi.org/{conf}/2026/program/content/{i}"
WD={0:'월',1:'화',2:'수',3:'목',4:'금',5:'토',6:'일'}
def when(r):
    if not r['start']: return 'TBD'
    s=datetime.datetime.fromisoformat(r['start']); e=datetime.datetime.fromisoformat(r['end'])
    return f"{s.month}/{s.day}({WD[s.weekday()]}) {s.strftime('%H:%M')}–{e.strftime('%H:%M')}"
def leads(r,n=2):
    a=r['authors']; s="; ".join(f"{x['n']} ({x['i']})" for x in a[:n])
    return s+(f" 외 {len(a)-n}인" if len(a)>n else "")

DESC={
'DIS01':"GUI 직접조작 + LLM 프롬프트를 결합한 **하이브리드 인터페이스(LCS)**로 비전문가의 3D 씬 커스터마이징 지원. ★통합 인터페이스의 핵심 형태.",
'DIS02':"비전문가 DB 탐색용 **적응형 mixed-initiative 질의** 프레임워크 — 시스템이 주도권을 갖는 GUI↔자연어 전환.",
'DIS03':"챗창이 아니라 **커서에 붙어** 흐름 속에서 돕는 in-the-flow 에이전트 — '단순 텍스트 챗' 너머의 표면 형태 탐구.",
'DIS04':"생성형 AI의 **의도 전달(intent communication) 동역학** 분석 — 의도기반 결과 명세 워크플로. (KAIST, Juho Kim 랩)",
'DIS05':"추상화 수준을 넘나드는 **의미 기반 제어 생성형 인터페이스**(파티클 VFX 편집).",
'DIS06':"데스크톱 시각화를 모바일로 **다단계 지능형 적응(shapeshifting)** — 디바이스 간 UI 자동 적응.",
'DIS07':"온라인 커뮤니티 정보탐색을 LLM **대화형 검색 + 멤버 페르소나**로 강화.",
'DIS08':"의도 기반 **이미지 추천**으로 보조 의사소통 지원 — in-context 추천 인터페이스(반복적 사용자 연구).",
'DIS09':"AI 컴패니언 관계 **종료의 심리적 안전 설계** — 관계/사용자 행동.",
'DIS10':"그룹 상호작용을 매개·형성하는 **대화 에이전트 53편 체계적 리뷰** + 디자인 공간. (NAVER AI Lab 공저)",
'DIS11':"고인 데이터로 학습된 '생성형 유령'과의 대화 설계(3인칭 표현 vs 1인칭 환생)와 사용자 engagement.",
'DIS12':"**[다크패턴/광고]** 라이브커머스 다크패턴을 사용자 **행동전략·해석**으로 재조명 — 설득 표면 + 행동.",
'DIS13':"**[금융 직결]** 모바일 투자앱 인지편향을 **원칙기반 피드백**으로 자기성찰 유도 — 금융 의사결정 행동변화. (KAIST/UNIST)",
'DIS14':"멀티에이전트 결과를 **아바타로 설명·투명화** — 에이전트 행동 가시화/신뢰(통합 인터페이스의 투명성).",
'DIS15':"자율주행차 내 **고령자용 대화형 AI 에이전트** 요구사항(2단계 형성연구).",
'CHI01':"**[생성형 UI]** 프롬프트로 **UI를 생성**할 때의 실행·평가 격차를 *의미 기반 가이드*로 해소. (서울대 🇰🇷)",
'CHI02':"**[칩/UI+광고 윤리]** LLM이 생성한 **1,000개 커머스 UI 컴포넌트의 다크패턴** 실태·요인·완화책. ★",
'CHI03':"**[리치 응답 설계]** 대화형 검색 **응답 포맷(granularity·미디어)**을 사용자 인지상태에 정렬. (NUS)",
'CHI04':"**[in-chat 추천]** 추천 블랙박스의 정보·권력 비대칭을 **투명·통제 가능 인터페이스**로 완화.",
'CHI05':"**[디자인 레퍼런스]** 생성형 AI 도구 37개의 **인터랙션 방법·인터페이스** 트렌드·디자인 기회 리뷰.",
'CHI06':"**[사용자 행동]** 대화형 LLM 사용 중 **과의존을 드러내는 행동지표**를 측정·식별. ★",
'CHI07':"**[사용자 행동 리뷰]** 인간-AI 의사결정에서 **AI 조언 의존**의 적절성에 대한 HCI 연구 분석 리뷰.",
'CHI08':"**[통합 대화검색 행동]** Gemini Live류 **멀티모달 대화 검색**을 도시 이동 중 어떻게 쓰는지 사용행동.",
'CHI09':"**[커머스+소비행동]** 라이브커머스의 알고리즘 추천·시간제한 프로모션이 충동구매 유발 → **합리적 소비 개입** UX.",
'CHI10':"**[설득/광고 표현]** CA의 **언어적 성격 표현**이 사용자 의사결정·인식에 미치는 영향.",
'CHI11':"**[금융 의사결정 지원]** 다운증후군 성인의 **금융 자립·의사결정**을 멀티-테크놀로지 프로브로 지원 — 포용 금융 UX.",
'CHI12':"**[금융앱 적응/접근성]** 자폐 성인이 **금융기술·도구·전략을 어떻게 적응**시키는지 — 인터넷은행 앱 포용 디자인.",
'CHI13':"**[AI 설명 × 의사결정]** 실제 **이커머스의 XAI(AI 설명)**에 대한 고령자 engagement — 설명이 구매/금융 의사결정에 실제로 도움이 되는가. (서울대 🇰🇷)",
'CHI14':"**[대화형 AI × 금융방어]** LLM **대화 인터페이스**로 온라인 사기에 '예방접종'(inoculation).",
'CHI15':"**[금융 행동경제 넛지]** **손실 민감도(손실회피)**를 자극하는 동적 보상이 참여·책임감을 높임.",
'CHI16':"**[메커니즘 ★]** 인간·에이전트가 **task-oriented 인터페이스를 함께 생성**(양방향 컨텍스트 루프) — 사용자가 GUI를 잡고 흐름을 바꾼다.",
'CHI17':"**[메커니즘×다크패턴 ★]** **GUI 에이전트가 조작적 인터페이스(다크패턴)에 얼마나 취약**한지 + 인간 감독의 역할 — ①↔③ 브리지.",
'CHI18':"**[생성형 UI 품질]** 디자이너 피드백으로 **UI 생성 모델 개선**(Apple) — 컴포넌트가 '잘 디자인'되게 하는 법.",
'CHI19':"**[GUI 에이전트 사용자행동]** 웹 브라우징 GUI 에이전트의 **실사용 이슈·영향·완화**를 사용자 보고 기반으로 특성화.",
'CHI20':"**[에이전트가 GUI 조작]** 음성 기반 **Computer-Using Agent**가 GUI를 직접 조작해 시각장애인 온라인 쇼핑 지원. (연세대 🇰🇷)",
'CHI21':"**[페르소나 생성 방법 ★]** GenAI로 페르소나를 만들고 평가한 **81편 스코핑 리뷰** — 페르소나 설계 방법론 지도.",
'CHI22':"**[성격 설계 ★]** LLM 대화 에이전트의 **성격 표현·정합**이 사용자 **신뢰/의존**에 주는 영향(목표지향 과업).",
'CHI23':"**[페르소나 정합 진단]** persona-conditioned 생성의 **주관적 정합**을 진단하는 프레임워크(PCGEF, Sony AI).",
'CHI24':"**[성격→자기개념]** AI 성격 특성이 대화로 **사용자 자기개념**을 바꿀 수 있다 — 페르소나 설계의 윤리 리스크.",
'CHI25':"**[페르소나 설득]** Dual-Persona 기반 **문화·성격 맞춤 설득 에이전트**(고령 돌봄·aging-in-place).",
}

# ---------------- DIS26_PLANNING.md ----------------
o=[]
o.append("# DIS 2026 참석 계획 (DIS26_PLANNING)\n")
o.append("> **ACM Designing Interactive Systems Conference 2026** · Singapore, National University of Singapore (NUS)")
o.append("> 일정: **2026-06-13(토) ~ 06-17(수)** · 시간은 모두 **현지 시각(SGT, UTC+8)**")
o.append("> 테마: *Beyond Interaction* · 현장 참석 전용 · 출처: https://programs.sigchi.org/dis/2026\n")
o.append("## 0. 관심 초점\n")
o.append("- **메인: 통합형 채팅 인터페이스(ChatGPT/Gemini/Claude류)의 디자인 + Orchestration** — 단순 텍스트가 아니라 액션칩·UI 컴포넌트·(광고)를 함께 내는 표면, 그리고 사용자 행동.")
o.append("- **금융에서의 AI 사용자 행동 / 새 통합 인터페이스로 인한 행동양상 변화**")
o.append("- **UX 관점** 중심\n")
o.append("## 1. 학회 일정 골격\n")
o.append("| 날짜 | 내용 |\n|---|---|")
o.append("| 6/13(토)–6/14(일) | 워크숍 · Doctoral Consortium · (6/14 18:00 Welcome Reception) |")
o.append("| **6/15(월)** | 본 학회 1일차 — 세션 09:30·11:00·14:00·16:10 · 18:30 Exhibition Reception |")
o.append("| **6/16(화)** | 본 학회 2일차 — 세션 09:00·11:00·14:00·16:10 |")
o.append("| **6/17(수)** | 본 학회 3일차 — 세션 09:00·11:00·14:00 · Closing Keynote Panel |")
o.append("\n> 휴식: 커피 10:30–11:00 / 점심 12:30–14:00 / 커피 15:30–16:10\n")

o.append("## 2. 추천 논문 15편 (관심 초점 기준 재선정)\n")
o.append("표기: 🇰🇷 한국 기관 저자 · 📄 PDF 확보(`DIS26/`) · 🔗 공식 프로그램(논문집은 학회 후 ACM DL 공개)")
o.append("그룹: **Ⅰ. 통합·하이브리드 인터페이스** / **Ⅱ. 대화형 검색·추천·관계 + 행동** / **Ⅲ. 다크패턴·광고·금융 행동** / **Ⅳ. 에이전트 설명성**\n")
GROUPS_D=[("Ⅰ. 통합·하이브리드/적응형 인터페이스",['DIS01','DIS02','DIS03','DIS04','DIS05','DIS06']),
          ("Ⅱ. 대화형 검색·추천·관계 + 사용자 행동",['DIS07','DIS08','DIS09','DIS10','DIS11']),
          ("Ⅲ. 다크패턴·광고·금융 행동",['DIS12','DIS13']),
          ("Ⅳ. 에이전트 설명성·맥락 대화",['DIS14','DIS15'])]
bd={r['code']:r for r in F['DIS']}
for gt,codes in GROUPS_D:
    o.append(f"### {gt}\n")
    for code in codes:
        r=bd[code]; pdf=has_pdf('DIS26',code)
        flags=("🇰🇷 " if r['korean'] else "")+("📄 " if pdf else "")
        o.append(f"#### {code} · {flags}{r['title']}")
        o.append(f"- 🕘 **{when(r)}** · 📍 {r['room']} · 세션 *{r['session']}* ({r['type']})")
        o.append(f"- 👤 {leads(r)}")
        o.append(f"- 💡 {DESC.get(code,'')}")
        links=[f"[프로그램]({plink('dis',r['id'])})"]
        if r.get('arxiv'): links.append(f"[arXiv](https://arxiv.org/abs/{r['arxiv'].split('v')[0]})")
        tail=(f" · 📄 `DIS26/{code}_*.pdf`" if pdf else " · ⏳ 논문집 미공개(학회 후 ACM DL)")
        o.append(f"- 🔗 {' · '.join(links)}{tail}\n")

o.append("## 3. 3일 추천 동선 (병렬세션 충돌 해소)\n```")
o.append("월 6/15  11:00 LT?   ★Hybrid GUI-LLM(DIS01)            → 16:10 Aud1  Agency&Explanation (DIS02·03·14·15)")
o.append("화 6/16  11:00 LT52  ★ConSearcher(DIS07)              → 14:00 Aud2  Group Conv Agents 리뷰(DIS10) → 16:10 Aud1 ★MindStock 금융(DIS13)")
o.append("수 6/17  09:00 LT52  ★IntentFlow(DIS04)+Generative Ghosts(DIS11) → 14:00 LT52 Elemental Alchemist(DIS05)·Death of Chatbot(DIS09) → 폐막 키노트")
o.append("```")
o.append("- 월 16:10 *Agency and Explanation in AI Systems*(Aud1) 세션에 DIS02·03·14·15가 몰려 있어 한 자리에서 4편 관람 가능.")
o.append("- ★ = 통합 인터페이스/금융 최우선.\n")

o.append("## 4. 🇰🇷 한국 기관 / 한국인 저자 참여 (별도 정리)\n")
o.append("> \"한국대학교(고려대)\" 단독 발표는 없음. 아래는 **한국 소속 저자 참여** 발표(추천 15편 + 그 외).\n")
o.append("| 시간(SGT) | 논문 | 한국 소속 | 세션 |\n|---|---|---|---|")
KR=[("월 16:10","Designing a Citizen-Empowered Model for Local Journalism (Pictorial)","UNIST","AI, Civic Participation & Journalism"),
("월 18:30","Comforting an Emotion-Mirroring Robot (PWiP)","Hongik Univ.","Provocations & WiP"),
("월 18:30","Transparent AI-Mediated Language Support (PWiP)","Seoul National Univ.","Provocations & WiP"),
("화 09:00","Co-designing Haptics for Deaf/HoH Music Education","KAIST · ETRI","Haptics and Sensory Interaction"),
("화 09:00","Augmentiary: LLM Interpretive Feedback for Journaling","UNIST","AI in Education and Reflection"),
("화 11:00","Design and Field Trial of Adilet","UNIST","Mediated Presence & Emotional Connection"),
("화 11:00","Reelee · SOTATE (physicalization)","UNIST","Mediated Presence & Emotional Connection"),
("화 11:00","ComiXR: Comic Layouts in XR","KAIST","Social XR and Virtual Companionship"),
("화 14:00","Supporting Dance Motor Skill Training in VR","Hanyang Univ.","AR for Embodied Skill"),
("화 16:10","When XR Comes Home","Sogang Univ.","Aging, Culture, and Domestic Technology"),
("화 16:10","Technology Redux","KAIST","Speculative Futures"),
("수 11:00","SoTA: Interactive Art Exhibition for Public AI","KAIST","AI in Creative Practice"),
("수 11:00","Designing Artificial Identity (framework)","SNU · ETRI","Robots in Social & Professional Roles"),
("수 14:00","Who Sets the Norm? Scaffolds for ADHD Relationships","KAIST","Algorithmic Intimacy and Identity"),
("수 14:00","Is This the Real Me? Algorithmic Self-Portraits","UNIST","Algorithmic Intimacy and Identity"),
("일 09:00","(워크숍) AI, Sensemaking & Decision-Making in Crisis","SeoulTech","WS15")]
def kr_inst(r):
    for a in r['authors']:
        if 'korea' in (a.get('c') or '').lower() or 'kaist' in (a.get('i') or '').lower():
            return a['i']
    return r['authors'][0]['i']
for r in F['DIS']:
    if r['korean']:
        w=when(r); KR.insert(0,(w.split(' ')[0]+" "+w.split(' ')[1].split('–')[0], f"**{r['code']}** "+r['title'][:46], kr_inst(r), r['session']))
for w,ti,inst,ses in KR:
    o.append(f"| {w} | {ti} | {inst} | {ses} |")
o.append("\n🔗 굵은 `DISxx`는 추천 15편 포함.\n")
o.append("## 5. PDF 안내\n")
o.append("DIS 2026 논문집은 학회 개최(6/13–17)에 맞춰 ACM DL에 공개됩니다. 현재는 **arXiv 프리프린트가 있는 논문만** `DIS26/`에 확보 — 나머지는 개최 후 보강 가능.\n")
# [disabled] DIS26_PLANNING.md is generated by gen_dis.py

# ---------------- CHI26.md ----------------
c=[]
c.append("# CHI 2026 관심 논문 리스트 (CHI26)\n")
c.append("> **ACM CHI Conference on Human Factors in Computing Systems 2026** · Barcelona (BCIC)")
c.append("> 일정: **2026-04-13 ~ 17** (개최 완료) · 출처: https://programs.sigchi.org/chi/2026")
c.append("> 채택 논문 1,702편 중 관심 초점으로 **25편** 선별 · 연관성 기준 5개 섹션으로 묶고 섹션 내 관련도순 정렬.\n")
c.append("## 관심 초점\n")
c.append("**통합형 채팅 인터페이스(ChatGPT/Gemini/Claude류)** 가 단순 텍스트가 아니라 **GUI 컴포넌트(버튼·카드)** 를 섞어 내고 사용자가 눌러 서비스를 실행하는 인터랙션 — 그 **디자인·사용자 행동**, 위에 얹는 **넛지·광고**, **AI 페르소나 설계**, **금융 의사결정**.\n")
c.append("1. **Agentic UI 메커니즘** — 에이전트가 GUI 컴포넌트를 생성·실행 (버튼 인터랙션)")
c.append("2. **AI 페르소나·정체성 설계**")
c.append("3. **넛지·설득·광고·커머스** (+ 다크패턴 경계)")
c.append("4. **금융 × AI 인터페이스** — 금융활동·의사결정")
c.append("5. **사용자 행동·신뢰·과의존**\n")
c.append("## 논문 리스트\n📄 PDF 위치 `papers/CHI26/` · 🔗 DOI = ACM DL · **섹션 내 순위 = 인용수(↓) + 관련도(★)**")
c.append("> 인용수: Semantic Scholar 기준(2026 논문이라 프리프린트 인용 위주, ACM 조회수 API 미제공). ★★★=비전 핵심 · ★★=강함 · ★=관련.\n")
import json as _j
CITES=_j.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'chi_cites.json')))
STAR={'CHI16':3,'CHI01':2,'CHI18':2,'CHI03':2,'CHI04':2,'CHI05':2,'CHI19':1,'CHI20':1,
'CHI22':3,'CHI21':3,'CHI24':2,'CHI25':2,'CHI23':1,
'CHI17':3,'CHI02':3,'CHI09':2,'CHI10':2,'CHI15':2,
'CHI13':2,'CHI14':2,'CHI11':2,'CHI12':2,
'CHI06':2,'CHI07':3,'CHI08':1}
def cc(code): return (CITES.get(code) or {}).get('cc') or 0
def stars(code): return '★'*STAR.get(code,1)
GROUPS_C=[
("Ⅰ. Agentic UI 메커니즘 — 에이전트가 GUI 컴포넌트를 생성·실행 (버튼 인터랙션)",['CHI16','CHI01','CHI05','CHI18','CHI03','CHI04','CHI19','CHI20']),
("Ⅱ. AI 페르소나·정체성 설계",['CHI22','CHI21','CHI24','CHI23','CHI25']),
("Ⅲ. 넛지·설득·광고·커머스 (+ 다크패턴 경계)",['CHI17','CHI02','CHI09','CHI10','CHI15']),
("Ⅳ. 금융 × AI 인터페이스 — 금융활동·의사결정",['CHI13','CHI14','CHI11','CHI12']),
("Ⅴ. 사용자 행동·신뢰·과의존",['CHI06','CHI07','CHI08'])]
bc={r['code']:r for r in F['CHI']}
ORDER={}  # remember ranked order for summary table
for gt,codes in GROUPS_C:
    ranked=sorted(codes,key=lambda x:(-cc(x),-STAR.get(x,1)))
    ORDER[gt]=ranked
    c.append(f"### {gt}\n")
    for i,code in enumerate(ranked,1):
        r=bc[code]; pdf=has_pdf('papers/CHI26',code)
        flags=("🇰🇷 " if r['korean'] else "")+("📄 " if pdf else "⏳ ")
        c.append(f"#### {i}. {code} · {stars(code)} · 인용 {cc(code)} · {flags}{r['title']}")
        c.append(f"- 👤 {leads(r)}")
        c.append(f"- 💡 {DESC.get(code,'')}")
        tail=(f"📄 `papers/CHI26/{code}_*.pdf`" if pdf else "⏳ ACM DL에서 직접 다운로드 권장(자동수집 차단)")
        c.append(f"- 🔗 [DOI](https://doi.org/{r['doi']}) · [프로그램]({plink('chi',r['id'])}) · {tail}\n")
c.append("## 요약 표 (섹션 → 인용수·관련도순)\n| 섹션 | 순위 | 코드 | 논문 | 인용 | 관련도 | PDF |\n|---|---|---|---|---|---|---|")
SECN={0:'Ⅰ 메커니즘',1:'Ⅱ 페르소나',2:'Ⅲ 넛지·광고',3:'Ⅳ 금융',4:'Ⅴ 행동'}
for gi,(gt,codes) in enumerate(GROUPS_C):
    for i,code in enumerate(ORDER[gt],1):
        r=bc[code]; pdf="✅" if has_pdf('papers/CHI26',code) else "⏳"
        c.append(f"| {SECN[gi]} | {i} | {code} | {r['title'][:46]} | {cc(code)} | {stars(code)} | {pdf} |")
c.append("")
open(f"{BASE}/CHI26.md",'w').write("\n".join(c))
print("CHI26.md written (DIS via gen_dis.py)")
print("CHI PDFs:", sum(has_pdf('papers/CHI26',f'CHI{n:02d}') for n in range(1,11)),"/10")
print("DIS PDFs:", sum(has_pdf('DIS26',r['code']) for r in F['DIS']),"/15")
