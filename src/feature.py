def feature_topic_rank(d):
    pass
    
def feature_diversity(d):
    pass

def feature_recency(d):
    # now is 2016
    return 2016 - d.year
 
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

def feature_venue_rank(venue):
    pass

def feature_venue_centrality(venue):
    pass

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
