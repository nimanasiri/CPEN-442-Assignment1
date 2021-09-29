from random import randint
import ngram_score as ns
import os

file4 = os.getcwd() + "\english_quadgrams.txt"
file3 = os.getcwd() + "\english_trigrams.txt"
file2 = os.getcwd() + "\english_bigrams.txt"
file1 = os.getcwd() + "\english_monograms.txt"
fitness4 = ns.ngram_score(file4)
fitness3 = ns.ngram_score(file3)
fitness2 = ns.ngram_score(file2)
fitness1 = ns.ngram_score(file1)

def fitness(pt):
    return (fitness4.score(pt) + fitness3.score(pt) + fitness2.score(pt) + fitness1.score(pt))/8

# Removes all the X's that separate duplicate letters
def prune_pt(pt):
    new_pt = [pt[0]]
    for i in range(1,len(pt) - 1):
        if pt[i-1] == pt[i+1] and pt[i] == 'X':
            continue
        
        new_pt.append(pt[i])

    new_pt.append(pt[len(pt) - 1])

    return new_pt

# Decode playfair ciphertext
def decode(key, ciphertext):
    ROW = 0
    COL = 1
    pt = []

    # make a map of the key
    key_map = {}

    for i in range(len(key)):
        for j in range(len(key)):
            key_map[key[i][j]] = [i,j]

    # Build PT
    for i in range(0,len(ciphertext),2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        char1r = key_map[char1][ROW]
        char1c = key_map[char1][COL]
        char2r = key_map[char2][ROW]
        char2c = key_map[char2][COL]


        if char1c == char2c:
            pt.append(key[(char1r + 4) % 5][char1c])
            pt.append(key[(char2r + 4) % 5][char2c])
        elif char1r == char2r:
            pt.append(key[char1r][(char1c + 4) % 5])
            pt.append(key[char2r][(char2c + 4) % 5])
        else:
            pt.append(key[char1r][char2c])
            pt.append(key[char2r][char1c])

    return prune_pt(pt)


def scramble_key(key):
    rand = randint(0,40)
    rand1 = randint(0,4)
    rand2 = randint(0,4)
    rand3 = randint(0,4)
    rand4 = randint(0,4)

    if rand <= 36:
        key[rand1][rand2], key[rand3][rand4] = key[rand3][rand4], key[rand1][rand2]
    elif rand == 37:
        for row in key:
            row.reverse()
    elif rand == 38:
        key.reverse()
    elif rand == 39:
        for i in range(len(key)):
            key[rand1][i], key[rand2][i] = key[rand2][i], key[rand1][i]
    elif rand == 40:
        for i in range(len(key)):
            key[i][rand1], key[i][rand2] = key[i][rand2], key[i][rand1]


def new_key(key):
    for i in range(25):
        rand1 = randint(0,4)
        rand2 = randint(0,4)
        rand3 = randint(0,4)
        rand4 = randint(0,4)
        key[rand1][rand2], key[rand3][rand4] = key[rand3][rand4], key[rand1][rand2]