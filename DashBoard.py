
import sqlite3
from tkinter import*
from PIL import Image, ImageTk
from Course import Courseclass
from Student import StudentClass
from Result import Resultclass
from report import reportclass
class SRM:
      def __init__(self,root):
            self.root=root
            self.root.title("Student Result managemnet System")
            self.root.geometry("1350x700+0+0")
            self.root.config(bg="white")
            #============icone========================
      

            self.logo_dash=Image.open(r"D:\SRMDBMS\SRMimage\logoDash.jpg")
            self.logo_dash=self.logo_dash.resize((50,50),Image.LANCZOS)
            self.logo_dash = ImageTk.PhotoImage(self.logo_dash)
            



            #==================title=====================
            title=Label(self.root, text="Student Result Management System", 
             padx=10,compound=LEFT, image=self.logo_dash,font=("goudy old style", 20, "bold"), 
            bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=70)

            #=========menu============
            M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
            M_Frame.place(x=10, y=70, width=1516, height=80)

            
            btn_course=Button(M_Frame,text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377" ,fg="white",cursor="hand2", command=self.add_Course). place(x=30,y=5,width=220,height= 40)        
            
            btn_student=Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_Student).place(x=260,y=5,width=220,height= 40) 

            btn_Result=Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=500,y=5,width=220,height= 40) 

            btn_View=Button(M_Frame, text="View Student result", font=("goudy old style", 15, "bold"), bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=740,y=5,width=220,height= 40)

            btn_Logout=Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377",fg="white",cursor="hand2").place(x=1000,y=5,width=220,height= 40) 

            btn_Exit=Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377",fg="white",cursor="hand2").place(x=1240,y=5,width=220,height= 40) 

            #==================Content Window ======================
            self.bgimage=Image.open(r"D:\SRMDBMS\SRMimage\bgImag.jpg")
            self.bgimage=self.bgimage.resize((920,400),Image.LANCZOS)
            self.bgimage = ImageTk.PhotoImage(self.bgimage)  # ✅ Correct


            self.lbl_img=Label(self.root,image=self.bgimage).place(x=500,y=190,width=920,height=400)


            #====================update Deatils ======================

            self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),
            border=10,relief=RIDGE,bg="#4A90E2",fg="white")
            self.lbl_course.place(x=500,y=590,width=300,height=100)


            self.lbl_student=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),
            border=10,relief=RIDGE,bg="#4A90E2",fg="white")
            self.lbl_student.place(x=810,y=590,width=300,height=100)


            self.lbl_result=Label(self.root,text="Total Result\n[0]",font=("goudy old style",20),
            border=10,relief=RIDGE,bg="#4A90E2",fg="white")
            self.lbl_result.place(x=1120,y=590,width=300,height=100)





            #==================Footer=====================
            Footer=Label(self.root, text="Student Result Management System\n Contact us for any query:999xxxxxx90", 
             padx=10, font=("goudy old style", 20), 
            bg="#033054", fg="white").pack(side=BOTTOM,fill=X)
      

      def add_Course(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=Courseclass(self.new_win)

      def add_Student(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=StudentClass(self.new_win)
      
      def add_result(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=Resultclass(self.new_win)

      def add_report(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=reportclass(self.new_win)




            




if __name__=="__main__":
      root=Tk()
      obj=SRM(root)
      root.mainloop()
