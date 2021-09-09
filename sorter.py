# Sorter 
def sorter(array: list, mode: str= "ascending")-> list:
    """
        sorts an array of numbers in ascending or descending order.
    """

    for idx, val in enumerate(array):
        prev_val = prev(idx, array)
        shifted = [] 
        if idx: 
            if mode== "ascending":
                if val < prev_val:
                    # move back if current value is lth prev value.
                    shifted = sorter(shiftBack(idx, array), mode= mode)
                    
            elif mode== "descending":
                if val > prev_val:
                    # move back if current value is gth prev value.
                    shifted = sorter(shiftBack(idx, array), mode= mode)
            
    return array
    
    
def prev(idx: int, array: list):
    """
        Returns the previous value of the index provided.
        Returns None if index is 0.
    """
    if idx!= 0:
        return array[idx-1]

    
def shiftBack(idx: int, array: list)-> list:
    """
        shifts the index value one position back.
        Returns the new array or the original if index provided is zero.
    """
    if idx!= 0:
        temp = array[idx-1]
        array[idx-1] = array[idx]
        array[idx] = temp
    return array


if __name__== "__main__":
    a = [1, 4, 3, 0, 2, 5]
    print(sorter(a, mode="ascending"))
    print(sorter(a, mode="descending"))
