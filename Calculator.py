class Calculator:

    def __init__(self, input1, input2):  # constractor
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        return self.input1 + self.input2  # add both num together

    def subtractor(self):
        return self.input1 - self.input2  # subtract both numbers input1 - input2

    def multiplier(self):
        return self.input1 * self.input2  # multiply both number together

    def divider(self):
        return round(self.input1 / self.input2, 2)  # input 1 devide input 2 and round to 2dp

    def clear(self):
        self.input1 = 0
        self.input2 = 0


if __name__ == "__main__":
    x = int(input("Please enter the first number: "))  # take in user input and convert it to int
    y = int(input("Please enter the second number: "))  # take in user input and convert it to int
    calc = Calculator(x, y)  # creates a new calculator object called calc
    print("Adder: "+str(calc.adder()))
    print("Subtractor: "+str(calc.subtractor()))
    print("Multiplier: "+str(calc.multiplier()))
    print("Divider: "+str(calc.divider()))
    print("Subtractor : "+str(calc.subtractor()))
    calc.clear()  # clears the input values then print the values of the 2 numbers
    print("Value after clear method num1 :"+str(calc.input1)+" num2 :"+str(calc.input2))
