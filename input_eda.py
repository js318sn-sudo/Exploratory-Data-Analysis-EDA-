# Exploratory Data Analysis (EDA) Project

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Plot Style
sns.set_style("whitegrid")

# Create Dataset
data = {
     "Name": ["Ravi", "Sita", "Kiran", "Anu", "Rahul",
             "Priya", "Arjun", "Divya", "Vikram", "Sneha"],
     "Age": [25, 30, 28, 35, 40, 27, 32, 29, 31, 26],
     "Gender": ["Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],

     "Department": ["IT", "HR", "Finance", "IT", "Management",
                   "HR", "Finance", "IT", "Management", "IT"],

     "Salary": [45000, 52000, 48000, 65000, 80000,
               50000, 58000, 62000, 72000, 54000],

     "Experience": [2, 5, 3, 8, 12, 4, 6, 5, 9, 3],

     "PerformanceScore": [78, 88, 82, 91, 95,
                         85, 89, 92, 90, 84]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Dataset")
print(df)

# First 5 Rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset Information
print("\nDataset Information")
df.info()

# Dataset Shape
print("\nDataset Shape")
print(df.shape)

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate Values
print("\nDuplicate Values")
print(df.duplicated().sum())

# Data Types
print("\nData Types")
print(df.dtypes)

# Summary Statistics
print("\nSummary Statistics")
print(df.describe())

# Histogram
df.hist(figsize=(10,8))
plt.suptitle("Histogram")
plt.show()

# Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(data=df.select_dtypes(include=np.number))
plt.title("Boxplot")
plt.show()

# Heatmap
plt.figure(figsize=(8,5))

correlation = df.select_dtypes(include=np.number).corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

# Countplot
plt.figure(figsize=(7,5))
sns.countplot(x="Department", data=df)
plt.title("Department Count")
plt.show()

# Pairplot
sns.pairplot(df.select_dtypes(include=np.number))
plt.show()

# Insights
print("\nInsights")
print("1. IT department employees tend to have higher salaries.")
print("2. Experience positively affects salary.")
print("3. Performance scores improve with experience.")
print("4. No missing values are present.")
print("5. No duplicate records were found.")



