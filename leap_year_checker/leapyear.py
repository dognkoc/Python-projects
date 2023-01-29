#this project is for the leap year checking purposes. Leap year comes after every four years.
#  The systematicly checking gives us 
# if the year is evenly divided by 4 but not divided by 100 until it is divided by 400 is leap year.

ask = int(input("Please type the year that you want to check 'YYYY': "))

if ask % 4 == 0:
    if ask % 400 == 0 and ask % 100 !=0:
        print(f"{ask} is a leap year!")
    else:
        print(f"{ask} is not a leap year!")
