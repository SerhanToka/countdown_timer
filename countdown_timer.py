import time

choosen_time = int(input("Enter time: "))

for x in range(chosen_time, 0, -1): # or we could use reversed(range(0, choosen_time)) for reverse timer
    seconds = x % 60
    minutes = int(x / 60) % 60
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

print(f"Your {choosen_time} second/s countdown is done!")