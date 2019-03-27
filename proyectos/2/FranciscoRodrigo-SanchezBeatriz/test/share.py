x = 5

class Foo():
    def foo_func(self):
        global x    # try commenting this out.  that would mean foo_func()
                    # is creating its own x variable and assigning it a
                    # value of 3 instead of changing the value of global x
        x += 3
        #print("X en Foo : %d" %x)

class Foo2():
    def foo2_fn(self):
        global x
        x +=5
        print("X en Foo2 : %d" %x)

def run():
    print("x antes detodo : %d" %x)
    Foo().foo_func()
    print("X en Foo : %d" %x)
    #Foo2().foo2_fn()

if __name__ == '__main__':
    run()
