import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """
    char: Optional[str]
    freq: int
    left: Optional['HuffmanNode']
    right: Optional['HuffmanNode']

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    return frequency



def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """

    # Create a priority queue to store the nodes
    pq = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(pq)

    # Build the Huffman Tree
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(pq, parent)

    if len(pq) == 0:
        return None
    else:
        return pq[0]


def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """

    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = code
        return

    generate_huffman_codes(node.left, code + '0', huffman_codes)
    generate_huffman_codes(node.right, code + '1', huffman_codes)


def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """

    frequency = calculate_frequencies(data)
    binary_tree = build_huffman_tree(frequency)
    huffman_codes = {}
    generate_huffman_codes(binary_tree, "", huffman_codes)

    result_encoded_data = "".join(huffman_codes[char] for char in data)
    return result_encoded_data, binary_tree


def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """

    if tree is None:
        return ""

    result = ""
    current = tree
    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            result += current.char
            current = tree

    return result


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2: Empty String
    print("\nTest Case 2: Empty String")
    sentence = ""
    encoded_data, tree = huffman_encoding(sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert sentence == decoded_data
    print("Pass: Empty String")

    # Test Case 3: None Input
    print("\nTest Case 3: None Input")
    try:
        encoded_data, tree = huffman_encoding(None)  # This should raise an error
        decoded_data = huffman_decoding(encoded_data, tree)
        assert False, "Expected an exception for None input"
    except TypeError:
        print("Pass: None Input handled correctly")

    # Test Case 4: String with repeated characters
    print("\nTest Case 4: String with repeated characters")
    sentence = "aaaaaaaabbbbbbbcccccc"
    encoded_data, tree = huffman_encoding(sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert sentence == decoded_data
    print("Pass: String with repeated characters")

    # Test Case 5: Very long text
    print("\nTest Case 5: Very long text")
    sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." * 1000
    encoded_data, tree = huffman_encoding(sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert sentence == decoded_data
    print("Pass: Very long text")

