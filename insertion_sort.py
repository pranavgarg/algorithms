from __future__ import print_function

def insertion_sort(items, n, direction=0):
    """
    Given a list of items, insertion_sort will sort
    the list up to n members. direction of 0 sort the
    list in an ascending manner. Other numbers sort
    in descending order.
    """
    for i in range( 1, n ):
        j = i
        if not bool( direction ):
            while ( j > 0 ) and ( items[j] < items[j-1] ):
                items = swap( items, (j, j-1) )
                j -= 1
        else:
            while ( j > 0 ) and ( items[j] > items[j-1] ):
                items = swap( items, (j, j-1) )
                j -= 1

    return items

def swap(items, pair):
    """
    swap takes a list of items and a tuple with
    two integers of the list indexes and swap 
    the members before returning the list.
    """
    
    temp = items[pair[0]]
    items[pair[0]] = items[pair[1]]
    items[pair[1]] = temp

    return items

if __name__ == '__main__':
    my_list = [1, 3, 10, 56, 21, 9, 85, 21]
    
    new_list = insertion_sort( my_list, len(my_list) )
    assert new_list == [1, 3, 9, 10, 21, 21, 56, 85]

    new_list = insertion_sort( my_list, len(my_list), -1 )
    assert new_list == [85, 56, 21, 21, 10, 9, 3, 1]


