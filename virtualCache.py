import sys
from collections import deque

## Terminal Properties
termArgs = sys.argv;
print(termArgs);

pyScript = termArgs[0]
filepath = termArgs[1]
cacheSize = termArgs[2]
ways = termArgs[3]

print("size: ", cacheSize)
print("ways:" , ways)


## Calc Sets 
def calcSets(cacheSize, ways, cacheLineSize):
    
    sets = (cacheSize)/(cacheLineSize*ways)
    return sets

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

### DECONSTRUCT MEMORY ADDRESS TO TAG, SET INDEX, OFFSET BINARY REPRESENTATIONS
def parseMemAdd(memAdd, setindexbits, offsetbits):
    scale = 16
    
    print ("memAdd in hex", memAdd)
    memAdd.split()
    bits = 4*(len(memAdd[2:]))
    # hex to binary
    res = str(bin(int(memAdd, scale))[2:].zfill(bits))

    ## Start index of all binary splits 
    offsetStart = bits-offsetbits
    setIndexStart = bits-(offsetbits+setindexbits)

    ## Generate each binary split based on required bits
    offset = res[offsetStart:]
    setIndex = res[setIndexStart:offsetStart]
    tag= res[:setIndexStart ]

    return tag, setIndex, offset




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

    f = open(filepath, "r")
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
        tag, setIndex, offset = parseMemAdd(mem_add,1,6)

        print("OFFSET: ", offset)
        print("SET INDEX: ", setIndex)
        print("TAG: ", tag)

        print("SETS: ", calcSets(cacheSize, ways, 2**6))

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

