# Topnym-Disambiguation

Our flowchart of work is based on three steps:

Gazetteer to Graphetteer
Toponym extraction
Toponym Resolution

We have provided the scripts for each steps in their relevant folders for reproduceability.

Gazetteer to Graphetteer:
Geonames is the well known database used for graph DB creation. We have used Neo4j for creation of graph. First script provided in this step folder is about importing the data and second script is linking those nodes to their respective nodes or location names.

Toponym Extraction:
For toponym extraction, we have used Stanford NER tagger. Through NER tagger we have tagged all the location names and then used a script to consider consecutive location tagged entries to be combined as one. For example: United /location Kingdom /location should be combined into United Kingdom/location.
Secondly we have used script to convert each space between two tagged entries to be converted into a new line(vertical formatting).
each and every line is then indexed.
After indexing of all articles, entries containing /location tag should be extracted with their relevant article number.


Toponym Resolution:
We have provided three different scripts for our approaches:
First script is to find the toponym based on highest population. 
Second script is to find the distance between pair of locations in the articles and find the shortest distance.
Third approach is to find the distance between the pair of locations in the articles based on the number of edges between them considering population property in it.


    
