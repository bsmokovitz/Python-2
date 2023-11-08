def readint(prompt, min, max):
    while True:
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
        except ValueError:
            print("Error: wrong input")
        except:
            print("Error: the value is not within permitted range (min..max)")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)