# Explanation of Union and Intersection Functions

## Union Function

### Reasoning Behind Decisions:
The `union` function computes the union of two linked lists by collecting all unique elements from both lists. 

   - To ensure that each element appears only once in the final result, sets are used to store the values from both linked lists.
   - This eliminates the need for checking duplicates manually and simplifies the logic.
   - Traverse both linked lists and store their values in separate sets.
   - Then, merge both sets into a single result set.
   - Once all unique values are collected, a new linked list is created, and the elements from the set are appended to it.

### Time Efficiency:
- **Traversing the first linked list:** `O(n)`
- **Traversing the second linked list:** `O(m)`
- **Adding elements to the set:** `O(1)` per element
- **Iterating through the set to append elements to the result list:** `O(n + m)`

**Total time complexity:** **O(n + m)**  
Where `n` is the number of elements in the first linked list and `m` is the number of elements in the second linked list.

### Space Efficiency:
- Two sets are used to store the unique elements of both lists: **O(n + m)**.
- The final linked list stores the union elements: **O(n + m)**.

**Total space complexity:** **O(n + m)**.

---

## Intersection Function

### Reasoning Behind Decisions:
The `intersection` function computes the intersection of two linked lists by finding common elements in both.

   - A set is created from the first linked list to store its values.
   - This allows for quick lookups when checking if an element from the second list exists in the first list.
   - Instead of using nested loops (`O(n * m)` complexity), a set lookup (`O(1)`) is used to determine if an element is in the first list.
   - This greatly improves performance compared to a naive approach.
   - A new linked list is created, and elements that are found in both sets are appended.

### Time Efficiency:
- **Traversing the first linked list:** `O(n)`
- **Adding elements of the first linked list to a set:** `O(n)`
- **Traversing the second linked list and checking for intersection:** `O(m)`

**Total time complexity:** **O(n + m)**.

### Space Efficiency:
- One set is used to store the first linked list’s elements: **O(n)**.
- The final linked list stores the intersection elements: **O(min(n, m))**, in the worst case where all elements intersect.

**Total space complexity:** **O(n + min(n, m))**.