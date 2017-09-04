from nltk.tag.stanford import StanfordNERTagger
from itertools import groupby
import sys
import codecs
stdin = codecs.getreader('utf-8')(sys.stdin)
stdout = codecs.getwriter('utf-8')(sys.stdout)

st = StanfordNERTagger('/home/xsherwan/Files/Stanford Tools/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
'/home/xsherwan/Files/Stanford Tools/stanford-ner-2017-06-09/stanford-ner.jar') # set the path correctly to your stanford ner

#inputlocations = open("sample.txt").read()
inputlocations = stdin.read()
tags = st.tag(inputlocations.split())

for tag, chunk in groupby(tags, lambda x:x[1]):
    if tag != u"O":
        stdout.write(u"{}/{}\n".format(u" ".join(w for w, t in chunk), tag))
    else:
            for w, t in chunk:
                stdout.write(u"{}/{}\n".format(w, t)) 


