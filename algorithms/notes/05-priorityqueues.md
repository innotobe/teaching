# Priority Queues (Ch 9.1–9.2) — 수업 메모

**권장 순서: DLL/Positional list 바로 다음, Tree 앞.** list 기반 PQ는 tree 몰라도 됨. 흐름: PQ(list로는 한쪽이 O(n)) → Tree → Heap(둘 다 O(log n)).

## 짚을 포인트
- **PQ는 ADT, Heap은 구현 중 하나** (stack을 array/linked로 구현한 것과 같은 관계).
  | 구현 | add | remove_min |
  |---|---|---|
  | unsorted list | O(1) | O(n) |
  | sorted list | O(n) | O(1) |
  | heap | O(log n) | O(log n) |
- **6쪽의 list = positional list(doubly linked)**. Python list로 바꾸면 sorted의 remove_min이 `pop(0)` → O(n). (내림차순 저장 후 `pop()`이면 O(1))
  sorted add는 둘 다 O(n)이지만 이유가 다름: linked는 자리 찾기 O(n), array는 binary search O(log n) + 밀어내기 O(n).
- **7–8쪽 코드**: `first()`, `after()`, `before()`, `add_after()`, `delete(p)` — positional list 복습 지점.

## 슬라이드 오류
- **10쪽 PQ-Sort 수도코드 Java 흔적**: `removeMin()`, `.key()`, comparator C, `S.remove_first()`(없는 메서드), `∅`.
  → 고친 이미지 `PQ-Sort.png`로 교체함. Python판:
  `e ← S.delete(S.first())`, `P.add(e, None)`, `(e, _) ← P.remove_min()`, `S.add_last(e)`.
- **PQ-Sort = 구현에 따라 다른 정렬**: unsorted → selection sort, sorted → insertion sort, heap → heap sort.

## 인문학 연결 (5분)
- 순서 규칙 = 정의관: FIFO(절차적 공정), 짧은 것 먼저(공리주의, 평균 최소), 오래 기다린 사람 먼저(Rawls maximin), 위급도(필요).
- α-fairness (Mo & Walrand, 2000): α=0 총합, α=1 proportional, α→∞ max-min. (모정훈 교수님)
