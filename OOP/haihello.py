
def decor(fn):
    def wrapper():
        data="<b>{fn()}<b>"
        return data
    return wrapper

@decor
def get_hello():
    return ("Hello")
@decor
def get_hai():
    return("Hai")

print(get_hello())
