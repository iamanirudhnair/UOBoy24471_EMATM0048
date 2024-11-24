class FishSpecies:
    """
    The class of Fish Species represents fish types, with specific needs and market details.
    """

    def __init__(self, name, fertilizer, feed, salt, maintenance_time, demand, price):
        """
        Initializes fish species with particular details.

        :param name: Fish species name
        :param fertilizer: Quantity of fertilizer needed for 1 fish 
        :param feed: Portion of feed required to produce 1 fish
        :param salt: Amount of salt required for one fish
        :param maintenance_time: Number of days took to raise 1 fish
        :param demand: Maximum fish number that can be sold in 1 quarter
        :param price: Price of 1 fish unit
        """
        self.name = name
        self.fertilizer = fertilizer  # in ml
        self.feed = feed  # in kg
        self.salt = salt  # in kg
        self.maintenance_time = maintenance_time  # in days
        self.demand = demand  # max number of fish to sell
        self.price = price  # price per unit of fish sold