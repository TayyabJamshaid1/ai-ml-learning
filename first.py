class Account:
      def __init__(self):
            self.balance=0
            self.account_number=0

      def debit(self,amount):
          self.balance=self.balance-amount
          print(f"{amount} is debited and remaining balance is {self.remaining()}")

      def credit(self,amount):
          self.balance=self.balance+amount
          print(f"{amount} is credited and remaining balance is {self.remaining()}")


      def remaining(self):
          return self.balance

      
a1=Account()
a1.credit(1000)
a1.credit(5000)
a1.debit(3000)
