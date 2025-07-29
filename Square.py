from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    

def main():
    square = Square(3)
    print("Area: ", square.area())

if __name__ == "__main__":
    main()
