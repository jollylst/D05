#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    num_input = input('Please enter one integer:')
    try:
        num = int(num_input)
        if num % 2 == 0:
            print(str(num)+' is even')
        else:
            print(str(num)+' is odd')
    except:
        print('Non-word numerals are not accepted!')
    return None


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    value = ""
    for num in range(1, 101):
        formatted_num = ('{:3}'.format(num))
        if num % 10 == 0:
            value = value + ' ' + formatted_num + '\n'
        else:
            value = value + ' ' + formatted_num
    print(value)




def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    total = 0
    count = 0
    num_input = ""
    average =""

    while True:
        num_input = input('Please enter one non-word numberals:')
        if num_input == 'done':
            break
        num = float(num_input)
        total += num
        count += 1
        average = total / count
    return average


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())


if __name__ == '__main__':
    main()
