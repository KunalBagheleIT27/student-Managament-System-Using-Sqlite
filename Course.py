from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Courseclass:
      def __init__(self, root):
            self.root = root
            self.root.title("Student Result management System")
            self.root.geometry("1200x480+80+170")
            self.root.config(bg="white")
            self.root.focus_force()

            #=========title===================
            title = Label(self.root, text="Manage Course details ",
                          font=("goudy old style", 20, "bold"),
                          bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)

            #==============variable ==============
            self.var_course = StringVar()
            self.var_Duration = StringVar()
            self.var_Charges = StringVar()

            #============Widgets=====================
            lbl_course = Label(self.root, text=" Course Name ", font=("goudy old style", 15, "bold"), bg="white").place(x=15, y=60)
            lbl_Duration = Label(self.root, text=" Duration ", font=("goudy old style", 15, "bold"), bg="white").place(x=15, y=100)
            lbl_Charges = Label(self.root, text=" Charges ", font=("goudy old style", 15, "bold"), bg="white").place(x=15, y=140)
            lbl_Description = Label(self.root, text=" Description ", font=("goudy old style", 15, "bold"), bg="white").place(x=15, y=180)

            #==============Entry Fields===========
            self.txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg="AliceBlue")
            self.txt_course.place(x=150, y=60, width=200)
            txt_Duration = Entry(self.root, textvariable=self.var_Duration, font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=150, y=100, width=200)
            txt_Charges = Entry(self.root, textvariable=self.var_Charges, font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=150, y=140, width=200)
            self.txt_Description = Text(self.root, font=("goudy old style", 15, "bold"), bg="AliceBlue")
            self.txt_Description.place(x=150, y=180, width=500, height=200)

            #==================Buttons fields=============
            self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add)
            self.btn_add.place(x=150, y=400, width=110, height=40)
            
            self.btn_Update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.update)
            self.btn_Update.place(x=270, y=400, width=110, height=40)

            self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.delete)
            self.btn_delete.place(x=390, y=400, width=110, height=40)

            self.btn_Clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.clear)
            self.btn_Clear.place(x=510, y=400, width=110, height=40)

            #==============search panel=============
            self.Var_Search = StringVar()
            lbl_Serach_Coursename = Label(self.root, text="Course Name: ", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
            txt_Serach_Coursename = Entry(self.root, textvariable=self.Var_Search, font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=870, y=60, width=180)
            
            btn_Search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

            #=========content====================
            self.C_frame = Frame(self.root, border=2, relief=RIDGE, bg="AliceBlue")
            self.C_frame.place(x=720, y=100, width=470, height=340)

            #===Scrollbar=============
            scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
            scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)

            self.Coursetable = ttk.Treeview(self.C_frame, columns=("cid", "name", "duration", "charges", "Description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
            scrollx.pack(side=BOTTOM, fill=X)
            scrolly.pack(side=RIGHT, fill=Y)
            scrollx.config(command=self.Coursetable.xview)
            scrolly.config(command=self.Coursetable.yview)

            self.Coursetable.heading("cid", text="Course ID")
            self.Coursetable.heading("name", text=" Name")
            self.Coursetable.heading("duration", text="Duration")
            self.Coursetable.heading("charges", text="charges")
            self.Coursetable.heading("Description", text="Description")
            self.Coursetable["show"] = 'headings'

            self.Coursetable.column("cid", width=100)
            self.Coursetable.column("name", width=100)
            self.Coursetable.column("duration", width=100)
            self.Coursetable.column("charges", width=100)
            self.Coursetable.column("Description", width=150)

            self.Coursetable.pack(fill=BOTH, expand=1)
            self.Coursetable.bind("<ButtonRelease-1>", self.get_data)
            self.show()

#===============================================================

      def clear(self):
            self.show()
            self.var_course.set("")
            self.var_Duration.set("")
            self.var_Charges.set("")
            self.Var_Search.set("")
            self.txt_Description.delete('1.0', END)
            self.txt_course.config(state=NORMAL)

#================================================================

      def delete(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()

            try:
                  if self.var_course.get() == "":
                        messagebox.showerror("Error", "Course name is required", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
                        row = cursor.fetchone()
                        if row is None:
                              messagebox.showerror("Error", "Please select a course from the list", parent=self.root)
                        else:
                              op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                              if op == True:
                                    cursor.execute("DELETE FROM course WHERE name=?", (self.var_course.get(),))
                                    conn.commit()
                                    self.trigger_popup("Row deleted successfully")
                                    self.clear()

            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}")

#==============================================================================================================

      def get_data(self, ev):
            self.txt_course.config(state='readonly')
            r = self.Coursetable.focus()
            content = self.Coursetable.item(r)
            rows = content["values"]
            self.var_course.set(rows[1])
            self.var_Duration.set(rows[2])
            self.var_Charges.set(rows[3])
            self.txt_Description.delete('1.0', END)
            self.txt_Description.insert(END, rows[4])

#==============================================================================================================

      def add(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()

            try:
                  if self.var_course.get() == "":
                        messagebox.showerror("Error", "Course name is required", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
                        row = cursor.fetchone()
                        if row is not None:
                              messagebox.showerror("Error", "Course Name is already present", parent=self.root)
                        else:
                              cursor.execute("INSERT INTO course (name, duration, charges, Description) VALUES(?, ?, ?, ?)", (
                                    self.var_course.get(),
                                    self.var_Duration.get(),
                                    self.var_Charges.get(),
                                    self.txt_Description.get("1.0", END)
                              ))
                              conn.commit()
                              self.trigger_popup("Row submitted successfully")
                              self.show()

            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}")

#==============================================================================================================

      def update(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()

            try:
                  if self.var_course.get() == "":
                        messagebox.showerror("Error", "Course name is required", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
                        row = cursor.fetchone()
                        if row is None:
                              messagebox.showerror("Error", "Select Course Name from the List", parent=self.root)
                        else:
                              cursor.execute("UPDATE course SET duration=?, charges=?, Description=? WHERE name=?", (
                                    self.var_Duration.get(),
                                    self.var_Charges.get(),
                                    self.txt_Description.get("1.0", END),
                                    self.var_course.get()
                              ))
                              conn.commit()
                              self.trigger_popup("Row updated successfully")
                              self.show()

            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}")

#=============================================================

      def trigger_popup(self, message):
            messagebox.showinfo("Information", message, parent=self.root)

#==============================================================================================================

      def search(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()

            try:
                  if self.Var_Search.get() == "":
                        messagebox.showerror("Error", "Course Name is required", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM course WHERE name=?", (self.Var_Search.get(),))
                        row = cursor.fetchone()
                        if row is None:
                              messagebox.showerror("Error", "No record found", parent=self.root)
                        else:
                              self.Coursetable.delete(*self.Coursetable.get_children())
                              self.Coursetable.insert("", END, values=row)

            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}")

      def show(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM course")
            rows = cursor.fetchall()
            self.Coursetable.delete(*self.Coursetable.get_children())

            for row in rows:
                  self.Coursetable.insert("", END, values=row)

# Running the application
if __name__=="__main__":
      root = Tk()
      obj = Courseclass(root)
      root.mainloop()
