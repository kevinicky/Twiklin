import csv
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#create stopwords corpus
stop_words = stopwords.words('indonesian')
#create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def clean_text(t):
    user_removed = re.sub(r'@[A-Za-z0-9]+','',t)
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
    lower_case_tweet = number_removed.lower()
    words = word_tokenize(lower_case_tweet)
    #remove stopwords
    sent = []
    for w in words:
        if w not in stop_words:
            sent.append(w)
    # join every words
    text = (' '.join(sent)).strip()
    # stemming using Sastrawi
    text = stemmer.stem(text)
    return text

old_csv = open('dataset.csv', 'r')
new_csv = open('clean_dataset.csv', 'a', newline = '')


old_reader = csv.reader(old_csv)
new_writer = csv.writer(new_csv)

for row in old_reader:
    print(row[0] + ' ' + row[1])
    new_writer.writerow([clean_text(row[0]), row[1]])

old_csv.close()
new_csv.close()
print()
print('Success clean dataset')
print('Saved to clean_dataset.csv')
