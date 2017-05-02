import code
import logging
import pickle

from util import get_name2author, get_id2paper, Author, Paper, Venue

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# create file handler
log_path = (__name__).join(["../log/", '.log'])
fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)
# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)

def save_author_paper_venue(path='../feature/'):
    name2author = get_name2author()
    logger.info("%d Authors loaded", len(name2author))
    id2paper = get_id2paper()
    logger.info("%d Papers loaded", len(id2paper))
    name2venue = {}
    
    for id_, paper in id2paper.items():
        for name in paper.authors:
            # set papers of author
            name2author[name].papers.append(paper.id)
            # set coauthors of author
            for coauthor in paper.authors:
                if coauthor == name:
                    continue
                name2author[name].coauthors[coauthor] += 1
        for reference in paper.references:
            # set cited
            if reference in id2paper:
                id2paper[reference].cited.append(paper.id)
        # set venue
        if paper.conference:
            if paper.conference not in name2venue:
                name2venue[paper.conference] = Venue(paper.conference)
            name2venue[paper.conference].papers.append(paper.id)

    with open(path+'author.pkl', 'w') as f:
        pickle.dump(name2author, f)
    with open(path+'paper.pkl', 'w') as f:
        pickle.dump(id2paper, f)
    with open(path+'venue.pkl', 'w') as f:
        pickle.dump(name2venue, f)

def load_author_paper_venue(path='../feature/'):
    with open(path+'author.pkl') as f:
        name2author = pickle.load(f)
    with open(path+'paper.pkl') as f:
        id2paper = pickle.load(f)
    with open(path+'venue.pkl') as f:
        name2venue = pickle.load(f)
    return name2author, id2paper, name2venue

def feature_topic_rank(d):
    pass
    
def feature_diversity(d):
    pass

def feature_recency(d):
    # now is 2016
    return 2016 - d.year
 
def feature_venue_rank(venue):
    pass

def feature_venue_centrality(venue):
    pass

def feature_h_index(author):
    return 0

def feature_author_rank(author):
    return 0

def feature_productivity(author):
    return 0

def feature_sociality(author):
    return 0

def feature_authority(author):
    return 0

def get_features(author):
    """
    param: author id
    return: a list of features
    """
    features = []
    features.append(feature_h_index(author))
    features.append(feature_author_rank(author))
    features.append(feature_productivity(author))
    features.append(feature_sociality(author))
    features.append(feature_authority(author))
    return features

if __name__ == '__main__':
    #save_author_paper_venue()
    name2author, id2paper, name2venue = load_author_paper_venue()

    author = name2author.itervalues().next()
    paper = id2paper.itervalues().next()
    venue = name2venue.itervalues().next()

    code.interact(local=locals())
