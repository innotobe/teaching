# Trees (Ch 8, 19쪽) — 수업 메모

## 짚을 포인트
- **Tree도 Position 위에서 정의**: `root()`, `parent(p)`, `children(p)`. `LinkedBinaryTree`는 positional list와 같은 패턴 (`_Node`, `Position`, `_validate`, `_make_position`). "노드 필드만 parent/left/right로 바뀜".
- **replace(p, o)**: p 자리 원소를 o로 바꾸고 **원래 원소(old)를 반환**. 구조는 안 바뀜, O(1). delete/remove_min도 지운 원소 반환하는 같은 관례.
- **8쪽 ordered pair**: left/right 구분. 자식이 하나여도 왼쪽인지 오른쪽인지 다른 트리. 수식 트리(a−b vs b−a), BST가 여기에 의존.
- **proper binary tree 성질 증명**:
  - e = i + 1: 간선 수를 두 번 세기. root 빼고 각 노드에 부모 간선 1개 → n−1. internal마다 자식 2 → 2i. 2i = n−1 = e+i−1.
  - n = 2e − 1: n = e + i에 대입.
  - 칠판용: 노드 1개(e=1, i=0)에서 external 하나에 자식 둘 붙이기를 반복 → i, e가 같이 1씩 증가, 차이 1 유지.
- **inorder 그리기의 x(v), y(v)**: 화면 좌표. x = inorder 순번(가로), y = depth(세로). inorder라서 왼쪽 subtree는 전부 v보다 왼쪽 → 겹치지 않음.
- 순회(`positions()`, `preorder()` 등)가 `yield`로 짜여 있음 → yield를 여기서 자세히.

## 왜 순회가 세 가지인가 (이 단원의 핵심 질문)
노드를 자식보다 **먼저** 처리해야 하느냐, **나중에** 처리해야 하느냐가 문제마다 다르기 때문.
- **Preorder (부모 → 자식)**: 자식 처리에 부모 정보가 먼저 필요. 목차/폴더 들여쓰기 출력, depth 계산, 트리 복사.
- **Postorder (자식 → 부모)**: 부모의 답이 자식들의 답으로 정해짐. 폴더 용량 합계, height, 수식 트리 계산, 트리 삭제.
- **Inorder (왼쪽 → 부모 → 오른쪽)**: binary tree에서 좌우 순서가 의미 있을 때. BST 정렬 출력, 중위 수식 출력, 트리 그리기 x좌표.

수식 트리 `(2 + 3) * 4` 하나로 시연:
- preorder `* + 2 3 4` (prefix)
- inorder `2 + 3 * 4` (괄호 붙이면 원래 식)
- postorder `2 3 + 4 *` (postfix — stack 단원 수식 계산과 연결)

**Euler tour = 세 순회를 합친 것**: 트리 바깥을 한 바퀴 돌며 각 노드를 왼쪽(pre), 아래(in), 오른쪽(post) 세 번 지남. 세 순회는 그중 한 시점만 쓰는 특수 경우.
예: 괄호 친 수식 출력 — 왼쪽 `(`, 아래 값, 오른쪽 `)` → `((2 + 3) * 4)`. inorder만 쓰면 괄호가 사라져 `2 + 3 * 4`가 되는 문제를 해결.

## 슬라이드 오류
- **8쪽 recursive definition**: "single node이거나, root가 ordered pair of children을 갖고 각각이 binary tree" → 자식 0개 또는 2개만 나옴 = proper binary tree 정의. 위의 "at most two"와 모순. 교재 본문은 empty tree를 허용해서 자식 하나 = 한쪽 subtree가 empty.
  퀴즈: "이 정의로 자식이 하나인 노드를 만들 수 있나?"
