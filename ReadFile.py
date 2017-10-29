
import csv
import itertools
import re
import operator
import string
from nltk.corpus import stopwords
from collections import defaultdict
com = defaultdict(lambda: defaultdict(int))

test_word = {}
with open('C:\Users\Sriram\Desktop\Twitter\output.csv','w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
fields = ["text", ""]
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
reader = csv.DictReader(open('C:\Users\Sriram\Desktop\Twitter\data1218Text.csv', 'rt'))
com = defaultdict(lambda : defaultdict(int))
for EachRow in reader:
    tempEachRow = next(itertools.islice(EachRow.values(), 1))
    TempEachRow = tempEachRow.split()
    for each in TempEachRow:
        tempEach = each.lower()
        tempEach = re.sub('[!@?#$&/()1234567890:.,-]', '', tempEach)
        tempEach = tempEach.replace(' ', '')
        if tempEach in stop:
            tempEach = " ";
        tempEach = tempEach.replace(' ', '')
        tempEach = tempEach.replace('  ', '')
        if tempEach in test_word.keys():
            test_word[tempEach] = test_word[tempEach] + 1
        else:
            test_word[tempEach] = 1
final_dict = sorted(test_word.items(), key = operator.itemgetter(1), reverse = True)
for i in range(len(final_dict)-1):
    for j in range(i+1,len(final_dict)):
        w1,w2 = sorted([final_dict[i], final_dict[j]])
        if w1 != w2:
            com[w1][w2] += 1
com_max = []
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1),reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1,t2), t2_count))
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max)
##with open('C:\Users\Sriram\Desktop\Twitter\output.csv','w') as resultFile:
#    wr = csv.writer(resultFile, dialect='excel')
#    for each in final_dict:
#        wr.writerow(each)
