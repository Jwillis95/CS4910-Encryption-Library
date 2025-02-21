from task6CBC import cbcEncryption

#uses aes-128-cbc

#Plaintext (total 21 characters): This is a top secret.
#Ciphertext (in hex format): 764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2
#IV (in hex format): aabbccddeeff00998877665544332211

goalCipherText = "764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2"
iv = bytes.fromhex("aabbccddeeff00998877665544332211")
plaintext = "This is a top secret."


plaintextBytes = plaintext.encode('utf-8')

print("Our plaintext: " + plaintext)



wordToTest = "placeholder"
#wordWasFound = 0


with open("words.txt", 'r') as wordlist:
    for line in wordlist:
        wordToTest = line.strip().encode('utf-8')

        wordToStop = wordToTest
        wordToTest = wordToTest.ljust(16, b'#'[0:1])[:16]

        print(f"Key length: {len(wordToTest)} (Expected: 16)")

        wordToTestEncrypted = cbcEncryption(plaintext, iv, wordToTest)
        print(wordToTestEncrypted)

        print(f"Trying key: {wordToTest} -> {wordToTest.hex()}")
        print(f"Encrypted output: {wordToTestEncrypted.hex()}")
        
        if wordToTestEncrypted.hex() == goalCipherText:
            print("Key found: " + wordToTest.decode(errors="ignore"))
            #wordWasFound += 1
            break
            

        # Check if the word is "syracuse"
        #if wordToStop == "Syracuse".encode('utf-8'):
            #print("Found syracuse, breaking out!")
            #break


#print(wordWasFound)



#open dictionary file
#break file into list word by word or line by line
#for each word, let word = key
#   encrypt M using key
#   check if M matches the ciphertext
#   if M matches the ciphertext, print("The key is: " + key)
#   break

