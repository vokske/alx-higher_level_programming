#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    '''
    This function deletes the item at a specific position in a list.

    Parameters:
    my_list: The provided list.
    idx: Index of the item to be deleted from the list.

    Returns:
    my_list: The modified list
    '''

    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        del(my_list[idx])
    return my_list
