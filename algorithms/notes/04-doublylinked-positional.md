# Doubly Linked Lists / Positional List (Ch 7.3, 12쪽) — 수업 메모

작년엔 코드 건너뜀. 올해는 positional list까지 다룸 (PQ 7–8쪽 코드, Tree의 Position이 이걸 씀).
녹화 시: ① DLL 1–6쪽 15분 + ② Positional list 7–12쪽 20분.

## 핵심 개념
- **index vs position**: index는 "앞에서 몇 번째"라는 숫자, position은 그 원소의 노드를 가리키는 표식.
  앞에 끼워 넣으면 index가 가리키는 원소는 바뀌지만 position은 그대로.
- **access vs search**: position으로 그 노드에 **접근**하는 건 O(1) (`p.element()`). 값이 x인 노드를 **찾는** 건 O(n). "찾는다" 대신 "접근한다"로 말할 것.
- **왜 doubly인가**: position은 노드까지 O(1)로 데려다주고, `_prev`가 있어야 거기서 넣고 빼기가 O(1).
  singly면 `before`, `add_before`, `delete`가 O(n) (앞 노드를 head부터 찾아야 함). array면 밀어내기 O(n).
- **position = 주소를 감싼 handle**: 안에는 실제 메모리 주소(reference)가 있지만 주소처럼 다룰 수는 없음 (계산 불가, `element()`만 공개, 소속·유효성 검사). C의 `FILE *`와 비슷. → OOP의 encapsulation.

## 코드 짚을 곳 (10–12쪽)
- **Position 클래스**: `_container`, `_node` 두 칸. `__eq__`는 `other._node is self._node`로 비교.
- **`_validate(p)`** (`_container`는 여기서만 쓰임): ① Position 타입인가 ② 이 리스트 소속인가 ③ 지운 노드인가(`_next is None` 관례). 소속 검사가 없으면 B가 A의 노드를 지우고 두 `_size`가 모두 틀어짐.
- **`_make_position(node)`**: 노드를 새로 만드는 게 아니라, **이미 있는 노드를 감싼 Position 객체를 새로 만들어** 돌려줌. header/trailer면 None → `while walk is not None:`이 멈추는 이유.
  ```python
  p = L.first()
  q = L.first()
  p is q    # False (다른 Position 객체)
  p == q    # True  (같은 노드)
  ```
- 나머지 메서드는 전부 "`_validate`로 노드 꺼내고 → 작업 → `_make_position`으로 감싸 반환" 한 패턴.
- **`__iter__` + `yield`**: 이 덱에서 처음 등장 (앞 덱·MIT 6.0001 자료에 없음). "`for e in L:`이 되게 하는 함수, `yield`는 원소를 하나씩 내보냄" 정도로 짧게. 자세한 건 Tree 순회에서.

## 시연 3개
```python
L = PositionalList()
L.add_last('A')
p = L.add_last('B')
L.add_last('C')
L.add_first('X')
p.element()          # 'B'  ← index였다면 'A'

M = PositionalList()
M.delete(p)          # ValueError: p does not belong to this container
```
