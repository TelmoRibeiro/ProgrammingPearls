from random import randint

def random_generator(file_name="random.txt",num_count=10**6):
    with open(file_name,"w") as f:
        for _ in range(num_count):
            f.write(f"{randint(1, num_count)}\n")

def main():
    random_generator()

if __name__ == "__main__": main()