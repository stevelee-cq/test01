import tkinter as tk
from tkinter import *
from tkinter import messagebox

name_str = "test"
xiaofei_num_str=1.58
def add_expense():
    expense = entry_expense.get()
    global xiaofei_num
    xiaofei_num_str = entry_expense.get()
    xiaofei_num = float(xiaofei_num_str)
    print(f"数值为：{xiaofei_num}")
    if expense.isdigit():
        listbox_expenses.insert(tk.END, "支出：" + expense)
        entry_expense.delete(0, tk.END)
        #上面已经把 entry_expense中暂存的文本内容删去了
    else:
        messagebox.showerror("错误", "请输入有效的数字！")
    get_input_text()


def get_input_text():
    xiaofei_num_str = entry_expense.get()
    print(xiaofei_num_str)

def add_income():
    income = entry_income.get()
    if income.isdigit():
        listbox_expenses.insert(tk.END, "收入：" + income)
        entry_income.delete(0, tk.END)
    else:
        messagebox.showerror("错误", "请输入有效的数字！")


def add_transfer():
    transfer = entry_transfer.get()
    if transfer.isdigit():
        listbox_expenses.insert(tk.END, "转账：" + transfer)
        entry_transfer.delete(0, tk.END)
    else:
        messagebox.showerror("错误", "请输入有效的数字！")


def delete_expense():
    try:
        index = listbox_expenses.curselection()
        listbox_expenses.delete(index)
    except:
        pass


def handle_selection(*args):
    selected_option = dropdown_var.get()
    global name_str
    name_str = selected_option
    print(f"你这笔款项的资金流向是：{name_str}")
    print("选择了选项:", selected_option)
def calculate_total():
    expenses = []
    incomes = []
    transfers = []

    for item in listbox_expenses.get(0, tk.END):
        if item.startswith("支出："):
            expenses.append(int(item[4:]))
        elif item.startswith("收入："):
            incomes.append(int(item[4:]))
        elif item.startswith("转账："):
            transfers.append(int(item[4:]))

    total_expenses = sum(expenses)
    total_incomes = sum(incomes)
    total_transfers = sum(transfers)

    messagebox.showinfo("总支出", "总支出金额为：" + str(total_expenses))
    messagebox.showinfo("总收入", "总收入金额为：" + str(total_incomes))
    messagebox.showinfo("总转账", "总转账金额为：" + str(total_transfers))


root = Tk()
root.title("记账本")
menubar=Menu(root)
for item in ['文件','编辑','视图','关于']:
    menubar.add_command(label=item)

root['menu']=menubar
label_title = tk.Label(root, text="日常收支消费记账本", font=("Helvetica", 16))
label_title.pack(pady=(10, 5))


frame_input_expense = tk.Frame(root)
frame_input_expense.pack(pady=(0, 5))
#填入消费金额，浮点型，对应数据库里面的float
label_expense = tk.Label(frame_input_expense, text="消费金额：")
label_expense.grid(row=0, column=0)
entry_expense = tk.Entry(frame_input_expense, width=10)
entry_expense.grid(row=0, column=1)





print("测试哨兵出现")  # 输出转换后的消费金额



button_add_expense = tk.Button(frame_input_expense, text="添加支出", command=add_expense)
button_add_expense.grid(row=0, column=2, padx=5)
#选择资金流向，有学校、网站购物、家人、其它四大类，对应数据库里面的name列
#上述的四大类型
selected_value = tk.StringVar()
options = ["学校", "购物网站", "家人","其它"]
#要用字符串变量存储上面几个选项，已为mysql中插入name用
dropdown_var = tk.StringVar(root)
dropdown_var.set("资金流向")  # 设置默认文字
menu = tk.OptionMenu(frame_input_expense, dropdown_var, *options, command=handle_selection)
menu.grid(row=0, column=4)


#添加收入部分
frame_input_income = tk.Frame(root)
frame_input_income.pack(pady=(0, 5))

label_income = tk.Label(frame_input_income, text="收入金额：")
label_income.grid(row=0, column=0)

entry_income = tk.Entry(frame_input_income, width=10)
entry_income.grid(row=0, column=1)

button_add_income = tk.Button(frame_input_income, text="添加收入", command=add_income)
button_add_income.grid(row=0, column=2, padx=5)

#添加转账金额部分，与前面两个部分一样，每个部分都要独立规划一个子框架tk.Frame（），用于容纳每个部分的组件
frame_input_transfer = tk.Frame(root)
frame_input_transfer.pack(pady=(0, 5))

label_transfer = tk.Label(frame_input_transfer, text="转账金额：")
label_transfer.grid(row=0, column=0)

entry_transfer = tk.Entry(frame_input_transfer, width=10)
entry_transfer.grid(row=0, column=1)

button_add_transfer = tk.Button(frame_input_transfer, text="添加转账", command=add_transfer)
button_add_transfer.grid(row=0, column=2, padx=5)

frame_listbox = tk.Frame(root)
frame_listbox.pack(fill=tk.BOTH, expand=True)

listbox_expenses = tk.Listbox(frame_listbox, width=20)
listbox_expenses.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_expenses = tk.Scrollbar(frame_listbox)
scrollbar_expenses.pack(side=tk.RIGHT, fill=tk.Y)

listbox_expenses.config(yscrollcommand=scrollbar_expenses.set)
scrollbar_expenses.config(command=listbox_expenses.yview)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=(5, 10))

button_delete = tk.Button(frame_buttons, text="删除", command=delete_expense)
button_delete.pack(side=tk.LEFT, padx=5)

button_total = tk.Button(frame_buttons, text="计算总支出", command=calculate_total)
button_total.pack(side=tk.LEFT, padx=5)

root.mainloop()

