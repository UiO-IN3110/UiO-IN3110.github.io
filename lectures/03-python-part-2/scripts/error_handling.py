def array(shape, *values):
    """Error example from the array class"""
    arr = []    
    n = len(values)
    if shape[0]*shape[1] != n:
        raise ValueError('The shape has to match the number of values provided') 
    
    for val in values:
        arr.append(float(val))
    return arr

A = array((1,6),,False,3,4,5,6)
print(A)


