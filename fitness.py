import os
from math import log10

file4 = os.getcwd() + "\english_grams\english_quadgrams.txt"
file3 = os.getcwd() + "\english_grams\english_trigrams.txt"
file2 = os.getcwd() + "\english_grams\english_bigrams.txt"
file1 = os.getcwd() + "\english_grams\english_monograms.txt"

file_list = [file1,file2,file3,file4]
gram_dicts = []
sum_freqs = []

# Populate the dictionaries/frequency sums for monograms -> quadgrams
for file_num in range(0,4):
    file_dict = dict()
    total_freq = 0
    cur_file = open(file_list[file_num], 'r')
    
    for line in cur_file.readlines():
        gram, freq = line.split(' ')
        file_dict[gram] = int(freq)
        total_freq += int(freq)

    gram_dicts.append(file_dict)
    sum_freqs.append(total_freq)


def fitness(gram_size, plaintext):
    # 0 indexed
    gram_dict = gram_dicts[gram_size - 1]
    sum_freq = sum_freqs[gram_size - 1]
    fitness = 0

    # + 1 because range is exclusive
    for i in range(len(plaintext) - gram_size + 1):
        pt_gram = plaintext[i:i+gram_size]
        if pt_gram in gram_dict:
            fitness += log10(float(gram_dict[pt_gram])/sum_freq)
        else:
            fitness += log10(0.01/sum_freq)

    return fitness

    
def quad_fitness(pt):
    return fitness(4,pt)


def total_fitness(pt):
    return (fitness(4,pt) + fitness(3,pt) + fitness(2,pt) + fitness(1,pt)) / 8