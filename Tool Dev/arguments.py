import sys

arguments = sys.argv
print("Items in the list 'arguments'")
print("-----------------------------")
print("arguments: \t\t\t" + str(arguments))
print("arguments[0] script name:\t" + arguments[0])
print("arguments[1] first arg:\t\t" + arguments[1])
print("arguments[2] second arg:\t" + arguments[2])
print("arguments[1:] all but [0]:\t" + str(arguments[1:]))