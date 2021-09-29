# Answers for All Questions:

## Q1
### a) plaintext  
OFFWITHTHEIRHEADSANDTHEPROCESSIONMOVEDONCOMMATHREEOFTHESOLDIERSREMAININGBEHINDTOEXECUTETHEUNFORTUNATEGARDENERS
COMMAWHORANTOALICEFORPROTECTIONDOTYOUSHANTBEBEHEADEDSAIDALICECOMMAANDSHEPUTTHEMINTOALARGEFLOWERPOTTHATSTOOD
NEARDOTTHETHREESOLDIERSWANDEREDABOUTFORAMINUTEORTWOCOMMALOOKINGFORTHEMCOMMAANDTHENQUIETLYMARCHEDOFFAFTERTHE
OTHERSDOTARETHEIRHEADSOFFSHOUTEDTHEQUEENDOTTHEIRHEADSAREGONECOMMAIFITPLEASEYOURMAJESTYTHESOLDIERSSHOUTEDINREPLY

### b) Cipher is simple substitution

### c) Mapping from cipher text (key) to plain text (value)
{'A': 'S', 'B': 'G', 'C': 'R', 'D': 'H', 'E': 'I', 'F': 'U', 'G': 'Y',
'H': 'T', 'I': 'W', 'J': 'O', 'K': 'A', 'L': 'B', 'M': 'X', 
'N': 'L', 'O': 'F', 'P': 'M', 'Q': 'Q', 'R': 'J', 'S': 'E', 'T': 'C', 
'U': 'D', 'V': 'N', 'W': 'Z', 'X': 'K', 'Y': 'V', 'Z': 'P'}

### d)
In q1.py I implemented the hillclimbing algorithm from [1]. In my implementation I modify and use ngram_score.py taken from [2] to find the 'fitness' 
of a quadgram which is related to the probability of it appearing in english text. I also spoke with Ningfeng Yang about my algorithm, and had him take a
look at my code to check my implementation.


[1] http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-simple-substitution-cipher/
[2] http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation


## Q2
### a)


### b)


### c)


### d)
I use the simulated annealing algorithm fomr [1], and shuffle the key every time I get stuck at a local maximum. I also had to change the logic to
deal with a playfair cipher rather than substitution cipher. While writing it, I checked my algorithm with Ningfeng Yang and also had him take a look
at my implementation.

# Fitness of correct plaintext -10708.039054223154

[1] http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-playfair/

## Q3
1.


2. Seconds or ms 


## Q4
1. 

2. Seconds or ms 

