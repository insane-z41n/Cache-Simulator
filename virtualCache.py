import sys
from collections import deque

##Global LRU Queue:
q = [];

##TODO for debug
def revListPrint(queue):
    for i,e in reversed(list(enumerate(q))):
        print(i,e)


### LRU QUEUE -------------------------------------
def LruPolicy(data):
    # q = queue[-1: 0]
    # print("q: ", q)
    for i,e in reversed(list(enumerate(q))):
        if(i == 0): #Reached last used element
            # print("last")
            q.pop(i)
            q.append(data)
            return e
        elif(e == data): #Found Match in Queue, so pop that element and shift other rows, add data to end of queue
            # print("match")
            q.pop(i)
            q.append(data)
            return data

    #Queue is empty, so simply add your data
    q.append(data)
    return data

### HELPER FUNCTION --------------------------

# Read instruction line and return information needed
# - PC Address
# - R/W Character
# - Memory Address
def parse_instruction(instruction):
    trace = ins.strip().split(' ')
    pc_add = trace[0]
    read_write = trace[1]
    mem_add = trace[2]
    return pc_add, read_write, mem_add

# Return list of line from file given in arguments
# - List of lines from file
def read_argument(arg):
    if len(arg) < 2:
        print("Please input the file")
        exit

    f = open(arg[1], "r")
    return arg[1], f.readlines()

### CREATE CACHE -----------------------------

# Get all instructions from file
file_name, instructions = read_argument(sys.argv)
count = 1 
error_lines = []
# Loop through each instruction  
for ins in instructions:

    try :
        pc_add, read_write, mem_add = parse_instruction(ins)
    except: 
        error_lines.append(count)
    count+=1
    # Get instruction infromation

if len(error_lines) > 0:
    # TODO: DEBUG ONLY
    print("\nFile lines {} incurred an error when reading file {}".format(error_lines, file_name))
else:
    # TODO: DEBUG ONLY
    print("File Read")

