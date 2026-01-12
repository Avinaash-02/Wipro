import time
timer = int(input("Enter the seconds For timer to drop: "))
while timer>=0:
    print(f'{timer}seconds left')
    timer -= 1
    time.sleep(0.9)
print("Time over !!")
