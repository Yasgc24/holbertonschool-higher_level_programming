# 0x03. Python - Data Structures: Lists, Tuples
***

![image](https://user-images.githubusercontent.com/98331961/169903516-869ed9e4-afac-43d5-bece-d4bfa9104b9e.png)

## General
***
* Why Python progrRequirementsamming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the del statement and how to use it

## Requirements
***

### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc

### C
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* Your code should use the Betty style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called lists.h
* Don’t forget to push your header file
* All your header files should be include guarded

### Trace
To help you with your journey, feel free to try your code inside Trace. The link is available on each task.

You will be able to see in real time your code and what is really happening.

You can find [here](https://usebirch.notion.site/Concept-Page-for-Holberton-1cd776c97f1b4feb86b3d5a16bd71e30) a quick explanation about how to use it.

## Tasks
***

#### 0. Print a list of integers
Write a function that prints all integers of a list.
* Prototype: def print_list_integer(my_list=[]):
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings

You can test your code [here](https://www.learnwithtrace.com/problems/f722e93/code)

#### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.
* Prototype: def element_at(my_list, idx):
* If idx is negative, the function should return None
* If idx is out of range (> of number of element in my_list), the function should return None
* You are not allowed to import any module
* You are not allowed to use try/except

You can test your code [here](https://www.learnwithtrace.com/problems/1e0b0ab/code)

#### 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).
* Prototype: def replace_in_list(my_list, idx, element):
* If idx is negative, the function should not modify anything, and returns the original list
* If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use try/except

You can test your code [here](https://www.learnwithtrace.com/problems/9ecde09/code)

#### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.
* Prototype: def print_reversed_list_integer(my_list=[]):
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings

You can test your code [here](https://www.learnwithtrace.com/problems/26beeb9/code)

#### 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
* Prototype: def new_in_list(my_list, idx, element):
* If idx is negative, the function should return a copy of the original list
* If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
* You are not allowed to import any module
* You are not allowed to use try/except

You can test your code [here](https://www.learnwithtrace.com/problems/2d02d0c/code)

#### 5. Can you C me now?
Write a function that removes all characters c and C from a string.
* Prototype: def no_c(my_string):
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use str.replace()

You can test your code [here](https://www.learnwithtrace.com/problems/bd5290b/code)

#### 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.
* Prototype: def print_matrix_integer(matrix=[[]]):
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings

You can test your code [here](https://www.learnwithtrace.com/problems/971b4a5/code)

#### 7. Tuples addition
Write a function that adds 2 tuples.
* Prototype: def add_tuple(tuple_a=(), tuple_b=()):
* Returns a tuple with 2 integers:
  * The first element should be the addition of the first element of each argument
  * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value 0 for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

You can test your code [here](https://www.learnwithtrace.com/problems/e0f9149/code)

#### 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.
* Prototype: def multiple_returns(sentence):
* If the sentence is empty, the first character should be equal to None
* You are not allowed to import any module
You can test your code [here](https://www.learnwithtrace.com/problems/c2ae977/code)

#### 9. Find the max
Write a function that finds the biggest integer of a list.
* Prototype: def max_integer(my_list=[]):
* If the list is empty, return None
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin max()

You can test your code here](https://www.learnwithtrace.com/problems/b376843/code)

#### 10. Only by 2
Write a function that finds all multiples of 2 in a list.
* Prototype: def divisible_by_2(my_list=[]):
* Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module

You can test your code [here](https://www.learnwithtrace.com/problems/41c0317/code)

#### 11. Delete at
Write a function that deletes the item at a specific position in a list.
* Prototype: def delete_at(my_list=[], idx=0):
* If idx is negative or out of range, nothing change (returns the same list)
* You are not allowed to use pop()
* You are not allowed to import any module

You can test your code [here](https://www.learnwithtrace.com/problems/d064c24/code)

#### 12. Switch
Complete the source code in order to switch value of a and b
* You can find the source code here
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long

You can test your code [here](https://www.learnwithtrace.com/problems/c445f19/code)
