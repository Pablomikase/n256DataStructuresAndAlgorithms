
## Reasoning Behind Decisions:
The LRU cache problem was solved using a class that has a parameter called `capacity`, which represents the number of slots the cache will have to store data. Additionally, this class needs a data structure to store the data, and the `OrderedDict` from Python is used. The `OrderedDict` class was chosen because it allows access to its content using indexes and internally utilizes a hash map.

## Time Efficiency:
The time complexity of the `get` method is **O(1)** because the `OrderedDict` class allows direct access to its content using indexes and internally uses a hash map.  
The time complexity of the `set` method is **O(1)** for the same reason, as accessing, inserting, and moving elements within an `OrderedDict` is done in constant time.

## Space Efficiency:
The space complexity depends on the maximum size of the cache, which is determined by the user since the class receives `capacity` as a parameter in the constructor. Thus, the space complexity is **O(c)**, where `c` is the capacity of the cache.
