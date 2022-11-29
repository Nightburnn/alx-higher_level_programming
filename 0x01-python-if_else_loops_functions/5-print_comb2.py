#!/usr/bin/python3
# printing 0 to 99
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
        continue
        print("{:02}, ".format(num), end="")
