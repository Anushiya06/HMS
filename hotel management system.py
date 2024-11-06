import random
import datetime

class Hotel:
    def __init__(self):
        self.room_types = {
            1: {"type": "Standard Non-AC", "price": 3500},
            2: {"type": "Standard AC", "price": 4000},
            3: {"type": "3-Bed Non-AC", "price": 4500},
            4: {"type": "3-Bed AC", "price": 5000}
        }
        self.rooms_info = {
            1: "Room amenities include: 1 Double Bed, Television, Telephone, Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and an attached washroom with hot/cold water.",
            2: "Room amenities include: 1 Double Bed, Television, Telephone, Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and an attached washroom with hot/cold water + Window/Split AC.",
            3: "Room amenities include: 1 Double Bed + 1 Single Bed, Television, Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1 Side table, Balcony with an Accent table with 2 Chair and an attached washroom with hot/cold water.",
            4: "Room amenities include: 1 Double Bed + 1 Single Bed, Television, Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1 Side table, Balcony with an Accent table with 2 Chair and an attached washroom with hot/cold water + Window/Split AC."
        }
        self.menu = {
            1: {"item": "Regular Tea", "price": 20},
            2: {"item": "Masala Tea", "price": 25},
            3: {"item": "Coffee", "price": 25},
            4: {"item": "Cold Drink", "price": 25},
            5: {"item": "Bread Butter", "price": 30},
            6: {"item": "Bread Jam", "price": 30},
            7: {"item": "Veg. Sandwich", "price": 50},
            8: {"item": "Veg. Toast Sandwich", "price": 50},
            9: {"item": "Cheese Toast Sandwich", "price": 70},
            10: {"item": "Grilled Sandwich", "price": 70},
            11: {"item": "Tomato Soup", "price": 110},
            12: {"item": "Hot & Sour", "price": 110},
            13: {"item": "Veg. Noodle Soup", "price": 110},
            14: {"item": "Sweet Corn", "price": 110},
            15: {"item": "Veg. Munchow", "price": 110},
            16: {"item": "Shahi Paneer", "price": 110},
            17: {"item": "Kadai Paneer", "price": 110},
            18: {"item": "Handi Paneer", "price": 120},
            19: {"item": "Palak Paneer", "price": 120},
            20: {"item": "Chilli Paneer", "price": 140},
            21: {"item": "Matar Mushroom", "price": 140},
            22: {"item": "Mix Veg", "price": 140},
            23: {"item": "Jeera Aloo", "price": 140},
            24: {"item": "Malai Kofta", "price": 140},
            25: {"item": "Aloo Matar", "price": 140},
            26: {"item": "Dal Fry", "price": 140},
            27: {"item": "Dal Makhani", "price": 150},
            28: {"item": "Dal Tadka", "price": 150},
            29: {"item": "Plain Roti", "price": 15},
            30: {"item": "Butter Roti", "price": 15},
            31: {"item": "Tandoori Roti", "price": 20},
            32: {"item": "Butter Naan", "price": 20},
            33: {"item": "Plain Rice", "price": 90},
            34: {"item": "Jeera Rice", "price": 90},
            35: {"item": "Veg Pulao", "price": 110},
            36: {"item": "Peas Pulao", "price": 110},
            37: {"item": "Plain Dosa", "price": 100},
            38: {"item": "Onion Dosa", "price": 110},
            39: {"item": "Masala Dosa", "price": 130},
            40: {"item": "Paneer Dosa", "price": 130},
            41: {"item": "Rice Idli", "price": 130},
            42: {"item": "Sambhar Vada", "price": 140},
            43: {"item": "Vanilla Ice Cream", "price": 60},
            44: {"item": "Strawberry Ice Cream", "price": 60},
            45: {"item": "Pineapple Ice Cream", "price": 60},
            46: {"item": "Butter Scotch Ice Cream", "price": 60}
        }
        self.bookings = []
        self.current_customer_id = 1

    def welcome_screen(self):
        print("""
                                 WELCOME TO HOTEL ANCASA

                         1 Booking

                         2 Rooms Info

                         3 Room Service(Menu Card)

                         4 Payment

                         5 Record

                         0 Exit
        """)

    def booking(self):
        print(" BOOKING ROOMS")
        name = input("Name: ")
        phone = input("Phone No.: ")
        address = input("Address: ")

        check_in = input("Check-In (dd/mm/yyyy): ")
        check_out = input("Check-Out (dd/mm/yyyy): ")

        print("\n----SELECT ROOM TYPE----")
        for key, value in self.room_types.items():
            print(f" {key}. {value['type']}")
        print("        Press 0 for Room Prices")

        room_type = int(input("-> "))
        if room_type == 0:
            self.show_room_prices()
            room_type = int(input("Select Room Type: "))

        room = self.room_types.get(room_type)
        if not room:
            print("Invalid room type selected.")
            return

        days = self.calculate_days(check_in, check_out)
        total_cost = days * room["price"]

        self.bookings.append({
            "customer_id": self.current_customer_id,
            "name": name,
            "phone": phone,
            "address": address,
            "check_in": check_in,
            "check_out": check_out,
            "room_type": room["type"],
            "days": days,
            "total_cost": total_cost
        })

        print("\n----BOOKING SUCCESSFUL----")
        print(f"Customer ID: {self.current_customer_id}")
        print(f"Name: {name}")
        print(f"Phone No.: {phone}")
        print(f"Address: {address}")
        print(f"Check-In: {check_in}")
        print(f"Check-Out: {check_out}")
        print(f"Room Type: {room['type']}")
        print(f"Total Cost: {total_cost}")

        self.current_customer_id += 1

    def show_room_prices(self):
        print("\n----ROOM PRICES----")
        for key, value in self.room_types.items():
            print(f" {key}. {value['type']} - Rs. {value['price']} per day")

    def room_info(self):
        print("\n----ROOM INFORMATION----")
        for key, info in self.rooms_info.items():
            print(f" {key}. {self.room_types[key]['type']}")
            print(info)
            print()

    def room_service(self):
        print("\n----ROOM SERVICE (MENU CARD)----")
        for key, item in self.menu.items():
            print(f" {key}. {item['item']} - Rs. {item['price']}")

    def payment(self):
        print("\n----PAYMENT----")
        customer_id = int(input("Enter Customer ID: "))
        customer = next((booking for booking in self.bookings if booking["customer_id"] == customer_id), None)

        if not customer:
            print("Invalid Customer ID.")
            return

        print("\n----PAYMENT DETAILS----")
        print(f"Customer ID: {customer_id}")
        print(f"Name: {customer['name']}")
        print(f"Phone No.: {customer['phone']}")
        print(f"Address: {customer['address']}")
        print(f"Check-In: {customer['check_in']}")
        print(f"Check-Out: {customer['check_out']}")
        print(f"Room Type: {customer['room_type']}")
        print(f"Total Cost: {customer['total_cost']}")

        print("\nPayment successful.")

    def record(self):
        print("\n----RECORD----")
        for booking in self.bookings:
            print(f"Customer ID: {booking['customer_id']}")
            print(f"Name: {booking['name']}")
            print(f"Phone No.: {booking['phone']}")
            print(f"Address: {booking['address']}")
            print(f"Check-In: {booking['check_in']}")
            print(f"Check-Out: {booking['check_out']}")
            print(f"Room Type: {booking['room_type']}")
            print(f"Total Cost: {booking['total_cost']}")
            print()

    def calculate_days(self, check_in, check_out):
        check_in_date = datetime.datetime.strptime(check_in, "%d/%m/%Y")
        check_out_date = datetime.datetime.strptime(check_out, "%d/%m/%Y")
        return (check_out_date - check_in_date).days

if __name__ == "__main__":
    hotel = Hotel()
    while True:
        hotel.welcome_screen()
        choice = int(input("-> "))
        if choice == 1:
            hotel.booking()
        elif choice == 2:
            hotel.room_info()
        elif choice == 3:
            hotel.room_service()
        elif choice == 4:
            hotel.payment()
        elif choice == 5:
            hotel.record()
        elif choice == 0:
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
