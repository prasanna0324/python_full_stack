def verify(func):
    def inner(name):
        if name == "Modi":
            print("Modi PM")
        else:
            return func(name)
    return  inner
@verify
def wish(name):
    print("hi",name,"GM")
wish("sree")
wish("teja")
wish("prasu") 