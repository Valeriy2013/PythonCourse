class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# inheritance
class Rectangle(Shape):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def __str__(self):
        result = "Rect is at {0}, {1} - width is {2} and height is {3}"
        return result.format(self.x, self.y, self.width, self. height)


rect = Rectangle(10, 10, 150, 50)
print(rect)


class Language:
    def __init__(self, name, interpreted):
        self.__name = name
        self.__interpreted = interpreted

    def get_name(self):
        return self.__name

    # def set_name(self, name):
    #     if self.__name != name:
    #         self.__name = name

    def is_interpreted(self):
        return self.__interpreted

    def get_description(self):
        result = self.__name + ' is '
        if self.__interpreted:
            result += 'an interpreted language!'
        else:
            result += 'a compiled language!'
        return result


language = Language('C#', False)
print(language.get_name())
print(language.get_description())


class CSharp(Language):
    def __init__(self):
        Language.__init__(self, 'C#', False)


class Python(Language):
    def __init__(self):
        Language.__init__(self, 'Python', True)


class PHP(Language):
    def __init__(self):
        Language.__init__(self, 'PHP', True)


csharp = CSharp()
print(csharp.get_description())
python = Python()
print(python.get_description())
php = PHP()
print(php.get_description())
