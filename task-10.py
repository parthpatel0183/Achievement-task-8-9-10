
print("Enter the length and width, to calculate perimeter and area od rectangle")

length=(int(input("Enter the length of the rectangle: ")))
width=(int(input("Enter the width of the rectangle: ")))

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def rectangle_area(self):
        return self.length*self.width
        
    def rectangle_perimeter(self):
        return 2*self.length*self.width

Rectangle = Rectangle(length, width)
print("The area of Rectangle is : ", Rectangle.rectangle_area(),"cm^2.")
print("The Perimeter of Rectangle is : ", Rectangle.rectangle_perimeter(),"cm.")