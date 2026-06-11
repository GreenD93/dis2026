import json, urllib.request, urllib.parse, re, sys, time, os, ssl, xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
MAIL = "yg93_jo@kbanknow.com"

def get(url, headers=None, timeout=40):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout, context=ctx)

def norm(s): return re.sub(r'[^a-z0-9]+',' ',(s or '').lower()).strip()

def crossref_doi(title):
    q = urllib.parse.urlencode({"query.bibliographic": title, "rows": 5, "mailto": MAIL})
    try:
        data = json.load(get(f"https://api.crossref.org/works?{q}"))
    except Exception as e:
        return None
    nt = norm(title)
    best=None
    for it in data.get("message",{}).get("items",[]):
        cand = norm(" ".join(it.get("title",[]) or []))
        if not cand: continue
        # token overlap
        a,b=set(nt.split()),set(cand.split())
        if not b: continue
        ov=len(a&b)/max(1,len(a))
        if ov>0.7:
            sc=ov + (0.2 if it.get("DOI","").startswith("10.1145") else 0)
            if not best or sc>best[0]: best=(sc,it.get("DOI"),it.get("publisher"))
    return best[1:] if best else None

def arxiv_pdf(title):
    q = urllib.parse.urlencode({"search_query": f'ti:"{title[:120]}"', "max_results": 3})
    try:
        xml = get(f"http://export.arxiv.org/api/query?{q}").read().decode()
    except Exception:
        return None
    ns={"a":"http://www.w3.org/2005/Atom"}
    root=ET.fromstring(xml); nt=norm(title)
    for e in root.findall("a:entry",ns):
        t=norm(e.findtext("a:title",default="",namespaces=ns))
        a,b=set(nt.split()),set(t.split())
        if b and len(a&b)/max(1,len(a))>0.75:
            for l in e.findall("a:link",ns):
                if l.get("title")=="pdf": return l.get("href")
            idu=e.findtext("a:id",default="",namespaces=ns)
            if "arxiv.org/abs/" in idu: return idu.replace("/abs/","/pdf/")
    return None

def download(url, path, headers=None):
    try:
        r=get(url, headers=headers)
        ct=r.headers.get("Content-Type","")
        blob=r.read()
        if b"%PDF" not in blob[:1024]:
            return f"not-pdf({ct})"
        open(path,"wb").write(blob)
        return f"ok {len(blob)//1024}KB"
    except Exception as e:
        return f"err {type(e).__name__}:{str(e)[:60]}"

def safe(t):
    t=re.sub(r'[^A-Za-z0-9 ._-]','',t).strip()
    return re.sub(r'\s+','_',t)[:80]

def process(items, outdir, prefix):
    os.makedirs(outdir, exist_ok=True)
    results=[]
    for i,it in enumerate(items,1):
        title=it["title"]; rec={"title":title}
        fn=f"{prefix}{i:02d}_{safe(title)}.pdf"
        path=os.path.join(outdir,fn)
        # 1 arxiv
        ax=arxiv_pdf(title); status=None; src=None; doi=None
        cr=crossref_doi(title)
        if cr: doi=cr[0]
        if ax:
            st=download(ax,path)
            if st.startswith("ok"): status=st; src="arXiv:"+ax
        if not status and doi and doi.startswith("10.1145"):
            for u in [f"https://dl.acm.org/doi/pdf/{doi}", f"https://dl.acm.org/doi/pdf/{doi}?download=true"]:
                st=download(u,path,headers={"User-Agent":UA,"Accept":"application/pdf"})
                if st.startswith("ok"): status=st; src="ACM:"+u; break
        rec.update({"doi":doi,"arxiv":ax,"pdf":fn if status else None,"status":status or "NO_PDF","src":src})
        results.append(rec)
        print(f"[{prefix}{i:02d}] {('DL '+status) if status else 'MISS'} | doi={doi} ax={'Y' if ax else '-'} | {title[:60]}")
        time.sleep(1)
    return results

if __name__=="__main__":
    sel=json.load(open("/tmp/selection.json"))
    which=sys.argv[1] if len(sys.argv)>1 else "both"
    out={}
    base="/Users/yg93_jo/workspace/dis2026"
    if which in ("CHI","both"):
        out["CHI"]=process(sel["CHI"], f"{base}/CHI26", "CHI")
    if which in ("DIS","both"):
        out["DIS"]=process(sel["DIS"], f"{base}/DIS26", "DIS")
    json.dump(out,open("/tmp/dlresults.json","w"),ensure_ascii=False,indent=1)
