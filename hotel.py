from tkinter import*
from PIL import Image,ImageTk   
from customer import Cust_Win
from Rooms import HotelRoom
from bill import HotelApp
from Info import HotelOverviewApp


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x100+0+0")

    ###############1 img########################
        img2=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\hotel.jpg")
        img2=img2.resize((1550,140),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbimg1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbimg1.place(x=0,y=0,width=1550,height=140)

        ###############logo########################
        img1=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\logo1.jpg")
        img1=img1.resize((230,140),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=230,height=140)

        ################ title######################

        lbl_title=Label(self.root,text="MILLD.WEST LUXURY RESORT & SPA",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        ####################main frame######################
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        ################menu#######################
        lbl_menu=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

          ####################button frame######################

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)


        cust_btn=Button(btn_frame,text="CUSTOMER",command= self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,command=self.roombookings,text="ROOMS",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text=" BILL DETAILS",command=self.bill,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        Info_btn=Button(btn_frame,text="REPORT",width=22,command=self.info,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        Info_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #################### right side img######################
        img3=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\lobby.jpeg")
        img3=img3.resize((1300,600),Image.AFFINE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbimg.place(x=225,y=0,width=1310,height=600)

        ################### side  images####################

        img4=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\1.jpeg")
        img4=img4.resize((230,210),Image.AFFINE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\2.jpeg")
        img5=img5.resize((230,190),Image.AFFINE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win( self.new_window)
    
    def roombookings(self):
        self.new_window=Toplevel(self.root)
        self.app=HotelRoom( self.new_window)
    
    def bill(self):
        self.new_window=Toplevel(self.root)
        self.app=HotelApp( self.new_window)
    
    def info(self):
        self.new_window=Toplevel(self.root)
        self.app=HotelOverviewApp( self.new_window)
     
    def logout(self):
        self.root.destroy() 
   




if __name__== "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
