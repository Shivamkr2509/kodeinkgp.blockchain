TASK:- Minimal Blockchain Implementation 

I have made this simple Blockchain Implementation using PYTHON, developed for my sophomores selection task for the Blockchain Team of KodeinKGP.

#_FEATURES :-
 1) There is a basic structure of a block which contains Index, Timestamp (with IST too to understand properly), data, previous hash which were mandatory but along with it there is nonce too which was optional and bonus also.
 2) I have used SHA_256 algorithm for hashing of blocks.
 3) Print statements to recognise if there is tamper in blocks or the chain is valid or not.
 4) There are some sample data which will show the working of the code.

#_BLOCK STRUCTURE:-
Each block contains:-
 1)Index:- In the blockchain what is the position of the block.
 2)Timestamp:- It will show the time on which block has been created or generated.
 3)Data:- Transaction details.
 4)Nonce:-Number of attempts required to find the proper hash as per the toughness that means the number of 0 in starting.
 5)Hash:- Heart of the block which is generated by the SHA-256 of all above fields.

#_VALIDATION LOGIC:-
There is a function "checkChainValidity" which ensures that the hash of each block should match with the recalculated hash to prevent the tampering and also it ensures that the previousHash of each block matches the actual hash of the previous block so that the contnuation can be verified.

#_PROOF-OF-WORK(PoW):-
In function "blockMining()" the logic implemented are as follows:
 1)Hash will only be valid if it starts with '00'.
 2)To achieve this, the block keeps increasing 'nonce' until a valid hash is found.
 3)It increases the effort required in real blockchains for mining.

By this we can ensure that:-
 1)It will be harder to modify a block.
 2)Every time computational work will be required to add a new block.


FILES INCLUDED:-
    1)blockchain.py
    2)README.md




Submitted by:-
        SHIVAM KUMAR[24AR10034]