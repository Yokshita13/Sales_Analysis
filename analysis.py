import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("output", exist_ok=True)

# Read your dataset
df = pd.read_csv("C:\\Users\\Prakhyat\\Desktop\\New folder\\.vscode\\clgproject\\BMW_Sales_Data.csv")
print("Columns in CSV:", df.columns.tolist())

# Clean data
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# 1️⃣ Yearly Sales
plt.figure(figsize=(6,4))
sns.barplot(x='Year', y='Quantity Sold', data=df, estimator='sum', errorbar=None)
plt.title("Yearly BMW Sales")
plt.savefig("output/yearly_sales.png", bbox_inches='tight')
plt.close()

# 2️⃣ Top 5 Models
top_models = df.groupby('Model')['Quantity Sold'].sum().sort_values(ascending=False).head(5)
top_models.plot(kind='bar', color='#1e90ff')
plt.title("Top 5 BMW Models")
plt.xlabel("Model")
plt.ylabel("Units Sold")
plt.savefig("output/top_models.png", bbox_inches='tight')
plt.close()

# 3️⃣ Region-wise Sales
region_sales = df.groupby('Region')['Quantity Sold'].sum()
region_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(5,5))
plt.title("Region-wise BMW Sales")
plt.ylabel("")
plt.savefig("output/region_sales.png", bbox_inches='tight')
plt.close()

# 4️⃣ Correlation Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Between Features")
plt.savefig("output/correlation.png", bbox_inches='tight')
plt.close()

# Summary stats
summary = {
    "total_sales": int(df['Quantity Sold'].sum()),
    "top_model": top_models.index[0],
    "top_region": region_sales.idxmax(),
    "avg_revenue": round(df['Revenue'].mean(), 2)
}

with open("output/summary.txt", "w") as f:
    for key, value in summary.items():
        f.write(f"{key}: {value}\n")

print("✅ Analysis Complete. Check 'output' folder.")


