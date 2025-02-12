from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict() #uses a hashMap internally
        self.capacity = capacity

    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        found_value = self.cache.get(key, -1)
        if found_value != -1:
            # Move the key to the end to indicate that it was recently used
            self.cache.move_to_end(key)
        return found_value

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2 - tests the limit of the cache
    my_cache = LRU_Cache(5)
    assert my_cache.get(1) == -1
    my_cache.set(1, 1)
    my_cache.set(2, 2)
    my_cache.set(3, 3)
    my_cache.set(4, 4)
    my_cache.set(5, 5)
    my_cache.set(6, 6)
    assert my_cache.get(1) == -1
    assert my_cache.get(2) == 2
    assert my_cache.get(3) == 3
    assert my_cache.get(4) == 4
    assert my_cache.get(5) == 5
    assert my_cache.get(6) == 6

    # Test Case 3 - Tests when cache moves elements and don't delete its value
    other_cache = LRU_Cache(3)
    other_cache.set(1, 'A')
    other_cache.set(2, 'B')
    other_cache.set(3, 'C')
    other_cache.get(1)
    other_cache.set(4, 'D')
    assert other_cache.get(1) == 'A'
    assert other_cache.get(2) == -1
    assert other_cache.get(3) == 'C'
    assert other_cache.get(4) == 'D'

    #Test Case 4 - Tests when an element is inserted multiple times
    cache = LRU_Cache(2)
    cache.set(1, 'A')
    cache.set(2, 'B')
    cache.set(1, 'C')
    assert cache.get(1) == 'C'
    assert cache.get(2) == 'B'
    assert len(cache.cache) == 2
