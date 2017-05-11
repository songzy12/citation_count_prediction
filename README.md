## Citation Count Prediction

This is an implementation of paper [1]  (not exactlty).
Most of the features used are enlighted by this paper.

## How to run

First set up the directory tree as follows, then put the raw data under `data`.
Just type the following command in your console to reproduce our results:

```
cd src && ./run.sh
```

## Project Structure

### data/

Raw data including author id map, paper information, training set, test set.

* author.txt
* paper.txt
* citation_train.txt
* citation_test.txt

### feature/

All the intermediate features extracted by `feature.py`, cached to accelerate for future use.

### log/

The log files used for debug.

### model/

The model trained for future use.

### result/

Predicted result for the test set, using the model trained on the features and the labeled training set.

### src/

* util: for read input from file, write output into file
* feature: get a bunch of features for specific author
* model: using training set to train the model
* predictor: use the model to predict results

### test/

Some test code to make sure each component works as expected.

## Feature

The feature we used can be classified into the following categories.

### Topic related

We run an LDA model on the abstracts of all the papers and extract 20 topics. Then the features related to topics include:

* The total and average topic perlexity of this author's papers.
* The weighed citation count of this author's average topic.
* The topic rank of this author's average topic.

### Recency

* The total and average paper age of this author's papers

### Venue

* The average venue rank of this author's papers' venues.

### Author

* The h-index of this author based on reference info.
* The rank of this author based on his reference info

### Paper

* The total number of papers of this author
* The total number of references in paper data
* The total number of citations in paper data

### Coauthor

* The total number of coauthors of this author
* The average paper citation count of his coauthors in training data

## Model

We use Random Forest with 100 estimators on the features we got. It performs better than Linear Regression. We also have intended to use SVM, but it just runs endlessly.

The time cost of our last run is around 44 min for feature extraction, 47 min for model training, 17 min for result prediction.

## References

[1] Yan, Rui, et al. "Citation count prediction: learning to estimate future citations for literature." Proceedings of the 20th ACM international conference on Information and knowledge management. ACM, 2011.
