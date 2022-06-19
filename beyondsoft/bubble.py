#! /usr/local/opt/python@3.8/bin/python3
li = [1, 4, 7, 2, 5, 8]
length = len(li)
for i in range(length - 1):
    for j in range(length - 1 - i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
print(li)
