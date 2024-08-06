unit=int(input("Enter the unit"))
if unit<=50:
         amount=unit*2.0

elif unit>=51 and unit<=100:
    amount=(50*2.0)+(unit-50)*2.50
elif unit>=101 and unit<=150:
    amount=(50*2.0)+(50*2.50)+(unit-100)*2.75
elif unit>=151 and unit<=250:
    amount=(50*2.0)+(50*2.50)+(50*2.75)+(unit-150)*5.25
else:
    amount=(50*2.0)+(50*2.50)+(50*2.75)+(50*5.25)+(unit-250)*6.30
print("Amount",amount)
