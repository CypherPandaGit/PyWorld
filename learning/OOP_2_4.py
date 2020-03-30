def new_decorator(func):

    def wrap_func():
        print("some code before executing func")

        func()

        print("Code here after executing func()")

    return wrap_func

@new_decorator # == func_need_decorator = new_decorator(func_need_decorator)
def func_need_decorator():
    print("Please decorate me")


func_need_decorator()
