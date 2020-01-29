from collections import deque
queue =deque( ["ram","sat","kasif"])
print (queue)
queue.append("ana")
print(queue)
queue.popleft()
print(queue)