class Shape:
    pass

class Circle(Shape):
    pass

class Square(Shape):
    pass


def factory(type):
    if type == "Circle":
        return Circle()

    if type == "Square":
        return Square()


if __name__ == "__main__":

    c = factory("Circle")
    s = factory("Square")

    print(c)
    print(s)


