import json,datetime,glob
F=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'final.json')))
import os as _os; BASE=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DIS=[r for r in F['DIS']]
def has_pdf(code): return bool(glob.glob(f"{BASE}/DIS26/{code}_*.pdf"))
def plink(i): return f"https://programs.sigchi.org/dis/2026/program/content/{i}"
WD={0:'월',1:'화',2:'수',3:'목',4:'금',5:'토',6:'일'}
def when(r):
    if not r['start']: return 'TBD'
    s=datetime.datetime.fromisoformat(r['start']); e=datetime.datetime.fromisoformat(r['end'])
    return f"{s.month}/{s.day}({WD[s.weekday()]}) {s.strftime('%H:%M')}–{e.strftime('%H:%M')}"
def leads(r,n=2):
    a=r['authors']; s="; ".join(f"{x['n']} ({x['i']})" for x in a[:n])
    return s+(f" 외 {len(a)-n}인" if len(a)>n else "")
def kr_inst(r):
    for a in r['authors']:
        if 'korea' in (a.get('c') or '').lower() or 'kaist' in (a.get('i') or '').lower(): return a['i']
    return r['authors'][0]['i']

DESC={
'DIS01':"GUI 직접조작 + LLM 프롬프트를 결합한 **하이브리드 인터페이스(LCS)** — 비전문가용 3D 씬 편집. ★통합 신규 인터페이스 원형.",
'DIS02':"시스템이 주도권을 갖는 **적응형 mixed-initiative 질의** — Orchestration이 사용자 의도를 보조(GUI↔자연어 전환).",
'DIS03':"챗창이 아니라 **커서에 붙어** 흐름 속에서 돕는 임베디드 에이전트 — 통합 서비스 안의 에이전트 형태.",
'DIS04':"생성형 AI의 **의도 전달(intent communication) 동역학** — 의도→결과 명세 워크플로. (KAIST, Juho Kim 랩)",
'DIS05':"멀티에이전트 결과를 **아바타로 설명·투명화** — '누가 무엇을 했나' 가시화로 Orchestration 신뢰 확보.",
'DIS06':"모바일 투자앱 인지편향을 **원칙기반 피드백**으로 자기성찰 유도 — **금융 의사결정 행동변화**. ★ (KAIST/UNIST)",
'DIS07':"고령층의 **디지털뱅킹 사용 장벽·기회**(홍콩) — Agentic 금융서비스가 놓치는 고객층의 실제 행동/포용. ★",
'DIS08':"비공식 전자상거래 생태계를 위한 **안전·책임 소셜마켓 도구** — 신뢰 기반 금융거래 행동 설계.",
'DIS09':"라이브커머스 **다크패턴**을 사용자 **행동전략·해석**으로 재조명 — 기만 인지/방어 인터페이스. ★",
'DIS10':"**보조기술(스크린리더 등)**이 다크패턴 경험을 드러내거나 오히려 강화 — 접근성 × 기만 방어.",
'DIS11':"**몰입형(VR/AR) 프라이버시 다크패턴**에 대한 사용자 경험·대응 — 기만 설계에 맞선 인터페이스 디자인.",
'DIS12':"**LLM+RAG로 사용자 페르소나 모델링**(Persona-L) + 고정관념 리스크 — 합성 페르소나로 고객 이해(주의점). ★",
'DIS13':"**다중 페르소나**로 디자이너 관점 확장(자전거 인프라 평가) — 현장조사 없이 다관점 고객 시뮬레이션.",
'DIS14':"**취약성 중심 페르소나 저니**로 공감적 프라이버시 리뷰 — 현장조사 없이 사용자 입장을 대리 체험. ★",
'DIS15':"온라인 커뮤니티 **멤버 페르소나**로 대화형 정보탐색 — 실제 사용자 군집을 페르소나로 모사.",
'DIS16':"**AI/에이전트 정체성(Artificial Identity) 설계 프레임워크**와 연구 어젠다 — 페르소나·정체성 설계의 정통 레퍼런스. ★★ (SNU·ETRI)",
'DIS17':"ACG(애니·만화·게임) 실천에서 길어낸 **캐릭터-바운드 공개 동반자**의 인터랙션 인사이트 — 캐릭터 페르소나 설계.",
}
GROUPS=[
("Ⅰ. 통합 신규 인터페이스 · Orchestration · Agentic AI","ChatGPT/Gemini류 통합 인터페이스가 텍스트를 넘어 GUI·에이전트·의도를 다루는 형태",['DIS01','DIS02','DIS03','DIS04','DIS05']),
("Ⅱ. AI 페르소나 — 정체성 설계 + 합성 페르소나(고객 이해)","에이전트 정체성·캐릭터를 설계하고, 실사용자 없이 LLM 페르소나로 고객을 모사·평가",['DIS16','DIS17','DIS12','DIS13','DIS14','DIS15']),
("Ⅲ. Agentic AI 금융 서비스에서의 고객 행동","투자·뱅킹·거래에서 사용자가 실제로 어떻게 의사결정/행동하는가",['DIS06','DIS07','DIS08']),
("Ⅳ. 인터페이스 디자인으로 사기·기만(deception/fraud) 방어","다크패턴·기만을 사용자가 어떻게 겪고, 인터페이스로 어떻게 막을까",['DIS09','DIS10','DIS11']),
]
bd={r['code']:r for r in DIS}
o=[]
o.append("# DIS 2026 참석 계획 (DIS26_PLANNING)\n")
o.append("> **ACM Designing Interactive Systems Conference 2026** · Singapore (NUS) · **2026-06-13~17** · 시간=현지(SGT)")
o.append("> 출처: https://programs.sigchi.org/dis/2026\n")
o.append("## 0. 이 정리의 관점 — 인터넷은행 AX팀\n")
o.append("> 통합 신규 인터페이스(Orchestration)·Agentic AI를 만드는 입장에서, **(Ⅰ) 통합/에이전트 인터페이스 · (Ⅱ) AI 페르소나(정체성 설계 + 합성 페르소나) · (Ⅲ) Agentic 금융서비스 고객 행동 · (Ⅳ) 인터페이스로 사기·기만 방어** 4갈래(연관성 기준 병합)로 DIS 논문을 정리한다.")
o.append("> 표기: 🇰🇷 한국 기관 저자 · 📄 PDF 확보(`DIS26/`) · 🔗 공식 프로그램(논문집은 학회 후 ACM DL 공개)\n")
o.append("## 1. 학회 일정 골격\n")
o.append("| 날짜 | 내용 |\n|---|---|")
o.append("| 6/13(토)–14(일) | 워크숍 · Doctoral Consortium · (14일 18:00 Welcome Reception) |")
o.append("| **6/15(월)** | 본 학회 1일차 — 세션 09:30·11:00·14:00·16:10 |")
o.append("| **6/16(화)** | 본 학회 2일차 — 세션 09:00·11:00·14:00·16:10 |")
o.append("| **6/17(수)** | 본 학회 3일차 — 세션 09:00·11:00·14:00 · Closing Keynote |")
o.append("\n> 휴식: 커피 10:30–11:00 / 점심 12:30–14:00 / 커피 15:30–16:10\n")

