#Python feature that we can use to make our code short.
# if want to use values of any list of tuples multiple times then better not to use index
# we can unpack the tuple or list like following
# list = [1, 2, 3]  OR tuple = (1, 2, 3)
# then instead of using list[0],list[1],list[2] or tuple[0], tuple[1] , tuple[2]
# use the following

coordinates = (1, 2, 3)

x,y,z = coordinates

print(x)
print(y)
print(z)
