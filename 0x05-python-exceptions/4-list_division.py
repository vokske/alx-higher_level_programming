#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for i in range(list_length):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                new_list.append(0)
            elif not isinstance(my_list_1[i], (int, float))\
                    or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                new_list.append(0)
            elif my_list_2[i] == 0:
                print("division by 0")
                new_list.append(0)
            else:
                new_list.append(my_list_1[i] / my_list_2[i])

    except IndexError:
        print("out of range")
    finally:
        return new_list
