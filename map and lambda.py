cube= lambda x: x**3
cube(2)

def func(n):
  ---snip---
  return list_of_numbers

map(cube, func(n)) # create a new list


# Task: 用map和reduce函数， 把‘123.456’ 转化为 float 123.456

digits={'1':100,'2':20,'3':3,'4':0.4,'5':0.05,'6':0.006,'.':0}

def char_to_float(char):
    return digits[char]

s='123.456'

reduce(lambda x,y:x+y,list(map(char_to_float,s))) 

#map()的结果需要用list（）转化成list； map的对象可以是list也可以是string, 如果是string会把每个char当成一个list





