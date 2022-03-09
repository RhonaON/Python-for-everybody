score = input("Enter Score: ") 
try: 
  score = float(score)
  if score > 1.0: 
    print("Error, input is out of range")
    quit()
  elif score < 0.0:
    print("Error, input is out of range")
    quit()
  elif 1.0 >= score >= 0.9:
    print ("A Grade:" + str(score))
  elif 0.9 > score >= 0.8:
    print ("B Grade:" + str(score))
  elif 0.8 > score >= 0.7:
    print ("C Grade:" + str(score))
  elif 0.7 > score >= 0.6:
    print ("D Grade:" + str(score))
  elif 0.6 > score >= 0.5:
    print ("Fail") 
except:
  print("Please input a number")


