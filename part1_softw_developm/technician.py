class Technician:

    """
    The class Technician stands for technician workers, 
    who are working in hatchery and are being paid on weekly basis.
    """
    def __init__(self, name, weekly_rate=500):
        """
        A technician being initialized with provided name and weekly rate.

        :param name: Technician's name
        :param rate weekly_rate: Amount weekly being paid to technician (default = 500)
        """

        self.name = name
        self.weekly_rate = weekly_rate

    def get_payment(self):
        """Return technician's pay for 9 weeks he worked (payment quarterly)
        
        :return: Quarterly total pay of the Technician
        """
        return self.weekly_rate * 9  # 9 weeks of work per quarter