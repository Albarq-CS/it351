import random
import time

MIN_WATER_LEVEL = 30

for i in range(10):
    water_level = random.randint(0, 100)
    print(f"Reading {i+1}: Water level = {water_level} liters")
    if water_level < MIN_WATER_LEVEL:
        print(" ALERT: Water level is too low!")
    time.sleep(1)
