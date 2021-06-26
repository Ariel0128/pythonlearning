# dictionary的用法：：：：
# pair data

Dict={}
for x in sorted(s):
    Dict[x]=Dict.get(x,0)+1   
#Sorting Dict by value (using Dict.get) & storing keys.
Dict_keys=sorted(Dict, key=Dict.get, reverse=True)  

for key in Dict_keys[:3]:
    print(key,Dict[key])

    #-----------------------    
    
# my version: too complicated

def funcname(string):
    uni_char=sorted(list(set(string)))
    num_list=[] #to store the char and its corresponding frequency
    for char in uni_char:
        num = sorted(string).count(char)
        num_list.append([char,num])
    num_list.sort(key=lambda x: x[1], reverse=True)
    print(num_list[0][0],num_list[0][1]) 
    print(num_list[1][0],num_list[1][1])
    print(num_list[2][0],num_list[2][1])
    
#############

    
# for语句的简写，注意对对象的处理要单独放在最前面，之前错写成 .append(...for... in.. if....)

def what(s,k):
    for i in range(0,len(s)//k):
        uni_char=[]
        char_list=list(s[k*i:k*i+k])
        [uni_char.append(char) for char in char_list if char not in uni_char]
        u= ''.join(uni_char)
        print(u)

#conditional function

def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0:
            if i%5==0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)
            
#process string -reverse & swapcase

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words=sentence.split(' ')
    new_string=' '.join(words[::-1]).swapcase()
    return new_string
  
# use while 
# avoid using calculation functions to save running time
# alternative: remove(max(order)) - time consuming

def filledOrders(order, k):
    # Write your code here
    n=sum(order)
    order.sort()
    while n>k:
        max_order=order.pop()
        n=n-max_order
    return len(order)
  
# not the best solution
# time consuming
def findSubstring(s, k):
    vowels=['a','e','i','o','u']
    list_of_num_vowels=[]
    string='Not found!'
    # Write your code here
    for i in range(0,len(s)-k+1):
        substr=s[i:i+k]
        num_vowels = sum(1 if a in vowels else 0 for a in substr)
        list_of_num_vowels.append(num_vowels)
    x=list_of_num_vowels.index(max(list_of_num_vowels))
    if max(list_of_num_vowels)>0:
        return s[x:x+k]
    else:
        return string

# 类似的：

def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum(1 if letter in vowels else 0 for letter in word)
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
