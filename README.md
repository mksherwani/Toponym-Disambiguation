# Topnym-Disambiguation

We have used Stanford NER Tagger for tokenizing the articles.
  After tokenizing we have merged the multiple named locations, Person names, and organization into a single name.
  Later We have run the script for Vertical indexing.
  Indexing is done to find out the distance between the locations in the text and words around it.

NEO4J is the main DB for the Geographic Names. with nodes and their relationships. 
    Nodes: Continents, Countries, Cities, Regions, Counties, Landmarks, AdminDivisions
    Relationship: IN, HAS, Adjacent
    
