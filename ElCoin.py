# Simple cryptocurrence (ElCoin)

import hashlib
import time
import json

class Block:    
    def __init__(self, index, proof_no, prev_hash, data, timestamp=None): # Constructor for block created
        self.index = index # Index for each block
        self.proof_no = proof_no # Proof of work number for each block
        self.prev_hash = prev_hash # Previous block hashes to chain with new block
        self.data = data # Transaction data
        self.timestamp = timestamp or time.time() # Timestamp for each block

    @property
    def calculate_hash(self):
        # This function will calculate the hash of every block
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no, self.prev_hash, self.data, self.timestamp)
        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self): # Representation of the block format
        return "\n{} - {} - {} - {} - {}".format(self.index, self.proof_no, self.prev_hash, self.data, self.timestamp)
        


class Blockchain:
    def __init__(self): # Constructor for the blockchain
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

    def construct_genesis(self): # Construct the initial block
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash): # Constructs a new block and add it to the chain
        block = Block(index=len(self.chain), proof_no=proof_no, prev_hash=prev_hash, data=self.current_data)
        self.current_data = []
        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block, prev_block): # Checks whether the blockchain is valid
        if prev_block.index + 1 != block.index: # Condition to check the block index
            return False
        
        elif prev_block.calculate_hash != block.prev_hash: # Condition to compare previous hashes
            return False

        elif not Blockchain.verifying_proof(block.proof_no. prev_block.proof_no): # Condition to verify proof of work
            return False

        elif block.timestamp <= prev_block.timestamp: # Condition to compare based on timestamp
            return False

        return True # If all ok then it can be chained

    def new_data(self, sender, recipient, quantity): # Adds a new transactions to the data of the transactions
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proof_of_work(last_proof): # Security features of the blockchain
        proof_no = 0
        while Blockchain.verifying_proof(proof_no, last_proof) is False:
            proof_no +=1

        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self): # Returns the last block in the chain 
        return self.chain[-1]

    def block_mining(self, details_miner):
        self.new_data(
            sender="0",  # It implies that this node has created a new block
            recipient=details_miner, # Creating a new block (or identifying the proof number) is awarded with 1
            quantity=1,
        )

        last_block = self.latest_block
        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)
        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)

        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data): # Obtains block object from the block data

        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])


# We add the transaction here
blockchain = Blockchain()

print("Starting ElCoin mining ...")

# We try to add new transaction (AHMAD sends ALI some ElCoin)
last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)
blockchain.new_data(
    sender="AHMAD",
    recipient="ALI", 
    quantity=5,
)
last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("\nElCoin Transaction has been successful")
print(blockchain.chain) 


# Attempts to add another transaction in ElCoin
last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="SYAFIQ", 
    recipient="ZAFRAN",  
    quantity=10,
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)
print(blockchain.chain)



