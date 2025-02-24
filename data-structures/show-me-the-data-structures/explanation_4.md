## Reasoning Behind Decisions:
The function `is_user_in_group` is designed to determine whether a user belongs to a given group or any of its subgroups. 

To achieve this, the function iterates over the root group and its subgroups in search of the specified user. The iteration is implemented using a stack-based depth-first search (DFS) approach. If a user is found in the current group, the function returns `True`. Otherwise, the function extends the stack with the subgroups of the current group to continue the search.

## Time Efficiency:
The time complexity of the algorithm is **O(n)**, where **n** represents the total number of groups and users in the root group and its subgroups.

## Space Efficiency:
The space complexity of the algorithm is **O(m)**, where **m** is the number of groups containing any subgroup and users. This is because the function maintains a stack that stores only the groups being iterated at any given moment.