from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class StudentClass:
      def __init__(self,root):
            self.root=root
            self.root.title("Student Result managemnet System")
            self.root.geometry("1200x480+80+170")
            self.root.config(bg="white")
            self.root.focus_force()
#=========title==================================================================================================================================================
            title=Label(self.root, text="Manage Student Details ", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)
#==============variable ================================================================================================================================================
            self.var_rollNo=StringVar()
            self.var_name=StringVar()
            self.var_email=StringVar()
            self.var_Dob=StringVar()
            self.var_address=StringVar()
            self.var_course=StringVar()
            self.var_date=StringVar()
            self.var_gender=StringVar()
            self.var_state=StringVar()
            self.var_contact=StringVar()
            self.var_city=StringVar()
            self.var_pin=StringVar()
#============Widgets===================== Column One====================================================================================
            lbl_Rollno=Label(self.root, text=" Roll no ",font=("goudy old style", 15, "bold"), bg="white",).place(x=15, y=60 )
            lbl_Name=Label(self.root, text=" Name ",font=("goudy old style", 15, "bold"), bg="white",).place(x=15, y=100 )
            lbl_Email=Label(self.root, text=" Email ",font=("goudy old style", 15, "bold"), bg="white",).place(x=15, y=140 )
            lbl_Gender=Label(self.root, text=" Gender ",font=("goudy old style", 15, "bold"), bg="white",).place(x=15, y=180 )
            
            lbl_state=Label(self.root, text=" State ",font=("goudy old style", 15, "bold"), bg="white",).place(x=15, y=220 )
            txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=150, y=220,width=150 )      
            lbl_city=Label(self.root, text=" City ",font=("goudy old style", 15, "bold"), bg="white",).place(x=310, y=220 )
            txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=380, y=220,width=100 )      
            lbl_pin=Label(self.root, text=" Pin Code",font=("goudy old style", 15, "bold"), bg="white",).place(x=490, y=220 )
            txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=580, y=220,width=100 )      
            lbl_address=Label(self.root, text=" Address ",font=("goudy old style", 15, "bold"), bg="white",).place(x=15, y=260 )
        
#==============Entry Feilds=======================================================================================================

            self.txt_roll=Entry(self.root,textvariable=self.var_rollNo,font=("goudy old style", 15, "bold"), bg="AliceBlue")
            self.txt_roll.place(x=150, y=60,width=200 )
            txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="AliceBlue",).place(x=150, y=100, width=200 )
            txt_email=Entry(self.root, textvariable=self.var_email,font=("goudy old style", 15, "bold"), bg="AliceBlue",).place(x=150, y=140 ,width=200)
            self.txt_gender=ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style", 15, "bold"),state='read',justify='center')
            self.txt_gender.place(x=150, y=180,width=200)
            self.txt_gender.current(0)
#============Widgets===================== Column two==================================================================================================
            lbl_dob=Label(self.root, text="D.O.B.",font=("goudy old style", 15, "bold"), bg="white",).place(x=360, y=60 )
            lbl_contact=Label(self.root, text=" Contact ",font=("goudy old style", 15, "bold"), bg="white",).place(x=360, y=100 )
            lbl_admission=Label(self.root, text=" admission",font=("goudy old style", 15, "bold"), bg="white",).place(x=360, y=140 )
            lbl_course=Label(self.root, text=" Course ",font=("goudy old style", 15, "bold"), bg="white",).place(x=360, y=180 )
           
#==============Entry Feilds=======================================================================================================================
            self.course_list=["Select"]
            self.Fetch_course()
            txt_dob=Entry(self.root,textvariable=self.var_Dob,font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=480, y=60,width=200 )
            txt_contact=Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=480, y=100, width=200 )
            txt_admission=Entry(self.root, textvariable=self.var_date,font=("goudy old style", 15, "bold"), bg="AliceBlue").place(x=480, y=140 ,width=200)
            self.txt_course=ttk.Combobox(self.root, textvariable=self.var_course,values= self.course_list,font=("goudy old style", 15, "bold"),state='read',justify='center')
            self.txt_course.place(x=480, y=180,width=200)
            self.txt_course.current(0)
            self.txt_address=Text(self.root, font=("goudy old style", 15, "bold"), bg="AliceBlue",)
            self.txt_address.place(x=150, y=260,width=535, height=100 )
