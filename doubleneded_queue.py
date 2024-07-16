from collections import deque

q=deque([10,20,30,40])
q.append(50)
q.appendleft(5)
print(q)
q.pop()
q.popleft()
print(q)
