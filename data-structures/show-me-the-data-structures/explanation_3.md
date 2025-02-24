## Reasoning Behind Decisions:
For the Huffman Coding problem, the program is implemented using a priority queue to store the nodes of the tree. 
The priority queue is used to store the nodes in the order of their frequency. The nodes are then popped from the queue, 
and the tree is built by combining them. The tree is then traversed to get the codes for each character. 
The codes are then stored in a dictionary, which is used to encode the input string. 
The encoded string is then decoded using the tree, and the decoded string is returned.

## Time Efficiency:
The time complexity of the program is O(n log n), where n is the number of characters in the input string. 
The program first builds the tree using the priority queue, which takes O(n log n) time. 
The tree is then traversed to get the codes for each character, which takes O(n) time. 
The input string is then encoded using the codes, which takes O(n) time. 
The encoded string is then decoded using the tree, which takes O(n) time. 
So the total time complexity of the program is O(n log n).

## Space Efficiency:
The space complexity of the program is O(n), where n is the number of characters in the input string. 
The program uses a priority queue to store the nodes of the tree, which takes O(n) space. 
It also uses a dictionary to store the codes for each character, which takes O(n) space. 
So the total space complexity of the program is O(n).