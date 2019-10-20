class Error(Exception):
    '''Base class for other exceptions.'''
    pass

class ValueSmallError(Error):
    '''Input value too small.'''
    pass

class valueLargeError(Error):
    '''Input value too large.'''
    pass

number = 10

while True:
    try:
        num = int(input("Enter a Number: "))
        if num<number:
            raise ValueSmallError
        elif num>number:
            raise valueLargeError
        break
    except ValueSmallError:
        print("This is too small.")
        print()
    except valueLargeError:
        print("This is too large.")
        print()
print("Congratulations you guessed correct.")