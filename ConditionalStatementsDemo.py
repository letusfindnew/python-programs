# IF condition it compares two values
#atmPIN = "1234"

#enteredPIN = input("Enter your ATM PIN:")

#if atmPIN == enteredPIN:
 #   print("You are authorized successfully..!")
#else:
 #   print("You have entered wrong PIN and Please try again...!")


#pin = 123
#for i in range(3):
    #yourAge = input("Enter your pin:") #"23"
    #yourAge = int(yourAge) #"19" -> 19
    #if yourAge == pin: # true or false
   #     print("You are logged in successfully..!")
  #  else:
 #       print("Please enter correct pin again")

#print("Your Internet banking account is locked now because you entered your PIN wrongly 3 times...")

age = 18

yourAge = input("Enter your age:") #"23"
yourAge = int(yourAge) #"19" -> 19
while yourAge > age:
    country = input("Enter your country:")
    if country == "INDIA":
        print("You are Major")
        #break
        yourAge = yourAge - 1
    else:
        print("You are not eligible...!")



