no = 11              #Global variable

def Display():
    no = 21          #local variable
    print("From Display : ", no)

print("Before : ", no)

Display()

print("After : ", no)