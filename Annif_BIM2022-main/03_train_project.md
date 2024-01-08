Next step is to train annif.
In this case I selected 350 row of complete data dump containing all Master thesis from TH Wildau repository in July 2023.
To start training insert following comand:
```
annif train thwildau-tfidf-de data-sets/THWildau/thwildau350.tsv
```
1) first call annif train
2) then call project ID as defined in projects.cfg
3) then insert path to folder of training data
4) training takes just couple of seconds since *tsv file is very small resulting in
5) -transforming subject corpus <br>
   -creating vectorizer<br>
   -creating similarity index<br>
   Hint: control if all three processes are complete. due to unknown reasons sometimes the creation of a similarity index is not completed
7) test with command:
```
echo "Technologie" | annif suggest thwildau-tfidf-de
```
![Alt](https://github.com/AndreaBrand/Annif_BIM2022/blob/main/images/echo_test.png)

see images: images/train_annif.png, echo_test.png
