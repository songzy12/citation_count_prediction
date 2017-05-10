import code
import pickle

from util import get_name2author, get_id2paper, Author, Paper, Venue, logger

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

    def set_venue_rank():
        logger.info("feature venue rank computation begins")
        venues = name2venue.values()
        for venue in venues:
            venue.citation_count = sum([len(id2paper[paper].cited) for paper in venue.papers])
        venues.sort(key=lambda venue: venue.citation_count)
        for i, venue in enumerate(venues):
            venue.rank = i+1
        logger.info("feature venue rank computation ends")

    def set_author_rank():
        logger.info("feature author rank computation begins")
        authors = name2author.values()
        for author in authors:
            author.citation_count = sum([len(id2paper[paper].cited) for paper in author.papers])
            author.reference_count = sum([len(id2paper[paper].references) for paper in author.papers])
        authors.sort(key=lambda author: author.citation_count)
        for i, author in enumerate(authors):
            author.rank = i+1   
        logger.info("feature author rank computation ends")

    set_venue_rank()
    set_author_rank()

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

logger.info("name, paper, venue to load")
name2author, id2paper, name2venue = load_author_paper_venue()
logger.info("name, paper, venue loaded")

def feature_topic_rank(d):
    return []
    
def feature_diversity(d):
    return []

def feature_recency(author):
    # now is 2016
    author.years = [2016 - id2paper[paper].year for paper in author.papers]
    if not len(author.years):
        return [0,0,0,0]
    author.years.sort()
    return [sum(author.years)*1.0/len(author.years),
            author.years[len(author.years)/2],
            author.years[0], author.years[-1]]
 
def feature_venue_rank(author):
    author.venue_ranks = [name2venue[id2paper[paper].conference].rank for paper in author.papers if id2paper[paper].conference]
    return [sum(author.venue_ranks)*1.0/len(author.venue_ranks) if len(author.venue_ranks) else 0]

def feature_venue_centrality(author):
    """
    venue centrality: like author authority
    """
    return []

def feature_h_index(author):
    """
    author's h index
    """
    counts = sorted([len(id2paper[paper].cited) for paper in author.papers])
    i = 0
    while i < len(counts) and i < counts[i]:
        i += 1
    return [i]

def feature_author_rank(author_name):
    """
    author's total citation count rank
    author's total citation
    author's average citation
    author's total reference
    author's average reference
    """
    author = name2author[author_name]
    if not len(author.papers):
        logger.info("author %s with papers length 0" % author_name)
    return [author.rank, author.citation_count, author.reference_count,
            author.citation_count*1.0/len(author.papers) if len(author.papers) else 0,
            author.reference_count*1.0/len(author.papers) if len(author.papers) else 0]


def feature_productivity(author):
    return [len(author.papers)]

def feature_sociality(author):
    return [len(author.coauthors), sum(author.coauthors.values())]

def feature_authority(author):
    return []

def get_features(author_name):
    """
    param: author id
    return: a list of features
    """
    features = []
    author = name2author[author_name]
    features += feature_h_index(author)
    features += feature_author_rank(author_name)
    features += feature_productivity(author)
    features += feature_sociality(author)
    features += feature_authority(author)

    features += feature_venue_rank(author)
    features += feature_venue_centrality(author)

    features += feature_recency(author)

    logger.debug("%s: %s" % (author_name, features))
    return features

if __name__ == '__main__':
    save_author_paper_venue()
    #author = name2author.itervalues().next()
    #paper = id2paper.itervalues().next()
    #venue = name2venue.itervalues().next()
    #code.interact(local=locals())
