# Advanced Optimization (Fall 2026) — 챕터별 결정과 메모

덱을 만들거나 고치기 전에 이 파일을 먼저 읽는다. 새로 정한 것은 이 파일에 추가한다.
최종 기준 문서는 `lecture-plan-fall2026v3.pdf` (2026-10-09).

## 수업 전체

- 범위: Ch. 1–7, 12, 19. 시간이 되면 Ch. 10 (10월 22일 buffer, §10.1–10.3).
- 화/목, 영어 강의, 수강생 6명. 60분 영어 강의 + 10분 한국어 질의응답이 목표.
  75분 원테이크로 녹화해 YouTube에 올린다.
- 강의는 엄밀할 필요가 없다. 이해가 안 되면 학생이 책을 읽는다. 증명은 수업에서 다루지 않는다.
- 11월 9–18일 출장. 11월 10·12·17일은 학생 발표(Shampoo, SOAP, Muon; 2명씩 3조), 녹화.
- 중간고사 10월 20일 (Ch. 3–6). 기말 프로젝트: IPOPT로 작은 AC OPF를 풀고 log를 Ch. 3·12·19로 해석.
- 그림: 책 그림은 저작권 때문에 그대로 쓰지 않는다. 다시 그리되, 책 그림이 보여 주는 경우를 모두 포함한다.
- 이 repo는 교수님 본인이 보는 용도다. 학생에게 공지하는 자료가 아니다 (public이므로 시험 자료는 두지 않는다).

## 덱 현황 (repo 기준)

| 장 | 최신 PDF | `.tex` in `src/` | 비고 |
|---|---|---|---|
| 1–2 | ch01, ch02 | 없음 | |
| 3 | ch03 | 없음 | 12pt 재작성본(ch03v2)을 다른 대화에서 만들었으나 repo에는 아직 없음 |
| 4 | ch04 | 없음 | 본문 약 9pt (구 형식) |
| 5 | ch05v3 | ch05v3.tex | 현재 서식 기준 |
| 6 | ch06v2 | 교수님이 올릴 예정 | 37장 |
| 7 | ch07v2 | 교수님이 올릴 예정 | 30장 |
| 12, 19 | ch12, ch19 | 없음 | 12pt 형식으로 다시 만들지 미정 |

Ch. 8–11, 16–18 덱도 있으나 수업 범위 밖이다.

## 챕터별

### Ch. 3
- Wolfe 조건 그림(Figure 3.3–3.5 대응)을 책을 베끼지 않고 다시 그렸다.
- 덱의 핵심 메시지: Wolfe 두 조건의 역할(Zoutendijk 증명에서 각각 어디에 쓰이는가), α = 1을 먼저 시도해야 빠른 국소 수렴이 나온다.

### Ch. 4
- §4.3 (subproblem의 정확한 해)는 넘긴다.
- Steihaug-CG는 Ch. 4에서 이름만 소개하고 Ch. 5에서 제대로 다룬다.

### Ch. 5
- 덱 35장(58 → 39 → 35). 숙제 5문제(4×4 Cholesky 손계산 포함).
- Nonlinear CG(§5.2)는 "linear CG에서 FR, PR 등을 만들 수 있다" 정도로 충분하다.
  어차피 BFGS/L-BFGS를 쓴다. 책 p. 124 이후는 정독하지 않는다.
- 책이 빠뜨리거나 증명 없이 넘기는 것: Thm 5.5와 (5.36)의 Chebyshev polynomial 논증,
  preconditioner C를 만들지 않고 M만으로 되는 이유, floating point에서 conjugacy가 무너지는 것,
  Lanczos와의 관계, CG-Steihaug와의 연결, PR+ global convergence 등 인용만 된 결과.

