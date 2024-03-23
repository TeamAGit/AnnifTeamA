Since the project goal is to add RVK notation to master theses of TH Wildau one team member extracted files from the TH Wildau repository (see: https://github.com/mensslen/Annif-Project)

Be careful to follow the recommendations of https://github.com/NatLibFi/Annif/wiki/Subject-vocabulary-formats. Be sure that the TSV file for the vocab only contains 2 columns.
Encoding seems not to matter. UTF-8 works as well as Latin-3.

Take a closer look at the hidden character in the TSV file or faulty cleanup when extracting classification from web sources. (I experienced problems with quotes. If you get stuck open the TSV file in the terminal with cat and check whether there are still characters you already removed!)

TSV File should look like this:
```
th-wildau:A	Allgemeines
th-wildau:AA	Bibliografien der Bibliografien, Universalbibliografien, Bibliothekskataloge, Nationalbibliografien
th-wildau:AA09900	Bibliografische Zeitschriften
th-wildau:AA10000-AA19900	Bibliografien der Bibliografien
th-wildau:AA10000	International, Allgemeines
th-wildau:AA10100	Antike Welt
th-wildau:AA10300	Ländergruppen/Entwicklungsländer
th-wildau:AA10400	Westliche Welt, Abendland, Europäische Welt
th-wildau:AA10500	Germanischer Kulturkreis
th-wildau:AA10600	Europa
```
Then load vocabulary 
```
annif load-vocab --language de rvkthwildau data-sets/THWildau/rvk_test2023v3.tsv
```
rvkthwildau is the vocabulary ID; data-sets/THWildau/rvk_test2023v3.tsv is the path

Attention: 

#) don't forget to put options --langage in the string otherwise you will get error message

#) if you run into error "getötet" or "killed" check data folder. The folder "date / vocabs" gets automatically populated with two files; first subjects.csv. This takes only a couple of seconds. subjects.ttl takes longer and might be the origin of process aportion. In this case check if files contain same data.
![Alt](https://github.com/AndreaBrand/Annif_BIM2022/blob/main/images/load_vocabulary.png)
see: images/load_vocabulary.png

I then loaded the complete RVK list:
```
annif load-vocab rvkthwildau data-sets/THWildau/rvk_test2023v3.tsv --force --language de
```

Depending on the size of TSV file load-vocab should not take to long, only a couple of minutes
