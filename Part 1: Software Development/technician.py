class Technician:

    def __init__(self, name, weekly_rate=500):
        self.name = name
        self.weekly_rate = weekly_rate

    def get_payment(self):
        return self.weekly_rate * 9  # 9 weeks of work per quarter
