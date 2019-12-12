from Monkey_Patching.add import *


class new:

    def new_add(a,b):
        return a-b

math.addition=new.new_add

print(math.addition(2,4))
print()