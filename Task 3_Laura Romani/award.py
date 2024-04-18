# designing program to assign award to thriatlon competitor
swimming = int(input("Provide time in minutes: "))
cycling = int(input("Provide time in minutes: "))
running = int(input("Provide time in minutes: "))
complete_thriatlon = (swimming + cycling + running)
print(complete_thriatlon)
if 0 <= complete_thriatlon <= 100 :
    print("You are awarded Provincial colours")

elif 101 <= complete_thriatlon <= 105 :
    print("You are awarded Provincial half colours")

elif 106 <= complete_thriatlon <= 110 :
    print("You are awarded Provincial scroll")

else :
    print("You have not won any award")


