import pandas as pd

df = pd.read_excel("stu_score.xlsx")

ans = df[(df.Age<30) & ((df.Grade == "A") | (df.Grade == "B"))]
print(ans)
