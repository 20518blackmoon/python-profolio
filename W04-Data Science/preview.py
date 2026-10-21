import os
os.chdir(os.path.dirname(os.path.abspath(__file__) ))
# 載入與檢視資料表內容
import pandas as pd
df = pd.read_csv('students.csv')
# 語法範例：預覽前五筆資料
print(df.head(10))
# 自訂筆數：檢視前十筆]
math_scores = df["math"]
print(math_scores.mean())
#平均值
print(math_scores.max())
#最大值
print(math_scores.min())
#最小值
print(df["math"].median())
#中位數
# axis=1 橫向加總(將國文、英文、數學分數加起來)
# axis=0 縱向加總(三科各自的全班總分)
df['total'] = df[['chinese', 'english', 'math']].sum(axis=1)
# 依照 total 降冪排序取第 1 名
top_student = df.sort_values(
    by='total', ascending=False
).head(1)
print(top_student)
