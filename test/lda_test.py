from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups
import code

dataset = fetch_20newsgroups(shuffle=True,
                             random_state=1,
                             remove=('headers', 'footers', 'quotes'))
documents = dataset.data

no_features = 1000
# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95,
                                min_df=2,
                                max_features=no_features,
                                stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()

no_topics = 100
# Run LDA
lda = LatentDirichletAllocation(n_topics=no_topics,
                                max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0).fit_transform(tf)

code.interact(local=locals())
