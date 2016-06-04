import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import  grid_search
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA

data = pd.read_csv('cleaned_train.csv')
data=data.drop('Unnamed: 0',1)
data=data.dropna()
labels = data.loc[:,'shot_made_flag']
features = data.drop('shot_made_flag',1)

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.1)

decision_tree_classifier = DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=4,
            max_features=4, max_leaf_nodes=None, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter='best')
decision_tree_classifier.fit(features_train,labels_train)

##TUNING THE CLASSIFIER######
"""
from sklearn.cross_validation import KFold

kf = KFold(len(features), n_folds=10)

from sklearn.grid_search import GridSearchCV


parameter_grid = {'criterion': ['gini', 'entropy'],
                  'splitter': ['best', 'random'],
                  'max_depth': [1, 2, 3, 4, 5],
                  'max_features': [1, 2, 3, 4]}

grid_search = GridSearchCV(clf,
                           param_grid=parameter_grid,
                           cv=kf)

grid_search.fit(features, labels)
#print('Best score: {}'.format(grid_search.best_score_))
#print('Best parameters: {}'.format(grid_search.best_params_))
print grid_search.best_estimator_
"""


from sklearn import cross_validation

rf_scores = cross_validation.cross_val_score(decision_tree_classifier, features, labels, cv=10)
print 'rf_scores : '+' , '.join(rf_scores)



#Taking testing set from cleaned_test.csv
"""
test_set = pd.read_csv('cleaned_test.csv')
test_set=test_set.drop('Unnamed: 0',1)
test_set=test_set.drop('shot_made_flag',1)
pred=decision_tree_classifier.predict(test_set)
main_text=''

test_set = pd.read_csv('predicting_set.csv')
test_set=test_set.drop('Unnamed: 0',1)
test_set=test_set.drop('shot_made_flag',1)
dic={'shot_id':[],'shot_made_flag':[]}
text='shot_id,shot_made_flag'+'\n'
for i in range(len(test_set)):
	text += str(test_set['shot_id'][i])+','+str(pred[i])+'\n'

f = open('submission.csv','w')
f.write(text)
"""