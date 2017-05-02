import code 
from collections import defaultdict

class Author:
    def __init__(self, name, id_):
        self.name = name
        self.id = id_

        self.papers = []
        self.coauthors = defaultdict(int)

class Paper:
    def __init__(self):
        self.title = ""
        self.authors = []
        self.year = 0
        self.conference = ""
        self.id = ""
        self.references = []
        self.abstract = ""

        self.cited = []

class Venue:
    def __init__(self, name):
        self.name = name
        self.papers = []

DATADIR = '/home/songzy/HW3/data/'
OUTDIR = '/home/songzy/HW3/result/'

def dump_results(results, result_path=OUTDIR+'results.txt'):
    """
    Dump a list of tuple (author id, predicted citation count) to file
    """
    with open(result_path, 'w') as f:
        for k, v in results:
            f.write(k+'\t'+str(v)+'\n')

def get_name2author(author_path=DATADIR+'author.txt'):
    """
    return: one dict, author name to Author
    """
    name2author = {}
    with open(author_path) as f:
        line = f.readline()
        while line:
            id_, name = line.strip().split('\t')
            name2author[name] = Author(name, id_)
            line = f.readline()
    return name2author 

def get_id2paper(paper_path=DATADIR+'paper.txt'):
    """
    return: one dict, paper id to Paper 
    """
    id2paper = {}
    with open(paper_path) as f:
        line = f.readline()
        while line:
            chunk = []
            while line != '\n':
                chunk.append(line)
                line = f.readline()

            id_, info = parse_chunk(map(lambda x: x.strip(), chunk))
            id2paper[id_] = info
            line = f.readline()
    return id2paper

def parse_chunk(chunk):
    paper = Paper()
    for line in chunk:
        t = line[1]
        content = line[2:] if t != 'i' else line[len('#index'):]
        if t == '*': paper.title = line[2:]
        elif t == '@': paper.authors = map(lambda x: x.strip(), content.split(','))
        elif t == 't': paper.year = int(content)
        elif t == 'c': paper.conference = content
        elif t == 'i': id_ = paper.id = content
        elif t == '%': paper.references.append(content)
        elif t == '!': paper.abstract = content
    return id_, paper

def get_train(train_path=DATADIR+'citation_train.txt'):
    """
    return: a dict of {author id: citation count}
    """
    # paper info is till 2011, citation count is till 2016
    m = {}
    with open(train_path) as f:
        line = f.readline()
        while line:
            id_, name, count = line.strip().split('\t')
            m[id_] = int(count)
            line = f.readline()
    return m

def get_test(test_path=DATADIR+'citation_test.txt'):
    """
    return: a list of author ids
    """
    l = []
    with open(test_path) as f:
        line = f.readline()
        while line:
            id_, name = line.strip().split('\t')
            l.append(id_)
            line = f.readline()
    return l
    
if __name__ == '__main__':
    # author2id, id2author = get_author2id_id2author()
    id2paper = get_id2paper()
    code.interact(local=locals())
