# 강의자료 repo 작업 지침

이 repo는 public이고 GitHub Pages(https://innotobe.github.io/teaching/)로 공개된다.
push한 PDF는 약 1분 뒤 첫 페이지 목록에 자동으로 뜬다.

## 구조

- `Nocedal/` — Advanced Optimization (Fall 2026, Nocedal & Wright 2nd ed.) 덱 PDF
- `src/` — 덱의 Beamer `.tex` 원본
- `algorithms/` — 자료구조및알고리즘 자료. 요청이 없으면 건드리지 않는다.
- `_config.yml`, `_data/courses.yml`, `index.html` — Pages 설정. 요청이 없으면 건드리지 않는다.

## 절대 규칙

- **교재 PDF는 이 repo에 넣지 않는다.** 교재는 private repo `innotobe/books`에 있다
  (`Numerical_Optimization.pdf`). 덱을 만들 때는 그 repo를 연결해서 읽는다.
- **push 전에 반드시 확인을 받는다.** 파일을 만들고 컴파일한 뒤, 무엇을 올릴지 말하고 허락을 받은 다음 push한다.
- 기존 버전 파일을 지우거나 덮어쓰지 않는다. 새 버전은 `chNNv2`, `chNNv3`처럼 번호를 올린다.
  같은 이름의 파일이 이미 있으면 다음 번호를 쓴다.
- PDF는 `Nocedal/`에, `.tex`는 `src/`에 같은 이름으로 둔다.

## Nocedal 덱 규칙

서식
- 16:9, `\documentclass[12pt,aspectratio=169]{beamer}`.
- 서식(preamble)은 `src/`에서 가장 최근 덱의 것을 그대로 쓴다.
- 본문 12pt. 10pt 미만 금지(footline 8pt만 예외). 긴 theorem이나 algorithm만 `\small`(10.95pt) 허용.
- `[shrink]` 금지.
- slide 한 장에 theorem 하나, 또는 displayed equation 3개 이하.
- 분량은 30장 안팎(엄격한 기준은 아님).

내용
- 식 번호와 theorem·algorithm 문구는 책과 일치시킨다. 책 PDF와 대조한다.
- 책에 없는 내용은 반드시 `(Not in the book.)`으로 표시한다.
- 증명은 slide에 싣지 않고, 빨간색 `Read: proof of Theorem X, pp. …`로 쪽수를 표시한다.
  쪽수는 책 PDF의 인쇄 쪽수로, 대조해서 확인한다.
- "Lecture 1 / Lecture 2" 같은 강의 회차 구분을 넣지 않는다.
- 다른 chapter 내용을 미리 보여주는 preview slide를 넣지 않는다.
- 책과 다른 표기를 쓸 때는 그 표기를 정의하는 줄을 먼저 둔다.
- 비유·은유 표현을 쓰지 않는다. 개념을 직접 서술한다.
- 숙제는 마지막 slide에, 5문제 안팎으로 적고 쉽게. 책 Exercise를 우선 쓰고,
  책에 없는 문제는 표시한다. 계산 문제는 답을 직접 계산해서 확인한다.

## 작업 순서

0. `Nocedal/NOTES.md`를 먼저 읽는다 (챕터별 결정, 책이 빠뜨린 것, 덱 현황). 새로 정한 것은 거기에 추가한다.
1. `innotobe/books`에서 해당 장을 읽고 식 번호, 정리 문구, 쪽수를 확보한다.
2. `src/`의 최신 덱 서식으로 `.tex`를 작성한다.
3. 컴파일하고 확인한다: overfull box 없음, 각 slide를 이미지로 보고 넘침·겹침 없음,
   하단 여백 확보, 식 번호를 책과 다시 대조.
4. PDF와 `.tex`를 사용자에게 보내고, 책과 다르게 처리한 부분을 알린다.
5. 허락을 받은 뒤 `Nocedal/`과 `src/`에 넣고 push한다.
