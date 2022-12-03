import sys
import math
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
    if(setindexbits == 0):
        setIndex = None

    tag= res[:setIndexStart]

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
t_bits = int(math.log2(setnum))
cache = Cache(int(setnum), ways)
# print("BEFORE:\n", cache)

# Get all instructions from file
instructions = read_file(filepath)
count = 1
miss_count = 0
hit_count = 0

error_lines = []
# Loop through each instruction  
f = open(filepath, 'r')
offset_change = ""
changes = []
while True:
    ins = f.readline()
    if not ins or ins == '#eof':
        break

    try :
        pc_add, read_write, mem_add = parse_instruction(ins)
        tag, setIndex, offset = parseMemAdd(mem_add,t_bits,6)
        if offset_change != "" and offset != offset:
            
            changes.append("OFFSET CHANGED:", offset)

        if(setIndex == None):
            setIndex = "0"

        result = cache.add_to_cache(binaryToDecimal(int(setIndex)), binaryToDecimal(int(tag)), pc_add)
        if result == 'miss':
            miss_count+=1
        else:
            hit_count+=1

    except Exception as e:
        error_lines.append("Input File Line: {} ERROR -> {}".format(count, e))
    count+=1
    # Get instruction infromation

print("CACHE:\n", cache)
print("T BITTIES: ", t_bits)
print("TOTAL MISSES: ", miss_count)
print("TOTAL HITS", hit_count)
print("Cache miss rate: {}% ".format(miss_count/(miss_count+hit_count) * 100))
if len(changes) > 0:
    print("CHANGE: " + changes)
if len(error_lines) > 0:
    # TODO: DEBUG ONLY
    for error in error_lines:
        print(error)
else:
    # TODO: DEBUG ONLY
    print("File Read Successfully")

