import tkinter as tk
from math import sqrt


def calculate_parameters():
    # 获取输入的值
    density = float(density_entry.get())
    velocity = float(velocity_entry.get())
    area = float(area_entry.get())
    temperature = float(temperature_entry.get())
    length = float(length_entry.get())
    viscosity = float(viscosity_entry.get())

    # 计算空气动力学公式参数
    dynamic_pressure = 0.5 * density * velocity ** 2
    mach_number = velocity / sqrt(1.4 * 287 * temperature)
    reynolds_number = (density * velocity * length) / viscosity

    # 显示结果
    dynamic_pressure_label.config(text="Dynamic Pressure: {:.2f}".format(dynamic_pressure))
    mach_number_label.config(text="Mach Number: {:.2f}".format(mach_number))
    reynolds_number_label.config(text="Reynolds Number: {:.2f}".format(reynolds_number))


# 创建主窗口
window = tk.Tk()
window.title("Air Dynamics Parameters Calculator")

# 创建标签和输入框
density_label = tk.Label(window, text="Density (kg/m^3):")
density_label.pack()
density_entry = tk.Entry(window)
density_entry.pack()

velocity_label = tk.Label(window, text="Velocity (m/s):")
velocity_label.pack()
velocity_entry = tk.Entry(window)
velocity_entry.pack()

area_label = tk.Label(window, text="Area (m^2):")
area_label.pack()
area_entry = tk.Entry(window)
area_entry.pack()

temperature_label = tk.Label(window, text="Temperature (°C):")
temperature_label.pack()
temperature_entry = tk.Entry(window)
temperature_entry.pack()

length_label = tk.Label(window, text="Length (m):")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

viscosity_label = tk.Label(window, text="Viscosity (Pa·s):")
viscosity_label.pack()
viscosity_entry = tk.Entry(window)
viscosity_entry.pack()

# 创建计算按钮
calculate_button = tk.Button(window, text="Calculate", command=calculate_parameters)
calculate_button.pack()

# 创建用于显示结果的标签
dynamic_pressure_label = tk.Label(window, text="Dynamic Pressure:")
dynamic_pressure_label.pack()

mach_number_label = tk.Label(window, text="Mach Number:")
mach_number_label.pack()

reynolds_number_label = tk.Label(window, text="Reynolds Number:")
reynolds_number_label.pack()

# 运行主循环
window.mainloop()
