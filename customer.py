######## original home page
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import tkinter as tk

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+250+175")
        root.configure(bg="lightblue")

        ###################varibles############
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


         ################ title######################

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         ###############logo########################
        img1=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\logo1.jpg")
        img1=img1.resize((100,40),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lbimg.place(x=5,y=2,width=100,height=40)

        ##################### label & entrys#######
        self.customers = []
        self.selected_index = None
        self.ref_var=StringVar()
        x=random.randint(1000,9999)
        self.ref_var.set(str(x))
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.mobile_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.nationality_var = tk.StringVar()
        self.idproof_var = tk.StringVar()
        self.check_in_var = tk.StringVar()
        self.check_out_var = tk.StringVar()

        self.gender_choices = ["Male", "Female", "Other"]
        self.idproof_choices = ["Driving License", "Aadhar Card", "PanCard", "Passport"]

        self.create_widgets()

    def create_widgets(self):
        # Frame for customer details input
        input_frame = ttk.Frame(self.root, padding=60)
        input_frame.grid(row=0, column=0, padx=0, pady=10)
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        # Labels
        ttk.Label(input_frame, text="Ref:",font=("arial",12,"bold")).grid(row=0, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="Name:",font=("arial",12,"bold")).grid(row=1, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="Age:",font=("arial",12,"bold")).grid(row=2, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="Gender:",font=("arial",12,"bold")).grid(row=3, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="Mobile:",font=("arial",12,"bold")).grid(row=4, column=0, sticky=W,padx=2, pady=6)
        ttk.Label(input_frame, text="Email:",font=("arial",12,"bold")).grid(row=5, column=0, sticky=W,padx=2, pady=6)
        ttk.Label(input_frame, text="Address:",font=("arial",12,"bold")).grid(row=6, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="Nationality:",font=("arial",12,"bold")).grid(row=7, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="ID-Proof:",font=("arial",12,"bold")).grid(row=8, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="Check-in Date:",font=("arial",12,"bold")).grid(row=9, column=0,sticky=W, padx=2, pady=6)
        ttk.Label(input_frame, text="Check-out Date:",font=("arial",12,"bold")).grid(row=10, column=0,sticky=W, padx=2, pady=6)

        # Entry widgets
        ttk.Entry(input_frame, textvariable=self.ref_var,font=("arial",12,"bold"),state="readonly",width=29).grid(row=0, column=1, padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.name_var,font=("arial",12,"bold"),width=29).grid(row=1, column=1, padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.age_var,font=("arial",12,"bold"),width=29).grid(row=2, column=1, padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.mobile_var,font=("arial",12,"bold"),width=29).grid(row=4, column=1, padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.email_var,font=("arial",12,"bold"),width=29).grid(row=5, column=1, padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.address_var,font=("arial",12,"bold"),width=29).grid(row=6, column=1, padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.nationality_var,font=("arial",12,"bold"),width=29).grid(row=7, column=1, padx=2, pady=6)

        

       ######### # Combo box for gender and idproof
        gender_combo = ttk.Combobox(input_frame, textvariable=self.gender_var, values=self.gender_choices,font=("arial",12,"bold"),width=27)
        gender_combo.grid(row=3, column=1, padx=2, pady=6)
        gender_combo.current(0)

        idproof_combo = ttk.Combobox(input_frame, textvariable=self.idproof_var, values=self.idproof_choices,font=("arial",12,"bold"),width=27)
        idproof_combo.grid(row=8, column=1, padx=2, pady=6)
        idproof_combo.current(0)

        ttk.Entry(input_frame, textvariable=self.check_in_var,font=("arial",12,"bold"),width=29).grid(row=9, column=1, padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.check_out_var,font=("arial",12,"bold"),width=29).grid(row=10, column=1, padx=2, pady=6)

        ######## Frame for action buttons
        button_frame = Frame(input_frame,bd=2,relief=RIDGE,bg="lightgreen")
        button_frame.place(x=0,y=400,width=412,height=50)

        # Buttons
        ttk.Button(button_frame, text="Add",command=self.add_customer).grid(row=1, column=0, padx=1)
        ttk.Button(button_frame, text="Update", command=self.update_customer).grid(row=1, column=1, padx=1)
        ttk.Button(button_frame, text="Delete", command=self.delete_customer).grid(row=1, column=2, padx=1)
        ttk.Button(button_frame, text="Reset", command=self.reset_fields).grid(row=1, column=3, padx=1)

        # Frame for customer list and image
        data_frame = ttk.Frame(self.root, padding=10)
        data_frame.grid(row=0, column=4, rowspan=4, padx=10, pady=10)

        # # Listbox to display customer data
        self.customer_listbox = tk.Listbox(data_frame, selectmode=tk.SINGLE,height=20,width=80,font=("arial",12,"bold"))
        self.customer_listbox.pack(side=tk.LEFT, fill=tk.Y)
        self.customer_listbox.bind("<<ListboxSelect>>", self.select_customer)
        
        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
        # scrollbar = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.customer_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.customer_listbox.yview)

        # Success message
        self.success_label = ttk.Label(self.root, text="", foreground="green",font=("arial",30,"bold"),background="lightblue")
        self.success_label.grid(row=4, column=3, columnspan=2)

    def add_customer(self):
        # Get customer details
        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        check_in_date = self.check_in_var.get()
        check_out_date = self.check_out_var.get()
        mobile = self.mobile_var.get()
        email = self.email_var.get()
        address=self.address_var.get()



        # Add customer to the list
        customer_data = (name, age, gender, check_in_date, check_out_date,mobile,email,address)
        self.customers.append(customer_data)

        # Update the listbox
        self.update_listbox()

        # Display success message
        self.success_label.config(text="Customer added successfully!")

        # clearing success message after a few seconds
        self.root.after(3000, self.clear_success_message)

    def update_customer(self):
        if self.selected_index is not None:
            # Get updated customer details
            name = self.name_var.get()
            age = self.age_var.get()
            gender = self.gender_var.get()
            check_in_date = self.check_in_var.get()
            check_out_date = self.check_out_var.get()
            mobile = self.mobile_var.get()
            email = self.email_var.get()
            address=self.address_var.get()
           

            # Update the customer data in the list
            self.customers[self.selected_index] = (name, age, gender, check_in_date, check_out_date,mobile,email,address)

            # Update the listbox
            self.update_listbox()

            # Display success message
            self.success_label.config(text="Customer updated successfully!")

            # clearing success message after a few seconds
            self.root.after(3000, self.clear_success_message)

    def delete_customer(self):
        if self.selected_index is not None:
            # Remove the selected customer from the list
            del self.customers[self.selected_index]

            # clearing the selection index
            self.selected_index = None

            # Update the listbox
            self.update_listbox()

            # Display success message
            self.success_label.config(text="Customer deleted successfully!")

            # clearing success message after a few seconds
            self.root.after(3000, self.clear_success_message)

    def select_customer(self, event):
        # Get the selected customer index from the listbox
        index = self.customer_listbox.curselection()

        if index:
            # Convert the tuple to an integer
            self.selected_index = int(index[0])

            # Get customer data
            customer_data = self.customers[self.selected_index]
            name, age, gender, check_in_date, check_out_date,mobile,email,address = customer_data

            # Set the customer data to the entry fields
            self.ref_var.set()
            self.name_var.set(name)
            self.age_var.set(age)
            self.gender_var.set(gender)
            self.check_in_var.set(check_in_date)
            self.check_out_var.set(check_out_date)
            self.mobile_var.set(mobile)
            self.email_var.set(email)
            self.address_var.set(address)


    def update_listbox(self):
        # clearing the listbox
        self.customer_listbox.delete(0, tk.END)

        # Add customer data to the listbox
        for customer_data in self.customers:
            name, age, gender, mobile, email, address, check_in_date, check_out_date = customer_data
            self.customer_listbox.insert(tk.END, f"(Name:{name},Age: {age}, Gender: {gender},Mobile:{mobile},Email Id:{email},Address:{address},CheckIn:{check_in_date},CheckOut:{check_out_date})")


    def reset_fields(self):
        # clearinging all the input fields
    
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.mobile_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.nationality_var.set("")
        self.check_in_var.set("")
        self.check_out_var.set("")


        # clearing the selection index
        self.selected_index = None

    def clear_success_message(self):
        # clearing the success message
        self.success_label.config(text="")





if __name__== "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()

