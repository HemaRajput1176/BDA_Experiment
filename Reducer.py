import sys
from datetime import datetime

current_user = None
prev_time = None
session = 1

for line in sys.stdin:
    user, ts = line.strip().split("\t")
    ts = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

    if user == current_user:
        gap = (ts - prev_time).total_seconds() / 60
        if gap > 30:
            session += 1
    else:
        session = 1

    print(f"User:{user} | Session:{session} | Time:{ts}")

    current_user = user
    prev_time = ts