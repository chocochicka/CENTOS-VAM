import time

start_time = time.time()
end_time = start_time + 60  # 60 seconds = 1 minute

while time.time() < end_time:
    print("Hello World")
    time.sleep(15)
