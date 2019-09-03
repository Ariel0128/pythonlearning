from scipy.constants import year

txt = "We have been together for {} years. We are {}. We have "


class Relationship:
    def __init__(self, year, gender, child):
        self.year = year
        self.gender = gender
        self.child = child

    def myfunc(self):
        print(txt.format(self.year, self.gender), end='')  # string format
        print(self.child, end='')
        if self.child == 1:
            print(' child.')
        else:
            print(" children.")


data1 = Relationship(5, "boy and girl", 5)
data1.myfunc()


class Partnership(Relationship):
    def __init__(self, year, gender, child, marriage):
        super().__init__(year, gender, child)  # class property inheritance
        self.marriage_status = marriage

    def myfunc(self):
        super().myfunc()  # class function inheritance
        print("we have " + str(self.marriage_status))


data2 = Partnership(3, 'girls', 'no', 'not married')
data2.myfunc()
data3 = Relationship(6, 'boys', 1)
data3.myfunc()


# iteration and stop iteration

class MyNumber:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        x = self.number
        if x <= 20:
            self.number += 1
            return x
        else:
            raise StopIteration


myclass = MyNumber(6)
myiter = iter(myclass)

for x in myiter:
    print(x)

