class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
def main():
    rect = Rectangle(3, 4)
    print("Width: ", rect.width)
    print("Height: ", rect.height)
    print("Area: ", rect.area())


if __name__ == "__main__":
    main()
