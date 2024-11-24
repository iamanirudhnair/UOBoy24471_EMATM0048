class Vendor:
    """
    The Vendor class stands for the supplier of the hatchery.
    It stores the information about prices of various supplies sold by the vendor.
    """
    def __init__(self, name, fertilizer_price, feed_price, salt_price):
        """
        Initializes a vendor with its name and prices for supplies.

        :param name: Vendor's name
        :param fertilizer_price: Per unit of fertilizer's price
        :param feed_price: Price per unit of feed
        :param salt_price: Per unit of salt's price
        """

        self.name = name
        self.prices = {
            'fertilizer': fertilizer_price,     # Setting price for fertilizer, feed & salt
            'feed': feed_price,
            'salt': salt_price
        }

    def get_price(self, supply_type):
        """
        Returns the price for provided supply type from particular vendor.

        :param supply_type: Supply type (fertilizer, feed or salt)
        :return: Price for the specified supply type
        """
        return self.prices.get(supply_type, 0)