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
| 6 | ch06v2.1 | ch06v2.1.tex | 28장 (2026-10-10). ch06v2(37장)에서 수업에 안 쓰는 slide를 뺀 판 |
| 7 | ch07v2 | 교수님이 올릴 예정 | 30장 |
| 10 | ch10v2 | ch10v2.tex | 30장 (2026-10-10). 시간이 되면 10월 22일 |
| 12 | ch12 | 없음 | 12pt 형식으로 다시 만들지 미정 |
| 19 | ch19 | 없음 | ch19v2를 만들 예정 (Ch. 15 일부 포함, 아래 Ch. 19 참고) |

Ch. 8, 9, 11, 16–18 덱도 있으나 수업 범위 밖이다.

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
- ch06v2.1 (2026-10-10): SR1 유도·존재 조건·Algorithm 6.2·Thm 6.1, 6.2, Broyden Thm 6.3, 6.4,
  Remarks on 6.5, Thm 6.7을 뺐다. 뺀 것은 Read 포인터로 쪽수만 남김. Reading Theorem 6.6(Dennis–Moré)은 남김.
- ch06v2.1에 추가 (Not in the book.):
  - Weighted norm = curvature를 고려한 error metric. 예: ∇²f = diag(1000, 0.001), B = ∇²f + I.
    해는 W에 Wy = s로만 의존하므로 Ḡ_k는 계산하지 않는다.
  - BFGS vs DFP 실험 (strong Wolfe, c₂ = 0.9, α = 1 먼저): quadratic n = 10, eigenvalues 1–100,
    H₀ = 10⁻⁴I에서 94 vs >5000, 10⁻²I에서 45 vs 249, I에서 11 vs 15; Rosenbrock H₀ = I에서 34 vs 84
    (BFGS 34는 책 p. 141과 일치). 이유: DFP는 B를 최소로 바꾸므로 B가 너무 큰 오류(짧은 step)가 남고,
    line search는 이를 고치지 못한다. BFGS가 남기는 H의 오류(긴 step)는 line search가 줄인다.
- (6.13) 유도는 W^{1/2} 변수 변환 → B̂u = u → projection 세 단계로 학생에게 공부용으로 낸다.

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
- 덱 30장 (2026-10-10, ch05v2/ch06v2 서식). 책에 증명이 있는 것: Thm 10.1, Lemma 10.2, Thm 10.3. (10.30)은 유도만.
- "(Not in the book.)" 두 곳: Ch. 6과의 비교(GN은 B_k = JᵀJ를 고르는 것), 활용 사례(전력계통 WLS state estimation,
  ML의 generalized Gauss–Newton과 Shampoo — Morwani et al., ICLR 2025).
- Figure 10.1, 10.2는 TikZ로 다시 그렸다. (10.30)은 책의 ≈ 형태만 실었다.
- 숙제: Ex 10.1(a), 10.2, 10.3(a) + 손계산(r₁ = x−2, r₂ = x²−1, x₀ = 0: GN step 2, LM(λ=1) step 1,
  Newton step −2, Newton은 descent 아님) + (10.6) 모형에 GN 구현.

### Ch. 12
- 5회 → 4회로 줄임 (11월 3·5·19·24일). 24일에 degeneracy, duality, sensitivity, AC OPF KKT 예제를 몰아넣었다.
  여유가 생기면 이 장에 한 회를 돌려주는 것이 우선이다.
- Sensitivity(multipliers as sensitivities)는 FREEDOM의 미분(KKT implicit differentiation)과 겹친다.
- 기존 ch12.pdf(17장)는 구 형식(작은 폰트, 한 장에 내용 과다)이고 비유 표현이 있다
  ("the linearization lies", "tells the truth", "switches the constraint on and off"). `Read:` 표시도 없다.
