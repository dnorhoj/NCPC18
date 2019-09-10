#!/usr/bin/python3
import sys
target = int(input())
text = input().split()
if len(text) != target:
    print("something is fishy")
    sys.exit()
else:
    for i, num in enumerate(text):
        if not num in [str(i+1),"mumble"]:
            print("something is fishy")
            sys.exit()
print("makes sense")