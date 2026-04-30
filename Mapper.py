import sys

for line in sys.stdin:
    ts, user = line.strip().split("|")
    print(f"{user}\t{ts}")