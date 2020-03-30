# LEGB RULE

# LOCAL
def report():
    # LOCAL ASSIGNMENT!!!
    x = 'local'
    print(x)

# ENCLOSING
x = 'THIS IS GLOBAL LEVEL'

def enclosing():
    x = 'Enclosing level'

    def inside():
        # LEGB
        print(x)
    inside()

enclosing()

# GLOBAL
x = 'THIS IS GLOBAL LEVEL'

def enclosing():
    # x = 'Enclosing level'

    def inside():
        # LEGB
        print(x)
    inside()

enclosing()
# BUILT IN

# GRAB GLOBAL
x = 'outside'

def report():
    # HEY GRAB THE GLOBAL LEVEL x VARIABLE!
    global x
    # REASSIGN GLOBALx
    x = 'inside'
    return x

print(report())
print()