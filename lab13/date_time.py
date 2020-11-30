import datetime


class DateTimeSupplier:

    def today(self):
        return datetime.date.today()


FRIDAY = 5
class DiscountCalculator:

    def __init__(self, date_supplier):
        self.date_supplier = date_supplier

    def calculate_discount(self, price):
        week_day = self.date_supplier.today().isoweekday()
        if week_day == FRIDAY:
            return price * 0.5
        else:
            return price * 0.9


def calculate_discount(price):
    week_day = datetime.date.today().isoweekday()
    if week_day == FRIDAY:
        return price * 0.5
    else:
        return price * 0.9


