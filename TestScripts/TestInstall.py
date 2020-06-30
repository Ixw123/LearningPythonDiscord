import numpy as np
import matplotlib.pyplot as plt
import random as rd
import math as m

def main():
    print("This is just a test file")
    x = np.linspace(0, 2*m.pi, 200) 
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()