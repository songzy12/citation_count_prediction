import code 

DATADIR = '/home/songzy/HW3/data/'
OUTDIR = '/home/songzy/HW3/result/'

def dump_results(results, result_path=OUTDIR+'results.txt'):
    """
    Dump a list of tuple (author id, predicted citation count) to file
    """
    with open(result_path, 'w') as f:
        for k, v in results:
            f.write(k+'\t'+str(v)+'\n')

def get_author2id_id2author(author_path=DATADIR+'author.txt'):
    author2id = {}
    id2author = {}
    with open(author_path) as f:
        line = f.readline()
        while line:
            id_, name = line.strip().split('\t')
            author2id[name] = id_
            id2author[id_] = name
            line = f.readline()
    return author2id, id2author

def get_id2paper(paper_path=DATADIR+'paper.txt'):
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
    title = year = conference = id_ = abstract = None
    authors = references = []
    for line in chunk:
        t = line[1]
        content = line[2:] if t != 'i' else line[len('#index'):]
        if t == '*': title = line[2:]
        elif t == '@': authors = map(lambda x: x.strip(), content.split(','))
        elif t == 't': year = int(content)
        elif t == 'c': conference = content
        elif t == 'i': id_ = content
        elif t == '%': references.append(content)
        elif t == '!': abstract = content
    return id_, {'title': title, 
                 'year': year,
                 'conference': conference,
                 'abstract': abstract,
                 'authors': authors,
                 'references': references} 

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
