## README


## Goal Of This Project

The Goal of this Project is to use the Annif Toolkit to assign RVK codes to around 15,000 of the university's theses.

## Process of assigning RVK codes.

## First Step getting digestible files

## Process of assigning RVK codes.
## First Step getting digestible files

01_rvk_transformation: Contains a script that extracts the RVK classification from an XML and transfers it into a tsv table.
02_extraction_of_th-wildau-repository: A script that obtains theses from the TH-Wildau repository.
03_cleaning_and_analysis: The extracted records are processed and analyzed for feasibility.
04_preparation_for_annif: The cleaned data gets prepared to feed Annif.


## Output of this 4 GitHub project are digestible files for Annif:
* "rvk_classification_flattened_with_uri.tsv" to load as vocabulary.
* "records_for_step_03_train_project_annif.tsv" is for training the project.
* A sub-folder "docs" in folder "preparation_for_annif" containing the necessary data for Annif (a tsv and txt file for each record), step 07.

For more information, check out the READMEs and Jupyter Notebooks in the respective folders!


## Second Step Using Annif with the output of the First Step

05_Annif_BIM2022-main
