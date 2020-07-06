from collections import deque

socialNetwork = {}
socialNetwork['you'] = ['Lily', 'Lucy', 'Ada']
socialNetwork['Lily'] = ['Hack']
socialNetwork['Lucy'] = ['Bob', 'Tom']
socialNetwork['Ada'] = []
socialNetwork['Hack'] = []
socialNetwork['Bob'] = []
socialNetwork['Tom'] = []


# 创建队列保存联系人
searchQueue = deque()
searchQueue += socialNetwork['you']
# 所有已经检查过的人
searched = []

while searchQueue:
    person = searchQueue.popleft()
    if 'm' in person:
        print(person + " is a mango seller!")
    elif person not in searched:
        searchQueue += socialNetwork[person]
        searched += person
