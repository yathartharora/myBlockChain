import datetime
import hashlib
import json

class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1,previous_hash = '0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain)+1 ,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions }
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof = new_proof + 1

        return new_proof

    def hash(self,block):
        encoded_block = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    def add_transaction(self,sender,receiver,amount):
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})

        previous_block = self.get_previous_block()
        return previous_block['index']+1

    def mine_block(bl):
        previous_block = bl.get_previous_block()
        previous_proof = previous_block['proof']
        proof = bl.proof_of_work(previous_proof)
        previous_hash = bl.hash(previous_block)
        block = bl.create_block(proof, previous_hash)
        response = {'message': "Congratulations, you just mined a block",
                    'index':block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash':block['previous_hash']
                    }
        return response['message']


    def get_chain(bl):
        response = {'chain': bl.chain,
                'length': len(bl.chain)
                }
        return response
