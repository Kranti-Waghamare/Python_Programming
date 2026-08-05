print("------------------------------------------------------")
print("------------ Ticket Pricing Software -----------------")
print("------------------------------------------------------")

print("Enter your Age : ")
Age = int(input())

if(Age <= 5):
    print("You are Free")
elif(Age > 5 and Age <= 18):
    print("Ticket price is 900")
elif(Age > 18 and Age <= 45):
    print("Ticket price is 1200")
else:
    print("Ticket Price is 500")