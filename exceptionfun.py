def divide_numbers():
       try:
        n1 =float(input("Enter the numerator:"))
        num2=float(input("Enter the denominator:"))
        if num2==0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result= n1/num2
       except ZeroDivisionError as e:
          print(f"Error:{e}")
       except ValueError:
          print("Error:invalid input.please enter the numeric values.")
       else:
          print(f"The result is :{result}")
       finally:
              print("Excuation completed")
divide_numbers()
          
                        