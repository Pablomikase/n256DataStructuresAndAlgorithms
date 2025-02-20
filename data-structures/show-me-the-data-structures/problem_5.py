import hashlib
import datetime

class Block:
    """
    A class to represent a block in the blockchain.

    Attributes:
    -----------
    timestamp : datetime.datetime
        The timestamp when the block was created.
    data : str
        The data stored in the block.
    previous_hash : str
        The hash of the previous block in the chain.
    hash : str
        The hash of the current block.
    """

    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        """
        Constructs all the necessary attributes for the Block object.

        Parameters:
        -----------
        timestamp : datetime.datetime
            The timestamp when the block was created.
        data : str
            The data stored in the block.
        previous_hash : str
            The hash of the previous block in the chain.
        """
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.

        Returns:
        --------
        str
            The hash of the block.
        """
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        """
        Return a string representation of the block.

        Returns:
        --------
        str
            A string representation of the block.
        """
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")

class Blockchain:
    """
    A class to represent a blockchain.

    Attributes:
    -----------
    chain : list[Block]
        The list of blocks in the blockchain.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Blockchain object.
        """
        self.genesis_block = None
        self.chain = []


    def create_genesis_block(self) -> None:
        """
        Create the genesis block (the first block in the blockchain).
        """
        self.genesis_block = Block(datetime.datetime.now(), "genesis_block", "0")
        self.chain.append(self.genesis_block)


    def add_block(self, data: str) -> None:
        """
        Add a new block to the blockchain.

        Parameters:
        -----------
        data : str
            The data to be stored in the new block.
        """
        if self.genesis_block is None:
            self.create_genesis_block()
        last_block = self.chain[-1]
        new_block = Block(datetime.datetime.now(), data, last_block.calc_hash())
        self.chain.append(new_block)


    def __repr__(self) -> str:
        """
        Return a string representation of the blockchain.

        Returns:
        --------
        str
            A string representation of the blockchain.
        """
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

if __name__ == "__main__":
    # Test cases
    # Test Case 1: Create a blockchain and add blocks
    print("Test Case 1: Basic blockchain functionality")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)

    # Test Case 2
    block1 = Block(datetime.datetime.now(), "Data 1", "0")
    block2 = Block(datetime.datetime.now(), "Data 2", "0")
    print(block1)
    print(block2)
    assert block1.hash != block2.hash # Different data, different hash
    print("Test Case 2: Pass")

    # Test Case 3 - Create a blockchain with a genesis block
    blockchain = Blockchain()
    blockchain.create_genesis_block()
    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].data == "genesis_block"
    print("Test Case 3: Pass")

    #Test Case 4 - Validate previous hash is present in the current block
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    assert blockchain.chain[1].previous_hash == blockchain.chain[0].hash
    assert blockchain.chain[2].previous_hash == blockchain.chain[1].hash
    print("Test Case 4: Pass")

    #Test Case 5 - Add block with empty data
    blockchain = Blockchain()
    blockchain.add_block("")
    assert len(blockchain.chain) == 2
    print("Test Case 5: Pass")

    #Test Case 6 - Add long data to the block
    blockchain = Blockchain()
    long_data = "A" * (10 ** 6)  # 1 millón de caracteres
    blockchain.add_block(long_data)
    #Print chain to check how long the data is
    #print(blockchain)
    assert len(blockchain.chain) == 2
    print("Test Case 6: Pass")

