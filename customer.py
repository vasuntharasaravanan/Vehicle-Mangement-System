class CustomerPanel:
    def __init__(self,vehicles,customers):
        self.vehicles = vehicles
        self.customers = customers

    def register_customer(self, customer_id, customer_name):
        try:
            self.customers[customer_id] = {
            "name" : customer_name,
            "rented":None
        }
            print(f"{customer_name} registered successfully!!")

        except (KeyError, TypeError, ValueError) as e:
            print(f"Error registering customer: {e}")

    def viewvehicledetails(self):
        try:
            print("------Available Vehicles------")
            available=False
            
            for vehicle_number,vehicle_data in self.vehicles.items():
                if vehicle_data["available"]:
                    print(f"Vehicle Number:{vehicle_number},Brand:{vehicle_data["brand"]},Type:{vehicle_data["type"]},Rent:{vehicle_data["rent"]}")
                    available=True
        
            if not available:
                print("Vehicle not Available")
                
        except (KeyError, TypeError) as e:
            print(f"Error viewing vehicle details: {e}")

    def rentvehicle(self,customer_id,vehicle_id):
        try:
            if customer_id not in self.customers:
                print("Customer Doesn't Exists")
                return
            if vehicle_id not in self.vehicles:
                print("vehicle are not available")
                return
            self.vehicles[vehicle_id]["available"]=False
            self.customers[customer_id]["rented"]=vehicle_id
            print(f"{self.customers[customer_id]["name"]} rented {self.vehicles[vehicle_id]["brand"]} successfully!")

        except (KeyError, TypeError) as e:
            print(f"Error renting vehicle: {e}")

    def returnvehicle(self,customer_id):
         try:
            if customer_id not in self.customers:
                print("Customer Doesn't Exists")
                return
            
            rented=self.customers[customer_id]["rented"]
            
            if not rented:
                print("Vehicle is not rented by customer")
                return
            
            self.vehicles[rented]["available"]=True
            
            print(f"{self.customers[customer_id]["name"]} Returned {self.vehicles[rented]["brand"]} Sucessfully!")
            self.customers[customer_id]["rented"]=None

         except (KeyError, TypeError) as e:
            print(f"Error returning vehicle: {e}")









