# The aim of this program is to calculate a total holiday cost = plane cost + hotel cost + car rental

# initiating user inputs to be stored in variables: I tried looking into a multiple choice but too difficult at this stage:

city_flights = input("Please choose one city destination: Florence, Rome or Naples? ")

num_nights = int(input("How many nights will you be staying at the hotel? "))

rental_days = int(input("How many days will you be renting a car for? "))


# creating functions to build a total holiday cost

# the hotel_cost function calculates the total hotel stay price using a budget nightly rate:
def hotel_cost(num_nights):
    hotel_night_rate = 80
    return num_nights * hotel_night_rate


# the plane_cost function uses an if/elif/else statement to bring back the cost of the plane ticket:
def plane_cost(city_flights):
    if city_flights == "Florence":
        flight_cost = 150
    elif city_flights == "Rome":
        flight_cost = 160
    else:
        flight_cost = 120
    return flight_cost


# the car_rental function calculates the total cost for the car rental using a budget daily rate (I could have used if/elif/else statements globally but this was not requested in the task?):
def car_rental(rental_days):
    daily_rental = 50
    return rental_days * daily_rental
    

# the holiday_cost function calculates the total cost of the holiday using the above functions (I found this redundant as I could have used variables to store each cost and add them up with a sum function?):
def holiday_cost(city_flights, num_nights, rental_days):
    total_holiday_cost = hotel_cost(num_nights) + plane_cost(city_flights) + car_rental(rental_days)
    return total_holiday_cost



# storing function values into variables to simplify print function (please feedback if wrong):
hotel = hotel_cost(num_nights)
plane = plane_cost(city_flights)
rental = car_rental(rental_days)
holiday = hotel + plane + rental


# using the print function to print a coincised output:
print(f"Holiday destination: {city_flights} \nTotal number of night stay: {num_nights} \nTotal number of car rental days {rental_days}")
print(f"The total cost for your holiday is £{holiday}, this includes: \n- Hotel cost £{hotel}; \n- Plane cost £{plane}; \n- Car rental cost £{rental}.")
    




