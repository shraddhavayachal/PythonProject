from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk


class Bill:
    def __init__(self, name, mobile, room_no, check_in, check_out, total_amount,tax,no_of_days, meal):
        self.name = name
        self.mobile = mobile
        self.room_no = room_no
        self.check_in = check_in
        self.check_out = check_out
        self.total_amount = total_amount
        self.tax = tax
        self.no_of_days = no_of_days
        self.meal = meal
        

class HotelApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+250+175")
        root.configure(bg="lightblue")

        self.bills = []
        self.selected_index = None

        self.name_var = tk.StringVar()
        self.mobile_var = tk.StringVar()
        self.room_no_var = tk.StringVar()
        self.check_in_var = tk.StringVar()
        self.check_out_var = tk.StringVar()
        self.total_amount_var = tk.StringVar()
        self.tax_var = tk.StringVar()
        self.no_of_days_var = tk.StringVar()
        self.meal_var = tk.StringVar()

         ################ title######################

        lbl_title=Label(self.root,text="ADD BILL DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         ###############logo########################
        img1=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\logo1.jpg")
        img1=img1.resize((100,40),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lbimg.place(x=10,y=10,width=100,height=40)


        self.create_widgets()

    def create_widgets(self):
        # Frame for bill details input
        input_frame = ttk.Frame(self.root, padding=60)
        input_frame.grid(row=0, column=0, padx=0, pady=10)
        lbl_title=Label(self.root,text="ADD BILL DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        # Labels
        ttk.Label(input_frame, text="Name:",font=("arial",12,"bold")).grid(row=0, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Mobile:",font=("arial",12,"bold")).grid(row=1, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Room Number:",font=("arial",12,"bold")).grid(row=2, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Check-in Date:",font=("arial",12,"bold")).grid(row=3, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Check-out Date:",font=("arial",12,"bold")).grid(row=4, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Total Amount:",font=("arial",12,"bold")).grid(row=5, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Tax:",font=("arial",12,"bold")).grid(row=6, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Number of Days:",font=("arial",12,"bold")).grid(row=7, column=0,padx=2, pady=6)
        ttk.Label(input_frame, text="Meal:",font=("arial",12,"bold")).grid(row=8, column=0,padx=2, pady=6)

        # Entry widgets
        ttk.Entry(input_frame, textvariable=self.name_var,font=("arial",12,"bold")).grid(row=0, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.mobile_var,font=("arial",12,"bold")).grid(row=1, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.room_no_var,font=("arial",12,"bold")).grid(row=2, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.check_in_var,font=("arial",12,"bold")).grid(row=3, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.check_out_var,font=("arial",12,"bold")).grid(row=4, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.total_amount_var,font=("arial",12,"bold") ).grid(row=5, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.tax_var,font=("arial",12,"bold")).grid(row=6, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.no_of_days_var,font=("arial",12,"bold")).grid(row=7, column=1,padx=2, pady=6)
        ttk.Entry(input_frame, textvariable=self.meal_var,font=("arial",12,"bold")).grid(row=8, column=1,padx=2, pady=6)

        # Frame for action buttons
        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.grid(row=1, column=0, padx=10, pady=10)

        # Buttons
        ttk.Button(button_frame, text="Add", command=self.add_bill).grid(row=0, column=0,padx=1)
        ttk.Button(button_frame, text="Update", command=self.update_bill).grid(row=0, column=1,padx=1)
        ttk.Button(button_frame, text="Delete", command=self.delete_bill).grid(row=0, column=2,padx=1)
        ttk.Button(button_frame, text="Reset", command=self.reset_fields).grid(row=0, column=3,padx=1)

        # Frame for bill list and image
        data_frame = ttk.Frame(self.root, padding=10)
        data_frame.grid(row=0, column=4, rowspan=4, padx=10, pady=10)

        # Listbox to display bill data
        self.bill_listbox = tk.Listbox(data_frame, selectmode=tk.SINGLE,height=20,width=80,font=("arial",12,"bold"))
        self.bill_listbox.pack(side=tk.LEFT, fill=tk.Y)
        self.bill_listbox.bind("<<ListboxSelect>>", self.select_bill)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bill_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.bill_listbox.yview)

        # Success message
        self.success_label = ttk.Label(self.root, text="", foreground="green",font=("arial",30,"bold"),background="lightblue")
        self.success_label.grid(row=4, column=3, columnspan=2)

    def calculate_total_amount(self):
        try:
            tax = float(self.tax_var.get())
            no_of_days = float(self.no_of_days_var.get())
            meal = float(self.meal_var.get())
            total_amount = (tax * no_of_days) + meal
            self.total_amount_var.set(total_amount)
        except ValueError:
            self.total_amount_var.set("Invalid Input")

    def add_bill(self):
        # Get bill details
        name = self.name_var.get()
        mobile = self.mobile_var.get()
        room_no = self.room_no_var.get()
        check_in = self.check_in_var.get()
        check_out = self.check_out_var.get()
        total_amount = self.total_amount_var.get()
        tax = self.tax_var.get()
        no_of_days = self.no_of_days_var.get()
        meal = self.meal_var.get()

        # Create a new bill object
        bill = Bill(name, mobile, room_no, check_in, check_out, total_amount,tax,no_of_days, meal)

        # Add bill to the list
        self.bills.append(bill)

        # Update the listbox
        self.update_listbox()

        # Display success message
        self.success_label.config(text="Bill added successfully!")

        # Clear success message after a few seconds
        self.root.after(3000, self.clear_success_message)

    def update_bill(self):
        if self.selected_index is not None:
            # Get updated bill details
            name = self.name_var.get()
            mobile = self.mobile_var.get()
            room_no = self.room_no_var.get()
            check_in = self.check_in_var.get()
            check_out = self.check_out_var.get()
            total_amount = self.total_amount_var.get()
            tax = self.tax_var.get()
            no_of_days = self.no_of_days_var.get()
            meal = self.meal_var.get()

            # Update the bill data in the list
            bill = Bill(name, mobile, room_no, check_in, check_out, total_amount, tax, no_of_days, meal)
            self.bills[self.selected_index] = bill

            # Update the listbox
            self.update_listbox()

            # Display success message
            self.success_label.config(text="Bill updated successfully!")

            # Clear success message after a few seconds
            self.root.after(3000, self.clear_success_message)

    def delete_bill(self):
        if self.selected_index is not None:
            # Remove the selected bill from the list
            del self.bills[self.selected_index]

            # Clear the selection index
            self.selected_index = None

            # Update the listbox
            self.update_listbox()

            # Display success message
            self.success_label.config(text="Bill deleted successfully!")

            # Clear success message after a few seconds
            self.root.after(3000, self.clear_success_message)

    def select_bill(self, event):
        # Get the selected bill index from the listbox
        index = self.bill_listbox.curselection()

        if index:
            # Convert the tuple to an integer
            self.selected_index = int(index[0])

            # Get bill data
            bill = self.bills[self.selected_index]

            # Set the bill data to the entry fields
            self.name_var.set(bill.name)
            self.mobile_var.set(bill.mobile)
            self.room_no_var.set(bill.room_no)
            self.check_in_var.set(bill.check_in)
            self.check_out_var.set(bill.check_out)
            self.total_amount_var.set(bill.total_amount)
            self.tax_var.set(bill.tax)
            self.no_of_days_var.set(bill.no_of_days)
            self.meal_var.set(bill.meal)

    def update_listbox(self):
        # Clear the listbox
        self.bill_listbox.delete(0, tk.END)

        # Add bill data to the listbox
        for bill in self.bills:
            self.bill_listbox.insert(tk.END, bill.name,bill.mobile,bill.room_no,bill.check_in,bill.check_out,bill.total_amount,bill.tax,bill.no_of_days,bill.meal)

    def reset_fields(self):
        # Clear all the input fields
        self.name_var.set("")
        self.mobile_var.set("")
        self.room_no_var.set("")
        self.check_in_var.set("")
        self.check_out_var.set("")
        self.total_amount_var.set("")
        self.tax_var.set("")
        self.no_of_days_var.set("")
        self.meal_var.set("")

        # Clear the selection index
        self.selected_index = None

    def clear_success_message(self):
        # Clear the success message
        self.success_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()
