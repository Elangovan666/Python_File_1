#Functions for Arthimetic Operations

def Addition(Num1,Num2):
    return Num1+Num2
def Subtract(Num1,Num2):
    return Num1-Num2
def Multiple(Num1,Num2):
    return Num1*Num2
def Divide(Num1,Num2):
    return Num1/Num2

#Operaions

print("Enter the Opertions (1/2/3/4)\n"
      "1.Addition\n"
      "2.Subtract\n"
      "3.Multiple\n"
      "4.Divide")

#Choice

choice = int(input("Enter the Options: "))

#Value Passing

Num1 = int(input("Enter The First Value: "))
Num2 = int(input("Enter The Second Value: "))

#Arthimetic Operations

if choice == 1:
    print(Num1,"+",Num2,"=",Addition(Num1,Num2))
elif choice == 2:
    print(Num1,"-",Num2,"=",Subtract(Num1,Num2))
elif choice == 3:
    print(Num1,"*",Num2,"=",Multiple(Num1,Num2))
elif choice == 4:
    print(Num1,"/",Num2,"=",Divide(Num1,Num2))
else:
    print("Thanks for Visiting")