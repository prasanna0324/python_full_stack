def verify(func):
    def inner(name):
        if name == "Modi":
            print("Modi PM")
        else:
            return func(name)
    return inner