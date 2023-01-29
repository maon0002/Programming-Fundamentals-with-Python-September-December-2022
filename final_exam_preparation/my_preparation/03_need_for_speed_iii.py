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