### Ch. 6
- 덱 37장 (2026-10-08). 수업: 10월 13일 BFGS(§6.1), 15일 SR1·Broyden·수렴(§6.2–6.4).
- 책에 증명이 있는 정리: Thm 6.1, 6.5, 6.6. 증명 없이 서술만: Thm 6.2, 6.3, 6.4, 6.7.
- 책이 빠뜨린 것:
  - (6.9)의 해가 DFP (6.13)이라는 유도. W^{1/2}로 변수를 바꾸면 projection 하나로 몇 줄에 나온다.
    (6.9)는 equality-constrained convex QP이고 closed form이 있다.
  - B ↔ H 변환 (Sherman–Morrison–Woodbury) 계산.
  - BFGS의 self-correction이 DFP보다 나은 이유: 서술만 있고 정량적 논증이 없다.
  - Nonconvex f에서 BFGS가 수렴하지 않는 예: Dai (2002, Wolfe line search),
    Mascarenhas (2004, exact line search). 덱에 "(Not in the book.)"으로 넣었다.
- 책 표기: Thm 6.4(ii)는 j = k−1, …, 1로 인쇄되어 있으나 j = 0까지 성립한다.
- 이름: DFP = Davidon–Fletcher–Powell, BFGS = Broyden–Fletcher–Goldfarb–Shanno.
  Powell은 Cambridge의 M. J. D. Powell (Princeton의 Warren Powell과 다른 사람).
- secant 발음: SEE-kənt (미국식).

### Ch. 7
- 수업: 10월 27일 §7.1, 29일 §7.2. §7.3–7.4는 "왜 넘기는가"만 말한다
  → ch07v2의 §7.3–7.4 슬라이드(24–27쪽)는 수업에서 넘긴다.
- 책 오식: p. 177의 "Algorithm 8.1"은 Algorithm 6.1이다.
- 책에 증명이 있는 정리: Thm 7.3. Thm 7.1, 7.2는 informal derivation, Thm 7.4는 증명 생략.
- 예전 ch07 덱에는 있고 ch07v2에 없는 것 (넣을지 미정):
  - CG-Steihaug의 model 감소가 B_k ≻ 0일 때 최적 감소의 절반 이상 (책 p. 173). 책에 있는 내용인데 v2에서 빠짐.
  - AD로 Hessian–vector product 계산 (forward-over-reverse). (Not in the book.)
  - IPOPT의 `hessian_approximation=limited-memory`가 compact representation. (Not in the book.)
  - Grid objective가 partially separable이라는 점. (Not in the book.)
- 예전 ch07 덱의 오류: m = 10, n = 10⁶에서 저장량 "80 MB"는 double precision 기준 160 MB.

### Ch. 10 (시간이 되면)
- Gauss–Newton은 B_k = J_kᵀJ_k를 고르는 방법, Levenberg–Marquardt는 그 model에 Ch. 4 trust region을 쓴 것.
- Ch. 4와 6만 있으면 되므로 Ch. 12 전에 넣을 수 있다. 전력계통 WLS state estimation이 Gauss–Newton이다.

### Ch. 12
- 5회 → 4회로 줄임 (11월 3·5·19·24일). 24일에 degeneracy, duality, sensitivity, AC OPF KKT 예제를 몰아넣었다.
  여유가 생기면 이 장에 한 회를 돌려주는 것이 우선이다.
- Sensitivity(multipliers as sensitivities)는 FREEDOM의 미분(KKT implicit differentiation)과 겹친다.

### Ch. 16, 18 (수업 범위 밖, FREEDOM용)
- QP/SQP는 강의용이 아니라 필요하면 FREEDOM을 위해 공부한다.
- 읽을 곳: §16.1 (equality-constrained QP), §18.1–18.3 (local SQP, Lagrangian Hessian, quasi-Newton, damped BFGS).
- 요점: QP의 Hessian은 ∇²f가 아니라 ∇²ₓₓL이어야 한다. ∇²ₓₓL은 해에서도 indefinite일 수 있다.
  Merit function, filter, Maratos effect는 NN 초기값이 나쁠 때 필요해지면 본다.

## 직접 구현

- 9월 2일 권고: Wolfe line search를 포함한 BFGS (~100줄)를 교수님이 직접 짠다.
  Rosenbrock에서 Wolfe를 켜고 끄며 s_kᵀy_k > 0이 깨지는 것을 본다. 코드는 Claude에게 짜게 하지 않는다.
- Ch. 6 수업(10월 13일) 전에 하면 HW6와 같은 내용이라 바로 수업에 쓸 수 있다.
