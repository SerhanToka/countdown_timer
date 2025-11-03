import time

choosen_time = int(input("Enter time in seconds: "))

for x in range(0, choosen_time):
    print(x)
    time.sleep(1)

print(f"Your {choosen_time} second/s countdown is done!")