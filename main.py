
import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

subjects = ["Python", "Maths", "Statistics"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

df["Result"] = np.where(
    (df[subjects] >= 35).all(axis=1),
    "Pass",
    "Fail"
)

print("\nStudent Details")
print(df.to_string(index=False))

print("\nClass Summary")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", round(df["Average"].max(), 2))
print("Lowest Average:", round(df["Average"].min(), 2))
print("Passed:", (df["Result"] == "Pass").sum())
print("Failed:", (df["Result"] == "Fail").sum())

print("\nSubject Averages")
for subject in subjects:
    print(subject, ":", round(np.mean(df[subject]), 2))

print("\nTop 5 Students")
top = df.nlargest(5, "Average")
print(top[["Name", "Average", "Grade"]].to_string(index=False))

print("\nAttendance")
print("Average Attendance:", round(df["Attendance"].mean(), 2), "%")