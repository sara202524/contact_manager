from tkinter import  *
from tkinter import ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *



contact_list = read_from_file("contact.dat")



def load_data(contact_list):
    contact_list = read_from_file("contacts.dat")
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
    errors = contact_validator(contact)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Person saved")
        contact_list.append(contact)
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
        title_number.set(selected_contact[5])


def edit_btn_click():
    pass


def remove_btn_click():
    pass





#appearance

contacts=Tk()
contacts.title('contacts')
contacts.geometry('1050x400')

#id
Label(contacts,text='id').place(x=80,y=20)
id = IntVar(value=1)
Entry(contacts, textvariable=id, state="readonly").place(x=100, y=20)

#name
Label(contacts,text='Name').place(x=60,y=60)
name = StringVar()
Entry(contacts, textvariable=name).place(x=100, y=60)

#family
Label(contacts,text='Family').place(x=50,y=100)
family = StringVar()
Entry(contacts, textvariable=family).place(x=100, y=100)

#number
Label(contacts,text='phone number').place(x=10,y=140)
phone_number=StringVar()
Entry(contacts,textvariable=phone_number).place(x=100,y=140)

#address
Label(contacts,text='address').place(x=50,y=180)
address=StringVar()
Entry(contacts,textvariable=address).place(x=100,y=180)

#title
Label(contacts,text='title').place(x=70,y=220)
title=StringVar()
Entry(contacts,textvariable=title).place(x=100,y=220)

table = ttk.Treeview(contacts, columns=[1, 2, 3, 4, 5, 6], show="headings")
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

# table.bind("<<TreeviewSelect>>", table_select)

table.place(x=300, y=20)



Button(contacts, text="Save", width=6, command=save_btn_click).place(x=20, y=220)
Button(contacts, text="Edit", width=6, command=edit_btn_click).place(x=90, y=220)
Button(contacts, text="Remove", width=6, command=remove_btn_click).place(x=160, y=220)
Button(contacts, text="Clear", width=6, command=reset_form).place(x=20, y=180, width=190)

reset_form()






















contacts.mainloop()



