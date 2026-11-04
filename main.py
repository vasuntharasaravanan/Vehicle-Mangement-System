from src.admin import AdminPanel
from src.customer import CustomerPanel
from storage import save_data, load_data

def main_display():
    print("*"*30)
    print(f"Welcome to Vasunthara Rentals")
    print("*"*30)
    print("Choose an Option : ")
    print("1. Admin Panel")
    print("2. Customer Panel")
    print("3. Exit Application")
           
def admin_display():
    print("*"*30)
    print(f"Welcome to Admin Panel")
    print("*"*30)
    print("Choose an Option : ")
    print("1. Add a Vehicle")
    print("2. View Inventory")
    print("3. Exit Admin Panel")

def customer_display():
    print("#"*30)
    print("Welocme to customer Panel")
    print("#"*30)
    print("Choose an Option : ")
    print("1. Register Customer")
    print("2. View available vehicles")
    print("3. Rent Vehicle")
    print("4. Return Vehicle")
    print("5. Exit Customer panel")


def main(): 
    vehicles, customer = load_data()
    admin = AdminPanel(vehicles)
    customer_panel = CustomerPanel(vehicles, customer)
    while True:
        main_display()

        try:
            user_choice = input("Enter your choice 1/2/3 : ")

        except Exception as e:
            print(e)
        if user_choice == "3":
             print(f"Thank you for Using Vasunthara Rentals")
             break
        elif user_choice == "1":
            while True:
                admin_display()
                try:
                    admin_choice = input("Enter your choice: ")
                except Exception as l:
                    print("\n Existing the admin panel!", l)
                    break

                if admin_choice == "3":
                    print("Exiting the admin panel!!")
                    break
                elif admin_choice == "1":
                    print("Adding a new vehicle ")
                    vehicle_number = input("Please enter the vehicle number: ")
                    vehicle_brand = input("Please enter the vehicle brand: ")
                    vehicle_type = input("Please enter the vehilce type: ")
                    vehicle_rent = input("Please enter the rent of the vehicle: ")
                    admin.add_vehicle(vehicle_number, vehicle_brand, vehicle_type, vehicle_rent)
                    save_data(vehicles, customer)


                elif admin_choice == "2":
                    print("Displaying all the vechicles : ")

                    try:
                        admin.view_inventory()
                    except (KeyError, TypeError) as e:
                        print(f"Error displaying inventory: {e}")
                else:
                    print("Invalid choice !! Use 1/2/3")
        elif user_choice == "2":
            while True:
                customer_display()

                try:
                    customer_choice = input("Enter your choice: ")
                except  (EOFError, KeyboardInterrupt):
                    print("\nExiting the customer panel!")
                    break
                if customer_choice =="5":
                    print("Exiting the customer panel!! ")
                    break
                elif customer_choice == "1":
                    print("Registering customer.")
                    cid=input("Enter customer id:")
                    cname=input("Enter customer name:")


                    try:
                        customer_panel.register_customer(cid, cname)
                        save_data(vehicles, customer)
                    except (KeyError, TypeError, ValueError) as e:
                        print(f"Error registering customer: {e}")
        
                elif customer_choice == "2":
                    print("Viewing the available vehicles ")

                    try:
                        customer_panel.viewvehicledetails()
                    except (KeyError, TypeError) as e:
                        print(f"Error viewing vehicles: {e}")

                elif customer_choice == "3":
                    print("Renting the vehicle ")
                    cid=input("Enter customer id:")
                    vid=input("Enter vehicle id:")

                    try:
                        customer_panel.rentvehicle(cid, vid)
                        save_data(vehicles, customer)
                    except (KeyError, TypeError) as e:
                        print(f"Error renting vehicle: {e}")

                elif customer_choice == "4":
                    print("Returning the vehicle")
                    cid=input("Enter customer id:")
                    try:
                        customer_panel.returnvehicle(cid)
                        save_data(vehicles, customer)
                    except (KeyError, TypeError) as e:
                        print(f"Error returning vehicle: {e}")   
                else:
                    print("Invalid choice !! Use 1/2/3/4/5")

        else:
            print("Invalid choice. Only use 1/2/3")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication closed.")
 

