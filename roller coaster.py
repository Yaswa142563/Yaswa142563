print("hello welcome to the roller coaster")
height =  int(input("enter your height in cm"))
if height>120:
    print("you are eligible to ride roller coaster")
    age = int(input("enter your age"))

    if age<15:
        bill = 5
        print(f"you should have to pay ${bill}")
    elif age<=18:
        bill = 7
        print(f"you should have to pay ${bill}")
    else:
        bill = 10
        print(f"you should have to pay ${bill}")
        need_snacks = input("do you need any snacks : yes or no")
        if need_snacks == "yes":
            bill = bill+3
            print(f"you bill is:${bill}")
        else:
            print(f"your bill is:${bill}")
else:
    print("sorry,you are not eligible to ride roller coaster")    