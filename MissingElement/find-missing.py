''' IDEA:
    mid + min =
        the value "expected" to be found on the halfway of [min,max]
    vector[mid] =
        the value "probed" and found halfway of [min,max] 

THE CODE ITSELF IS PROBLEMATIC BUT I BELIEVE TO BE CLOSE        
'''

def binary_search(min_value, max_value, vector):
    print(f"min: {min_value} | max:{max_value}")
    
    if min_value >= max_value:
        return min_value
    
    mid_value = (min_value + max_value) // 2
    print(f"mid: {mid_value}")
    
    if vector[mid_value] == mid_value + min_value:
        return binary_search(mid_value + 1, max_value, vector)
    else:
        return binary_search(min_value, mid_value, vector)

def get_num_vector(file_name="sort.txt"):
    vector = []
    with open(file_name,"r") as f:
        for line in f:
            num = int(line.strip())
            vector.append(num)
    return vector

def main():
    num_vector  = get_num_vector()
    missing_num = binary_search(1, 10**6, num_vector)
    print(f"missing_num: {missing_num}")

if __name__ == "__main__": main()