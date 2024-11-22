class FishSpecies:

    def __init__(self, name, fertilizer, feed, salt, maintenance_time, demand, price):

        self.name = name
        self.fertilizer = fertilizer  # in ml
        self.feed = feed  # in kg
        self.salt = salt  # in kg
        self.maintenance_time = maintenance_time  # in days
        self.demand = demand  # max number of fish to sell
        self.price = price  # price per unit of fish sold