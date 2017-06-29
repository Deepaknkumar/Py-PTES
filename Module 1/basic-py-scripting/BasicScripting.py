#! /usr/bin/env python
import sys

# List Variables
list_example = [100,222,333,444,"Weird String"];
list_example_length = len(list_example);

for iteration in list_example:
    index_value = list_example.index(iteration);
    print("The length of list list_example is %s, the value as position %s is %s" % (str(list_example_length),str(index_value), str(iteration)));

print("List Variable Script finished!")

# Dictionary
dictionary_example = {'james':123, 'jack':456}
print(dictionary_example['james']);

# Arguments passed to script directly
arguments = sys.argv
print("The number of arguments passed was: %s" % str(len(arguments)));
i=0;
for x in arguments:
    print("The %d argument is %s" % (i,x))
    i += 1
end
