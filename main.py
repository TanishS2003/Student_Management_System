import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.state('zoomed')

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=(
            "times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ===============Manage Frame========================
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=620)

        m_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white", font=(
            "times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=18)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=12, padx=20, sticky='w')

        txt_roll = Entry(Manage_Frame, textvariable=self.roll_no_var, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=12, padx=20, sticky='w')

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        lbl_email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=12, padx=20, sticky='w')

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=12, padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=(
            "times new roman", 14, "bold"), state='readonly')
        combo_gender['values'] = ('Male', 'Female', 'Other')
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=12, padx=20, sticky='w')

        dt = date.today()
        dob_cal = DateEntry(Manage_Frame, selectmode='day', date_pattern="dd/MM/yyyy",
                            textvariable=self.dob_var, maxdate=dt, font=("", 11, "bold"),  disableddaybackground="red", disableddayforeground="black", normalbackground="white", weekendbackground="white", othermonthbackground="white")
        dob_cal.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=12, padx=20, sticky='w')

        self.txt_address = Text(Manage_Frame, width=30, height=4,
                                font=("times new roman", 12, "bold"))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        # ===============Button Frame========================
        Button_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        Button_Frame.place(x=15, y=550, width=420)

        add_button = Button(Button_Frame, text="Add",
                            command=self.add_students, width=10, height=2)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        update_button = Button(
            Button_Frame, command=self.update, text="Update", width=10, height=2)
        update_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = Button(
            Button_Frame, command=self.delete, text="Delete", width=10, height=2)
        delete_button.grid(row=0, column=2, padx=10, pady=5)

        clear_button = Button(Button_Frame, command=self.clear,
                              text="Clear", width=10, height=2)
        clear_button.grid(row=0, column=3, padx=10, pady=5)

        # ===============Detail Frame========================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=840, height=620)

        lbl_search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white", font=(
            "times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=(
            "times new roman", 14, "bold"), state='readonly', width=10)
        combo_search['values'] = ('Roll_No', 'Name', 'Contact')
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        search_button = Button(
            Detail_Frame, command=self.search_data, text="Search", width=10)
        search_button.grid(row=0, column=3, padx=10, pady=10)

        show_button = Button(
            Detail_Frame, command=self.fetch_data, text="Show All", width=10)
        show_button.grid(row=0, column=4, padx=10, pady=10)

        # ===============Table Frame========================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=800, height=530)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender",
                                                                "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")

        self.student_table['show'] = 'headings'

        self.student_table.column("roll", width=80)
        self.student_table.column("name", width=120)
        self.student_table.column("email", width=120)
        self.student_table.column("gender", width=80)
        self.student_table.column("contact", width=120)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=300)

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.roll_no_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or self.gender_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "" or self.txt_address.get('1.0', END) == "":
            messagebox.showerror("Error", "All the fields are required!")
        else:
            con = pymysql.connect(host="localhost", user='root',
                                  password='', database='sms')
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (
                self.roll_no_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0', END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Student Added Successfully!")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user='root',
                              password='', database='sms')
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

    def update(self):
        if self.roll_no_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or self.gender_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "" or self.txt_address.get('1.0', END) == "":
            messagebox.showerror("Error", "No  Student Selected!")
        else:
            con = pymysql.connect(host="localhost", user='root',
                                  password='', database='sms')
            cur = con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (

                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0', END),
                self.roll_no_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo(
                "Success", "Student Details Updated Successfully!")

    def delete(self):
        if self.roll_no_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or self.gender_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "" or self.txt_address.get('1.0', END) == "":
            messagebox.showerror("Error", "No  Student Selected!")
        else:

            con = pymysql.connect(host="localhost", user='root',
                                  password='', database='sms')
            cur = con.cursor()
            cur.execute("delete from students where roll_no=%s",
                        self.roll_no_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Student Deleted Successfully!")

    def search_data(self):
        con = pymysql.connect(host="localhost", user='root',
                              password='', database='sms')
        cur = con.cursor()
        cur.execute("select * from students where " +
                    str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()
