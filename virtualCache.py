import sys

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
