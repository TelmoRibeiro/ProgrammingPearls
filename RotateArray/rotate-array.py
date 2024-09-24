''' PROBLEM:
    rotate the first i elements of an array a
    input: a[] = [e0,e1,e2,e3,e4] | i = 2
    ouput: a[] = [e2,e3,e4,e0,e1]
    b . c => c . b

    SOLUTION:
    a = b  . c
    ->
    a = bR . c
    ->
    a = bR . cR
    ->
    a = c . b

    reverse the first i elements in place
    reverse the remanining elements in place
    reverse the whole array


'''

def reverse(array, min_pos, max_pos):
    result = array.copy()
    for index in range(min_pos, max_pos + 1):
        result[index] = array[min_pos + max_pos - index]
    return result

def rotate(array,i):
    result = array.copy()
    result = reverse(result,0,i-1)
    result = reverse(result,i,len(result)-1)
    result = reverse(result,0,len(result)-1)
    return result

def main():
    i = 2
    array = [1,2,3,4,5]
    print(array)
    print(rotate(array,2))

if __name__ == "__main__": main()