# 요청: Chapter 19 덱 `ch19v2` 만들기

이 파일이 요청 전체다. 추가 지시를 기다리지 말고 아래 "할 일" 순서대로 진행한다.
질문은 되돌릴 수 없거나 범위가 크게 달라지는 경우에만 한다. 그 밖에는 가장 합리적인 쪽으로 정하고, 무엇을 정했는지 결과와 함께 알린다.

과목: Advanced Optimization (Fall 2026, 서강대, 영어 강의, 수강생 6명), 교재 Nocedal & Wright, *Numerical Optimization* 2nd ed.
작성: 2026-11-26, Ch. 12 덱(v2–v8)을 만든 대화에서 넘김.

## 할 일

1. `innotobe/teaching`(push 권한)과 `innotobe/books`를 연결한다.
2. teaching repo의 `CLAUDE.md`와 `Nocedal/NOTES.md`를 읽는다. NOTES에서는 "수업 전체", "덱 현황", "Ch. 12"(self-contained 작성 규칙), "Ch. 19" 항목을 본다.
3. `innotobe/books`의 `Numerical_Optimization.pdf`에서 Chapter 19를 읽고, Ch. 19가 참조하는 다른 장의 해당 부분도 읽는다 (아래 "가장 중요한 조건" 참고).
4. `src/ch12v8.tex`의 preamble로 `ch19v2.tex`를 쓴다. 30장 안팎.
5. 컴파일하고 확인한다 (아래 "기술 메모"의 확인 절차).
6. PDF와 `.tex`를 보내고, 슬라이드 구성(장별 제목 한 줄씩), 책과 다르게 처리한 부분, 다른 장에서 가져와 넣은 내용의 목록을 알린다.
7. push 허락을 받은 뒤 `Nocedal/ch19v2.pdf`, `src/ch19v2.tex`를 넣고 NOTES를 고쳐 push한다. 허락 없이는 push하지 않는다.

## 현재 상태

- repo `innotobe/teaching`, branch `main`, 마지막 commit `a559cdc`. 작업 트리는 깨끗하다.
- Ch. 12는 2026-11-26 수업에서 `ch12v8`(25장)로 끝났다.
- 남은 수업일은 12/1, 12/3, 12/8, 12/10 네 회이고 전부 Ch. 19에 쓴다 (IPOPT log 읽기 포함).
- Ch. 19는 `Nocedal/ch19.pdf`(구 형식: 작은 폰트, 한 장에 내용 과다)만 있고 `.tex`가 없다. `ch19v2`는 새로 쓴다. `ch19.pdf`는 지우지 않는다.
- NOTES에 고칠 줄이 있다 (push할 때 함께):
  - 일정: "Ch. 12 세 회(11/24·26, 12/1) + Ch. 19 세 회" → Ch. 12는 11/24·26 두 회로 끝, Ch. 19는 네 회.
  - Ch. 19 항목의 "형식은 ch05v3 서식" → `src/`의 가장 최근 덱(ch12v8) 서식.
  - Ch. 19 항목의 "교수님이 §19.1을 먼저 읽으신 뒤 시작" → 읽지 않고 바로 시작하는 것으로 바뀜.
  - 덱 현황 표의 Ch. 19 행.

## 가장 중요한 조건: Ch. 12에서 Ch. 19로 바로 넘어간다

수업이 다룬 장은 Ch. 1–7과 12다 (Ch. 10은 NOTES에서 수업 여부를 확인한다). Ch. 8, 9, 11, 13–18은 다루지 않았다.
Ch. 19 본문에는 다루지 않은 장의 개념이 설명 없이 쓰인다. 그런 개념이 나올 때마다 덱 안에서 설명한다.

- 처음 나오는 자리에 둔다. 덱 앞쪽에 "사전 지식" 묶음으로 몰아넣지 않는다.
- 분량은 필요한 만큼만. 정의 한두 줄이면 되는 것은 한두 줄로, 한 장이 필요한 것(예: merit function과 filter, inertia)은 한 장으로.
- 출처를 적는다: 책의 절·식 번호와 쪽수. 책에 있는 내용이므로 `(Not in the book.)`이 아니라 "(From Chapter 15.)"처럼 표시한다.
- 왜 필요한지를 먼저 쓰고 정의를 쓴다.
- 교수님은 §19.1을 읽지 않은 상태에서 덱을 본다. 덱만 읽고 이해되어야 한다.

