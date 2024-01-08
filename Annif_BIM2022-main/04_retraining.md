Retrained annif with complete data set:
```
annif train thwildau-tfidf-de data-sets/THWildau/records_for_step_03_train_project_annif.tsv
```
Followed by short echo test
```
echo "Technologie" | annif suggest thwildau-tfidf-de
```
![Alt](https://github.com/AndreaBrand/Annif_BIM2022/blob/main/images/echo_test.png)
