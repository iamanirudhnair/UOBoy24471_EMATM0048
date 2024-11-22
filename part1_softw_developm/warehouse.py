import math

class Warehouse:

    def __init__(self, capacity_main, capacity_aux, costs):

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
        self.costs = costs
    
    def apply_depreciation(self):

        for supply_type, amount in self.supplies.items(): # Loop through each supply type
            depreciation = math.ceil(amount * self.depreciation_rate[supply_type])
            self.supplies[supply_type] -= depreciation

    def get_total_cost(self):
        total_cost = 0
        for supply_type, amount in self.supplies.items():
            total_cost += amount * self.costs[supply_type]
        return total_cost