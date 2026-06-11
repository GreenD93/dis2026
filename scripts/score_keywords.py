import json, datetime, re, collections

SGT = datetime.timezone(datetime.timedelta(hours=8))
CET = datetime.timezone(datetime.timedelta(hours=2))  # Barcelona April = CEST

# Interest keyword groups (weighted). Lowercased, matched on title+abstract+keywords.
GROUPS = {
 "Agentic AI & Orchestration": (3, ["agentic","ai agent","autonomous agent","llm agent","llm-based","multi-agent","multiagent","agent orchestration","human-agent","human–agent","copilot","ai assistant","intelligent agent","llm-powered","language model agent","tool-use","agent design"]),
 "Conversational & Unified Interface": (3, ["conversational","chatbot","chat interface","chat-based","dialogue system","conversational agent","voice assistant","voice interface","multimodal interface","natural language interface","conversational ui","conversational interface"]),
 "Financial Domain": (3, ["fintech","mobile banking","banking","financial","finance","investment","investing","investor","stock","trading","spending","budgeting","payment","insurance","retirement saving","personal finance","money management"]),
 "AI Persona & Design": (3, ["persona","chatbot personality","agent persona","social robot","anthropomorph","embodied agent","virtual agent","character design","ai companion","relational agent"]),
 "Behavior & Persuasion": (2, ["nudge","persuasive","behavior change","behavioral design","behaviour change","microinteraction","habit formation","gamification","self-tracking","commitment device","choice architecture"]),
 "LLM / GenAI (context)": (1, ["large language model","llm","generative ai","gpt","prompt","genai","foundation model"]),
}

def score_content(c):
    text = " ".join([c.get("title") or "", c.get("abstract") or "",
                     " ".join(c.get("keywords") or []), " ".join(c.get("tags") or [])]).lower()
    total = 0; matched = collections.defaultdict(set)
    for g,(w,kws) in GROUPS.items():
        for kw in kws:
            if kw in text:
                total += w; matched[g].add(kw)
    return total, {g:sorted(v) for g,v in matched.items()}

def load(path):
    d = json.load(open(path))
    ct = {x["id"]: (x.get("displayName") or x.get("name")) for x in d["contentTypes"]}
    tracks = {t["id"]: t["name"] for t in d["tracks"]}
    rooms = {r["id"]: r["name"] for r in d["rooms"]}
    ts = {t["id"]: t for t in d["timeSlots"]}
    sessions = {s["id"]: s for s in d["sessions"]}
    people = {p["id"]: p for p in d["people"]}
    return d, ct, tracks, rooms, ts, sessions, people

def author_names(c, people):
    out=[]
    for a in c.get("authors") or []:
        pid=a.get("personId") if isinstance(a,dict) else a
        p=people.get(pid)
        if not p: continue
        nm=" ".join(x for x in [p.get("firstName"),p.get("middleInitial"),p.get("lastName")] if x)
        affs=[af.get("institution") or af.get("name") or "" for af in (p.get("affiliations") or [])]
        out.append((nm, "; ".join([a for a in affs if a])))
    return out

def session_time(c, sessions, ts, tz):
    sid = (c.get("sessionIds") or [None])[0]
    s = sessions.get(sid)
    if not s: return None
    slot = ts.get(s.get("timeSlotId"))
    if not slot: return (s.get("name"), None, None)
    st=datetime.datetime.fromtimestamp(slot["startDate"]/1000, tz)
    en=datetime.datetime.fromtimestamp(slot["endDate"]/1000, tz)
    return (s.get("name"), st, en)
