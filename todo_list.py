from tkinter import *
from tkinter.font import Font

def delete_item():
    selected_index = lista.curselection()
    if selected_index:
        lista.delete(selected_index)
        checkbox_list[selected_index[0]].destroy()

def add_item():
    new_item = entry.get()
    if new_item:
        lista.insert(END, new_item)
        entry.delete(0, END)

        var = IntVar()
        c = Checkbutton(checkbox_frame, text=new_item, variable=var, bg="#3498db", fg="#ecf0f1", activebackground="#2980b9", activeforeground="#ecf0f1", selectcolor="#3498db")
        c.pack(side=TOP)
        checkbox_list.append(c)

def cross_off_item():
    selected_index = lista.curselection()
    if selected_index:
        checkbox_list[selected_index[0]].config(font=Font(size=10, overstrike=True))

def uncross_item():
    selected_index = lista.curselection()
    if selected_index:
        checkbox_list[selected_index[0]].config(font=Font(size=10, overstrike=False))

root = Tk()
root.title("Todo list")
root.geometry("650x500")
root.configure(bg="#2c3e50")

font = Font(family="Helvetica", size=30, weight="bold")

frame = Frame(root, bg="#2c3e50")
frame.pack(pady=10)

lista = Listbox(frame,
                font=font,
                width=35,
                height=5,
                bg="#34495e", 
                bd=0,
                fg="#ecf0f1", 
                highlightthickness=0,
                selectbackground="#2980b9",
                activestyle="none")
lista.pack(side=LEFT, fill=BOTH)

stuff = ["Zrobic zadania z pythona", "Zdac sesje", "Zrobic zadanie domowe", "Pojsc na uczelnie", "Nie sciagac"]
checkbox_frame = Frame(root, bg="#2c3e50")
checkbox_frame.pack()

checkbox_list = []

for item in stuff:
    lista.insert(END, item)
    var = IntVar()
    c = Checkbutton(checkbox_frame, text=item, variable=var, bg="#3498db", fg="#ecf0f1", activebackground="#2980b9", activeforeground="#ecf0f1", selectcolor="#3498db")
    c.pack(side=TOP)
    checkbox_list.append(c)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

lista.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista.yview)

entry = Entry(root, font=("Helvetica", 24), bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1", relief=FLAT) 
entry.pack(pady=20)

button_frame = Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)

delete_button = Button(button_frame, text="Delete Item", command=delete_item, bg="#e74c3c", fg="black", activebackground="#c0392b", relief=FLAT)  # Button customization
add_button = Button(button_frame, text="Add Item", command=add_item, bg="#2ecc71", fg="black", activebackground="#27ae60", relief=FLAT)  # Button customization
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item, bg="#e67e22", fg="black", activebackground="#d35400", relief=FLAT)  # Button customization
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item, bg="#3498db", fg="black", activebackground="#2980b9", relief=FLAT)  # Button customization

delete_button.grid(row=0, column=0, padx=10)
add_button.grid(row=0, column=1, padx=10)
cross_off_button.grid(row=0, column=2, padx=10)
uncross_button.grid(row=0, column=3, padx=10)

root.mainloop()
