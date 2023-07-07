class VendingMachine:
    def __init__(self):
        self.state = 'Idle'
        self.juices = {'PEPS': 30, 'MOUN': 30, 'DPEP': 50, 'COKE': 20, 'GATO': 20, 'DCOK': 30, 'MINM': 25, 'TROP': 30}
        self.stock = {juice: 1 for juice in self.juices.keys()}

    def run(self):
        while True:
            if self.state == 'Idle':
                self.idle_state()
            elif self.state == 'Dispensing':
                self.dispensing_state()
            elif self.state == 'InsufficientFunds':
                self.insufficient_funds_state()
            elif self.state == 'OutOfStock':
                self.out_of_stock_state()
            elif self.state == 'RefillPrompt':
                self.refill_prompt_state()
            elif self.state == 'Refill':
                self.refill_state()

    def idle_state(self):
        print("Welcome to the vending machine!")
        print("List of drinks:")
        for juice, price in self.juices.items():
            print(f"{juice} - ${price}")

        user_input = input("Enter the four-letter code for your drink: ")
        if user_input.lower()=='refill':
            self.state = 'Refill'

        elif user_input in self.juices:
            if self.stock[user_input] > 0:
                cost = self.juices[user_input]
                amount = float(input("Enter the amount of money you will feed: "))
                if amount == cost:
                    print("Dispensing drink...")
                    self.stock[user_input] -= 1
                    self.state = 'Dispensing'
                elif amount < cost:
                    self.state = 'InsufficientFunds'
                else:
                    change = amount - cost
                    print(f"Dispensing drink and returning ${change} in change.")
                    self.stock[user_input] -= 1
                    self.state = 'Dispensing'
            elif sum(self.stock.values())==0:
                self.state = 'RefillPrompt'
            else:
                self.state = 'OutOfStock'   
        else:   
            print("Invalid input. Please try again.")

    def dispensing_state(self):
        print("Enjoy your drink!")
        self.state = 'Idle'

    def insufficient_funds_state(self):
        print("The entered amount is less than the cost. Please enter a sufficient amount.")
        self.state = 'Idle'

    def out_of_stock_state(self):
        print("Selected juice is out of stock. Please choose another drink.")
        self.state = 'Idle'

    def refill_prompt_state(self):
        print("Please refill all the juices.")
        self.state = 'Idle'

    def refill_state(self):
        print("Vending Machine has been refilled...")
        self.stock = {juice: 1 for juice in self.juices.keys()}
        self.state = 'Idle'

# Run the vending machine
machine = VendingMachine()
machine.run()
