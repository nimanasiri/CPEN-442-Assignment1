import ngram_score as ns
from math import log
from datetime import datetime
import random
import sys
import os

file = os.getcwd() + "\english_quadgrams.txt"

random.seed(datetime.now())
fitness = ns.ngram_score(file)


ciphertext = "JOOIEHDHDSECDSKUAKVUHDSZCJTSAAEJVPJYSUJVTJPPKHDCSSJOHDSAJNUESCACSPKEVEVBLSDEVUHJSMSTFHSHDSFVOJCHFVKHSBKCUSVSCATJPPKIDJCKVHJKNETSOJCZCJHSTHEJVUJHGJFADKVHLSLSDSKUSUAKEUKNETSTJPPKKVUADSZFHHDSPEVHJKNKCBSONJISCZJHHDKHAHJJUVSKCUJHHDSHDCSSAJNUESCAIKVUSCSUKLJFHOJCKPEVFHSJCHIJTJPPKNJJXEVBOJCHDSPTJPPKKVUHDSVQFESHNGPKCTDSUJOOKOHSCHDSJHDSCAUJHKCSHDSECDSKUAJOOADJFHSUHDSQFSSVUJHHDSECDSKUAKCSBJVSTJPPKEOEHZNSKASGJFCPKRSAHGHDSAJNUESCAADJFHSUEVCSZNG"

char_map = {'A': 'W', 'B': 'P', 'C': 'L', 'D': 'R', 'E': 'U', 'F': 'I', 'G': 'T',
                            'H': 'F', 'I': 'Q', 'J': 'J', 'K': 'Y', 'L': 'M', 'M': 'C', 
                            'N': 'K', 'O': 'G', 'P': 'N', 'Q': 'B', 'R': 'X', 'S': 'S', 'T': 'V', 
                            'U': 'Z', 'V': 'H', 'W': 'D', 'X': 'A', 'Y': 'E', 'Z': 'O'}

max_fitness = -sys.maxsize - 1
max_map = {}
max_plain = ""
i = 0

# Update plaintext with new mapping
plain_list = []
for char in ciphertext:
    plain_list.append(char_map[char])


max_fitness = fitness.score(''.join(plain_list))

max_map = dict(char_map)
max_plain = list(plain_list)

print(plain_list)
print(max_fitness)

while i < 100000:
    i += 1
    # Swap two random characters in char_map
    first_char = chr(ord('A') + random.randint(0,25))
    second_char = chr(ord('A') + random.randint(0,25))
    #print('SWAPPING THESE TWO: {}, {}'.format(first_char, second_char))
    char_map[first_char], char_map[second_char] = char_map[second_char], char_map[first_char]


    for k in range(len(plain_list)):
        if ciphertext[k] == first_char:
            plain_list[k] = char_map[first_char]
        elif ciphertext[k] == second_char:
            plain_list[k] = char_map[second_char]

    cur_fitness = fitness.score(''.join(plain_list))


    if cur_fitness > max_fitness:
        max_fitness = cur_fitness
        max_map = dict(char_map)
        max_plain = list(plain_list)
        i = 0
    else:
        char_map[first_char], char_map[second_char] = char_map[second_char], char_map[first_char]
        plain_list = list(max_plain)


print("max_fitness ", max_fitness)
print(max_map)
print(max_plain)


# Fitness of correct plaintext -1806.5979492125941