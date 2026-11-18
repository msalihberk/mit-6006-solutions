def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    max_long = 0
    prev_long = 0
    prev_element = None
    for element in A:
        if prev_element is None:
            prev_element = element
            continue
        if element > prev_element:
            prev_long += 1
            if prev_long > max_long:
                max_long = prev_long
                count = 1
            elif prev_long == max_long:
                count += 1
        elif prev_long != 0:
            prev_long = 0
        prev_element = element

    if count == 0:
        count = len(A)
            
    return count
