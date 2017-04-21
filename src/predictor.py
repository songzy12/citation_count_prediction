from util import *

def get_results(author_test):
    results = []
    for id_ in author_test:
        results += (id_, predict(id_)),
    return results
 
def predict(id_):
    return 0
        
if __name__ == '__main__':
    author_test = get_test()
    results = get_results(author_test)
    dump_results(results)
