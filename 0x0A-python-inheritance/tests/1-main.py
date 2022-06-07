#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(None)
my_list.append(8.37)
my_list.append(5.04)
my_list.append(None)
my_list.append(0.45)
print(my_list)
my_list.print_sorted()
print(my_list)