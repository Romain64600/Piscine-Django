def my_var():

    int_42 = 42
    _42 = "42"
    quarante2 = "quarante-deux"
    _42_float = 42.0
    _42_true = True
    _42_list = [42]
    _42_dict = {42: 42}
    _42_tuple = (42,)
    _42_set = set()
    print(int_42, 'est de type', type(int_42))
    print(_42, 'est de type', type(_42))
    print(quarante2, 'est de type', type(quarante2))
    print(_42_float, 'est de type', type(_42_float))
    print(_42_true, 'est de type', type(_42_true))
    print(_42_list, 'est de type', type(_42_list))
    print(_42_dict, 'est de type', type(_42_dict))
    print(_42_tuple, 'est de type', type(_42_tuple))
    print(_42_set, 'est de type', type(_42_set))
    return

if __name__ == '__main__':
    my_var()