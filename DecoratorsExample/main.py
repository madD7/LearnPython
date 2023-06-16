"""
Simple Decorator creation and usage example.
compute_execution_time decorator example.
"""
import time

def my_func():
    return "In myFunc()."


def my_root_func():
    print("We are inside my_root_func()")

    # Func defined inside a function.
    # The myRootFunc can return back mySubFunc()
    def my_sub_func():
        print("\tWe are inside mySubFunc()")
        return "\tValue returned by mySubFunc()"

    # Executing mySubFunc()
    my_sub_func()

    return my_sub_func
# End of myRootFunc()


def accepts_func_arg(new_func):
    print("We are inside a function that accepts another function as argument.")
    print("Executing the passed function")
    print(new_func())


# This is how to create a decorator
def new_decorator(original_func):

    # Create a wrap_func which will execute original_func
    def wrap_func():
        print("Printing before the original function")
        original_func()
        print("Printing after the original function execution")

    return wrap_func


@new_decorator      # Special syntax
def func_uses_decorator():
    print("I m func_uses_decorator")


def compute_execution_time(original_func):
    def log_time_func():
        cur_time = time.time()
        original_func()
        new_time = time.time()
        print("Execution time: " + str(new_time - cur_time))
    return log_time_func        # Return a function. Dont put '()'


@compute_execution_time
def my_wait_func():
    print("Entered my_wait_func")
    time.sleep(3)
    print("Exiting my_wait_func")
    return None


if __name__ == "__main__":
    # We are not executing myFunc, and assigning the return value from it to myFuncVar
    myFuncVar = my_func
    del my_func

    # Check the output.
    # The variable still points to the original function object.
    print(myFuncVar())

    # my_root_func returns a function
    newFuncVar = my_root_func()
    print(newFuncVar())        # Executing the returned function.

    accepts_func_arg(newFuncVar)

    # Passing a function to a decorator function
    # This is same a using a @ decorator.
    print("Passing newFuncVar to a decorator function")
    func_returned = new_decorator(newFuncVar)
    func_returned()

    # This function will print the lines of the wrap_func
    print("Executing Decorated function")
    func_uses_decorator()

    print("Time logging example ")
    my_wait_func()

    print("Exiting")
