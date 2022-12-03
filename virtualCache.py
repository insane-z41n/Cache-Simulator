import sys
from Cache import Cache
from collections import deque




## Calc Sets 
def calcSets(cacheSize, ways, cacheLineSize):
    
    sets = float((cacheSize)/(cacheLineSize*ways))
    # print("cacheSize ------> ", cacheSize)
    # print("cacheLineSize------> ", cacheLineSize)
    # print("ways------> ", ways)

    # print("cacheLineSize * ways------> ", cacheLineSize*ways)
    # print("SETS ------> ", sets)

    return sets


### DECONSTRUCT MEMORY ADDRESS TO TAG, SET INDEX, OFFSET BINARY REPRESENTATIONS
def parseMemAdd(memAdd, setindexbits, offsetbits):
    scale = 16
    
    # print ("memAdd in hex", memAdd)
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
    trace = instruction.strip().split(' ')
    pc_add = trace[0]
    read_write = trace[1]
    mem_add = trace[2]
    return pc_add, read_write, mem_add

# Return list of line from file given in arguments
# - List of lines from file
def read_file(filepath):
    f = open(filepath, "r")
    return f.readlines()

# Return Decimal from binary
# - Decimal value
def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

### CREATE CACHE -----------------------------

## Terminal Properties
termArgs = sys.argv;
# print(termArgs);

pyScript = termArgs[0]
filepath = termArgs[1]
cacheSize = 1024 if (len(sys.argv) < 3) else termArgs[2]
ways = 16 if (len(sys.argv) < 4) else int(termArgs[3])

# print("size: ", cacheSize)
# print("ways:" , ways)

setnum = calcSets(int(cacheSize), int(ways), 2**6)
cache = Cache(int(setnum), ways)
print(cache)

# Get all instructions from file
instructions = read_file(filepath)
count = 1 
error_lines = []
# Loop through each instruction  
for ins in instructions:

    try :
        pc_add, read_write, mem_add = parse_instruction(ins)
        tag, setIndex, offset = parseMemAdd(mem_add,1,6)

        cache.add_to_cache(binaryToDecimal(int(setIndex)), tag, pc_add)

    except Exception as e:
        print("ERROR -> ", e) 
        error_lines.append(count)
    count+=1
    # Get instruction infromation

#print(cache)

if len(error_lines) > 0:
    # TODO: DEBUG ONLY
    print("\nFile lines {} incurred an error when reading file {}".format(error_lines, filepath))
else:
    # TODO: DEBUG ONLY
    print("File Read")