#==================Buttons feilds ==========================================================================================================================
            self.btn_add=Button(self.root,text="Save", font=("goudy old style", 15, "bold"), bg="#0b5377" ,fg="white",cursor="hand2",command=self.add)
            self.btn_add.place(x=150,y=400,width=110,height= 40)             
            self.btn_Update=Button(self.root, text="Update", font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.update)
            self.btn_Update.place(x=270,y=400,width=110,height= 40) 
            self.btn_delete=Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#0b5377",fg="white",cursor="hand2",command=self.delete)
            self.btn_delete.place(x=390,y=400,width=110,height= 40) 
            self.btn_Clear=Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#0b5377",fg="white",cursor="hand2",command=self.clear)
            self.btn_Clear.place(x=510,y=400,width=110,height= 40) 
#=====================search pannel=================================================================================================================================================================================
            self.Var_Search=StringVar()
            lbl_Serach_roll=Label(self.root, text="Roll No" ,font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60 )
            txt_Serach_roll=Entry(self.root, textvariable=self.Var_Search,font=("goudy old style", 15, "bold"), bg="AliceBlue",).place(x=870, y=60 ,width=180)       
            btn_Search=Button(self.root,text="Search", font=("goudy old style", 15, "bold"), bg="#0b5377" ,fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height= 28)         
#=============================content=================================================================================================================================================================================================================
            self.C_frame=Frame(self.root, border=2,relief=RIDGE,bg="AliceBlue")
            self.C_frame.place(x=720, y=100,width=470,height=340)
