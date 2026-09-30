import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__) ))
import csv
with open("students.csv", "r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  students = list(reader)
  print(students)
for s in students:
  chinese = int(s["chinese"])
  english = int(s["english"])
  math = int(s["math"])
  average = (chinese + english + math) / 3
  print(s["name"], average)

highest_average_student = max(students, key=lambda s: (int(s["chinese"]) + int(s["english"]) + int(s["math"])) / 3)
print("最高平均學生:", highest_average_student["name"], "平均:", (int(highest_average_student["chinese"]) + int(highest_average_student["english"]) + int(highest_average_student["math"])) / 3)

highest_math_student = max(students, key=lambda s: int(s["math"]))
print("最高數學學生:", highest_math_student["name"], "分數:", highest_math_student["math"])