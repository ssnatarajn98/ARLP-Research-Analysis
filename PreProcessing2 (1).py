import csv
import itertools
import re
import operator
from nltk.corpus import stopwords
import string
##loading file
test_word = {}
with open("C:\Users\Sriram\Desktop\Twitter\outputsample.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
## This one uses csv file that yang created from the json file that contained the tweets he pulled
fields = ["ID", "datetime","has_media","is_reply","is_retweet","medias","nbr_favorite","nbr_reply","nbr_retweet","text","url","user_id","usernameTweet",""]
reader = csv.DictReader(open("C:\Users\Sriram\Desktop\Twitter\helptr.csv", 'rt'))
## these two lines just pulls out all uses words and punctuation
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
for EachRow in reader:
    tempEachRow = EachRow['text']
    #tempEachRow = next(itertools.islice(tempEachRow.values(), 1))
    TempEachRow = tempEachRow.split()
    for each in TempEachRow:
		## converts each word to lowercase
        tempEach = each.lower()
		## cleans more unneccesary stuff
        tempEach = re.sub('[!@?#$/()1234567890:.,-]', '', tempEach)
        if tempEach in stop:
            tempEach = " ";
        tempEach = tempEach.replace(' ', '')
		## adds each word and their frequency
        if tempEach in test_word.keys():
            test_word[tempEach] = test_word[tempEach] + 1
        else:
            test_word[tempEach] = 1
## sorts key words
final_dict = sorted(test_word.items(), key = operator.itemgetter(1), reverse = True)
## writes to new csv file
with open("/Users/chaofan/Documents/Test/output.csv",'w') as resultFile:
     wr = csv.writer(resultFile, dialect='excel')
     for each in final_dict:
         wr.writerow(each)
