import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
data = df[df["scenario"] == "04_CustAgeDist"].copy()

data["age"] = data["prep_course"].astype(int)
data["gender"] = data["study_hours"]

sns.histplot(
    data=data,
    x="age",
    hue="gender",
    bins=5,
    kde=True
)

plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")
plt.show()
