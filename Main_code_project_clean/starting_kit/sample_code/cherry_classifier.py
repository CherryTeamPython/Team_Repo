#Here are the different imports for the cross validation:

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split as tts

#Here are our different SKLEARN Classifiers imports:

from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.base import BaseEstimator 
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import neighbors, datasets
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.neural_network import MLPClassifier
# NOT WORKING from sklearn.gaussian_process import GaussianProcessClassifier

def  best_fit(names, classifiers, x, y):
    score_boucle_train = []
    final_array = []
    best=["",0]

    for name, clf in zip(names, classifiers):
        score_boucle_train.append( cross_val_score(clf, x, y, cv=10, n_jobs=1 ))

    final_array=np.mean(score_boucle_train, axis=1, dtype=np.float64)

    for score, name in zip(final_array, names):
        if score>best[1] :
            best[1]=score
            best[0]=name
    return best
