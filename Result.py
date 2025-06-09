from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class Resultclass:
      def __init__(self,root):
            self.root=root
            self.root.title("Student Result managemnet System")
            self.root.geometry("1200x480+80+170")
            self.root.config(bg="white")
            self.root.focus_force()

            #=========title===================

            title=Label(self.root, text="Add Student Result  ",font=("goudy old style", 20, "bold"), 
            bg="#033054", fg="white").place(x=10, y=15, width=1180, height=50)

 #====================button widgets ===============================================


            #variables=====================
            self.var_roll=StringVar()
            self.var_name=StringVar()
            self.var_course=StringVar()
            self.var_marksob=StringVar()
            self.var_fullmarks=StringVar()
            self.roll_list=[]
            self.Fetch_roll()

            lbl_select=Label(self.root, text="Select Student",font=("goudy old style", 15, "bold"), bg="white",).place(x=50, y=100 )
            lbl_name=Label(self.root, text="Name",font=("goudy old style", 15, "bold"), bg="white",).place(x=50, y=160 )
            lbl_course=Label(self.root, text="Course",font=("goudy old style", 15, "bold"), bg="white",).place(x=50, y=220 )
            lbl_Marksob=Label(self.root, text="Marks Obtained",font=("goudy old style", 15, "bold"), bg="white",).place(x=50, y=280 )
            lbl_fullmarks=Label(self.root, text="Full Marks",font=("goudy old style", 15, "bold"), bg="white",).place(x=50, y=340 )

            self.txt_Student=ttk.Combobox(self.root, textvariable=self.var_roll,values= self.roll_list,font=("goudy old style", 15, "bold"),state='read',justify='center')
            self.txt_Student.place(x=280, y=100,width=200)
            self.txt_Student.set("Select")


            btn_Search=Button(self.root,text="Search", font=("goudy old style", 15, "bold"), bg="#1E90FF" ,fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=120,height= 28)         
            
            
            txt_name=Entry(self.root, textvariable=self.var_name,font=("goudy old style", 18, "bold"), bg="AliceBlue",state='readonly').place(x=280, y=160 ,width=340)       
            txt_course=Entry(self.root, textvariable=self.var_course,font=("goudy old style", 18, "bold"), bg="AliceBlue",state='readonly').place(x=280, y=220 ,width=340)       
            txt_Marksob=Entry(self.root, textvariable=self.var_marksob,font=("goudy old style", 18, "bold"), bg="AliceBlue",).place(x=280, y=280 ,width=340)       
            txt_fullmarks=Entry(self.root, textvariable=self.var_fullmarks,font=("goudy old style", 18, "bold"), bg="AliceBlue",).place(x=280, y=340 ,width=340)       


            btn_add=Button(self.root,text="Submit", font=("Times new Roman", 15, "bold"), bg="green" ,fg="white",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height= 35)         
            btn_clear=Button(self.root,text="Clear", font=("Times new Roman", 15, "bold"), bg="black" ,fg="white",cursor="hand2",command=self.clear).place(x=450,y=420,width=120,height= 35)         
            

            #[===============image]===============
            
            self.bgimage=Image.open(r"D:\SRMDBMS\SRMimage\Rimage.jpg")
            self.bgimage=self.bgimage.resize((500,300),Image.LANCZOS)
            self.bgimage = ImageTk.PhotoImage(self.bgimage)
            self.lbl_img=Label(self.root,image=self.bgimage).place(x=630,y=100)


      def Fetch_roll(self):
            conn = sqlite3.connect("student_result.db")
            
            cursor = conn.cursor()

            try:
                  cursor.execute("SELECT rollno FROM Student")
                  row = cursor.fetchall()
                  #v = []
                  if len(row) > 0:
                        for rows in row:
                              self.roll_list.append(rows[0])
                 # print(v)
    
            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}")
#============================================================================================
      def search(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()
            try:
                  
                  cursor.execute("SELECT name,course_id FROM Student WHERE rollno=?", (self.var_roll.get(),))
                  rows = cursor.fetchone()
                  if rows is not None:
                        self.var_name.set(rows[0])
                        self.var_course.set(rows[1])

                  else:
                        messagebox.showerror("Error", "NO Record Found", parent=self.root)
            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
#==========================================================================================================================

      def add(self):
            if self.var_roll.get() == "" or self.var_marksob.get() == "" or self.var_fullmarks.get() == "":
                  messagebox.showerror("Error", "All fields are required", parent=self.root)
                  return
            try:
                  marks_ob = float(self.var_marksob.get())
                  full_marks = float(self.var_fullmarks.get())
                  percentage = (marks_ob / full_marks) * 100
                  con = sqlite3.connect("student_result.db")
                  cur = con.cursor()
                  cur.execute("INSERT INTO Result (rollno, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)",
                              (
                                    self.var_roll.get(),
                                    self.var_name.get(),
                                    self.var_course.get(),
                                    self.var_marksob.get(),
                                    self.var_fullmarks.get(),
                                    str(round(percentage, 2))
                              ))
                  con.commit()
                  con.close()
                  messagebox.showinfo("Success", "Result added successfully", parent=self.root)
                  
            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

      def clear(self):
            self.var_roll.set("select")
            self.var_name.set("")
            self.var_course.set("")
            self.var_marksob.set("")
            self.var_fullmarks.set("")





if __name__=="__main__":
      root=Tk()
      obj=Resultclass(root)
      root.mainloop()