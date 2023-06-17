from MyPackage import myModule  # Importing the whole module
from MyPackage.mySubPackage.mySubModule import my_sub_func

"""
Execute function from myModule
"""


if __name__ == "__main__":
    print(__name__)
    myModule.my_func()      # Accessing the function with module name as the module was imported.
    my_sub_func()           # Accessing function directly as func was imported.

