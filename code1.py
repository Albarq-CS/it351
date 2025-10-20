import random
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Sensor ID", "Temperature (°C)", "Humidity (%)"]

for sensor_id in range(1, 6):
    temperature = round(random.uniform(15, 40), 2)
    humidity = round(random.uniform(20, 90), 2)
    table.add_row([f"Sensor {sensor_id}", temperature, humidity])

print(" Random IoT Sensor Readings:\n")
print(table)
