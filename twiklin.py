from PyQt5 import QtCore, QtGui, QtWidgets
import re
import tweepy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pickle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 601)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 111, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 101, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 300, 101, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 10, 111, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lbl_rating = QtWidgets.QLabel(self.centralwidget)
        self.lbl_rating.setGeometry(QtCore.QRect(600, 220, 211, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lbl_rating.setFont(font)
        self.lbl_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rating.setObjectName("lbl_rating")
        self.et_name = QtWidgets.QLineEdit(self.centralwidget)
        self.et_name.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.et_name.setObjectName("et_name")
        self.et_count = QtWidgets.QLineEdit(self.centralwidget)
        self.et_count.setGeometry(QtCore.QRect(160, 30, 113, 20))
        self.et_count.setObjectName("et_count")
        self.lbl_pos = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pos.setGeometry(QtCore.QRect(330, 30, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_pos.setFont(font)
        self.lbl_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pos.setObjectName("lbl_pos")
        self.list_tweet = QtWidgets.QListWidget(self.centralwidget)
        self.list_tweet.setGeometry(QtCore.QRect(30, 90, 241, 192))
        self.list_tweet.setObjectName("list_tweet")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(100, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.lbl_neg = QtWidgets.QLabel(self.centralwidget)
        self.lbl_neg.setGeometry(QtCore.QRect(330, 320, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_neg.setFont(font)
        self.lbl_neg.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_neg.setObjectName("lbl_neg")
        self.list_pos = QtWidgets.QListWidget(self.centralwidget)
        self.list_pos.setGeometry(QtCore.QRect(330, 90, 256, 192))
        self.list_pos.setObjectName("list_pos")
        self.list_neg = QtWidgets.QListWidget(self.centralwidget)
        self.list_neg.setGeometry(QtCore.QRect(330, 380, 256, 192))
        self.list_neg.setObjectName("list_neg")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 170, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.list_neu = QtWidgets.QListWidget(self.centralwidget)
        self.list_neu.setGeometry(QtCore.QRect(30, 380, 256, 192))
        self.list_neu.setObjectName("list_neu")
        self.lbl_neu = QtWidgets.QLabel(self.centralwidget)
        self.lbl_neu.setGeometry(QtCore.QRect(30, 320, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_neu.setFont(font)
        self.lbl_neu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_neu.setObjectName("lbl_neu")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 101, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_search.clicked.connect(self.process_tweets)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Positive Tweets"))
        self.label_3.setText(_translate("MainWindow", "Negative Tweets"))
        self.label_4.setText(_translate("MainWindow", "Count"))
        self.lbl_rating.setText(_translate("MainWindow", "0.0"))
        self.lbl_pos.setText(_translate("MainWindow", "0"))
        self.btn_search.setText(_translate("MainWindow", "SEARCH"))
        self.lbl_neg.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Rating"))
        self.lbl_neu.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Neutral Tweets"))

    def process_tweets(self):
        username = self.et_name.text()
        count = int(self.et_count.text())
        self.list_neg.clear()
        self.list_neu.clear()
        self.list_pos.clear()
        self.list_tweet.clear()

        #create stopwords corpus
        stop_words = stopwords.words('indonesian')
        #create stemmer
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        print(username)
        

        # connect to twitter api
        consumer_key = 'qwFexwZ95GXY1EVRWlxr3ZJnL'
        consumer_key_secret = '5vJxUIh74oOIqckSacDWTJ7T2ANqTIhmUUpkmI8vcMZ0zmlWRJ'
        access_token = '2285972083-8f4L3CCiSqoMNo6ivDJg4FaKEzIuRQTXDjEzZ5L'
        access_token_secret = 'auHv2h6TLsxULyPU45GKskpPV8TRsEYnd5BHU2PoYrAQG'

        auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        
        # load classifier
        f = open('model.obj', 'rb')
        classifier = pickle.load(f)
        f.close()

        # initialize variable
        pos_calc = 0
        neg_calc = 0
        neu_calc = 0
        pos_c = 0
        neg_c = 0
        neu_c = 0
        

        public_tweets = tweepy.Cursor(api.search, q='from:' + username, show_user = True, tweet_mode='extended').items(count)
        count = 0
        for t in public_tweets:
            count += 1
            print(t.full_text)
            self.list_tweet.addItem(t.full_text)
            user_removed = re.sub(r'@[A-Za-z0-9]+','',t.full_text)
            link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
            number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
            lower_case_tweet = number_removed.lower()
            words = word_tokenize(lower_case_tweet)
            # remove stopwords
            sent = []
            for w in words:
                if w not in stop_words:
                    sent.append(w)
            # join every words
            tweet = (' '.join(sent)).strip()
            # stemming using Sastrawi
            tweet = stemmer.stem(tweet)

            prob_dist= classifier.prob_classify(tweet)
            
            label = prob_dist.max()
             
            print(label + " " + str(prob_dist.prob(label)))
            if prob_dist.prob(label) < 0.01:
                neu_c += 1
                neu_calc += prob_dist.prob(label)
                self.list_neu.addItem(t.full_text)
            else:
                if label == '1':
                    pos_c += 1
                    pos_calc += prob_dist.prob('1')
                    self.list_pos.addItem(t.full_text)
                elif label == '-1':
                    neg_c += 1
                    neg_calc += prob_dist.prob('-1')
                    self.list_neg.addItem(t.full_text)
    
        
        if pos_c == 0:
            pos_calc = 0
        else:
            pos_calc = round(pos_calc / count, 2) * 100
        
        if neg_c == 0:
            neg_calc = 0
        else:
            neg_calc = round(neg_calc / count, 2) * 100
        
        if neu_c == 0:
            neu_calc = 0
        else:
            neu_calc = round(neu_calc / count, 2) * 100

        rating = pos_calc - neg_c

        # set text
        self.lbl_pos.setText(str(pos_calc))
        self.lbl_neg.setText(str(neg_calc))
        self.lbl_neu.setText(str(neu_calc))
        self.lbl_rating.setText(str(rating))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
