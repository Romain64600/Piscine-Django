def get_numbers():

    numbers_file = open("numbers.txt", "r")

    numbers = numbers_file.read()

    print(numbers.replace(",", "\n"))

    numbers_file.close()

    return

if __name__ == '__main__':
    get_numbers()