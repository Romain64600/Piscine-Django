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

#     import sys

#     total = len(sys.argv)

#     if len(sys.argv) == 1:
#         print('Unknow state')
#         return

#     if (sys.argv[1] in states):
#         capital = states[sys.argv[1]]
#         print(capital_cities[capital])
#     else:
#         print('Unknow state')

#     return

# if __name__ == '__main__':
#     data()

    import sys

    total = len(sys.argv)

    if len(sys.argv) == 1:
        print('Unknow state')
        return

    if (sys.argv[1] in capital_cities.values()):

        key_list = [k  for (k, val) in capital_cities.items() if val == sys.argv[1]]
        print(key_list)

        key_list2 = [h  for (h, val) in states.items() if val == key_list]
        print(key_list2)
        return


if __name__ == '__main__':
    data()