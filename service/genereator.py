import random,string

class Generator() :

    def __init__(self) :
        pass

    def idrandom(self,size=6,chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def numerandom(self,lenght):
        sstring="abcdefghijklmoqprstxyz"
        return ''.join(random.choice(sstring) for x in range(lenght))

    def cnprandom(self,size=13,chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))       
