# import the Pandas library
import pandas as pd

# import the NumPy library
import numpy as np

# name the data frame as 'admission_data'
# header=0 means that the headers for the variable names are to be found in the first row
# sep="," means that "," is used as the separator between the values because we are using the file type .csv (comma-separated values)
admission_data = pd.read_csv("Admission_Predict.csv", header=0, sep=",")

# we have a large CSV file (of 400 rows), you we use the head() function to only show the top 5 rows
print(admission_data.head())

# we use the info() function to list the data types within our data set
print(admission_data.info())

# max() function is used to find the highest value of a variable
max_CGPA = max(admission_data["CGPA"])

print(max_CGPA)

# min() function is used to find the lowest value of a variable
min_CGPA = min(admission_data["CGPA"])

print(min_CGPA)

# mean() function is used to find the average value of a variable
mean_CGPA = np.mean(admission_data["CGPA"])

print(mean_CGPA)

# find the 25% percentile for GPA
percentile25 = np.percentile(admission_data["CGPA"], 25)

# find the 75% percentile for GPA
percentile75 = np.percentile(admission_data["CGPA"], 75)

print(percentile25, percentile75)

# we use the std() function from NumPy to find the standard deviation of a variable
std_CGPA = np.std(admission_data["CGPA"])

print(std_CGPA)

# we use the describe() function in Python to summarize data
print(admission_data["CGPA"].describe())