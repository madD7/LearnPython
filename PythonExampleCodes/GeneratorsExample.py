"""
Generator functions allow us to write a function that
sends back a value and then later resume to pickup where it left off.
Thus, they suspend & resume their EXECUTION & STATE from
the last point of value generation.
It allows to generate a sequence of values overtime.
When a generator function is compiled, they become an object that
supports an iteration protocol.

Advantages:
    Instead of having to compute an entire series of values upfront,
    the generator computes one value
    and waits until next value is called for.
"""


# Simple function that creates square of numbers.
# Stores result in memory (list) and results the memory.
def creates_squares(n):
    result = []
    for x in range(n):
        result.append(x ** 2)

    return result


# This is generator.
# the result is not stored in memory.
def create_cubes(n):
    for x in range(n):
        yield x ** 3


# Another generator example
def gen_fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b  # a = b and b = old a + old b
# End of gen_fibonacci


# Understanding next
def simple_gen():
    for x in range(3):
        yield x


if __name__ == "__main__":
    print(creates_squares(11))

    print("Lets yield some cubes")
    for x in create_cubes(3):
        print(x)

    print("Lets yield some more cubes. Counting now restarts from begining.")
    for x in create_cubes(4):
        print(x)

    print("Printing fibonacci")
    for x in gen_fibonacci(7):
        print(x)

    # Lets assign a simple_gen instance to gen.
    # gen is a generator object
    gen = simple_gen()
    print(gen)

    # Now watch this
    print("Printing next value from gen")
    print(next(gen))

    print("Printing one more next value from gen")
    print(next(gen))

    print("Printing next value from gen third time")
    print(next(gen))

    try:
        print(next(gen))
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
        print("Stop iteration causes the for loop to break when a gen is used in for loop.")

    # Though a string object is iteratable, the string can't be
    # iterated using the 'next()'. Thus string object is not iterator.
    # We need to turn string object into generator.
    s = "Hello World!"
    s_iter = iter(s)

    next(s_iter)
    next(s_iter)
    print(next(s_iter))  # Prints 'l'
    next(s_iter)
    print(next(s_iter))  # Prints 'o'