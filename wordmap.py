import csv
import itertools
import re
import operator
from nltk.corpus import stopwords
import string

test_word = {}
with open("C:\Users\Sriram\Desktop\Twitter\output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
fields = ["text", ""]
reader = csv.DictReader(open("C:\Users\Sriram\Desktop\Twitter\data1218Text.csv", 'rt'))
TEXT = ''
for EachRow in reader:
    tempEachRow = next(itertools.islice(EachRow.values(), 1))
    TempEachRow = tempEachRow.split()
    for each in TempEachRow:
        TEXT = TEXT + ' ' + each
text_file = open("OutputFileSample.txt", "w")
text_file.write(TEXT)
text_file.close()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
