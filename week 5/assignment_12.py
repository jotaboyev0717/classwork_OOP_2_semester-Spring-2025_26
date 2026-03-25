from abc import ABC, abstractmethod


class Billable(ABC):
    @abstractmethod
    def tip_amount(self):
        pass


class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass


class Order(Billable, Displayable):
    def __init__(self, dish, price):
        if price < 0:
            raise ValueError(f"Invalid price: {price}")
        self.dish = dish
        self.price = price

    def tip_amount(self):
        result = round(self.price * 0.15, 2)
        return result

    def display(self):
        result = f"{self.dish}: ${self.price:.2f}"
        return result


class HappyHourOrder(Order):
    def __init__(self, dish, price, discount):
        super().__init__(dish, price)
        self.discount = discount

    def final_price(self):
        result = round(self.price * (1 - self.discount), 2)
        return result

    def tip_amount(self):
        result = round(self.final_price() * 0.15, 2)
        return result

    def display(self):
        final_price = self.final_price()
        percent = int(self.discount * 100)
        result = f"{self.dish}: ${self.price:.2f} -> ${final_price:.2f} (-{percent}%)"
        return result


class DeliveryOrder(Order):
    def __init__(self, dish, price, delivery_rate):
        super().__init__(dish, price)
        self.delivery_rate = delivery_rate

    def tip_amount(self):
        result = round(self.price * 0.15 + self.price * self.delivery_rate, 2)
        return result

    def display(self):
        percent = int(self.delivery_rate * 100)
        result = f"{self.dish}: ${self.price:.2f} (delivery, fee {percent}%)"
        return result


class LoyaltyReward:
    def __init__(self, dish, price=0):
        self.dish = dish
        self.price = 0

    def tip_amount(self):
        result = 0.0
        return result

    def display(self):
        result = f"{self.dish}: $0.00 (loyalty reward)"
        return result


class BillSummary:
    def __init__(self):
        self.lines = []

    def add_line(self, description, tip):
        result = (description, tip)
        self.lines.append(result)
        return result

    def print_bill(self):
        for description, tip in self.lines:
            print(f"  {description} | tip: ${tip:.2f}")
        result = None
        return result


class TableBill:
    def __init__(self, guest_name):
        self.guest_name = guest_name
        self.orders = []
        self.summary = BillSummary()

    def add_order(self, order):
        self.orders.append(order)
        result = order
        return result

    def close(self):
        print(f"Bill for {self.guest_name}")

        subtotal = 0
        total_tips = 0

        for order in self.orders:
            description = order.display()
            tip = order.tip_amount()
            self.summary.add_line(description, tip)
            subtotal += order.price
            total_tips += tip

        self.summary.print_bill()

        grand_total = subtotal + total_tips

        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Total Tips: ${total_tips:.2f}")
        print(f"Grand Total: ${grand_total:.2f}")

        result = grand_total
        return result


bill = TableBill('Jasur')

bill.add_order(Order('Steak', 45))
bill.add_order(HappyHourOrder('Cocktail', 20, 0.50))
bill.add_order(DeliveryOrder('Sushi Set', 30, 0.20))
bill.add_order(LoyaltyReward('Free Dessert', 0))

try:
    bill.add_order(Order('Bad Dish', -15))
except ValueError as e:
    print(f'Skipped: {e}')

bill.close()

try:
    b = Billable()
except TypeError:
    print('Cannot instantiate abstract class')