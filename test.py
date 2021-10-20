var = 1
def function_name(arg1="Default1", arg2="Default2"):
    print("Hello.")
    print(arg1)
    print(arg2)
    global var 
    var = 2

print(var)
function_name()
print(var)