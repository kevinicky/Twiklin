import csv
import pickle
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

def save_classifier(classifier):
    object = classifier
    file = open('model.obj', 'wb')
    pickle.dump(object, file)

    print("success train data")
    print("data saved to train.obj")

fp = open('clean_dataset.csv', 'r')
classifier = NaiveBayesClassifier(fp, format='csv')

save_classifier(classifier)