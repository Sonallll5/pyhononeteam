def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
interest = simple_interest(45,3,7)
print(f"The simple interest is: {interest}")
