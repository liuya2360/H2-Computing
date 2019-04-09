# OOP versions of WS1-S2 Solutions

# Vending Machine Problem

class VendingMachine():
    def __init__(self):
        self.drinkOptions = {"$1.20": 120, "$0.80": 80}
        self.changeOptions = [100, 50, 20, 10]

    def getOption(self):
        print("Available Options:")
        i = 1
        options = {}
        for key in self.drinkOptions.keys():
            print("{0:<5}{1:<10}".format("[" + str(i) + "]", key + " Drink"))
            options[i] = key
            i += 1
        validSelection = False
        while not validSelection:
            selection = input("\nPlease select one option: ")
            try:
                selection = int(selection)
                if selection < 1 or selection > len(self.drinkOptions):
                    raise ValueError()
            except:
                print("Invalid user input; option selected does not exist.")
            else:
                validSelection = True
        self.selection = options[selection]
        print()

    def getPayment(self):
        validPayment = False
        while not validPayment:
            credit = input("Please input an amount ($) you are " + \
                            "inserting into the machine: ")
            try:
                self.credit = int(float(credit) * 100)
                if (self.credit / 100) != float(credit) or \
                    self.credit % 10 != 0 or \
                    self.credit < self.drinkOptions[self.selection]:
                    raise ValueError()
            except:
                print("Invalid payment amount.")
            else:
                validPayment = True
        print()
            
    def computeChange(self):
        self.change = self.credit - self.drinkOptions[self.selection]
        tempChange = self.change
        self.c100 = tempChange // 100
        tempChange = tempChange % 100
        self.c50 = tempChange // 50
        tempChange = tempChange % 50
        self.c20 = tempChange // 20
        tempChange = tempChange % 20
        self.c10 = tempChange // 10

    def outputChange(self):
        print("Price of selected drink: " + self.selection)
        print("Amount paid: " + str(self.credit / 100))
        print("Change due: " + str(self.change / 100))
        print("\t$1.00 coins returned: " + str(self.c100))
        print("\t$0.50 coins returned: " + str(self.c50))
        print("\t$0.20 coins returned: " + str(self.c20))
        print("\t$0.10 coins returned: " + str(self.c10))
    
    def main(self):
        self.getOption()
        self.getPayment()
        self.computeChange()
        self.outputChange()
        


vm = VendingMachine()
vm.main()
