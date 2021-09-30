from datetime import datetime
from fitness import quad_fitness
import random
import sys
import copy

random.seed(datetime.now())


def new_key():
    char_list = []
    char_map = {}

    for i in range(26):
        char_list.append(chr(ord('A')+i))

    random.shuffle(char_list)

    for i in range(26):
        char_map[chr(ord('A')+i)] = char_list[i]

    return char_map

# Fitness of correct plaintext -1806.5979492125941
ciphertext = "JOOIEHDHDSECDSKUAKVUHDSZCJTSAAEJVPJYSUJVTJPPKHDCSSJOHDSAJNUESCACSPKEVEVBLSDEVUHJSMSTFHSHDSFVOJCHFVKHSBKCUSVSCATJPPKIDJCKVHJKNETSOJCZCJHSTHEJVUJHGJFADKVHLSLSDSKUSUAKEUKNETSTJPPKKVUADSZFHHDSPEVHJKNKCBSONJISCZJHHDKHAHJJUVSKCUJHHDSHDCSSAJNUESCAIKVUSCSUKLJFHOJCKPEVFHSJCHIJTJPPKNJJXEVBOJCHDSPTJPPKKVUHDSVQFESHNGPKCTDSUJOOKOHSCHDSJHDSCAUJHKCSHDSECDSKUAJOOADJFHSUHDSQFSSVUJHHDSECDSKUAKCSBJVSTJPPKEOEHZNSKASGJFCPKRSAHGHDSAJNUESCAADJFHSUEVCSZNG"

GOAL_FITNESS = -1807

char_map = new_key()

max_fitness = -sys.maxsize - 1
max_map = {}
max_plain = ""

# Update plaintext with new mapping
plain_list = []
for char in ciphertext:
    plain_list.append(char_map[char])


max_fitness = quad_fitness(''.join(plain_list))

max_map = copy.deepcopy(char_map)
max_plain = copy.deepcopy(plain_list)

while max_fitness < GOAL_FITNESS:
    max_fitness -= 200
    char_map = new_key()
    print("Current fitness: {}, Goal Fitness: {}".format(max_fitness, GOAL_FITNESS))
    for i in range(0,100000):
        # Swap two random characters in char_map
        first_char = chr(ord('A') + random.randint(0,25))
        second_char = chr(ord('A') + random.randint(0,25))
        char_map[first_char], char_map[second_char] = char_map[second_char], char_map[first_char]

        for k in range(len(plain_list)):
            if ciphertext[k] == first_char:
                plain_list[k] = char_map[first_char]
            elif ciphertext[k] == second_char:
                plain_list[k] = char_map[second_char]

        cur_fitness = quad_fitness(''.join(plain_list))


        if cur_fitness > max_fitness:
            max_fitness = cur_fitness
            max_map = copy.deepcopy(char_map)
            max_plain = copy.deepcopy(plain_list)
            i = 0
        else:
            char_map[first_char], char_map[second_char] = char_map[second_char], char_map[first_char]
            plain_list = copy.deepcopy(max_plain)


print("max_fitness ", max_fitness)
print(max_map)
print(''.join(max_plain))