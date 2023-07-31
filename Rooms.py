import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
# import mysql.connector
import random
from tkinter import messagebox
import tkinter as tk

class Room:
    def __init__(self, room_type, room_no, room_available, no_of_days, meals, check_in, check_out):
        self.room_type = room_type
        self.room_no = room_no
        self.room_available = room_available
        self.no_of_days = no_of_days
        self.meals = meals
        self.check_in = check_in
        self.check_out = check_out

class HotelRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x590+250+175")
        root.configure(bg="lightblue")

        self.rooms = []
        self.selected_index = None

        self.room_type_var = tk.StringVar()
        self.room_no_var = tk.StringVar()
        self.room_available_var = tk.StringVar()
        self.no_of_days_var = tk.StringVar()
        self.meals_var = tk.StringVar()
        self.check_in_var = tk.StringVar()
        self.check_out_var = tk.StringVar()

        self.room_type_choices = ["Single", "Double","Combined", "Suite","Villa","Private Pool Room","Private Terrace Room"]
        self.meals_choices = ["Breakfast","Lunch","High Tea ","Dinner"," All "]
         ################ title######################

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         ###############logo########################
        img1=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\logo1.jpg")
        img1=img1.resize((100,40),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lbimg.place(x=5,y=2,width=100,height=40)
        self.create_widgets()

    def create_widgets(self):
        # Frame for room details input
        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.grid(row=0, column=0, padx=10, pady=10)
        
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # Labels
        ttk.Label(input_frame, text="",font=("arial",12,"bold")).grid(row=0, column=0,sticky=W, padx=2,pady=6)
        ttk.Label(input_frame, text="Room Type:",font=("arial",12,"bold")).grid(row=1, column=0,sticky=W, padx=2,pady=6)
        ttk.Label(input_frame, text="Room Number:",font=("arial",12,"bold")).grid(row=2, column=0,sticky=W, padx=2,pady=6)
        ttk.Label(input_frame, text="Room Available:",font=("arial",12,"bold")).grid(row=3, column=0,sticky=W, padx=2,pady=6)
        ttk.Label(input_frame, text="Number of Days:",font=("arial",12,"bold")).grid(row=4, column=0,sticky=W, padx=2,pady=6)
        ttk.Label(input_frame, text="Meal:",font=("arial",12,"bold")).grid(row=5, column=0,sticky=W, padx=2,pady=6)
        ttk.Label(input_frame, text="Check-in Date:",font=("arial",12,"bold")).grid(row=6, column=0,sticky=W, padx=2,pady=6)
        ttk.Label(input_frame, text="Check-out Date:",font=("arial",12,"bold")).grid(row=7, column=0,sticky=W, padx=2,pady=6)

        # Entry widgets
        room_type_combo = ttk.Combobox(input_frame, textvariable=self.room_type_var,font=("arial",12,"bold"), values=self.room_type_choices)
        room_type_combo.grid(row=1, column=1, padx=5, pady=5)
        room_type_combo.current(0)
        meals_combo = ttk.Combobox(input_frame, textvariable=self.meals_var,font=("arial",12,"bold"), values=self.meals_choices)
        meals_combo.grid(row=5, column=1, padx=5, pady=5)
        meals_combo.current(0)
        ttk.Entry(input_frame, textvariable=self.room_no_var,font=("arial",12,"bold")).grid(row=2, column=1, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.room_available_var,font=("arial",12,"bold")).grid(row=3, column=1, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.no_of_days_var,font=("arial",12,"bold")).grid(row=4, column=1, padx=5, pady=5)
        # ttk.Entry(input_frame, textvariable=self.meals_var).grid(row=4, column=1, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.check_in_var,font=("arial",12,"bold")).grid(row=6, column=1, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.check_out_var,font=("arial",12,"bold")).grid(row=7, column=1, padx=5, pady=5)

        # Frame for action buttons
        button_frame = ttk.Frame(self.root, padding=10)
        button_frame.grid(row=1, column=0, padx=10, pady=10)

        # Buttons
        ttk.Button(button_frame, text="Add", command=self.add_room).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Update", command=self.update_room).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_room).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_fields).grid(row=0, column=3, padx=5, pady=5)

        # Frame for room list and image
        data_frame = ttk.Frame(self.root, padding=10)
        data_frame.grid(row=0, column=4, rowspan=4, padx=10, pady=10)

        # Listbox to display room data
        self.room_listbox = tk.Listbox(data_frame, selectmode=tk.SINGLE, height=10,width=80,font=("arial",12,"bold"))
        self.room_listbox.pack(side=tk.LEFT, fill=tk.Y)
        self.room_listbox.bind("<<ListboxSelect>>", self.select_room)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.room_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.room_listbox.yview)

        # Success message
        self.success_label = ttk.Label(self.root, text="", foreground="green",font=("arial",30,"bold"),background="lightblue")
        self.success_label.grid(row=2, column=4, columnspan=2)

    def add_room(self):
        # Get room details
        room_type = self.room_type_var.get()
        room_no = self.room_no_var.get()
        room_available = self.room_available_var.get()
        no_of_days = self.no_of_days_var.get()
        meals = self.meals_var.get()
        check_in = self.check_in_var.get()
        check_out = self.check_out_var.get()

        # Create a new room object
        room = Room(room_type, room_no, room_available, no_of_days, meals, check_in, check_out)

        # Add room to the list
        self.rooms.append(room)

        # Update the listbox
        self.update_listbox()

        # Display success message
        self.success_label.config(text="Room added successfully!")

        # Clear success message after a few seconds
        self.root.after(3000, self.clear_success_message)

    def update_room(self):
        if self.selected_index is not None:
            # Get updated room details
            room_type = self.room_type_var.get()
            room_no = self.room_no_var.get()
            room_available = self.room_available_var.get()
            no_of_days = self.no_of_days_var.get()
            meals = self.meals_var.get()
            check_in = self.check_in_var.get()
            check_out = self.check_out_var.get()

            # Update the room data in the list
            room = Room(room_type, room_no, room_available, no_of_days, meals, check_in, check_out)
            self.rooms[self.selected_index] = room

            # Update the listbox
            self.update_listbox()

            # Display success message
            self.success_label.config(text="Room updated successfully!")

            # Clear success message after a few seconds
            self.root.after(3000, self.clear_success_message)

    def delete_room(self):
        if self.selected_index is not None:
            # Remove the selected room from the list
            del self.rooms[self.selected_index]

            # Clear the selection index
            self.selected_index = None

            # Update the listbox
            self.update_listbox()

            # Display success message
            self.success_label.config(text="Room deleted successfully!")

            # Clear success message after a few seconds
            self.root.after(3000, self.clear_success_message)

    def select_room(self, event):
        # Get the selected room index from the listbox
        index = self.room_listbox.curselection()

        if index:
            # Convert the tuple to an integer
            self.selected_index = int(index[0])

            # Get room data
            room = self.rooms[self.selected_index]

            # Set the room data to the entry fields
            self.room_type_var.set(room.room_type)
            self.room_no_var.set(room.room_no)
            self.room_available_var.set(room.room_available)
            self.no_of_days_var.set(room.no_of_days)
            self.meals_var.set(room.meals)
            self.check_in_var.set(room.check_in)
            self.check_out_var.set(room.check_out)

    def update_listbox(self):
        # Clear the listbox
        self.room_listbox.delete(0, tk.END)

        # Add room data to the listbox
        for room in self.rooms:
            self.room_listbox.insert(tk.END, room.room_type,room.room_no,room.meals,room.check_in,room.check_out)

    def reset_fields(self):
        # Clear all the input fields
        self.room_type_var.set("")
        self.room_no_var.set("")
        self.room_available_var.set("")
        self.no_of_days_var.set("")
        self.meals_var.set("")
        self.check_in_var.set("")
        self.check_out_var.set("")

        # Clear the selection index
        self.selected_index = None

    def clear_success_message(self):
        # Clear the success message
        self.success_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelRoom(root)
    root.mainloop()
