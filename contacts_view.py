from tkinter import  *
from tkinter import ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *


contact_list = read_from_file("contact.dat")

def load_data(contact_list):
    contact_list = read_from_file("contact.dat")
    for row in table.get_children():
        table.delete(row)

    for contact in contact_list:
        table.insert("", END, values=contact)


def reset_form():
    id.set(len(contact_list) + 1)
    name.set("")
    family.set("")
    phone_number.set("")
    address.set("")
    title.set("")
    load_data(contact_list)


def save_btn_click():
    person = (id.get(), name.get(), family.get(), phone_number.get(), address.get(), title.get())
    errors = contact_validator(person)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Person saved")
        contact_list.append(person)
        write_to_file("contact.dat", contact_list)
        reset_form()


def table_select(x):
    selected_contact = table.item(table.focus())["values"]
    if selected_contact:
        id.set(selected_contact[0])
        name.set(selected_contact[1])
        family.set(selected_contact[2])
        phone_number.set(selected_contact[3])
        address.set(selected_contact[4])
        title.set(selected_contact[5])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


#appearance
window = Tk()
window.title('contacts')
window.geometry('1050x400')


#id
Label(window,text='id').place(x=30,y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=100, y=20)

#name
Label(window,text='Name').place(x=30,y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=60)

#family
Label(window,text='Family').place(x=30,y=100)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=100)

#number
Label(window,text='phone no').place(x=30,y=140)
phone_number=StringVar()
Entry(window,textvariable=phone_number).place(x=100,y=140)

#address
Label(window,text='address').place(x=30,y=180)
address=StringVar()
Entry(window,textvariable=address).place(x=100,y=180)

#title
Label(window,text='title').place(x=30,y=220)
title=StringVar()
Entry(window,textvariable=title).place(x=100,y=220)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.place(x=300, y=20)


table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="number")
table.heading(5, text="address")
table.heading(6, text="title")



table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=130)
table.column(5, width=200)
table.column(6, width=100)

table.bind("<<TreeviewSelect>>", table_select)



Button(window, text="Save", width=6, command=save_btn_click).place(x=70, y=320)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=137, y=320)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=207, y=320)
Button(window, text="Clear", width=6, command=reset_form).place(x=70, y=280, width=190)



window.mainloop()





