import glob
def read_txt(max_i:int, docs:list, path:str):
    """
    max_i = number of txt to be read
    docs = list, to save corpus
    path = where you save txt file
    """  
    myFiles = glob.glob(path)
    if type(docs) != list:
        return "Error: docs must be a list"
    ind = 0
    while ind <= max_i:
        for i in myFiles:
            with open(i) as f:
                lines = f.readlines()
                docs += lines
            ind += 1
    return docs