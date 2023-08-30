from tkinter02 import Tk, Menu

def show_menu(event):
    menubar.post(event.x_root, event.y_root)

root = Tk()

# 创建菜单栏对象
menubar = Menu(root)

# 创建子菜单对象
submenu = Menu(menubar, tearoff=False)
submenu.add_command(label="子菜单项1")
submenu.add_command(label="子菜单项2")

# 将子菜单添加到菜单栏
menubar.add_cascade(label="文件", menu=submenu)
# 绑定鼠标右键单击事件到主窗口
root.bind("<Button-3>", show_menu)

root.mainloop()
