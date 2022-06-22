import inspect

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__


def open_browser(a):
    pass


def go_to_companyname_homepage(b,c):
    pass


def find_registration_button_on_login_page(d,f):
    pass



def print_func_name(func_name):
    name = func_name.__name__.replace("_"," ").capitalize()
    arg  = str(inspect.signature(func_name)).replace("(","").replace(")","")
    print("Имя функции:", name + ".", "Аргументы:", arg)

l = open_browser, go_to_companyname_homepage, find_registration_button_on_login_page

for func in l:
    print_func_name(func)


