def num_sorter(input_file="random.txt",output_file="sort.txt",max_value=10**6):
    bitmap = [0] * (max_value + 1)
    
    # read input_file => bitmap
    with open(input_file, "r") as f:
        for line in f:
            num     = int(line.strip())
            bitmap[num] += 1
    
    # write bitmap => output_file
    with open(output_file,"w") as f:
        for num in range(1, max_value + 1):
            while bitmap[num] > 0:
                f.write(f"{num}\n")
                bitmap[num] -= 1

    return bitmap

def main():
    num_sorter()

if __name__ == "__main__": main()