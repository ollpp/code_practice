tmp = 0
def test1(x):
    global tmp
    tmp = x
    print(x)
    test2(2)

def test2(y):
    global tmp
    print(tmp+y)

test1(1)
print(tmp)