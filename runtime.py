
def foo(alist):
    print("This is foo")
    print(alist[3])

def bar(alist):
    print("This is bar")
    foo(alist)

def main():
    alist = [10, 20, 30]
    bar(alist)


main()