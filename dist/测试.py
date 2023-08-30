import tkinter as tk

def get_input_text():
    xiaofei_num_str = entry_expense.get()
    print(xiaofei_num_str)

root = tk.Tk()

frame_input_expense = tk.Frame(root)
frame_input_expense.pack()

entry_expense = tk.Entry(frame_input_expense, width=10)
entry_expense.grid(row=0, column=1)

button_get_input = tk.Button(root, text="获取输入", command=get_input_text)
button_get_input.pack()

root.mainloop()
