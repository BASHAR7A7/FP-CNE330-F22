import datetime
print (datetime.datetime.today().strftime("%H"))
print(datetime.datetime.today().strftime("%M"))
hour=int(input("Enter a Hour: "))
minute=int(input("Enter a Minute: "))
while True:
    if hour == int(datetime.datetime.today().strftime("%H")) and minute == int(datetime.datetime.today().strftime("%M")):
        print("Alarm Raised")
        break
    else:
        print("Alarm Not Raised")
        break