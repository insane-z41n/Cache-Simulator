from CacheInfo import CacheInfo

##Global LRU Queue:
q = []

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


class Cache:
    def __init__(self, num_sets, slots):
        self.num_sets = num_sets
        self.slots = slots
        self.cache = create_cache(num_sets, slots)
    
    def __str__(self):
        msg = ""
        for i in range(self.num_sets):
            msg += 'SET: {}\n'.format(i)
            for slot in self.cache[i]:
                msg+='\t{}'.format(slot)
        return msg

    def add_to_cache(self, setIndex, tag, data):
        print(self.cache)
        frames = self.cache[setIndex]
        for f in frames:
            if f.tag == "":
                f.tag = tag
                f.data = data
                f.val = 1
                LruPolicy(f.tag)
                self.cache[setIndex] = frames
                return "miss"
            elif tag == f.tag:
                LruPolicy(f.tag)
                self.cache[setIndex] = frames
                return "hit"
        
        evicted = LruPolicy(tag)
        for f in frames:
            if f.tag == evicted:
                f.tag = tag
                f.data = data
                f.val = 1
                self.cache[setIndex] = frames
                return "miss"


def create_cache(num_sets, slots):
    cache = {}
    for i in range(num_sets):
        cache[i] = CacheInfo.initialize_cache_info_for_set(slots)
    
    return cache



    

    





