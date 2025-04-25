import numpy as np

def calculate_power_consumption(power_sheets):
    total_power = 0
    for sheet in power_sheets:
        power = np.array(sheet).sum()
        total_power += power
    return total_power / len(power_sheets)

power_sheets = [
    [25, 40, 60],
    [15, 30, 50],
    [10, 20, 30]
]

result = calculate_power_consumption(power_sheets)
print("Total power consumption:", result)
