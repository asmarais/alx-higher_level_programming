#!/usr/bin/python3
for i in range(8):
    for j in range(10):
        if i > j or i == j:
            continue
        print(f"{i:d}{j:d}", end=', ')
print(f"{89}")
