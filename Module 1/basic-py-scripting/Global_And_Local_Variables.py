#! /usr/bin/env python

hacker = "Shealth"

def local_variable_example():
    hacker = "You"
    print("The local variable is %s" % hacker)

local_variable_example();
print("The global variable is  %s" % hacker)