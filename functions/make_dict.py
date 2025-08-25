def make_dict(root_name, lists):
    dict_to_return = {}
    for i in range(len(lists)):
        dict_to_return.update({f'{root_name}{i+1}': lists[i]})
    return dict_to_return


def list_to_string(list):
    string = ", ".join(list)
    string = string.replace(', ', '\r\n')

    return string


# pot_1 = ['Martin', 'Natille', 'Cecile', 'Alex']
# pot_2 = ['David', 'Kushner', 'Dominic', 'Fike']
# pot_3 = ['HI', 'BYE', 'GOOD', 'HELLO']
# pot_4 = ['Change', 'Dollars', 'Money', 'Coin']

# root_name = 'pot'
# lists = [pot_1, pot_2, pot_3, pot_4]

# print(list_to_string(pot_1))

# print(make_dict(root_name, lists))