#============================Scrollbar====================================================================================================================================================================================================
            scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
            scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)
            self.Coursetable=ttk.Treeview(self.C_frame,columns=("rollno","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
            scrollx.pack(side=BOTTOM,fill=X)
            scrolly.pack(side=RIGHT,fill=Y)
            scrollx.config(command=self.Coursetable.xview)
            scrolly.config(command=self.Coursetable.yview)
            self.Coursetable.heading("rollno", text="Roll No")
            self.Coursetable.heading("name", text="  Student Name")
            self.Coursetable.heading("email", text="Email")
            self.Coursetable.heading("gender", text= "Gender")
            self.Coursetable.heading("dob", text="D.O.B.")
            self.Coursetable.heading("contact", text="Contact No")
            self.Coursetable.heading("admission", text="admission")
            self.Coursetable.heading("course", text="Course")
            self.Coursetable.heading("state", text="State")
            self.Coursetable.heading("city", text="City")
            self.Coursetable.heading("pin", text="Pin Code")
            self.Coursetable.heading("address", text="Address")
            self.Coursetable["show"]='headings'
            self.Coursetable.column("rollno", width=100)
            self.Coursetable.column("name", width=100)
            self.Coursetable.column("email", width=100)
            self.Coursetable.column("gender", width=100)
            self.Coursetable.column("dob", width=100)
            self.Coursetable.column("contact", width=100)
            self.Coursetable.column("admission", width=100)
            self.Coursetable.column("course", width=100)
            self.Coursetable.column("state", width=100)
            self.Coursetable.column("city", width=100)
            self.Coursetable.column("pin", width=100)
            self.Coursetable.column("address", width=100)
            self.Coursetable.pack(fill=BOTH,expand=1)
            self.Coursetable.bind("<ButtonRelease-1>",self.get_data)
            self.show()   
#===========================================================================================================================
      def clear(self):
            self.var_rollNo.set("")
            self.var_name.set("")
            self.var_email.set("")
            self.var_Dob.set("")
            self.var_contact.set("")
            self.var_date.set("")
            self.var_course.set("Select")
            self.var_gender.set("Select")
            self.var_state.set("")
            self.var_city.set("")
            self.var_pin.set("")
            self.txt_address.delete('1.0', END)
            self.Var_Search.set("")
            self.txt_roll.config(state="normal")
            self.show()

#=====================================================================================================================================================
      def delete(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()
            try:
                  if self.var_rollNo.get() == "":
                        messagebox.showerror("Error", "Roll Number is required", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM student WHERE rollno=?", (self.var_rollNo.get(),))
                        row = cursor.fetchone()
                        if row == None:
                               messagebox.showerror("Error", "Invalid Roll No", parent=self.root)
                        else:
                              op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                              if op == True:
                                    cursor.execute("DELETE FROM student WHERE rollno=?", (self.var_rollNo.get(),))
                                    conn.commit()
                                    messagebox.showinfo("Delete", "Student record deleted successfully", parent=self.root)
                                    self.clear()
                                    conn.close()
            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
#==============================================================================================================
      def get_data(self, ev):
            self.txt_roll.config(state='readonly')
            r = self.Coursetable.focus()
            content = self.Coursetable.item(r)
            row = content['values']
            self.var_rollNo.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_Dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_date.set(row[6])
            self.var_course.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])
            self.txt_address.delete('1.0', END)
            self.txt_address.insert(END, row[11])

#====================================================================================================================================================
      def add(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()

            try:
                  if self.var_rollNo.get()=="":
                        messagebox.showerror("Error",f"Roll Number should be required.", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM Student  where rollno=?",(self.var_rollNo.get(),) )
                        row=cursor.fetchone()
                        if row!=None:
                              messagebox.showerror("Error",f"Roll Number already present.", parent=self.root)
                        else:
                              cursor.execute("insert into Student(rollno,name,email,gender,dob,contact,admission,course_id,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                              self.var_rollNo.get(),
                              self.var_name.get(),
                              self.var_email.get(),
                              self.var_gender.get(),
                              self.var_Dob.get(),
                              self.var_contact.get(),
                              self.var_date.get(),     # admission date
                              self.var_course.get(),
                              self.var_state.get(),
                              self.var_city.get(),
                              self.var_pin.get(),
                              self.txt_address.get("1.0",END)
                              ))
                              conn.commit()
                              messagebox.showinfo("success", "Student Added Successfully ",parent=self.root)
                              self.show()
            except Exception as ex:
                  messagebox.showerror("Error",f"Error due to {str(ex)}")
#==============================================================================================================
      def update(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()
            try:
                  if self.var_rollNo.get() == "":
                        messagebox.showerror("Error", "Roll Number is required", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM Student WHERE rollno = ?", (self.var_rollNo.get(),))
                        row = cursor.fetchone()
                        if row==None:
                              messagebox.showerror("Error", "Select Student from List.", parent=self.root)
                        else:
                              cursor.execute(" UPDATE Student SET name=?, email = ?,gender = ?,dob = ?, contact = ?, admission = ?, course_id = ?, state = ?,  city = ?, pin = ?, address = ? WHERE rollno = ? " 
                                             , (
                                                   self.var_name.get(), 
                                                   self.var_email.get(), 
                                                   self.var_gender.get(), 
                                                   self.var_Dob.get(), 
                                                   self.var_contact.get(),
                                                   self.var_date.get(),
                                                   self.var_course.get(), 
                                                   self.var_state.get(), 
                                                   self.var_city.get(), 
                                                   self.var_pin.get(),
                                                   self.txt_address.get("1.0", END).strip(),
                                                   self.var_rollNo.get()
                                                   ))
                              conn.commit()
                              messagebox.showinfo("Success", "Student details updated successfully.", parent=self.root)
                              self.show()

            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
            finally:
                  conn.close()
      

#==============================================================================================================
      def show(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()

            try:
                  cursor.execute("SELECT * FROM Student  " )
                  row=cursor.fetchall()
                  self.Coursetable.delete(*self.Coursetable.get_children())
                  for rows in row:
                        self.Coursetable.insert('',END,values=rows)
                  
            except Exception as ex:
                  messagebox.showerror("Error",f"Error due to {str(ex)}")

#==============================================================================================================
      def Fetch_course(self):
            conn = sqlite3.connect("student_result.db")
            
            cursor = conn.cursor()

            try:
                  cursor.execute("SELECT name FROM course")
                  row = cursor.fetchall()
                  #v = []
                  if len(row) > 0:
                        for rows in row:
                              self.course_list.append(rows[0])
                 # print(v)
    
            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}")

   
  # Always close the connection


#===================================================================================================================================================
      def search(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()
            try:
                  if self.Var_Search.get() == "":
                        messagebox.showerror("Error", "Please enter Roll No", parent=self.root)
                        return
                  cursor.execute("SELECT * FROM Student WHERE rollno=?", (self.Var_Search.get(),))
                  rows = cursor.fetchone()
                  if rows is not None:
                        self.Coursetable.delete(*self.Coursetable.get_children())
                        self.Coursetable.insert('', 'end', values=rows)
                  else:
                        messagebox.showerror("Error", "NO Record Found", parent=self.root)
            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

#=============================================================================================================================================


if __name__=="__main__":
      root=Tk()
      obj=StudentClass(root)
      root.mainloop()
