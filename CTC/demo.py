#methods, class variables, instance variables, constructor etc.
#self keyword is mandatory for calling variables names into method
#new key word is not required to create object from class unlike java

class Calculator:
    num = 100  #class variables

    def __init__(self,a,b):         #default constructor is called
        self.firstnumber = a
        self.secondnumber = b      #instance variables. Self is nothing but the obj will be first passed to the constructor
        print("I am called automatically")

    def getData(self):
        print("I am now executing method in class calculator")

    def sum(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2,3)   #how many ever arguments you pass, that many aruguments should be defined in __init__ method
obj.getData()
print(obj.sum())