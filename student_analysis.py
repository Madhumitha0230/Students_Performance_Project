import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student_performances.csv")
print(df.head())
df["Average_Score"] = (
    df["Math_Score"] +
    df["Reading_Score"] +
    df["Writing_Score"]
) / 3
df[["Math_Score", "Reading_Score", "Writing_Score"]].mean().plot(kind="bar",color=["skyblue","lightgreen","salmon"])
avg = df[["Math_Score", "Reading_Score", "Writing_Score"]].mean()
avg.plot(kind="bar",color=["skyblue","lightgreen","salmon"])
df.groupby("Gender")[["Math_Score", "Reading_Score", "Writing_Score"]].mean().plot(kind="bar")
plt.title("Average Scores by Subject")
plt.ylabel("Score")
plt.xlabel("Subject")

for i,v in enumerate(avg):
    plt.text(i,v+1,str(round(v,1)),ha='center')
    plt.savefig("average_scores.png")
plt.show()