import hashlib
import time
from datetime import datetime

class block:
    def __init__(self,timestamp,index,data,previousHash,tough=2):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previousHash=previousHash
        self.tough=tough
        self.nonce=0
        self.hash=self.blockMining()

    def hashBlock(self):
        finalString= str(self.index)+str(self.timestamp)+str(self.data)+str(self.previousHash)+str(self.nonce)
        hashedString= hashlib.sha256(finalString.encode()).hexdigest()
        return hashedString
    
    def blockMining(self):
        print('Block Mining',self.index)
        hashComputed=self.hashBlock()

        while not hashComputed.startswith('0'*self.tough):
            self.nonce +=1
            hashComputed = self.hashBlock()

        print('Block',self.index,'mined & nonce =',self.nonce,'hash=',hashComputed)

        return hashComputed


class blockchain:
    def __init__(self):
        self.chain=[self.createGenesisBlock()]
        self.tough=2

    def createGenesisBlock(self):
        return block(time.time(),0,'Genesis Block','0',tough=2)
    
    def getLatestBlock(self):
        return self.chain[-1]
    
    def addBlock(self,data):
        previousBlock=self.getLatestBlock()
        newBlock=block(time.time(),previousBlock.index+1,data,previousBlock.hash,tough=2)
        self.chain.append(newBlock)

    def checkChainValidity(self):
        for i in range(1,len(self.chain)):
            currentBlock=self.chain[i]
            previousBlock=self.chain[i-1]

            if currentBlock.hash != currentBlock.hashBlock():
                print('Block[',i,'] has mismatched')
                print('Block has been TEMPERED')
                return False
            
            if currentBlock.previousHash != previousBlock.hash :
                print('Block[',i,'] is not linked with previous block properly')
                print('Link has been broken')
                return False

        return True




# Initialize blockchain
my_chain = blockchain()

# Add some blocks
my_chain.addBlock("First expense: Coffee ₹50")
my_chain.addBlock("Second expense: Lunch ₹100")
my_chain.addBlock("Third expense: Dinner ₹140")

print("Blockchain valid:-", my_chain.checkChainValidity())

for block in my_chain.chain:
    print("\nBlock",block.index)
    print("Timestamp:",datetime.fromtimestamp(block.timestamp).strftime('%Y-%m-%d %H:%M:%S'))
    print("Data:",block.data)
    print("Prev Hash:",block.previousHash)
    print("Hash:",block.hash)