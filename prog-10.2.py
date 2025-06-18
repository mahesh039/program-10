try:
    num=int(input("enter a number:"))
    result=10/num
    print("Result:",result)
except valueError:
    print("Error:invalid input! please enter a valid number.")
except ZeroDevisionError:
    print("Error:Division by Zero!")
            
