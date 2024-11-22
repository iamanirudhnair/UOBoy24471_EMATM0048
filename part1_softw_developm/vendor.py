class Vendor:

    def __init__(self, name, fertilizer_price, feed_price, salt_price):

        self.name = name
        self.prices = {
            'fertilizer': fertilizer_price,     # Setting price for fertilizer, feed & salt
            'feed': feed_price,
            'salt': salt_price
        }

    def get_price(self, supply_type):

        return self.prices.get(supply_type, 0)