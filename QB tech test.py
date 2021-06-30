# s='abcabcabcabc'
# t='abcabc'
# return 最小公约数 ‘abc’ 不能的话 -1
# string可以有乘法运算，除法不行

def func(s,t):
    s_len=len(s)
    t_len=len(t)
    if s_len%t_len!=0:
        return -1
    else:
        if t*(s_len//t_len)!=s:
            return -1
        else:
            for i in range(2,t_len//2+1):
                substring=t[:i]
                if substring*(t_len//i)==t:
                    return t[:i]
            return t
          
# or to be shorter:
def func(s,t):
    s_len=len(s)
    t_len=len(t)
    if s_len%t_len==0:
        if t*(s_len//t_len)==s:
            for i in range(2,t_len//2+1):
                substring=t[:i]
                if substring*(t_len//i)==t:
                    return t[:i]
            return t
    else:
      return -1
      
# optimization
# sum() can be replaced by 

for price in prices:
  total_price += price

# whole codes:

def calculateAmount(prices):
    # Write your code here
    discount = 0
    total_price = 0

    for price in prices:
        price_after_discount = price - discount
        if(price_after_discount < 0):
            price_after_discount = 0
            
        total_price += price_after_discount

        if(discount == 0):
            discount = price
        else:
            discount = min(price, discount)
       
    return total_price
