class Order:
    items = []
    quatities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quatities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quatities[i] * self.prices[i]
        return total
        

"""
---Single Responsibility Principle---

Detached the Payment functionality from the Order class and created a new PaymentProcessor class.
Now, we can add any payment-related functionality to the PaymentProcessor class without burdening the Order class.
This way, each class will have a single responsibility, leading to increased cohesion and introducing coupling.
"""
class PaymentProcessor:
    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
    
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)
order.add_item("Mice", 3, 12)

print(f"Total price: {order.total_price()}")
paymentProcessor = PaymentProcessor()
paymentProcessor.pay_debit(order, "0372455")