from warehouse import Warehouse  # Importing the different classes from their respective python files
from technician import Technician
from vendor import Vendor  # Like importing the Vendor class from vendor.py
from fish_species import FishSpecies

class Hatchery:
    """
    This class imitates a fish hatchery business.
    It handles hiring technicians, managing supplies, selling fish, and running the hatchery operations.
    """
    def __init__(self, num_quarters=8, initial_cash=10000, fixed_costs=1500):
        """
        Initializing the hatchery with the given parameters.

        :param num_quarters: Declaring the number of quarters (time periods) to run the simulation
        :param initial_cash: Initial amount of cash for the hatchery
        :param fixed_costs: Fixed costs (like rent, utilities) per quarter
        """
        self.quarters = num_quarters  # Setting number of quarters the simulation will run
        self.cash = initial_cash
        self.fixed_costs = fixed_costs
        self.warehouse = Warehouse(20, 10, {'fertilizer': 0.10, 'feed': 0.001, 'salt': 0.001})
        self.technicians = []
        self.fish_species = self.initialize_fish_species()  # Initializing list of fish species the hatchery manages
        self.vendors = [
            Vendor("Slippery Lakes", 0.30, 0.10, 0.05),
            Vendor("Scaly Wholesaler", 0.20, 0.40, 0.25)
        ]

    def initialize_fish_species(self):
        """
        Modifying list of fish species, each with particular properties.

        :return: List of FishSpecies objects
        """
        return [
            FishSpecies("Clef Fins", 100.0, 12, 2, 2.0, 25, 250),
            FishSpecies("Timpani Snapper", 50.0, 9, 2, 1.0, 10, 350),
            FishSpecies("Andalusian Brim", 90.0, 6, 2, 0.5, 15, 250),
            FishSpecies("Plagal Cod", 100.0, 10, 2, 2.0, 20, 400),
            FishSpecies("Fugue Flounder", 200.0, 12, 2, 2.5, 30, 550),
            FishSpecies("Modal Bass", 300.0, 12, 6, 3.0, 50, 500)
        ]  # Create and return list of fish species with their properties
    
    def hire_technician(self, name):
        """
        Hiring a technician if not already hired, provided the hatchery has space for more technicians.

        :param name: Entering the name of the technician to be hired
        """
        if any(tech.name == name for tech in self.technicians):  # Checking if technician already exists
            print(f"Technician {name} is already hired.")
            return
        if len(self.technicians) < 5:  # Check if there is space for more technicians (max 5)
            technician = Technician(name)
            self.technicians.append(technician)
            print(f"Hired {name}, weekly rate={technician.weekly_rate} in quarter {self.quarters}\n")
        else:
            print("Maximum number of technicians already hired.")  # Prompt if max technician limit is reached
    
    def fire_technician(self, name):
        technician = next((tech for tech in self.technicians if tech.name == name), None)  # Finding technician
        if technician:
            self.technicians.remove(technician)
            print(f"Let go {name}, weekly rate={technician.weekly_rate} in quarter {self.quarters}")
        else:
            print(f"Technician {name} not found.")
    
    def sell_fish(self, fish_type, amount):
        """
        Selling certain amount of fish, updating the hatchery's supplies and cash.

        :param fish_type: Type of fish to sell
        :param amount: Number of fishes to sell
        :return: Revenue from the sale
        """
        fish = next((f for f in self.fish_species if f.name == fish_type), None)
        if fish:
            max_can_sell = min(fish.demand, self.warehouse.supplies['fertilizer'] // fish.fertilizer,
                               self.warehouse.supplies['feed'] // fish.feed, len(self.technicians))
            amount_to_sell = min(amount, max_can_sell)  # Calculating how many fishes to be sold
            revenue = amount_to_sell * fish.price
            self.cash += revenue  # Adding revenue to hatchery's cash
            # Deducting supplies based on the fish sold
            self.warehouse.supplies['fertilizer'] -= amount_to_sell * fish.fertilizer
            self.warehouse.supplies['feed'] -= amount_to_sell * fish.feed
            self.warehouse.supplies['salt'] -= amount_to_sell * fish.salt
            print(f"Fish {fish_type}, demand {fish.demand}, sell {amount}: {amount_to_sell}")
            return revenue
        return 0  # Return 0 if we were not able to sell any fish

    def run_quarter(self):
        """
        Runs functions for a single quarter (time period).

        :return: True if the hatchery endures to the next quarter, False if bankrupt
        """
        
       # print(f"\n================================\n====== SIMULATING quarter {quarters} ======\n================================")
            
        # Manage technician adjustments
        self.adjust_technicians()
        self.adjust_fish_sales()

        # Deducting fixed costs and technician payments
        self.cash -= self.fixed_costs  # Deducts fixed costs and technician payments
        for technician in self.technicians:
            self.cash -= technician.get_payment()  
        
        supply_costs = self.warehouse.get_total_cost()
        self.cash -= supply_costs
        
        self.warehouse.apply_depreciation()  # Apply depreciation to supplies in the warehouse
        
        # Displaying status of the hatchery
        self.display_status()

        self.restock_supplies()

        # Checking if hatchery has gone bankrupt or not
        if self.cash < 0:
            print(f"Hatchery went bankrupt at the end of quarter {self.quarters}")
            return False

        # Increment the quarter after the cycle
        self.quarters += 1  # Incrementing the quarter number
        return True

    def adjust_technicians(self):
        """
        Adjusts the number of technicians based on user input (hire or let go).
        """
        print("Current Technicians:")
        for tech in self.technicians:
            print(f"- {tech.name}")
        
        action = self.get_integer_input("To add enter positive, to remove enter negative, no change enter 0.\n>>> Enter number of technicians: ")
        
        if action > 0:
            for _ in range(action):
                name = input(">>> Enter technician name: ").strip()
                if name:
                    self.hire_technician(name)
        elif action < 0:
            for _ in range(abs(action)):
                name = input(">>> Enter technician name to remove: ").strip()
                if name:
                    self.fire_technician(name)

    def adjust_fish_sales(self):
        """
        Adjusting the number of fish to be sold based on user input.
        """
        sales = {}
        for fish in self.fish_species:
            sales[fish.name] = self.get_integer_input(f"Fish {fish.name}, demand {fish.demand}, sell {fish.demand}: ")
        
        total_sales = 0  # Processing sales and calculate the revenue
        for fish_name, amount in sales.items():
            total_sales += self.sell_fish(fish_name, amount)
        print(f"Total revenue from fish sales: £{total_sales}")

    def display_status(self):
        """
        Displays current status of hatchery, including cash, supplies, and technicians.
        """
        print("\nHatchery Status:")
        print(f"Hatchery Name: Eastaboga, Cash: £{self.cash:.2f}\n")
        print("Warehouse Main:")
        print(f" Fertiliser, {self.warehouse.supplies['fertilizer']:.2f} (capacity=20)")
        print(f" Feed, {self.warehouse.supplies['feed']:.2f} (capacity=400)")
        print(f" Salt, {self.warehouse.supplies['salt']:.2f} (capacity=200)\n")
        print("Warehouse Auxiliary:")
        print(f" Fertiliser, {self.warehouse.supplies['fertilizer']:.2f} (capacity=10)")
        print(f" Feed, {self.warehouse.supplies['feed']:.2f} (capacity=200)")
        print(f" Salt, {self.warehouse.supplies['salt']:.2f} (capacity=100)\n")
        print("Technicians:")
        for tech in self.technicians:
            print(f" Technician {tech.name}, weekly rate={tech.weekly_rate}")
        
    def restock_supplies(self):
        """
        Restocks supplies from vendor if hatchery has enough cash.
        """
        print("\nList of Vendors")
        print(" 1. Slippery Lakes: price=0.30, demand=0.10, delivery fee=0.05")
        print(" 2. Scaly Wholesaler: price=0.20, demand=0.40, delivery fee=0.25")
        vendor_choice = self.get_integer_input(">>> Enter the number of vendor you want to restock supplies from: ")
        vendor = self.vendors[vendor_choice - 1]
        
        if self.cash > vendor.get_delivery_cost():
            self.cash -= vendor.get_delivery_cost()
            self.warehouse.add_supplies(vendor.supply())
        else:
            print(f"Not enough cash to buy from {vendor.name}.")
    
    def get_integer_input(self, prompt):
        """
        Helper function to ensure valid integer input.
        """
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
