# set up input variables
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
  h = float(hrs)
  r = float(rate)
except:
  print("Error, please enter numeric input")
  quit()

print(hrs, rate)
# print h * r
if h > 40:
  reg = h * r
  ovr = (h - 40.0) * (r * 0.5)
  pay = reg + ovr
else:
  pay = h * r 
print("Pay:", pay)  

