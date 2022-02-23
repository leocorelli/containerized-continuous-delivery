import numpy as np

def list_squares(n: int):
    '''Prints the first n square numbers, beginning with 1.'''
    for i in range(1, n+1):
        print(f"{i}: {np.power(i,2)}")

if __name__ == "__main__":
    list_squares(10)