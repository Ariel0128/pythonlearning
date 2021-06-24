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
