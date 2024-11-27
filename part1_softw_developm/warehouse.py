import math # Importing math module for mathematical functions

class Warehouse:
    """
    The Warehouse class manages the supplies (fertilizer, feed & salt) for the hatchery.
    It computes costs and manages depreciation of supplies.
    """
    def __init__(self, capacity_main, capacity_aux, costs):
        """
        Initializes warehouse with given quantitities and costs of supplies.

        :param capacity_main: Supply capacity of main warehouse
        :param capacity_aux: Auxiliary warehouse's supply capacity
        :param costs: Dictionary with costs per unit of fertilizer, feed, and salt
        """
        self.capacity_main = capacity_main # Setting capacity for the main and auxilliary warehouse
        self.capacity_aux = capacity_aux
        self.supplies = {
            'fertilizer': 0, # Initializing supplies with 0 units
            'feed': 0,
            'salt': 0
        }
        self.depreciation_rate = {
            'fertilizer': 0.4, # Depreciation rates of supplies
            'feed': 0.1,
            'salt': 0.0
        }
        self.costs = costs  # cost per litre/g for each supply type
    
    def add_supply(self, supply_type, amount):
        """
        Adds specific quantity of supplies to the warehouse.

        :param supply_type: Type of supplies (fertilizer, feed, salt)
        :param amount: Capacity to be added to the warehouse
        """
        if supply_type in self.supplies:
            self.supplies[supply_type] += amount # Adding specified amount to current supply
    
    def apply_depreciation(self):
        """
        Calculates depreciation to the warehouse supplies, diminishing their value over time.
        Depreciation is based on presumed rates.
        """
        for supply_type, amount in self.supplies.items(): # Loop through each supply type
            depreciation = math.ceil(amount * self.depreciation_rate[supply_type])
            self.supplies[supply_type] -= depreciation # Subtract depreciation from the supply

    def get_total_cost(self):
        total_cost = 0
        for supply_type, amount in self.supplies.items():
            total_cost += amount * self.costs[supply_type] # Adding the cost for each supply
        return total_cost