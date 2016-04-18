def checkio(f,g):
    def h(*args,**kwargs):
        ff, gg = None, None

        try: ff = f(*args, **kwargs)
        except: pass
        try: gg = g(*args, **kwargs)
        except: pass

        if ff == None and gg == None:
            return None, 'both_error'
        elif ff == None:
            return gg, 'f_error'
        elif gg == None:
            return ff, 'g_error'
        elif ff == gg:
            return ff, 'same'
        else:
            return ff, 'different'
    return h

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing

    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"

    # Remove odds from list
    f = lambda nums:[x for x in nums if ~x%2]
    def g(nums):
      for i in range(len(nums)):
        if nums[i]%2==1:
          nums.pop(i)
      return nums
    assert checkio(f,g)([2,4,6,8]) == ([2,4,6,8],'same'), "evens, first"
    assert checkio(f,g)([2,3,4,6,8]) == ([2,4,6,8],'g_error'), "evens, second"

    # Fizz Buzz
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (6)==('Fizz','same'), "fizz buzz, first"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (30)==('Fizz Buzz','same'), "fizz buzz, second"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (7)==('7','different'), "fizz buzz, third"
