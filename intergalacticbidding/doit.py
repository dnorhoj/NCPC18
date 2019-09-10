#!/usr/bin/python3
import sys
import itertools

icpc_number = None
participants = {}

for i, line in enumerate(sys.stdin):
    stdin = line.split()
    if i == 0:
        icpc_number = int(stdin[1])
        continue

    if int(stdin[1]) <= icpc_number:
        participants[stdin[0]] = int(stdin[1])

for i in range(1, len(participants)+1):
    for combination in itertools.combinations(participants,i):
        vals = [participants.get(key) for key in combination]
        if sum(vals) == icpc_number:
            print(len(combination))
            for name in combination:
                print(name)
            sys.exit()
            
print("0")