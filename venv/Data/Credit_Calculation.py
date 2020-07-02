import math
class CreditCalculation:
    payment = 0
    period = 0
    def calculate_payment(self, principal, period):
        self.period = period

        if principal / self.period > principal // self.period:
            lastpayment = (principal - ((self.period - 1) * math.ceil(principal / self.period)))
            self.payment = math.ceil(principal / self.period)
            print("Your monthly payment = {0} with last month payment = {1}.".format(int(self.payment), lastpayment))
        else:
            self.payment = principal / self.period
            print("Your monthly payment = {}".format(int(self.payment)))

    def calculate_months(self, principal, amount):

        if principal / amount > principal // amount:
            self.period = principal / amount
            print("It takes {} month to repay the credit".format(int(math.ceil(self.period))))
        else:
            print("It takes {} month to repay the credit".format(int(math.ceil(principal / amount))))

cc = CreditCalculation()
print("Enter the credit principal:")
principal = int(input())
print('What do you want to calculate?\n'
      'type "m" - for count of months,\n'
      'type "p" - for monthly payment')
if input() == 'p':
    print("Enter count of months:")
    month = int(input())
    cc.calculate_payment(principal, month)
else:
    print("Enter monthly payment:")
    payment = int(input())
    cc.calculate_months(principal, payment)