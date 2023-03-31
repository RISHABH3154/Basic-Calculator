# from tkinter import *
# from PIL import Image, ImageDraw, ImageFont, ImageTk
#
#
# def hi():
#     print("Hello Rishabh calculator")
#
# # def flash():
#
# rishabh_root = Tk()
# rishabh_root.title("Rishabh's Calculator")
# rishabh_root.geometry("300x550")
# rishabh_root.minsize(200, 200)
# rishabh_root.maxsize(800, 700)
#
# photo = Image.open('jp logo.png')
# img = photo.resize((40, 40))
# my_img = ImageTk.PhotoImage(img)
# Label(rishabh_root, image=my_img).pack(fill=X)
#
# Label(rishabh_root, text="Welcome to the new calculator", font=("3t1f", 12, "bold"), bg="grey", fg="white", padx=10, pady=10, borderwidth=20,relief=SUNKEN).pack(side="top", fill=X)
#
# f1 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# f1.pack(side=LEFT, pady=4)
# f2 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# f2.pack(side=LEFT)
# # f3 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# # f3.pack(side=LEFT)
# # f4 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# # f4.pack(side=LEFT)
# # f5 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# # f5.pack(side=LEFT)
# # f6 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# # f6.pack(side=LEFT)
# # f7 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# # f7.pack(side=LEFT)
# # f8 = Frame(rishabh_root, bg="red", borderwidth=10, relief=RIDGE)
# # f8.pack(side=LEFT)
# # f9 = Frame(rishabh_root, bg="grey", borderwidth=10, relief=RIDGE)
# # f9.pack(side=LEFT)
#
# B1 = Button()
# B1 = Button(f1, text="1", fg="red", command=hi)
# B1.pack(pady=5, padx=12)
# B2 = Button(f2, text="2", fg="red", bd=6, activebackground="pink", highlightcolor="red")
# B2.pack(pady=5, padx=12)
# # B3 = Button(f3, text="3", fg="red")
# # B3.pack(pady=5, padx=12)
# # B4 = Button(f4, text="4", fg="red")
# # B4.pack(pady=5, padx=12)
# # B5 = Button(f5, text="5", fg="red")
# # B5.pack(pady=5, padx=12)
# # B6 = Button(f6, text="6", fg="red")
# # B6.pack(pady=5, padx=12)
# # B7 = Button(f7, text="7", fg="red")
# # B7.pack(pady=5, padx=12)
# # B8 = Button(f8, text="8", fg="red")
# # B8.pack(pady=5, padx=12)
# # B9 = Button(f9, text="9", fg="red")
# # B9.pack(pady=5, padx=12)
#
#
# f3 = Frame(rishabh_root, bg="red")
# f3.pack()
# l2 = Label(f3, text="Hello", borderwidth=2)
# l2.pack()
# rishabh_root.mainloop()
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create display widget
        self.display = tk.Entry(self.master, width=25, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4)

        # Create buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)
        self.create_button("C", 4, 0)
        self.create_button("=", 4, 2)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 12), command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

