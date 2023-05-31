# Decoration: These are used to add extra new fucnction to an existing functions.
def div(a,b):
    print (a/b)
#div(4,2)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner
# To connect the two functions
div = smart_div(div)
div(2,4)