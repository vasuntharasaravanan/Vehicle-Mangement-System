
vehicles = {}

class AdminPanel:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def add_vehicle(self, vehicle_number, vehicle_brand, vehicle_type, vehicle_rent):
        try:
            self.vehicles[vehicle_number] = {
            "number" : vehicle_number,
            "brand" : vehicle_brand,
            "type" : vehicle_type,
            "rent" : vehicle_rent,
            "available":True
        }
            print(f"Vehicle : {vehicle_number} was added successfully!!")
        
        except (TypeError, ValueError) as e:
            print(f"Error adding vehicle: {e}")





    def view_inventory(self):
        try:
            for vehicle_number, vehicle_data in self.vehicles.items(): # syntax: key, value in dictionary.items
                print(f"Number : {vehicle_number}, {vehicle_data["brand"]} , {vehicle_data["type"]} {vehicle_data["rent"]}")

        except (KeyError, TypeError) as e:
            print(f"Error viewing inventory: {e}")


       
