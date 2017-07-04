# -*- coding: utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('C:/Users/Moizzy/Desktop/thesis writing/Code sample/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'C:/Users/Moizzy/Desktop/thesis writing/Code sample/stanford-ner-2016-10-31/stanford-ner.jar',
					   encoding='utf-8')

text = 'France’s advertising regulator has ordered the fashion house Saint Laurent to remove posters of extremely thin models in degrading poses after an outcry over their appearance around Paris. The campaign features a reclining woman in a fur coat and fishnet tights opening her legs; another has a model in a leotard and stilettos on roller skates bending over a stool.Stephane Martin, head of the advertising regulator ARPP, told AFP that his organisation had received 120 complaints about the way the posters depicted women. The authority bars all “degrading and humiliating” representations of people.One of the offending posters is labelled by a protester. One of the offending posters with a protester’s sticker on it. Photograph: Charles Platiau/Reuter. It has written to Saint Laurent asking it to “stop the use of these images, to withdraw them or to change them”, Martin said, explaining that a more detailed assessment of the campaign would be made on Friday. Britain’s advertising watchdog banned a Saint Laurent advert two years ago that featured a model who appeared to be unhealthily underweight. The latest campaign was created in-house by Saint Laurent, which is under a new Belgian designer, Anthony Vaccarello, whose debut collection featured a dress that exposes one breast. Saint Laurent has declined to comment. The label made its name by putting women in men’s tuxedos, a gesture that chimed with the rising feminist wave of the 1970s. Raphaelle Remy-Leleu, from the French women’s group Osez le Féminisme! (“Dare to be Feminist”), said the poster campaign “ticks all the sexist boxes. The women are objectified, hypersexualised and put in submissive positions”.'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)



