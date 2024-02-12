
def helo_decorator(fn):
    def wrapper(user):
        data="Hello !"+fn(user)
        return (data)
    return wrapper

        


@helo_decorator
def morning_greeting(user):
    return f"good morning {user}"
@helo_decorator

def afternoon_greeting(user):
    return f"good afternoon {user}"
@helo_decorator

def evening_greeting(user):
    return f"good evening {user}"

print(morning_greeting("hari"))