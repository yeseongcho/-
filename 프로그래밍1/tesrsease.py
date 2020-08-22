import math

"""
i = int
angle = (2 * math.pi / 40) * i
"""

def compute_and_plot(x):
    no_of_symbols = int(math.sin(x)*40+40+0.5)
    print(no_of_symbols)

def main():
    angle = 0
    for i in range(41):
        angle = (2 * math.pi / 40) * i
        compute_and_plot(angle)

main()