NOTES에 이미 확인해 둔 것 (책 본문과 다시 대조한다):

| 출처 | 내용 | Ch. 19에서 쓰이는 곳 |
|---|---|---|
| §15.2 Example 15.1 | active set 결정이 combinatorial | §19.1, interior-point를 쓰는 이유 |
| §15.4 | merit function(ℓ₁), filter, restoration phase | §19.3–19.4 step acceptance, §19.7 |
| §15.5–15.6 | Maratos effect, second-order correction | §19.4 |
| §16.2 Lemma 16.3 | inertia(K) = inertia(ZᵀGZ) + (m, m, 0) | §19.3 inertia correction |
| Ch. 16, 18 | KKT matrix, symmetric indefinite factorization, Hessian 수정, damped BFGS, penalty parameter 갱신 | 결과만 한 줄씩 |

이 표에 없는 것도 Ch. 19를 읽으면서 찾는다. 예상되는 것: slack variable s를 넣은 형태 c_I(x) − s = 0, multiplier y와 z, fraction-to-boundary rule, barrier parameter μ의 갱신, primal-dual system의 대칭화, central path.
Ch. 14(LP의 interior-point)도 다루지 않았으므로 Ch. 19가 Ch. 14의 결과에 기대는 곳이 있으면 같은 방식으로 처리한다.

수업에서 이미 다뤄서 한 줄 상기로 충분한 것: Newton method와 line search(Ch. 3), trust region(Ch. 4), CG(Ch. 5, 7), BFGS와 L-BFGS(Ch. 6, 7), LDLᵀ에서 inertia 읽기(§3.4, Appendix A), KKT·LICQ·strict complementarity·second-order 조건(Ch. 12).

## 덱의 범위와 목적

- §19.1–19.3 중심. 나머지 절은 Ch. 19를 읽고 필요한 만큼 넣는다.
- 기말 프로젝트가 "IPOPT로 작은 AC OPF를 풀고 log를 Ch. 3·12·19로 해석"이다. IPOPT 기본 설정의 log가 덱 내용으로 설명되어야 한다.
  IPOPT는 filter line search, second-order correction, restoration phase, inertia correction을 쓴다.
- Ch. 12와 연결할 두 곳:
  - LICQ 실패 → active constraint Jacobian이 rank-deficient → multiplier가 유일하지 않음 → KKT matrix singular → IPOPT의 δ_c 보정. Ch. 12에서는 말하지 않았으므로 KKT matrix 슬라이드에서 처음 말한다.
  - Theorem 12.6의 조건(null space 위에서 ∇²L이 positive definite)이 inertia 조건 (n, m, 0)과 같다.
- 숙제 장 바로 앞에 "chapters not covered" 한 장(5분 분량)을 둔다. 12/10에 따로 개관 수업을 하지 않기 때문이다.
  내용은 NOTES의 Ch. 12 항목에 적힌 것(SQP, augmented Lagrangian, ℓ₁ penalty 등 Ch. 19의 대안과 그것이 IPOPT의 어디에 나오는지)을 따른다.
- 네 회 수업에 어떻게 나눌지(몇 쪽까지가 몇 회인지)는 결과를 보낼 때 제안한다. 슬라이드 안에는 회차 구분을 넣지 않는다.

## 작성 규칙 (CLAUDE.md의 규칙에 더해, Ch. 12에서 반복해서 지적받은 것)

1. self-contained. 정의·식을 번호로만 인용하지 않고 그 자리에서 한 줄로 다시 적는다. 치환 단계를 건너뛰지 않는다. 기호는 쓰기 전에 정의한다.
2. 에센스만. 예제는 적게. 책에 없는 예제는 넣지 않는다.
3. convex optimization과 달라지는 부분을 중심으로 구성한다. 학생은 교수님의 3시간 convex 강의(Boyd 방식의 Lagrangian, duality, KKT)를 안다고 가정한다.
   Ch. 19에서 달라지는 곳: Newton step이 descent라는 보장이 없음, step acceptance 기준이 필요함, KKT matrix가 singular일 수 있음, 찾는 것은 local solution.
