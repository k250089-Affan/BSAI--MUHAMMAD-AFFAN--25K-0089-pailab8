import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
data = df[df["scenario"] == "05_AdVsRevenue"].copy()

data["ad_spend"] = data["study_hours"].astype(float)
data["revenue"] = data["prep_course"].astype(float)

sns.regplot(
    data=data,
    x="ad_spend",
    y="revenue",
    marker="+",
    scatter_kws={"color": "darkgreen"}
)

plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()
