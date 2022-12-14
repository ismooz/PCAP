def read_int(prompt, min, max):
    while True:
        try:
            response = int(input(prompt))
            if min <= response <= max:
                return response
            else:
                print("Error: the value is not within permitted range " + str(min) + ".." + str(max))
        except ValueError:
            print("Error: wrong input")

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)