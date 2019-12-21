class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v, stack = {0}, rooms[0]

        while stack:
            key = stack.pop()
            if key not in v:
                v.add(key)
                for i in rooms[key]:
                    if i not in v: stack.append(i)
        return True if len(rooms) == len(v) else False