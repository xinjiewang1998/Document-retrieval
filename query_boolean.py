from collections import defaultdict
import pickle
import os
import numpy as np

from string_processing import *


def intersect_query(doc_list1, doc_list2):
    # TODO: you might like to use a function like this 
    # in your run_boolean_query implementation
    # for full marks this should be the O(n + m) intersection algorithm for sorted lists
    # using data structures such as sets or dictionaries in this function will not score full marks
    first = 0
    second = 0
    res = []
    while first < len(doc_list1) and second < len(doc_list2):
        if doc_list1[first] < doc_list2[second]:
            first += 1
        elif doc_list1[first] == doc_list2[second]:
            res.append(doc_list1[first])
            first += 1
            second += 1
        else:
            second += 1
    if second == len(doc_list2):
        for i in range(first, len(doc_list1)):
            if doc_list1[i]==doc_list2[len(doc_list2)-1]:
                res.append(doc_list1[i])
    if first == len(doc_list1):
        for i in range(second, len(doc_list2)):
            if doc_list2[i] == doc_list1[len(doc_list1)-1]:
                res.append(doc_list2[i])
    return res


def union_query(doc_list1, doc_list2):
    # TODO: you might like to use a function like this 
    # in your run_boolean_query implementation
    # for full marks this should be the O(n + m) union algorithm for sorted lists
    # using data structures such as sets or dictionaries in this function will not score full marks
    first=0
    second=0
    res=[]
    while first<len(doc_list1) and second<len(doc_list2):
        if doc_list1[first]<doc_list2[second]:
            res.append(doc_list1[first])
            first+=1
        elif doc_list1[first]==doc_list2[second]:
            res.append(doc_list1[first])
            first+=1
            second+=1
        else:
            res.append(doc_list2[second])
            second += 1
    if second==len(doc_list2):
        for i in range(first,len(doc_list1)):
            res.append(doc_list1[i])
    if first==len(doc_list1):
        for i in range(second,len(doc_list2)):
            res.append(doc_list2[i])
    return res


def run_boolean_query(query, index):
    """Runs a boolean query using the index.

    Args:
        query (str): boolean query string
        index (dict(str : list(tuple(int, int)))): The index aka dictionary of posting lists

    Returns:
        list(int): a list of doc_ids which are relevant to the query
    """
    # TODO: implement this function
    q_toks = query.split()
    relevant_docs = []
    index1 = 0
    while len(relevant_docs) == 0:
        if q_toks[index1] in index.keys():
            for id, tf in index[q_toks[index1]]:
                relevant_docs.append(id)

        if index1 == len(relevant_docs) - 1 and len(relevant_docs) == 0:
            return relevant_docs
        index1 += 2
    if index1 == len(relevant_docs) - 1:
        return relevant_docs
    next = index1

    while next < len(q_toks):
        temp_list1 = []
        if q_toks[next] in index.keys():
            for id, tf in index[q_toks[next]]:
                temp_list1.append(id)
            if q_toks[next - 1] == 'AND':
                relevant_docs = intersect_query(relevant_docs, temp_list1)
            elif q_toks[next - 1] == 'OR':
                relevant_docs = union_query(relevant_docs, temp_list1)
        next += 2

    return relevant_docs


# load the stored index
(index, doc_freq, doc_ids, num_docs) = pickle.load(open("stored_index.pik", "rb"))

print("Index length:", len(index))
if len(index) != 906290:
    print("Warning: the length of the index looks wrong.")
    print("Make sure you are using `process_tokens_original` when you build the index.")
    raise Exception()

# the list of queries asked for in the assignment text
queries = [
    "Welcoming",
    "Australasia OR logistic",
    "heart AND warm",
    "global AND space AND wildlife",
    "engine OR origin AND record AND wireless",
    "placement AND sensor OR max AND speed"
]

# run each of the queries and print the result
ids_to_doc = {v: k for k, v in doc_ids.items()}
for q in queries:
    res = run_boolean_query(q, index)
    res.sort(key=lambda x: ids_to_doc[x])
    print(q)
    for r in res:
        print(ids_to_doc[r])
