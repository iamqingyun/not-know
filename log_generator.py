import random
from datetime import datetime, timedelta

with open("build.log", "w") as f:
    start_time = datetime(2024, 3, 1)
    for i in range(1000):  # 生成1000行日志
        time = start_time + timedelta(minutes=i)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        if random.random() < 0.2:  # 20%错误率
            errors = ["ERROR_FILE_NOT_FOUND", "ERROR_PERMISSION_DENIED"]
            f.write(f"{timestamp} | BUILD_ID:{i} | STATUS:FAIL | CODE:{random.choice(errors)}\n")
        else:
            f.write(f"{timestamp} | BUILD_ID:{i} | STATUS:SUCCESS | DURATION:{random.randint(1,60)}s\n")