#!/usr/bin/python3
for i in range(97, 123):
    asciiWithoutQandE = chr(i)
    numberToAlpha = "" + asciiWithoutQandE
if i == 101 or i == 113:
    continue
    print("{}".format(numberToAlpha), end='')
