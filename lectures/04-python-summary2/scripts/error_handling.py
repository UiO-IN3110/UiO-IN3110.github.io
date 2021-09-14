def array(shape, *values):
    """Error example from the array class"""
    arr = []    
    n = len(values)
    for val in values:
        arr.append(val)
    return arr

A = array((1,6),2,3,4,5,6)
print(A)