import datetime as _dt
from collections import defaultdict
THEME_BY_SEC={0:'🧩 통합·Orchestration',1:'🎭 AI 페르소나',2:'💰 금융 고객행동',3:'🛡 사기·기만 방어'}
code2theme={code:THEME_BY_SEC[i] for i,(t,s,codes) in enumerate(GROUPS) for code in codes}
o.append("## 2. 요일별 추천 일정 (세션 · 장소 · 시간)\n")
o.append("> 같은 세션(시간·장소)에 여러 추천 논문이 묶이면 한 자리에서 연속 관람. 주제: 🧩 통합·Orchestration · 🎭 AI 페르소나 · 💰 금융 고객행동 · 🛡 사기·기만 방어\n")
days=defaultdict(lambda: defaultdict(list))
for r in DIS:
    s=_dt.datetime.fromisoformat(r['start']) if r['start'] else None
    dk=(r['start'] or 'zzz', f"{s.month}/{s.day}({WD[s.weekday()]})" if s else '기타')
    skey=(r['start'] or 'z', r['end'] or 'z', r['session'] or '', r['room'] or '')
    days[(dk[0][:10],dk[1])][skey].append(r)
for dk in sorted(days):
    o.append(f"### 📅 {dk[1]}\n")
    for skey in sorted(days[dk]):
        rs=days[dk][skey]; r0=rs[0]
        tm=when(r0).split(' ',1)[1] if r0['start'] else 'TBD'
        o.append(f"**🕘 {tm} · {r0['session']} · 📍 {r0['room']}**\n")
        for r in rs:
            pdf=has_pdf(r['code']); flags=("🇰🇷" if r['korean'] else "")+("📄" if pdf else "")
            links=[f"[프로그램]({plink(r['id'])})"]
            if r.get('arxiv'): links.append(f"[arXiv](https://arxiv.org/abs/{r['arxiv'].split('v')[0]})")
            o.append(f"- `{r['code']}` {code2theme.get(r['code'],'')} {flags} **{r['title']}**")
            o.append(f"  - {DESC[r['code']]}")
            o.append(f"  - 🔗 {' · '.join(links)}" + (f" · 📄 `DIS26/{r['code']}_*.pdf`" if pdf else " · ⏳ 학회 후 ACM DL"))
        o.append("")
