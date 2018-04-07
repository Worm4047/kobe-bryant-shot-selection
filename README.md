# kobe-bryant-shot-selection 

## Objective:
	Using 20 years of data on Kobe's swishes and misses,  predict which shots will find the bottom of the net? 

## Dataset:
	This data contains the location and circumstances of every field goal attempted by Kobe Bryant took during his 20-year career. Your task is to predict whether the basket went in (shot_made_flag).

	I have removed 5000 of the shot_made_flags (represented as missing values in the csv file). These are the test set shots for which you must submit a prediction. You are provided a sample submission file with the correct shot_ids needed for a valid prediction.

## Procedure followed:
	1. Cleaning of data of all null values .
	2. Diving sets into training and testing data .
	3. Converting string data to categorical binary data.
	4. Using basic classification to determine overfitting.
	5. Utilizing kfold cross validation and gridsearch CV to obtain accuracy of about 70 %.

## Order of execution of files
	1. cleaning_data.py
	2. unique_params.py
	3. string_binary.py
	4. index.py
