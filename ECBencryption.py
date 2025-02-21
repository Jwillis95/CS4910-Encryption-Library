
import os

plaintext = "This is some plaintext."
blockSize = 16

print("Plaintext: " + plaintext + "\n")

plaintext = plaintext.encode()

def splitIntoBlocks(data: bytes, blockSize: int = 16):
#break plaintext into blocks of size 16 bytes each
#split into blocks

#size of last block = length of total message % size of each block


    lastBlockSize = len(data) % blockSize

    paddingLength = blockSize - lastBlockSize

    data += bytes([paddingLength] * paddingLength)
#padding = size of each block - size of last block
#last block = length of last block + padding

    blocks = []
    for i in range(0, len(data), blockSize):

        blocks.append(data[i:i + blockSize])
    
    return blocks

key = os.urandom(blockSize)
print("Key: " + str(key.hex()) + "\n")

blocks = splitIntoBlocks(plaintext, blockSize)
print("Blocks: " + str(blocks) + "\n")

ECBencrypted = bytearray()



for block in blocks:
    #print(block)
    blockBytes = bytes(block)
    #print(blockBytes)
    blockBytesEncrypted = bytes(b ^ k for b, k in zip(blockBytes, key))
    ECBencrypted.extend(blockBytesEncrypted)

print("Encrypted string: " + str(ECBencrypted.hex()) + "\n")


ECBunencrypted = bytearray()

for block in range(0, len(ECBencrypted), blockSize):

    encryptedBlockBytes = ECBencrypted[block: block + blockSize]

    ECBBlocksUnencrypted = bytes(e ^ k for e, k in zip(encryptedBlockBytes, key))
    #print(ECBBlocksUnencrypted.hex())
    ECBunencrypted.extend(ECBBlocksUnencrypted)

paddingLength = ECBunencrypted[-1]
ECBunencrypted = ECBunencrypted[:-paddingLength]

print("Unencrypted string: " + str(ECBunencrypted) + "\n")