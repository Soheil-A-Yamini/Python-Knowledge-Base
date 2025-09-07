# Pyramid Pattern Example

def print_pyramid(levels=5):
    for i in range(1, levels + 1):
        print(' ' * (levels - i) + '*' * (2 * i - 1))

if __name__ == "__main__":
    print_pyramid()