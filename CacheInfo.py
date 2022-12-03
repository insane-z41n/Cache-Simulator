class CacheInfo:
    def __init__(self, way, tag, val, data):
        self.way = way
        self.tag = tag
        self.val = val
        self.data = data

    def initialize_cache_info_for_set(slots):
        s = []
        for i in range(slots):
            #                way|tag|val|data
            s.append(CacheInfo(i, "", 0, ""))
        return s

    def __str__(self):
        return 'way: {} | tag: {} | val: {} | data: {}\n'.format(
            self.way, 
            self.tag,
            self.val,
            self.data
        )
