#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if j >= 2:
            print(end=", ")
        print(f"{i}{j}".format(i, j), end="")
print()
