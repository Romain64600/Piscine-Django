def data():

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    import sys

    total = len(sys.argv)

    if len(sys.argv) == 1:
        print('Unknow state')
        return

    if (sys.argv[1] in states):
        capital = states[sys.argv[1]]
        print(capital_cities[capital])
    else:
        print('Unknow state')

    return

if __name__ == '__main__':
    data()