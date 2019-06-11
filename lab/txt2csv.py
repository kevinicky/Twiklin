from nltk.tokenize import sent_tokenize
import csv
import os
import re

def clean_text(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)"," ",tweet).split()).lower()

path = 'dataset'
subfolder = os.listdir(path)

for p in subfolder:
    full_path = path + '/' + p
    txt_path = os.listdir(full_path)

    for t in txt_path:
        full_txt_path = full_path + '/' + t
        print(full_txt_path)

        file_txt = open(full_txt_path, 'r')
        text = sent_tokenize(file_txt.read())
        csv_file = open('dataset.csv', 'a', newline = '')
        csv_writer = csv.writer(csv_file)
        for t in text:
            csv_writer.writerow([clean_text(t)])