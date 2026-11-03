# Queues (Ch 6.2, 12쪽) — 수업 메모

## 짚을 포인트
- **10쪽 ArrayQueue = ring buffer(circular array)**: `_front = (_front + 1) % len(_data)`.
- **밑줄 `_data`, `_front`, `_size`**: "내부용이니 건드리지 말라"는 관례(PEP 8). 강제 아님.
  - `__init__`, `__len__` (앞뒤 밑줄 둘) = special method(dunder). 내부용이 아니라 Python이 부르는 공개 인터페이스. 1학년이 셋을 혼동하기 쉬움.
- **깨 보기 시연** (invariant가 깨지면 에러 없이 틀린 값):
  ```python
  q = ArrayQueue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q._front = 2
  q.first()                          # 3 (정답은 1)
  [q.dequeue() for _ in range(3)]    # [3, None, None]
  len(q), q._data                    # 0, [1, 2, None, ...]  ← 1, 2는 영영 못 꺼냄
  ```
  `first()`는 `_size == 0`만 검사하고 `_front`가 맞는지는 검사 안 함.
- Python list로 queue를 만들면 `pop(0)`이 O(n) → 그래서 circular array.

## 수업 도입 (카페 사진)
- "이 사진에서 queue를 찾아보세요": 주문→제조 queue, 손님 줄(사진엔 없음 → queue는 규칙으로 정의됨), 함정으로 컵·빨대 = stack.
- "카페는 정말 FIFO인가?" 라떼(4분) 1잔 + 아메리카노(1분) 3잔: FIFO 평균 대기 5.5분 vs 짧은 것 먼저 3.25분 → priority queue로 연결.
- 확장: 사이렌오더, fast pass(starvation), 응급실, 수강신청 설계(선착순/학년/마일리지) → 공정성·정의 이야기 5분.
