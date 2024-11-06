import tkinter as tk
from tkinter import messagebox

class Hotel:
    def __init__(self, hotel_id, name, location, rooms_available, price_per_night):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available
        self.price_per_night = price_per_night

class User:
    def __init__(self, user_id, name, bookings=None):
        if bookings is None:
            bookings = []
        self.user_id = user_id
        self.name = name
        self.bookings = bookings

class HotelManagementSystem:
    def __init__(self):
        self.hotels = []
        self.users = []

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def add_user(self, user):
        self.users.append(user)

    def filter_hotels_by_location(self, location):
        return [hotel for hotel in self.hotels if hotel.location == location]

    def display_user_bookings(self, user_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if user:
            bookings = []
            for booking in user.bookings:
                hotel = next((h for h in self.hotels if h.hotel_id == booking), None)
                if hotel:
                    bookings.append(f"Hotel Name: {hotel.name}, Location: {hotel.location}, Price per Night: {hotel.price_per_night}")
            return bookings
        else:
            return None

    def book_hotel(self, user_id, hotel_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        hotel = next((h for h in self.hotels if h.hotel_id == hotel_id), None)
        if user and hotel and hotel.rooms_available > 0:
            user.bookings.append(hotel_id)
            hotel.rooms_available -= 1
            return True
        else:
            return False

# Initialize Hotel Management System
hms = HotelManagementSystem()

# Functions for GUI
def add_hotel():
    try:
        hotel_id = int(entry_hotel_id.get())
        name = entry_hotel_name.get()
        location = entry_hotel_location.get()
        rooms_available = int(entry_hotel_rooms.get())
        price_per_night = float(entry_hotel_price.get())
        hms.add_hotel(Hotel(hotel_id, name, location, rooms_available, price_per_night))
        messagebox.showinfo("Success", "Hotel added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter correct values.")

def add_user():
    try:
        user_id = int(entry_user_id.get())
        name = entry_user_name.get()
        hms.add_user(User(user_id, name))
        messagebox.showinfo("Success", "User added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter correct values.")

def display_all_hotels():
    text_display.delete("1.0", tk.END)
    for hotel in hms.hotels:
        text_display.insert(tk.END, f"ID: {hotel.hotel_id}, Name: {hotel.name}, Location: {hotel.location}, Rooms Available: {hotel.rooms_available}, Price per Night: {hotel.price_per_night}\n")

def filter_hotels_by_location():
    location = entry_filter_location.get()
    filtered_hotels = hms.filter_hotels_by_location(location)
    text_display.delete("1.0", tk.END)
    for hotel in filtered_hotels:
        text_display.insert(tk.END, f"ID: {hotel.hotel_id}, Name: {hotel.name}, Location: {hotel.location}, Rooms Available: {hotel.rooms_available}, Price per Night: {hotel.price_per_night}\n")

def book_hotel():
    try:
        user_id = int(entry_booking_user_id.get())
        hotel_id = int(entry_booking_hotel_id.get())
        if hms.book_hotel(user_id, hotel_id):
            messagebox.showinfo("Success", "Booking successful!")
        else:
            messagebox.showerror("Failure", "Booking failed. Either the hotel is full or user/hotel ID is incorrect.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter correct values.")

def display_user_bookings():
    try:
        user_id = int(entry_display_user_id.get())
        bookings = hms.display_user_bookings(user_id)
        text_display.delete("1.0", tk.END)
        if bookings:
            for booking in bookings:
                text_display.insert(tk.END, f"{booking}\n")
        else:
            messagebox.showerror("Error", "User not found")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter correct values.")

# Create main window
root = tk.Tk()
root.title("Hotel Management System")

# Create and place widgets for adding hotels
tk.Label(root, text="Hotel ID:").grid(row=0, column=0)
entry_hotel_id = tk.Entry(root)
entry_hotel_id.grid(row=0, column=1)

tk.Label(root, text="Hotel Name:").grid(row=1, column=0)
entry_hotel_name = tk.Entry(root)
entry_hotel_name.grid(row=1, column=1)

tk.Label(root, text="Hotel Location:").grid(row=2, column=0)
entry_hotel_location = tk.Entry(root)
entry_hotel_location.grid(row=2, column=1)

tk.Label(root, text="Rooms Available:").grid(row=3, column=0)
entry_hotel_rooms = tk.Entry(root)
entry_hotel_rooms.grid(row=3, column=1)

tk.Label(root, text="Price per Night:").grid(row=4, column=0)
entry_hotel_price = tk.Entry(root)
entry_hotel_price.grid(row=4, column=1)

btn_add_hotel = tk.Button(root, text="Add Hotel", command=add_hotel)
btn_add_hotel.grid(row=5, column=0, columnspan=2)

# Create and place widgets for adding users
tk.Label(root, text="User ID:").grid(row=6, column=0)
entry_user_id = tk.Entry(root)
entry_user_id.grid(row=6, column=1)

tk.Label(root, text="User Name:").grid(row=7, column=0)
entry_user_name = tk.Entry(root)
entry_user_name.grid(row=7, column=1)

btn_add_user = tk.Button(root, text="Add User", command=add_user)
btn_add_user.grid(row=8, column=0, columnspan=2)

# Create and place widgets for displaying all hotels
btn_display_hotels = tk.Button(root, text="Display All Hotels", command=display_all_hotels)
btn_display_hotels.grid(row=9, column=0, columnspan=2)

# Create and place widgets for filtering hotels by location
tk.Label(root, text="Filter by Location:").grid(row=10, column=0)
entry_filter_location = tk.Entry(root)
entry_filter_location.grid(row=10, column=1)

btn_filter_location = tk.Button(root, text="Filter Hotels", command=filter_hotels_by_location)
btn_filter_location.grid(row=11, column=0, columnspan=2)

# Create and place widgets for booking hotels
tk.Label(root, text="User ID for Booking:").grid(row=12, column=0)
entry_booking_user_id = tk.Entry(root)
entry_booking_user_id.grid(row=12, column=1)

tk.Label(root, text="Hotel ID for Booking:").grid(row=13, column=0)
entry_booking_hotel_id = tk.Entry(root)
entry_booking_hotel_id.grid(row=13, column=1)

btn_book_hotel = tk.Button(root, text="Book Hotel", command=book_hotel)
btn_book_hotel.grid(row=14, column=0, columnspan=2)

# Create and place widgets for displaying user bookings
tk.Label(root, text="User ID for Bookings:").grid(row=15, column=0)
entry_display_user_id = tk.Entry(root)
entry_display_user_id.grid(row=15, column=1)

btn_display_user_bookings = tk.Button(root, text="Display User Bookings", command=display_user_bookings)
btn_display_user_bookings.grid(row=16, column=0, columnspan=2)

# Create text widget for displaying information
text_display = tk.Text(root, height=10, width=50)
text_display.grid(row=17, column=0, columnspan=2)

# Run the application
root.mainloop()
