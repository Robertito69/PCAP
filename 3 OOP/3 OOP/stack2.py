import sys

class Stack:
    def __init__(self):
        self.__stack_list = []
        
        
stack_object= Stack()
try:
    print(len(stack_object.stack_list))
except:
    print("El atributo es privado")