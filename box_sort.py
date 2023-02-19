# Author: Aline Lindholm Lima Botti
# GitHub username: Aline-Lima
# Date: 01/31/2023
# Description: Box class whose init method takes three parameters

class Box:
    """class Box which has the methods: init, volume, get_length, get_width, get_height"""

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        result = self._length * self._width * self._height
        return result

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


def box_sort(box):
    """ uses insertion sort to sort a list of Boxes from greatest volume to least volume.
    It sorts the list "in place" by mutating the list """

    for i in range(1, len(box)):
        """ traversing the array from 1 to length of array(a)"""

        temp = box[i]

        """Shift elements of array[0 to i-1], that are
         greater than temp, to one position ahead
         of their current position"""

        j = i - 1
        while j >= 0 and temp.volume() > box[j].volume():
            box[j + 1] = box[j]
            j -= 1
        box[j + 1] = temp
    print(box)


def main():
    b1 = Box(3.4, 19.8, 2.1)
    b2 = Box(1.0, 1.0, 1.0)
    b3 = Box(8.2, 8.2, 4.5)
    box_list = [b1, b2, b3]
    box_sort(box_list)
    for box in box_list:
        print(box.volume())


main()