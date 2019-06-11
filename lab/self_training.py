from nltk.tokenize import sent_tokenize
import pickle
import re
import os
import csv
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

def save_classifier(classifier):
    object = classifier
    file = open('train.obj', 'wb')
    pickle.dump(object, file)

def clean_text(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)"," ",tweet).split()).lower()

path = 'dataset'
subfolder = os.listdir(path)

for p in subfolder:
    full_path = path + '/' + p
    txt_path = os.listdir(full_path)

    for t in txt_path:
        f = open('train.obj', 'rb')
        classifier = pickle.load(f)
        f.close()

        full_txt_path = full_path + '/' + t
        print(full_txt_path)

        file_txt = open(full_txt_path, 'r')
        text = sent_tokenize(file_txt.read())
        csv_file = open('dataset.csv', 'a', newline = '')
        csv_writer = csv.writer(csv_file)
        prob_dist= classifier.prob_classify(clean_text(t))
        
        for t in text:
            csv_writer.writerow([clean_text(t), prob_dist.max()])
        
        csv_file.close()

    fp = open('dataset.csv', 'r')
    classifier = NaiveBayesClassifier(fp, format='csv')

    save_classifier(classifier)
    fp.close()