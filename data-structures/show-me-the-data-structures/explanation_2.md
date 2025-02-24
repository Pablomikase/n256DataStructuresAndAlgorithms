## Reasoning Behind Decisions

For the second problem, we had to find files beneath a given path with a specific file name suffix. To achieve this, the program uses a `for` loop to iterate over all the contents of the root directory. It then checks whether each found path is a file or a directory.

- If it is a file, the program verifies if the file name ends with the given suffix. If it does, the file name is appended to the list of found files.
- If it is a directory, the program recursively searches within that directory.

This process continues until all directories have been searched. The program then returns the list of found files.

## Time Efficiency

The time complexity of the program is **O(n)**, where **n** is the total number of directories and files in the root directory. This is because:

- The program iterates over all directories and files in the given root directory (**O(n)**).
- Checking whether a file name ends with the suffix is an **O(1)** operation.
- Appending a file name to the list of found files is an **O(1)** operation.
- Recursively searching directories results in visiting each file and directory once.

Thus, the overall time complexity is **O(n)**.

## Space Efficiency

The space complexity of the program depends on the input. If the input directory contains a large number of files and subdirectories, the space usage will increase accordingly. 

- The program stores the resulting file paths in a list, meaning the worst-case space complexity is **O(m)**, where **m** is the number of files matching the suffix.
- The recursive calls can increase memory usage in cases where there are many nested directories, leading to a space complexity of **O(d)**, where **d** is the depth of the directory tree.

Overall, the space complexity is **O(m + d)**.