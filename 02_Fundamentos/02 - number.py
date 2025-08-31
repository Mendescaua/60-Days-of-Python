#int 
a = 10

#float
b = 2.5

print(a.is_integer()) #True
print(b.is_integer()) #False

#Decimal
from decimal import Decimal, getcontext # U need import first
getcontext().prec = 2  # Set precision to 2 decimal places
c = Decimal(2.50) + Decimal(10.23)
print(c)  # True

#round
soma = 2.50 + 10.23
print(round(soma))