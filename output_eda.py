# Output:
Name  Age  Gender  Department  Salary  Experience  PerformanceScore
0    Ravi   25    Male          IT   45000           2                78
1    Sita   30  Female          HR   52000           5                88
2   Kiran   28    Male     Finance   48000           3                82
3     Anu   35  Female          IT   65000           8                91
4   Rahul   40    Male  Management   80000          12                95
5   Priya   27  Female          HR   50000           4                85
6   Arjun   32    Male     Finance   58000           6                89
7   Divya   29  Female          IT   62000           5                92
8  Vikram   31    Male  Management   72000           9                90
9   Sneha   26  Female          IT   54000           3                84

First 5 Rows
    Name  Age  Gender  Department  Salary  Experience  PerformanceScore
0   Ravi   25    Male          IT   45000           2                78
1   Sita   30  Female          HR   52000           5                88
2  Kiran   28    Male     Finance   48000           3                82
3    Anu   35  Female          IT   65000           8                91
4  Rahul   40    Male  Management   80000          12                95

Dataset Information
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 7 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Name              10 non-null     object
 1   Age               10 non-null     int64 
 2   Gender            10 non-null     object
 3   Department        10 non-null     object
 4   Salary            10 non-null     int64 
 5   Experience        10 non-null     int64 
 6   PerformanceScore  10 non-null     int64 
dtypes: int64(4), object(3)
memory usage: 692.0+ bytes

Dataset Shape
(10, 7)

Missing Values
Name                0
Age                 0
Gender              0
Department          0
Salary              0
Experience          0
PerformanceScore    0
dtype: int64

Duplicate Values
0

Data Types
Name                object
Age                  int64
Gender              object
Department          object
Salary               int64
Experience           int64
PerformanceScore     int64
dtype: object

Summary Statistics
             Age       Salary  Experience  PerformanceScore
count  10.000000     10.00000    10.00000         10.000000
mean   30.300000  58600.00000     5.70000         87.400000
std     4.522782  11187.29438     3.12872          5.125102
min    25.000000  45000.00000     2.00000         78.000000
25%    27.250000  50500.00000     3.25000         84.250000
50%    29.500000  56000.00000     5.00000         88.500000
75%    31.750000  64250.00000     7.50000         90.750000
max    40.000000  80000.00000    12.00000         95.000000


# EDA Output

## Histogram

![Histogram](histogram.png)

## Boxplot

![Boxplot](boxplot.png)

## Heatmap

![Heatmap](heatmap.png)

## Countplot

![Countplot](countplot.png)

## Pairplot

![Pairplot](pairplot.png)

## Insights

1. The dataset contains no missing values.
2. The dataset contains no duplicate records.
3. Employee salaries vary across departments.
4. Experience shows a positive relationship with salary.
5. Performance scores generally increase with experience.






























===== Histogram Output =====
Histogram graph displayed successfully.

===== Boxplot Output =====
Boxplot graph displayed successfully.

===== Heatmap Output =====
Correlation Heatmap displayed successfully.

===== Countplot Output =====
Department Countplot displayed successfully.

===== Pairplot Output =====
Pairplot displayed successfully.


Insights
1. IT department employees tend to have higher salaries.
2. Experience positively affects salary.
3. Performance scores improve with experience.
4. No missing values are present.
5. No duplicate records were found.


