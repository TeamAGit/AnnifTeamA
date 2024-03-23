# README

## Goal Of This Project

The primary objective of this project is to leverage the Annif Toolkit to assign RVK codes to approximately 15,000 theses from the University of Wildau. The project comprises two main phases. The initial phase involves generating digestible files suitable for processing through the Annif toolkit. Subsequently, the second phase entails utilizing the Annif toolkit for classification.

## First Step - Generating Digestible Files

### 01_rvk_transformation
- This component incorporates a script designed to extract RVK classifications from XML files and convert them into a structured tsv table format. The script parses the XML data meticulously, extracting relevant RVK codes associated with each thesis entry.

### 02_extraction_of_th-wildau-repository
- Here, a script is utilized to retrieve theses data from the TH-Wildau repository, enabling access to the necessary information for processing.

### 03_cleaning_and_analysis
- Extracted records undergo processing and analysis to ensure their suitability and feasibility for subsequent stages of the project.

### 04_preparation_for_annif
- In this stage, the cleaned data is further refined and formatted to be compatible with the Annif toolkit. 

#### Output of the First Step and Uses
- "rvk_classification_flattened_with_uri.tsv": This file serves as the vocabulary for loading into the Annif toolkit. 
- "records_for_step_03_train_project_annif.tsv": Used for training the Annif project. 
- A sub-folder "docs" in folder "preparation_for_annif" containing the necessary data for Annif (a tsv and txt file for each record), step 07.

## Second Step - Utilizing Annif with First Step Output

### 05_Annif_BIM2022-main
- This phase involves the utilization of the Annif toolkit in conjunction with the output generated from the first step for classification purposes. The Annif toolkit employs machine learning algorithms to classify thesis entries based on their content and associated metadata. By utilizing the prepared data from the first step, Annif can assign RVK codes to theses.

For more detailed information, please refer to the READMEs and Jupyter Notebooks located within the respective folders!
