from CacheInfo import CacheInfo

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


def create_cache(num_sets, slots):
    cache = {}
    for i in range(num_sets):
        cache[i] = CacheInfo.initialize_cache_info_for_set(slots)
    
    return cache




