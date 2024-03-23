In order to evaluate quality of the project, you need documents which were manually classifed. Therefore you have to populate docs folder with pairs of fulltext files and a correspondin tsv file with URIs and RVK classification:
![Alt](https://github.com/AndreaBrand/Annif_BIM2022/blob/main/images/eval_ft_rvk.png)

Next run command
```
annif eval thwildau-tfidf-de data-sets/THWildau/docs/test/
```
Results in terminal look like this (please keep in mind that our training/testing materials are incomplete):
![Alt](https://github.com/AndreaBrand/Annif_BIM2022/blob/main/images/eval_result.png)
