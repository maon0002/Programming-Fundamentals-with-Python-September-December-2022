# Problem 3 - Need for Speed III
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#2.
#
# You have just bought the latest and greatest computer game – Need for Seed III. Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.
# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
#     • "Drive : {car} : {distance} : {fuel}":
#         ◦ You need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
#         ◦ If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel, and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
#         ◦ You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"
#     • "Refuel : {car} : {fuel}":
#         ◦ Refill the tank of your car.
#         ◦ Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up.
#         ◦ Print a message in the following format: "{car} refueled with {fuel} liters"
#     • "Revert : {car} : {kilometers}":
#         ◦ Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
#         ◦ If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
# Input/Constraints
#     • The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
#     • The fuel and distance amounts in the commands will never be negative.
#     • The car names in the commands will always be valid cars in your possession.
# Output
#     • All the output messages with the appropriate formats are described in the problem description.

# {'Audi A6': ['38000', '62'],
# 'Mercedes CLS': ['11000', '35'],
# 'Volkswagen Passat CC': ['45678', '5']}

def revert(car, kilometers, car_dict_temp):
    min_condition = True
    if car_dict_temp[car][0] - kilometers < 10000:
        car_dict_temp[car][0] = 10000
        min_condition = False
    else:
        if not min_condition:
            diff = abs(car_dict_temp[car][0] - 10000)
        else:
            diff = kilometers
            car_dict_temp[car][0] -= diff
        print(f"{car} mileage decreased by {diff} kilometers")
    return car_dict_temp


def refuel(car, fuel, car_dict_temp):
    if car_dict_temp[car][1] + fuel > 75:
        diff = abs(75 - car_dict_temp[car][1])
        car_dict_temp[car][1] = 75
        print(f"{car} refueled with {diff} liters")
    else:
        car_dict_temp[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    return car_dict_temp


def drive(car, distance, fuel, car_dict_temp):

    if car_dict_temp[car][1] < fuel:
        print("Not enough fuel to make that ride")
    if car_dict_temp[car][1] >= fuel:
        car_dict_temp[car][0] += distance
        car_dict_temp[car][1] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if car_dict_temp[car][0] > 100000:
        del car_dict_temp[car]
        print(f"Time to sell the {car}!")
    return car_dict_temp


# ('Audi A6', [10000, 65])
# ('Mercedes CLS', [11094, 24])
# ('Volkswagen Passat CC', [45678, 5])
def print_result(car_dict_temp):
    for cars in car_dict_temp.items():
        car = cars[0]
        mileage = cars[1][0]
        fuel = cars[1][1]
        print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


def actions(car_dict):
    car_dict_temp = car_dict.copy()
    while True:
        action_string = input()
        if action_string == "Stop":
            print_result(car_dict_temp)
            break

        commands = action_string.split(" : ")
        action = commands[0]
        car = commands[1]

        if action == "Drive":
            distance = int(commands[2])
            fuel = int(commands[3])
            car_dict_temp = drive(car, distance, fuel, car_dict_temp)
        elif action == "Refuel":
            fuel = int(commands[2])
            car_dict_temp = refuel(car, fuel, car_dict_temp)
        elif action == "Revert":
            kilometers = int(commands[2])
            car_dict_temp = revert(car, kilometers, car_dict_temp)


def car_storage_func(num):
    obtained_cars_dict = {}
    while num > 0:
        car_string = input()
        "{car}|{mileage}|{fuel}"
        car, mileage, fuel = car_string.split("|")
        obtained_cars_dict[car] = [int(mileage), int(fuel)]
        num -= 1
    actions(obtained_cars_dict)
    return obtained_cars_dict


obtained_cars = int(input())
car_storage_func(obtained_cars)
