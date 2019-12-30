import random
import time

def gen_tree():
    print("\033c")
    for i in range(1, 30, 2):
        line = random.randint(1, 30)
        if i==1:
            ch="@"
        elif line%3==0:
            ch="^"
        elif line%4==0:
            ch="o"
        else:
            ch = "*"
        print("{:^35}".format(ch*i))
    print("{:^35}".format(" /\ "))
    print("{:^35}".format(("_"*int((i/2)))+"/  \_"+"_"*int((i/2))))
    time.sleep(.75)
    gen_tree()

gen_tree()