4. 표기는 Nocedal 그대로. Boyd와 다른 곳(slack s, multiplier y와 z, c_i ≥ 0 부호, Lagrangian의 − 부호)은 처음 나올 때 한 줄로 밝힌다.
5. 동기를 먼저, 정의를 나중에.
6. 본문과 표의 표현을 일치시킨다. 부등호 방향이 헷갈리게 읽히는 문장은 다시 쓴다.
7. 비유·은유 금지, 회차 구분 금지, preview slide 금지, `[shrink]` 금지. 증명은 싣지 않고 빨간 `Read: …, pp. …`로 인쇄 쪽수를 표시한다.
8. slide 한 장에 theorem 또는 algorithm 하나, 또는 displayed equation 3개 이하. 본문 12pt, 긴 theorem·algorithm만 `\small`.
9. 식 번호와 theorem·algorithm 문구는 책과 일치시키고 PDF와 대조한다. 책과 숫자가 다르면 책을 다시 확인한다. 책 자체의 오타도 있다 (Ch. 12 p. 336의 −0.4는 −0.8이 맞음).
10. 확인하지 않은 IPOPT 세부 사항(옵션 이름, 기본값, log 열 이름, 부호 규약)은 쓰지 않는다. 쓰려면 IPOPT 공식 문서에서 확인하고 `(Not in the book.)`으로 표시한다.
11. 숙제는 마지막 장에 5문제 안팎, 쉽게. 책 Exercise 우선, 책에 없는 문제는 표시. 계산 문제는 답을 직접 계산해서 NOTES에 적는다.
12. 그림은 책 그림을 그대로 쓰지 않고 TikZ로 다시 그린다.

## 진행 방식

- 오타, 빠진 한 줄, 정의 누락 같은 작은 수정은 묻지 않고 고친다.
- 기존 파일은 지우거나 덮어쓰지 않는다. 수정본은 `ch19v3`, `ch19v4`로 번호를 올린다. 교수님이 번호를 지정하면 그 번호를 쓴다.
- 버전을 올릴 때마다 NOTES의 덱 현황 표와 Ch. 19 항목에 바뀐 것을 적는다. 새로 정한 것도 NOTES에 적는다.
- `algorithms/`, `_config.yml`, `_data/courses.yml`, `index.html`은 건드리지 않는다. 교재 PDF를 teaching repo에 넣지 않는다.

## 대화 방식

- 한국어 존댓말, 호칭은 "교수님". 답을 먼저, 뒤는 짧게. 수학·기술 용어는 영어 원어 그대로 (한글 음차 금지).
- 교수님은 덱을 읽으면서 개념 질문을 하신다. 물은 것에만 답한다. 이미 아시는 내용을 다시 설명하지 않는다. 칭찬하지 않는다.
  틀렸으면 한 문장으로 틀렸다고 하고 고친다. 반복해서 사과하지 않는다.
- 교수님의 배경: Boyd & Vandenberghe, Bertsekas로 공부했고 IPOPT로 AC OPF를 푼다. Nocedal 책의 Ch. 13–18은 읽지 않았다.
- 강의 전사본을 주시면 1) 내용 2) 발표 3) 영어 세 항목으로 피드백한다.

## 기술 메모

- 서식: `\documentclass[12pt,aspectratio=169]{beamer}`. preamble은 `src/ch12v8.tex`의 `\begin{document}` 앞부분을 그대로 쓴다.
- 쪽수: Ch. 12에서는 인쇄 쪽수 = PDF 쪽수 − 19였다. Ch. 19에서도 같은지 한 쪽을 직접 확인한 뒤 쓴다.
- 확인 절차: pdflatex 두 번 → log에서 overfull box 0개 → `pdftoppm -r 100 -png`로 모든 장을 이미지로 보고 넘침·겹침·하단 여백 확인 → 식 번호와 쪽수를 책과 다시 대조.
- 이 환경에서는 glob을 쓴 `rm` 명령이 차단된다. 이미지는 매번 새 디렉터리에 만든다.
- TikZ `plot`에서 `sqrt` 안이 음수가 되면 오류가 난다. `abs(...)`로 감싼다.
- git: fetch는 `git fetch --depth=50 origin main`, push는 `git -c push.negotiate=true push origin HEAD`. commit 메시지의 attribution 줄은 새 대화가 받는 안내를 따른다.
- GitHub Pages(https://innotobe.github.io/teaching/) 첫 화면 목록은 PDF만 보여 준다. push한 PDF는 약 1분 뒤에 뜬다.
