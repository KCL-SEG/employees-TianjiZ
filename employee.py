"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary_or_hours, hourly_rate=None):
        self.name = name
        self.salary = salary_or_hours if hourly_rate is None else salary_or_hours * hourly_rate
        self.hourly_rate = hourly_rate
        self.commission = 0
        self.contract_count = 0

    def add_commission(self, commission, contract_count=0):
        self.commission = commission
        self.contract_count = contract_count

    def get_pay(self):
        return self.salary + self.commission

    def __str__(self):
        if self.hourly_rate is None:
            base_str = f"{self.name} works on a monthly salary of {self.salary}."
        else:
            hours = self.salary // self.hourly_rate
            base_str = f"{self.name} works on a contract of {hours} hours at {self.hourly_rate}/hour."

        if self.commission > 0:
            if self.contract_count > 0:
                commission_str = f" and receives a commission for {self.contract_count} contract(s) at {self.commission // self.contract_count}/contract"
            else:
                commission_str = f" and receives a bonus commission of {self.commission}"
            return f"{base_str}{commission_str}. Their total pay is {self.get_pay()}."
        else:
            return f"{base_str} Their total pay is {self.get_pay()}."

# Employee instances
billie = Employee('Billie', 4000)
charlie = Employee('Charlie', 100, 25)
renee = Employee('Renee', 3000)
renee.add_commission(800, 4)
jan = Employee('Jan', 150, 25)
jan.add_commission(660, 3)
robbie = Employee('Robbie', 2000)
robbie.add_commission(1500)
ariel = Employee('Ariel', 120, 30)
ariel.add_commission(600)
