# Linked Lists (Ch 7.1, 11쪽) — 수업 메모

## 슬라이드 오류
- **3쪽 Node class가 Java 코드 그대로** (`public`, `private`, `;`, getter/setter, 생성자 2개). 닫는 `}`가 저작권 표시와 겹침.
  - "이거 Python 맞나?"로 시작해서 학생들과 Python으로 바꿔 보기.
  - Python판: `class _Node: __slots__ = '_element', '_next'` + `__init__(self, element, next)` 하나.

## 짚을 포인트
- **용어**: pointer 대신 reference, 말로는 **"가리킨다"**로 통일. "a에 list가 들어 있다"가 아니라 "a가 list를 가리킨다".
  ```python
  a = [1, 2]
  b = a
  b.append(3)
  a          # [1, 2, 3]
  a is b     # True
  ```
  C pointer와 하는 일은 같고, `*`/`&`/주소 계산/free/segfault는 없음. `None` = "아무것도 안 가리킴".
- **`__slots__`**: 객체마다 `__dict__`를 안 만들고 칸을 고정 → 메모리 절약 + 선언 안 한 속성 추가 불가.
  - 실측(Python 3.13, node 100만 개): 없음 88 MB vs 있음 48 MB.
  - 노드처럼 수가 많고 속성이 고정된 클래스에만 씀.
- **9쪽 LinkedStack**: push = `self._head = self._Node(e, self._head)` → "새 노드가 기존 head를 가리키고, head가 새 노드를 가리킨다".
