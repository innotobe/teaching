# Stacks (Ch 6.1, 21쪽) — 수업 메모

## 슬라이드 오류 (원본 Goodrich 덱)
- **8쪽** 제목 "Performance and Limitations"인데 limitation 항목 없음 (Java판 고정배열 내용을 지우고 제목만 남김).
- **10쪽** `matching ')', '}', or '['` → 마지막은 `']'`.
- **10쪽** "correct: ((( )(( )){([( )])}" 는 correct 아님 → `(` 2개 남음. 학생에게 손으로 stack trace 시켜 찾게 하기 좋음 (`return S.is_empty()`가 왜 필요한지로 연결).
- **11쪽** `S.is_empty()`와 `S.isEmpty()` 혼재 (Java 흔적).
- **15–17쪽** `valStk.size()`, `isNumber`, 줄 끝 `;` — Java 흔적.
- **18쪽** span 정의 off-by-one: 예시 S=[1,1,2,3,1]은 X[i] 자신을 포함 → 정의에 "including X[i] itself" 필요. "an an array" 오타.
- **20쪽** "push x" → `i`. **21쪽** "exactly one" → `once`.
- 남겨둘 오류 vs 고칠 오류: 10쪽 correct 예시·18쪽 span은 발견 유도용으로 남길 만함. 오타류는 고칠 것. 수업 후 올리는 자료는 고친 버전.

## 짚을 포인트
- **8쪽 amortized**: push(`append`)는 배열이 차면 O(n) 복사 → amortized O(1). 빼면 틀린 문장. (CPython은 pop에서 shrink도 함)
- **6–7쪽 "array-based"**: Python list = dynamic array. 그림의 변수 `t`는 Python 코드에서 `len(self._data) − 1`.
- **15–17쪽 expression evaluation**: 괄호 처리 없음 → 괄호는 숙제.
  - 괄호 규칙: `(`는 바로 push, `)`면 `(`까지 doOp 후 `(` 버림, `prec('(') = −1`.
  - `≤` vs `<`: `≤`는 left-assoc (8−3−2=3), `<`로 바꾸면 right-assoc.
  - 실물 계산기 `2 + 3 × 4` = 20 vs 14로 시작하면 좋음.

## 데모
- `two_stack_evaluator.html` (괄호 없음), `two_stack_evaluator_parens.html` (괄호, 규칙 숨김 모드), `spans_stack.html`
