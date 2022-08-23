#!/usr/bin/python3
for c in range(ord('a'), ord('z')+1):
    if c == q:
        continue;
    elif c == e:
        continue;
    else:
        print('{}'.format(chr(c)), end='')
