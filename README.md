# README

## Output Of This Project
Output of this GitHub project are digestible files for Annif:
* "rvk_classification_flattened_with_uri.tsv" to load as vocabulary.
* "records_for_step_03_train_project_annif.tsv" is for training the project.
* A sub-folder "docs" in folder "preparation_for_annif" containing the necessary data for Annif (a tsv and txt file for each record), step 07.

## 4 Major Steps - 4 Folders
To get the bibliographic data from the TH-Wildau repository into Annif, 4 major steps (folders) are necessary which will be briefly described in the following. 

01_rvk_transformation: Contains a script that extracts the RVK classification from an XML and transfers it into a tsv table.
02_extraction_of_th-wildau-repository: A script that obtains theses from the TH-Wildau repository.
03_cleaning_and_analysis: The extracted records are processed and analyzed for feasibility. 
04_preparation_for_annif: The cleaned data gets prepared to feed Annif. 

For more information, check out the READMEs and Jupyter Notebooks in the respective folders!
