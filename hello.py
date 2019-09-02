from scipy.constants import year


class Relationship:
    def __init__(self, year, gender, child):
        self.year = year
        self.gender = gender
        self.child = child

    def myfunc(self):
        print("We have been together for " + str(self.year) + " years. We are " + str(self.gender), end='')
        print(". We have " + str(self.child), end='')  # use str() to concat strings
        if self.child == 1:
            print(' child.')
        else:
            print(" children.")


data1 = Relationship(5, "boy and girl", 5)
data1.myfunc()


class Partnership(Relationship):
    def __init__(self, year, gender, child, marriage_status):
        Relationship.__init__(self, year, gender, child)


data2 = Partnership(3, 'girls', 'no', 'not married')
data2.myfunc()
data3 = Relationship(6, 'boys', 1)
data3.myfunc()

# how to print Partnership properties
