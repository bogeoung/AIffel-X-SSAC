from collections import deque
class MyCircularDeque:
    def __init__(self, k: int):
        # 데크사이즈를 k로 지정하는 생성자별
        self.k = k
        # 이 ListNode가 뭘까..
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.right = self.tail
        self.tail.left = self.head
        self.len = 0

    def _add(self,node:ListNode, new:ListNode):
        # node의 right와 new를 연결
        n = node.right
        node.right = new
        new.left = node
        new.right = n
        n.left = new

    def _del(self, node:ListNode):
        # node.right를 지움.
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        # 데크 처음에 아이템을 추가하고 성공할 경우 true 리턴
        # deque가 꽉차있으 false 리턴
        if self.len == self.k:
            return False
        # 새노드를 추가했으므로, 노드의 개수를 1개 추가
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        # 데크 마지막에 아이템을 추가하고 성공할 경우 true 리턴
        if self.len == self.k:
            return False
        self.len += 1
        # 이 때 self.tail이 아닌 이유 -> self.tail이 들어가면 self.tail.right과 new ListNode가 연결되기 때문
        # 따라서 self.tail의 이전에 연결하고 싶기 때문에, self.tail.left가 들어감.
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        # 데크 처음에 아이템을 삭제하고 성공할 경우 true 리턴면
        # 데크가 비어있으면 False 리턴
        if self.len == 0:
            return False
        self.len -= 1
        # 제일 처음 노드는 self.head.right임. 따라서 self.head를 넣음.
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        # 데크 마지막에 아이템을 삭제하고 성공할 경우 true 리턴
        if self.len == 0:
            return False
        self.len -= 1
        # _del 메소드는 입력된 노드의 right를 지우는 메소드이기 때문에 tail.left.left를 넣음.
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        # 데크의 첫 번째 아이템을 가져옴. 데크가 비어있으면 -1 리턴
        if self.len == 0:
            return -1
        else:
            return self.head.right.val

    def getRear(self) -> int:
        # 데크의 마지막 아이템을 가져옴. 데크가 비어있으면 -1 리턴
        if self.len == 0:
            return -1
        else:
            return self.tail.left.val

    def isEmpty(self) -> bool:
        # 데크가 비어 있는지 여부를 판별
        return self.len == 0

    def isFull(self) -> bool:
        # 데크가 가득 차 있는지 여부를 판별
        return self.len == self.k

# You MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()