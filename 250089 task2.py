import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
data = df[df["scenario"] == "02_MonthlySales"]

for company, group in data.groupby("school_type"):
    plt.plot(group["study_hours"], group["exam_score"], marker="o", label=company)

plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()
plt.show()
