# scripts/ — 큐레이션 파이프라인 (재생성용)

> `CHI26.md` · `DIS26_PLANNING.md` 는 **생성물**이다. 직접 손으로 고치지 말고 여기 스크립트로 재생성한다.
> (원래 `/tmp`에 두고 작업했으나 휘발성이라 repo로 이관 — 재사용·수정 가능하게.)

## 파일
| 파일 | 역할 |
|---|---|
| `final.json` | **큐레이션 상태(SSOT)** — 선정 논문(CHI 25 / DIS 17)의 코드·제목·저자·세션·시간·DOI·arXiv·🇰🇷 플래그 |
| `chi_cites.json` | CHI 논문 인용수(Semantic Scholar) — 섹션 내 순위에 사용 |
| `build_chi26.py` | `final.json`+`chi_cites.json` → `../CHI26.md` (5개 소주제, 섹션 내 인용수·관련도순) |
| `build_dis26.py` | `final.json` → `../DIS26_PLANNING.md` (요일별 세션·장소·시간, 🇰🇷 저자+이메일) |
| `fetch_program.py` | SIGCHI 원본 프로그램 JSON 재다운로드 (원본 재집계 필요할 때만) |
| `score_keywords.py` | 관심사 키워드 가중 스코어링 헬퍼 — 원본 JSON에서 후보 논문 발굴용 (`final.json` 만들 때 사용) |
| `download_pdfs.py` | 선정 논문 PDF 다운로더 (arXiv 우선 → ACM). ACM은 Cloudflare로 간헐 차단 |

## 재생성
```bash
cd scripts
python3 build_chi26.py    # → ../CHI26.md
python3 build_dis26.py    # → ../DIS26_PLANNING.md
```

## 자주 하는 수정
- **논문 추가/제외**: `final.json` 의 `CHI`/`DIS` 배열 편집 (code·title·doi·arxiv·session·start/end·room·authors·korean).
- **섹션 구성·순서**: `build_chi26.py` 의 `GROUPS_C`, `build_dis26.py` 의 `GROUPS`.
- **CHI 순위 가중치**: `build_chi26.py` 의 `STAR`(관련도) — 정렬키는 `(-인용수, -STAR)`.
- **설명 문구**: 각 빌더 상단 `DESC` 딕셔너리.
- **인용수 갱신**: Semantic Scholar `paper/batch`(fields=citationCount)로 `chi_cites.json` 재생성.

## 주의
- PDF(`CHI26/`,`DIS26/`)는 `.gitignore` 제외 — 원격엔 md만 올라간다.
- DIS 논문집은 학회 개최(2026-06-13~17) 후 ACM DL 공개 → arXiv 없는 논문은 그때 PDF 보강.
