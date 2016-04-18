def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
