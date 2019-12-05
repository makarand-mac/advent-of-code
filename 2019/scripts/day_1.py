# Script Written by Makarand Deshpande (Github: makarand-mac)
import math


def first_puzzle():
    total_required_fuel = 0

    with open("./2019/data/day_1.txt") as data:
        dataset = data.read().splitlines()

        for point in dataset:
            mass = int(point)
            fuel_required = math.floor(mass / 3) - 2
            total_required_fuel = total_required_fuel + fuel_required

    print(total_required_fuel)


def second_puzzle():

    total_required_fuel = 0

    with open("./2019/data/day_1.txt") as data:
        dataset = data.read().splitlines()

        for point in dataset:
            mass = int(point)

            fuel_required_for_this_module = 0

            while mass > 1:
                fuel_required = math.floor(mass / 3) - 2
                if fuel_required < 1:
                    break
                else:
                    fuel_required_for_this_module = fuel_required + fuel_required_for_this_module
                    mass = fuel_required
            
            total_required_fuel = total_required_fuel + fuel_required_for_this_module
    
    print(total_required_fuel)

first_puzzle()
second_puzzle()