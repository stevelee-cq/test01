import tkinter as tk

def handle_selection(*args):
    selected_option = dropdown_var.get()
    print("选择了选项:", selected_option)

root = tk.Tk()

options = ["选项 1", "选项 2", "选项 3"]
dropdown_var = tk.StringVar(root)
dropdown_var.set("请选择一个选项")  # 设置默认文字

menu = tk.OptionMenu(root, dropdown_var, *options, command=handle_selection)
menu.pack()

root.mainloop()
