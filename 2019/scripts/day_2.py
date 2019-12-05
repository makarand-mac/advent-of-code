import math


def first_puzzle():

    with open("./2019/data/day_2.txt") as data:
        dataset = data.read().split(",")
        dataset = [int(value) for value in dataset]

        print(len(dataset))

        dataset[1] = 12
        dataset[2] = 2
        pointer = 0 
        opcode = dataset[pointer]

        operations = 0

        while opcode is 1 or opcode is 2:

            if opcode is 1:
                # Summation Operation

                first_value = dataset[dataset[pointer + 1]]
                second_value = dataset[dataset[pointer + 2]]

                dataset[dataset[pointer + 3]] = first_value + second_value
                pointer += 4
                opcode = dataset[pointer]

                operations += 1

            elif opcode is 2:
                # Multiplication Operation

                first_value = dataset[dataset[pointer + 1]]
                second_value = dataset[dataset[pointer + 2]]

                dataset[dataset[pointer + 3]] = first_value * second_value

                pointer += 4
                opcode = dataset[pointer]

                operations += 1
            
        
        print("Operations", operations)
        print("0 value", dataset[0])


def second_puzzle():

    with open("./2019/data/day_2.txt") as data:
        filedata = data.read().split(",")

        output = 0

        for verb in range(0, 100):
            for noun in range(0, 100):
                dataset = [int(value) for value in filedata]

                dataset[1] = verb
                dataset[2] = noun
                pointer = 0 
                opcode = dataset[pointer]

                operations = 0

                while opcode is 1 or opcode is 2:

                    if opcode is 1:
                        # Summation Operation

                        first_value = dataset[dataset[pointer + 1]]
                        second_value = dataset[dataset[pointer + 2]]

                        dataset[dataset[pointer + 3]] = first_value + second_value
                        pointer += 4
                        opcode = dataset[pointer]

                        operations += 1

                    elif opcode is 2:
                        # Multiplication Operation

                        first_value = dataset[dataset[pointer + 1]]
                        second_value = dataset[dataset[pointer + 2]]

                        dataset[dataset[pointer + 3]] = first_value * second_value

                        pointer += 4
                        opcode = dataset[pointer]

                        operations += 1 

                output = dataset[0]
                if output == 19690720:
                    print("Verb", verb)
                    print("Noun", noun)
                    break
            if output == 19690720:
                break

print("First puzzle output")
first_puzzle()
print("\nSecond puzzle output")
second_puzzle()
