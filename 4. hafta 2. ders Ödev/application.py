import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1- read the file
df = pd.read_csv('StudentsPerformance.csv')
print(df.head())

# 2- count male and female number
gender_counts = df["gender"].value_counts()
print(gender_counts)

# 3- visualize histogram graph
sns.barplot(x=gender_counts.index, y=gender_counts.values)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Number of female and male students')
plt.show()

# 4- what type of race groups are there in race/ethnicity column?
race = df["race/ethnicity"].value_counts()
print(race)

# 5- visualize the above
sns.barplot(x= race.index, y=race.values)
plt.xlabel('Race/Ethnicity')
plt.ylabel('Count')
plt.title('Number of Students by Race/Ethnicity')
plt.show()

# 6- find unique values in parental level of education column
parental_education = df["parental level of education"].value_counts()
print(parental_education)

# 7- find unique values in lunch column
lunch = df["lunch"].value_counts()
print(lunch)

# 8- find test preparation course types and their counts
test_preparation = df["test preparation course"].value_counts()
print(test_preparation)

# 9- find average math score, reading score, writing score according to gender column
# for both genders
average_scores = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
print(average_scores)

# Calculate average scores for female and male students separately
# female_avg = df[df["gender"] == "female"][["math score", "reading score", "writing score"]].mean()
# print("Average scores for female students:", female_avg)

# male_avg = df[df["gender"] == "male"][["math score", "reading score", "writing score"]].mean()
# print("\nAverage scores for male students:",male_avg)

# 10- find average math score, reading score, writing score according to race/ethnicity column
average_scores_ethnicity =df.groupby("race/ethnicity")[["math score", "reading score", "writing score"]].mean()
print(average_scores_ethnicity)

# 11- find average math score, reading score, writing score according to parental level of education column
average_scores_parental_education = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()
print(average_scores_parental_education)

# 12- find average math score, reading score, writing score according to lunch column
average_scores_lunch = df.groupby("lunch")[["math score", "reading score", "writing score"]].mean()
print(average_scores_lunch)

# 13- find average math score, reading score, writing score according to test preparation course column
average_scores_test_preparation = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean()
print(average_scores_test_preparation)