- 증명 처리 (2026-10-10): 교수님은 증명을 전부 읽는다. 학생 reading assignment는 Thm 12.1(KKT) 증명의 구조,
  Thm 12.6(second-order sufficient), Lemma 12.2의 T_Ω ⊂ F 방향만. Lemma 12.2의 반대 방향, Thm 12.5, §12.6 MFCQ 세부는 뺀다.
  Ch. 12는 중간고사 범위 밖이므로 HW12에 증명의 한 단계를 묻는 문제를 넣는다
  (예: Thm 12.1 증명에서 LICQ가 쓰이는 곳, LICQ가 깨지는 예에서 그 단계가 실패하는 이유).

### Ch. 19 — v2를 만들 것 (2026-10-10 결정)
- Ch. 15에서 Ch. 19가 쓰는 부분을 포함해서 `ch19v2`를 새로 만든다. 수업은 Ch. 12 → 19로 바로 가므로 그 부분을 19 덱 안에 넣는다.
- Ch. 19 본문이 참조하는 Ch. 15 부분 (책 본문 대조로 확인):
  - §15.2 Example 15.1: inequality 문제의 active set 결정이 combinatorial하다는 것. §19.1이 interior-point를 쓰는 이유로 이 예를 든다.
  - §15.4 merit function (ℓ₁ exact merit)과 filter, restoration phase. §19.3–19.4 step acceptance와 §19.7 이 직접 참조한다.
  - §15.5 Maratos effect, §15.6 second-order correction과 nonmonotone 기법. §19.4가 merit function이 Maratos effect를 일으킬 때 쓰라고 한다.
- IPOPT는 filter line search, second-order correction, restoration phase를 쓴다. 기말 프로젝트에서 IPOPT log를 해석하려면 이 부분이 필요하다.
- Ch. 19가 Ch. 16, 18에서 가져오는 것도 있다: KKT matrix와 symmetric indefinite factorization (16.7), (16.12),
  Hessian 수정·inertia, damped BFGS (18.14)–(18.15), penalty parameter ν 갱신. 덱에서는 결과만 한 줄씩 서술한다.
- 형식은 ch05v3 서식, 30장 안팎. 기존 ch19.pdf는 지우지 않는다.
- Lemma 16.3 (§16.2)을 inertia 슬라이드에 넣는다: inertia(K) = inertia(ZᵀGZ) + (m, m, 0).
  §19.3이 inertia correction의 근거로 인용하고, IPOPT가 factorization에서 inertia를 보고 δ를 더하는 이유다.
  Inertia를 LDLᵀ에서 읽는 것은 §3.4와 Appendix A(Bunch–Kaufman)로 이미 수업 범위다.
- 책 안에서 IPOPT가 쓰지만 수업 밖인 나머지 (넣지 않고 언급만):
  §14.2 Mehrotra predictor-corrector (`mu_strategy adaptive`일 때만), (18.14)–(18.15) damped BFGS (L-BFGS 옵션일 때만),
  (18.12) elastic mode·§17.2 ℓ₁ penalty (IPOPT restoration phase가 푸는 문제와 비슷한 형태).
- 위 Ch. 15 부분과 Lemma 16.3을 넣으면 IPOPT 기본 설정의 log는 책 내용으로 설명된다.


### Ch. 16, 18 (수업 범위 밖, FREEDOM용)
- QP/SQP는 강의용이 아니라 필요하면 FREEDOM을 위해 공부한다.
- 읽을 곳: §16.1 (equality-constrained QP), §18.1–18.3 (local SQP, Lagrangian Hessian, quasi-Newton, damped BFGS).
- 요점: QP의 Hessian은 ∇²f가 아니라 ∇²ₓₓL이어야 한다. ∇²ₓₓL은 해에서도 indefinite일 수 있다.
  Merit function, filter, Maratos effect는 NN 초기값이 나쁠 때 필요해지면 본다.

## 직접 구현

- 9월 2일 권고: Wolfe line search를 포함한 BFGS (~100줄)를 교수님이 직접 짠다.
  Rosenbrock에서 Wolfe를 켜고 끄며 s_kᵀy_k > 0이 깨지는 것을 본다. 코드는 Claude에게 짜게 하지 않는다.
- Ch. 6 수업(10월 13일) 전에 하면 HW6와 같은 내용이라 바로 수업에 쓸 수 있다.
