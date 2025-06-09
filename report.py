from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class reportclass:
      def __init__(self,root):
            self.root=root
            self.root.title("Student Result managemnet System")
            self.root.geometry("1200x480+80+170")
            self.root.config(bg="white")
            self.root.focus_force()

            #=========title===================

            title=Label(self.root, text="View  Student Result  ",font=("goudy old style", 20, "bold"), 
            bg="#033054", fg="white").place(x=10, y=15, width=1180, height=50)
            

            #search ============
            self.var_search=StringVar()
            self.var_id=""

            lbl_select=Label(self.root, text="Search By Roll Number ",font=("goudy old style", 15, "bold"), bg="white",).place(x=300, y=100 )
            txt_serach=Entry(self.root, textvariable=self.var_search,font=("goudy old style", 15), bg="light blue",).place(x=530, y=100, width=150, height=35 )

            btn_Search=Button(self.root,text="Search", font=("goudy old style", 15, "bold"), bg="#1E90FF" ,fg="white",cursor="hand2",command=self.search).place(x=700,y=100,width=120,height= 35)         
            btn_clear=Button(self.root,text="Clear", font=("goudy old style", 15, "bold"), bg="green" ,fg="white",cursor="hand2",command=self.clear).place(x=830,y=100,width=120,height= 35)         


            #===result_labels=====
            lbl_roll=Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE).place(x=150,y=230,width=150,height= 50)
            lbl_name=Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE).place(x=300,y=230,width=150,height= 50)
            lbl_course=Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE).place(x=450,y=230,width=150,height= 50)
            lbl_marks=Label(self.root,text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height= 50)
            lbl_full=Label(self.root,text="Total Marks", font=("goudy old style", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height= 50)
            lbl_per=Label(self.root,text="Percentage", font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE).place(x=900,y=230,width=150,height= 50)

            self.roll=Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE)
            self.roll.place(x=150,y=280,width=150,height= 50)
            self.name=Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE)
            self.name.place(x=300,y=280,width=150,height= 50)
            self.course=Label(self.root,  font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE)
            self.course.place(x=450,y=280,width=150,height= 50)
            self.marks=Label(self.root, font=("goudy old style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
            self.marks.place(x=600,y=280,width=150,height= 50)
            self.full=Label(self.root, font=("goudy old style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
            self.full.place(x=750,y=280,width=150,height= 50)
            self.per=Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2,relief=GROOVE)
            self.per.place(x=900,y=280,width=150,height= 50)

            btn_delete=Button(self.root,text="delete", font=("goudy old style", 15, "bold"), bg="red" ,fg="white",cursor="hand2", command=self.delete).place(x=500,y=350,width=150,height= 35)         
      
      #============ search button==============

      def search(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()
            try:
                  if self.var_search.get()=="":
                        messagebox.showerror("Error","Roll No. should be required",parent=self.root)
                  
                  else:
                       cursor.execute("SELECT *from  Result WHERE rollno=?", (self.var_search.get(),))
                  rows = cursor.fetchone()
                  if rows is not None:
                        self.var_id=rows[0]
                        self.roll.config(text=rows[1])
                        self.name.config(text=rows[2])
                        self.course.config(text=rows[3])
                        self.marks.config(text=rows[4])
                        self.full.config(text=rows[5])
                        self.per.config(text=rows[6])


                  else:
                        messagebox.showerror("Error", "NO Record Found", parent=self.root)
            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
#==========================================================================================================================
      def clear(self):
                  self.var_id=""
            
                  self.roll.config(text="")
                  self.name.config(text="")
                  self.course.config(text="")
                  self.marks.config(text="")
                  self.full.config(text="")
                  self.per.config(text="")
                  self.var_search.set("")
      

      def delete(self):
            conn = sqlite3.connect("student_result.db")
            cursor = conn.cursor()

            try:
                  if self.var_id == "":
                        messagebox.showerror("Error", "Search Student Result First", parent=self.root)
                  else:
                        cursor.execute("SELECT * FROM Result WHERE rid=?", (self.var_id,))
                        row = cursor.fetchone()
                        if row is None:
                              messagebox.showerror("Error", "invalid Student result", parent=self.root)
                        else:
                              op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                              if op == True:
                                    cursor.execute("DELETE FROM Result WHERE rid=?", (self.var_id,))
                                    conn.commit()
                                    self.trigger_popup("Result deleted successfully!")
                                    self.clear()

            except Exception as ex:
                  messagebox.showerror("Error", f"Error due to {str(ex)}")











if __name__=="__main__":
      root=Tk()
      obj=reportclass(root)
      root.mainloop()