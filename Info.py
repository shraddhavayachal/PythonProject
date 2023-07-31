import tkinter as tk
from tkinter import RIDGE, Label, ttk
from PIL import Image, ImageTk

class HotelOverviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Overview")
        self.root.geometry("1550x100+0+0")
        root.configure(bg="lightblue")

        self.create_widgets()

    def create_widgets(self):
        # Header
        lbl_title=Label(self.root,text="WELCOME TO MILLD.WEST LUXURY RESORT & SPA",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=50)

        # Hotel image
        img3=Image.open(r"C:\Users\SHRADDHA VAYACHAL\Desktop\PYTHON\Hotel_Management_System\images\hotel.jpg")
        img3=img3.resize((500,300),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE,background="lightblue")
        lbimg.place(x=900,y=200,width=700,height=500)

        

        # Overview paragraph
        overview_text = """
        MILLD.WEST LUXURY RESORT & SPA is a luxurious 5-star hotel located in the heart of the city. 
        We offer world-class amenities and exceptional services to ensure a comfortable and memorable stay for our guests. 
        Our spacious and elegantly designed rooms provide a perfect blend of modernity and comfort, making it an ideal choice
        for both business and leisure travelers. 
        Our team of dedicated staff is committed to providing the highest level of hospitality and personalized services to 
        cater to the unique needs of each guest.
        At MILLD.WEST LUXURY RESORT & SPA,we strive to create a delightful experience for our guests,making their stay truly 
        unforgettable.
        Amenties provide by our resort are
        -Swimming Pool,Waterpark,Restaurants,Bars,SPA,GYM.
        -Amphitheatre, Sound Show ,Bungee Jumping 
        -Free Parking,Free WIFI,24/7 Room Service
        Special features: Like a rooftop garden, historical significance, or eco-friendly initiatives, make sure to mention them. 
        Discount: 
        15% OFF for group upto 10 people
        "Stay & Play Package: Enjoy a Complimentary Experience!"
        Nearby attractions:
        -Calangute Beach             -Anjuna Flea Market:
        -Fort Aguada                 -Chapora Fort
        -Splashdown Waterpark        -Saturday Night Market at Arpora  
        -St. Alex Church             -Club Cubana
        Ease of access to public transportation, Airport, Roadways.
        Booking information: Provide information about how guests can book rooms and any current promotions or
        special offers.
        Location:
        MILLD.WEST LUXURY RESORT & SPA,Villa Goesa Rd,behind Farenheit Hotel, Khobra 
        Waddo, Calangute, Baga, Goa-403517
        Contact: 022-381-5672/022-021-0221/022-904-4561
        Email:MilldWestResort@gmail.com
        """

        overview_label = ttk.Label(self.root, text=overview_text, font=("Cambria",14,"italic"), wraplength=1000, justify=tk.LEFT,background="lightblue")
        overview_label.pack(side=tk.LEFT,pady=0,padx=0)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelOverviewApp(root)
    root.mainloop()