o.append("## 3. 소주제 색인\n")
for title,sub,codes in GROUPS:
    o.append(f"- **{title}** — {', '.join(codes)}")
o.append("")

# Korean section
o.append("## 4. 🇰🇷 한국 기관 / 한국인 저자 참여 (별도) + 교신/제1저자 이메일\n")
o.append("> \"한국대학교(고려대)\" 단독 발표는 없음. 추천 17편 중 한국 소속 + 그 외 주요 한국 발표.")
o.append("> 이메일은 **공개 교수/연구실 페이지 또는 arXiv PDF(IntentFlow)에서 확인**한 값. 확인 안 된 것은 *(미확인)* 표기 — 추정 주소는 넣지 않음.\n")
o.append("| 시간(SGT) | 논문 | 한국 소속 | 교신/제1저자 · 이메일 |\n|---|---|---|---|")
# 추천 🇰🇷 논문(코드별) 이메일
REC_EMAIL={
'DIS04':"Juho Kim(교신) · juhokim@kaist.ac.kr / Yoonsu Kim(제1) · yoonsu16@kaist.ac.kr",
'DIS06':"Hwajung Hong(교신) · hwajung@kaist.ac.kr",
'DIS16':"Jihye Lee(SNU)/Minsu Jang(ETRI) · *(미확인)*",
}
KR=[("월 18:30","Comforting an Emotion-Mirroring Robot (PWiP)","Hongik Univ.","Dokshin Lim · doslim@hongik.ac.kr"),
("월 18:30","Transparent AI-Mediated Language Support (PWiP)","Seoul National Univ.","Joonhwan Lee(PI) · @snu.ac.kr *(정확주소 미확정)*"),
("화 09:00","Co-designing Haptics for Deaf/HoH Music Education","KAIST · ETRI","Woohun Lee · woohun.lee@kaist.ac.kr"),
("화 09:00","Augmentiary: LLM Interpretive Feedback for Journaling","UNIST","Kyungho Lee(PI) · kyungho@unist.ac.kr"),
("화 11:00","ComiXR: Comic Layouts in XR","KAIST","Ian Oakley(PI) · ianoakley@kaist.ac.kr"),
("화 11:00","Adilet · Reelee · SOTATE (physicalization)","UNIST","Young-Woo Park(PI) · ywpark@unist.ac.kr"),
("화 14:00","Value-Sensitive AI for Prayer","Yonsei (공저)","Younah Kang · yakang@yonsei.ac.kr"),
("화 14:00","Group Conversational Agents: A Review","NAVER AI Lab (공저)","Young-Ho Kim · navercorp.com *(정확주소 미확정, younghokim.net)*"),
("화 16:10","When XR Comes Home","Sogang Univ.","Minjin Rheu · *(미확인, 현 Loyola/luc.edu)*"),
("화 16:10","Technology Redux","KAIST","Youn-kyung Lim(PI) · younlim@kaist.ac.kr"),
("화 14:00","Supporting Dance Motor Skill Training in VR","Hanyang Univ.","Yongjae Yoo(PI) · yongjaeyoo@hanyang.ac.kr"),
("수 14:00","Who Sets the Norm? ADHD Relationships","KAIST","Hwajung Hong(PI) · hwajung@kaist.ac.kr"),
("수 14:00","Is This the Real Me? Algorithmic Self-Portraits","UNIST","Kyungho Lee(PI) · kyungho@unist.ac.kr"),
("일 09:00","(워크숍) AI, Sensemaking & Decision-Making in Crisis","SeoulTech","Kyoungwon Seo · kwseo@seoultech.ac.kr")]
for r in DIS:
    if r['korean']:
        w=when(r);KR.insert(0,(w.split(' ')[0]+" "+w.split(' ')[1].split('–')[0], f"**{r['code']}** "+r['title'][:42], kr_inst(r), REC_EMAIL.get(r['code'],"*(미확인)*")))
for w,ti,inst,em in KR: o.append(f"| {w} | {ti} | {inst} | {em} |")
o.append("\n🔗 굵은 `DISxx`는 추천 17편 포함. 이메일 출처: KAIST/UNIST/Yonsei/Hanyang/Hongik/SeoulTech 공개 교수·연구실 페이지, IntentFlow는 arXiv PDF.\n")
o.append("## 5. PDF 안내\n")
o.append("DIS 2026 논문집은 학회 개최(6/13–17)에 맞춰 ACM DL 공개. 현재는 **arXiv 프리프린트가 있는 4편**(DIS04·08·12·15)만 `DIS26/`에 확보 — 나머지는 개최 후 보강 가능.\n")
open(f"{BASE}/DIS26_PLANNING.md",'w').write("\n".join(o))
print("DIS26_PLANNING.md written ·", sum(has_pdf(r['code']) for r in DIS),"/15 PDF")
