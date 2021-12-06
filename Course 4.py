#!/usr/bin/env python
# coding: utf-8

# In[14]:


def get_length(dna):
    len(dna)
    return len(dna)
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """


def is_longer(dna1, dna2):
    if len(dna1)>len(dna2):
        print('True')
    else:
        print('False')
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """


def count_nucleotides(dna, nucleotide):
    dna.count(nucleotide)
    return dna.count(nucleotide)
    

    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """


def contains_sequence(dna1, dna2):
    
    if str(dna2) in str(dna1):
        print('True')
    else:
        print('False')
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """




def is_valid_sequence(dna):
    neo=['A', 'T', 'C', 'G']
    count = 0
    for elem in dna:
      if elem not in neo:
        count = count + 1
    
    if count>0:
        print('Invalid')
    else:
        print('Valid')
    return count == 0




def insert_sequence(dna1, dna2, index):
    if index==0:
        return dna2+dna1
    elif index>0:
        return dna1[:index]+dna2+dna1[index:]

    


def get_complement(nuc):
    '''(str) -> str
    Return the nucleotide's complement.

    >>> get_complement('A')
    T
    >>> get_complement('C')
    G
    '''

    if nuc == "A":
        print ('T')
    elif nuc == 'T':
        print ('A')
    elif nuc == 'C':
        print ('G')
    elif nuc == 'G':
        print ('C')



def get_complementary_sequence(dna):
    complement = { 'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C' }
    return ''.join([complement[base] for base in dna[::-1]])
    





