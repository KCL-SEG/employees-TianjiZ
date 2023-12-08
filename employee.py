"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay

    def __str__(self):
        base_str = f"{self.name} works on a base pay of {self.base_pay}."
        return base_str

class Commission:
    def __init__(self, amount):
        self.amount = amount

    def get_commission(self):
        return self.amount

class ContractCommission(Commission):
    def __init__(self, contracts, commission_per_contract):
        super().__init__(contracts * commission_per_contract)
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def __str__(self):
        return f"receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract."

class BonusCommission(Commission):
    def __init__(self, bonus):
        super().__init__(bonus)
        self.bonus = bonus

    def __str__(self):
        return f"receives a bonus commission of {self.bonus}."

class CommissionedEmployee(Employee):
    def __init__(self, name, base_pay, commission):
        super().__init__(name, base_pay)
        self.commission = commission

    def get_pay(self):
        return super().get_pay() + self.commission.get_commission()

    def __str__(self):
        base_str = super().__str__()[:-1]  # Remove the period at the end
        commission_str = self.commission.__str__()
        return f"{base_str} and {commission_str}. Their total pay is {self.get_pay()}."

# Employee instances
billie = Employee('Billie', 4000)
charlie = Employee('Charlie', 2500)  # Assuming Charlie's base pay is pre-calculated
renee = CommissionedEmployee('Renee', 3000, ContractCommission(4, 200))
jan = CommissionedEmployee('Jan', 3750, ContractCommission(3, 220))  # Assuming Jan's base pay is pre-calculated
robbie = CommissionedEmployee('Robbie', 2000, BonusCommission(1500))
ariel = CommissionedEmployee('Ariel', 3600, BonusCommission(600))  # Assuming Ariel's base pay is pre-calculated

