def login_required(func):
    def inner(is_login):
        if is_login==False:
         print('login required')
        else:
            return func(is_login)
    return inner
def home_page(is_login):
    print("home page")
def products(is_login):
    print("product page")
@login_required   
def orders(is_login):
    print("orders page")
@login_required
def profile(is_login):
    print("profile page")
home_page(True)
products(False)
orders(False)
profile(False)