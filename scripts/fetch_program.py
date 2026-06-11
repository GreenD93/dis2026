"""SIGCHI 공식 프로그램 JSON 다운로드.
사용: python3 fetch_program.py   → scripts/chi2026.json, scripts/dis2026.json 저장
출처: files.sigchi.org/conference/program/{CHI|DIS}/2026 (대문자 주의)
build_chi26.py / build_dis26.py 는 final.json(큐레이션 결과)만 쓰므로 평소엔 불필요.
새 학회·신규 논문 반영 등 원본 재집계가 필요할 때만 사용.
"""
import urllib.request, ssl, os
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0"
for conf in ("CHI", "DIS"):
    url = f"https://files.sigchi.org/conference/program/{conf}/2026"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = urllib.request.urlopen(req, timeout=60, context=ssl.create_default_context()).read()
    out = os.path.join(HERE, f"{conf.lower()}2026.json")
    open(out, "wb").write(data)
    print(f"{conf}: {len(data)//1024} KB -> {out}")
