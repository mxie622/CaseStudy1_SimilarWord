# Need gensim:
from gensim.summarization import keywords
from gensim import corpora, models, similarities 
from gensim.models import Word2Vec

def update_dic_by_corpus(documents, ind: int, dic):
    """
    dic as output to save keywords and their frequency, dic = {'word1': 2, 'word2':3, ... }
    """
    a = keywords(documents[ind], ratio = 1) # Take all keywords to represent one description
    word = ""
    d = []   
    n = len(a)
    i = 0
    while i < n:
        if a[i] == '\n' :
            d.append(word)
            word = ""   
        else:
            word += a[i]
        i += 1
    d.append(word)   
    word = ""
    for j in d:
        if j != "":
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1

def sim_words(target_word_list: list, similar_word_list:list, model, similarity_score = 0.5): # 2 outcomes: dict, list
    """
    Outcome1 -> dictionary: All keywords: 

    {'informal': [['informal', 1.0],
      ['technical assistance', 0.5606825],
      ['completing credits', -0.6259817],
      ['established currently taught', 0.58370966],
      ['business owners', -0.5048344],
      ['cultural engagement', -0.5284517],
      .
      .
      .}

    Outcome2 -> List: Untrained keywords:
    ['social capital',
     'financial capital',
     'loyalty',
     'competition',
     'priorities',
     'representation',
     .
     .
     .]
    """  
    dp = []# save for similar words
    res = {} # output 
    word_not_found = [] # save target words unfound in corpus
    for i in range(len(target_word_list)):
        res[target_word_list[i]] = [""]
        for j in similar_word_list:   
            if target_word_list[i] in model.wv.vocab:
                if abs(model.wv.similarity(target_word_list[i], j)) > similarity_score: # take similarity_score > 0.5
                    dp.append([j, model.wv.similarity(target_word_list[i], j)]) # [words, similarity score]
            else:
                model.build_vocab([[target_word_list[i]]], update = True)
                word_not_found.append(target_word_list[i])
            if dp != []:
                res[target_word_list[i]] = dp
        dp = [] 
    return res, word_not_found
    