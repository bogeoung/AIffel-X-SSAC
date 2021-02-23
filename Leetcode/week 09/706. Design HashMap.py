class MyHashMap:

    def __init__(self):
        self.myhash = dict()

    def put(self, key: int, value: int) -> None:
        # 키, 값을 해시맵에 삽입함. 만약 이미 존재하는 키라면 업데이트 함.
        # 키 값이 존재하는지 확인
        # 둘이 뭐가 다른지 잘 이해가 안감...
        if key in self.myhash:
            self.myhash[key] = value
        else:
            self.myhash[key] = value

    def get(self, key: int) -> int:
        # 키에 해당하는 값을 조회함. 만약 키가 존재하지 않는다면 -1을 리턴
        if key in self.myhash:
            return self.myhash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        # 키에 해당하는 키, 값을 해시맵에서 삭제함.
        if key in self.myhash:
            del self.myhash[key]
        else:
            return


# Your MyHashMap object will be instantiated and called as such:
# hashMap = MyHashMap()
# hashMap.put(1,1)
# hashMap.put(2,2)
# hashMap.get(1)
# hashMap.get(3)
# hashMap.put(2,1)
# hashMap.get(2)
# hashMap.remove(2)
# hashMap.get(2)