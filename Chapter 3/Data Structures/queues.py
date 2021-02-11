from collections import deque  # import deque class from collections module
queue = deque([])  # wrap empty list it in a deque object
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # removes first item in a queue
print(queue)
if not queue:
    print("empty")
