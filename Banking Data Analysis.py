import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'D:\Finlatics\Banking\banking_data.csv')

# Analyze the 'age' column
# Get unique age values
age_counts = df['age'].unique()
print("Unique age values:", age_counts)

# Get descriptive statistics for the 'age' column
print("Descriptive statistics for age:\n", df['age'].describe())

# Get value counts for the 'age' column
age_value_counts = df['age'].value_counts()
print("Age value counts:\n", age_value_counts)

# Create a box plot and count plot for the 'age' column
plt.figure(figsize=(10, 5))
sns.boxplot(y='age', data=df)
plt.title("Box plot for age")
plt.show()

plt.figure(figsize=(10, 5))
sns.countplot(y='age', data=df)
plt.title("Count plot for Age")
plt.show()

# Analyze the 'job' column
# Get value counts for the 'job' column
job_value_counts = df['job'].value_counts()
print("Job value counts:\n", job_value_counts)

plt.figure(figsize=(10, 5))
sns.countplot(y='job', data=df)
plt.title("Count plot for Job")
plt.show()

# Analyze the 'marital_status' column
marriage_value_counts = df['marital_status'].value_counts()
print("Marital status value counts:\n", marriage_value_counts)

# Analyze the 'education' column
education_value_counts = df['education'].value_counts()
print("Education value counts:\n", education_value_counts)

# Analyze the 'default' column
default_value_counts = df['default'].value_counts()
print("Default value counts:\n", default_value_counts)

# Calculate the proportion of clients with default credit
proportion = (default_value_counts['yes'] / df.shape[0])
print('Proportion of clients having credit in default is:', proportion)

# Analyze the 'balance' column
balance_value_counts = df['balance'].value_counts()
print("Balance value counts:\n", balance_value_counts)

# Get descriptive statistics for the 'balance' column
print("Descriptive statistics for balance:\n", df['balance'].describe())

# Analyze the 'housing' column
housingloan_value_counts = df['housing'].value_counts()
print("Housing loan value counts:\n", housingloan_value_counts)

# Analyze the 'loan' column
personalloan_value_counts = df['loan'].value_counts()
print("Personal loan value counts:\n", personalloan_value_counts)

# Analyze the 'contact' column
contact_value_counts = df['contact'].value_counts()
print("Contact value counts:\n", contact_value_counts)

# Analyze the 'day' column
contactday_value_counts = df['day'].value_counts()
print("Contact day value counts:\n", contactday_value_counts)

# Analyze the 'month' column
contactmonth_value_counts = df['month'].value_counts()
print("Contact month value counts:\n", contactmonth_value_counts)

# Analyze the 'duration' column
duration_value_counts = df['duration'].value_counts()
print("Duration value counts:\n", duration_value_counts)

# Analyze the 'poutcome' column
outcome_value_counts = df['poutcome'].value_counts()
print("Poutcome value counts:\n", outcome_value_counts)

# Analyze the 'y' column (whether the client subscribed to the term deposit)
subscribed_value_counts = df['y'].value_counts()
print("Subscription (y) value counts:\n", subscribed_value_counts)

# Generate the correlation matrix heatmap for numerical columns
# Select numerical columns from the dataframe
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Calculate the correlation matrix
corr_matrix = numeric_df.corr()

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(10, 10))
sns.heatmap(corr_matrix, annot=True, cmap='PuBuGn', fmt=".2f")
plt.title("Correlation Matrix of this data")
plt.show()