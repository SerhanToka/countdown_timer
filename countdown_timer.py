import time

chosen_time = int(input("Enter time in second/s: "))

for x in range(chosen_time, 0, -1): # or we could use reversed(range(0, chosen_time)) for reverse timer
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

time = f"{hours:02}:{minutes:02}:{seconds:02}"

print(f"Your {time} countdown is done!")