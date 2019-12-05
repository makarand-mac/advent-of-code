def first_quiz():

    with open("./2019/data/day_3.txt") as data:
        lines = data.read().splitlines()

        first_line_values = lines[0].split(",")
        second_line_values = lines[1].split(",")

        current_point = (0, 0)

        first_line_points = set()
        second_line_points = set()

        for point in first_line_values:

            action, steps = point[0], point[1:]
            
            for step in range(1, int(steps) + 1):

                if action == "R":
                    current_point = (current_point[0] + 1, current_point[1])
                    first_line_points.add(current_point)
                elif action == "L":
                    current_point = (current_point[0] - 1, current_point[1])
                    first_line_points.add(current_point)
                elif action == "U":
                    current_point = (current_point[0], current_point[1] + 1)
                    first_line_points.add(current_point)
                elif action == "D":
                    current_point = (current_point[0], current_point[1] - 1)
                    first_line_points.add(current_point)

        print(current_point)

        current_point = (0, 0)
        for point in second_line_values:

            action, steps = point[0], point[1:]

            
            for step in range(1, int(steps) + 1):

                if action == "R":
                    current_point = (current_point[0] + 1, current_point[1])
                    second_line_points.add(current_point)
                elif action == "L":
                    current_point = (current_point[0] - 1, current_point[1])
                    second_line_points.add(current_point)
                elif action == "U":
                    current_point = (current_point[0], current_point[1] + 1)
                    second_line_points.add(current_point)
                elif action == "D":
                    current_point = (current_point[0], current_point[1] - 1)
                    second_line_points.add(current_point)

        print(current_point)

        intersection_points = first_line_points.intersection(second_line_points)
        for int_point in intersection_points:

            distance = abs((0 - int_point[0])) + abs((0 - int_point[1]))
            print(distance, int_point)

def second_quiz():

    with open("./2019/data/day_3.txt") as data:
        lines = data.read().splitlines()

        first_line_values = lines[0].split(",")
        second_line_values = lines[1].split(",")

        first_steps_took = 0
        second_steps_took = 0

        current_point = (0, 0)

        first_line_points = list()
        second_line_points = list()

        for point in first_line_values:

            action, steps = point[0], point[1:]
            
            for step in range(1, int(steps) + 1):

                if action == "R":
                    current_point = (current_point[0] + 1, current_point[1])
                    first_line_points.append(current_point)

                    first_steps_took = first_steps_took + 1

                    if current_point == (6491, 1524):
                        break
                elif action == "L":
                    current_point = (current_point[0] - 1, current_point[1])
                    first_line_points.append(current_point)

                    first_steps_took = first_steps_took + 1
                    if current_point == (6491, 1524):
                        break
                elif action == "U":
                    current_point = (current_point[0], current_point[1] + 1)
                    first_line_points.append(current_point)

                    first_steps_took = first_steps_took + 1
                    if current_point == (6491, 1524):
                        break
                elif action == "D":
                    current_point = (current_point[0], current_point[1] - 1)
                    first_line_points.append(current_point)

                    first_steps_took = first_steps_took + 1
                    if current_point == (6491, 1524):
                        break
            
            if current_point == (6491, 1524):
                break
        print(first_steps_took)

        current_point = (0, 0)
        for point in second_line_values:

            action, steps = point[0], point[1:]

            for step in range(1, int(steps) + 1):

                if action == "R":
                    current_point = (current_point[0] + 1, current_point[1])
                    second_line_points.append(current_point)

                    second_steps_took = second_steps_took + 1
                    if current_point == (6491, 1524):
                        break
                elif action == "L":
                    current_point = (current_point[0] - 1, current_point[1])
                    second_line_points.append(current_point)
                    second_steps_took = second_steps_took + 1
                    if current_point == (6491, 1524):
                        break
                elif action == "U":
                    current_point = (current_point[0], current_point[1] + 1)
                    second_line_points.append(current_point)
                    second_steps_took = second_steps_took + 1
                    if current_point == (6491, 1524):
                        break
                elif action == "D":
                    current_point = (current_point[0], current_point[1] - 1)
                    second_line_points.append(current_point)
                    second_steps_took = second_steps_took + 1
                    if current_point == (6491, 1524):
                        break
            if current_point == (6491, 1524):
                break
        print(second_steps_took)
        print(first_steps_took + second_steps_took)

first_quiz()
print("\n\nSecond quiz output : \n")
second_quiz()