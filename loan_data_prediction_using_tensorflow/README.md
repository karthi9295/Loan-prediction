# Python Loan prediction project overview

##Objective

This project deals with determining whether a loan should be approved or not based on validating the feature variables from loan application with the loan prediction model built using Tensorflow Deep Learning platform.

##Tensorflow model

The model is already built with a data comprising of more than 890 thousand observations and 75 variables.




##Pre-requisites
	Applications : Python 3.5.4 (or) Anaconda build with Python 3.5.4
	Python packages : TensorFlow 1.2.1, Keras 2.0, scikit-learn 0.18.2, pandas 0.20.2, numpy 1.13.3

##Example


##Performance

1. 3-class("bad", "warning" and "safe" loan) classifying: Approximately 90~93% accuracy. The batching is done as below:
	
	bad_index = ['Charged Off','Does not meet the credit policy. Status:Charged Off','Default'] - bad - 0
	warning_index = ['Late (31-120 days)','Late (16-30 days)','In Grace Period'] - warning - 1
	safe_index = ['Fully Paid','Does not meet the credit policy. Status:Fully Paid'] - safe - 2
	

## Run the app locally or in cloud

## Instructions to run.

1. Here I have already created the model and located in the current directory namely, "neural_net_model.h5" and its supporting JSON file.

2. Say if you want to create a new model, navigate to the other folder, (i.e) "loan_data_cleansing" and go through the README.md to create new model using the train data. After done with that model creation, follow the steps given below.

3. Now place the dataset for which you want get the loan approval status in the .data/ directory.

4. The program is already pre built in such a way that it uses the already created model. Execute the below mentioned script from the current directory:

	$ python main_clean.py
	
4. The output will show the top 5 applicants loan approval status by mentioning either 0 or 1 or 2. Map the value based on the batching index which is given above under model performance section

	


