# %%
import pandas as pd
df = pd.read_csv('vgsales.csv')
print(df.to_string()) 

# %%
# Remove rows/columns with too many missing values:
df.dropna(inplace=True)
df.dropna(axis=1, inplace=True)
print(df.to_string())


# %%
# Check for duplicates:ตรวจหาข้อมูลซ้ำกัน
df.duplicated().sum()

# %%
# Remove duplicates:ลบข้อมูลซ้ำกัน
df = df.drop_duplicates()

# %%
# Check for outliers:ตรวจหาค่าผิดปกติ
for col in ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"{col} → Outliers: {len(outliers)} rows")

# %%
# Remove outliers:ลบค่าผิดปกติ
df_no_outliers = df[(df['Global_Sales'] >= lower) & (df['Global_Sales'] <= upper)]
print(f"DataFrame shape after removing outliers: {df_no_outliers.shape}")

#%%
# Remove outliers from all sales columns
sales_cols = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']
for col in sales_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

print("จำนวนแถวที่เหลือ:", len(df))


# %%
# แสดงกราฟแท่งของ 10 เกมที่มียอดขายสูงสุด
import matplotlib.pyplot as plt

top_games = df.groupby("Name")["Global_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_games.plot(kind="bar")
plt.title("Top 10 Best-Selling Games (Global)")
plt.ylabel("Global Sales (Millions)")
plt.xlabel("Game")
plt.xticks(rotation=45, ha="right")
plt.show()


# %%
# แสดงกราฟแท่งของยอดขายรวมตามประเภทเกม
genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
genre_sales.plot(kind="bar", color="skyblue")
plt.title("Total Global Sales by Genre")
plt.ylabel("Global Sales (Millions)")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.show()

# %%
# แสดงกราฟเส้นของแนวโน้มยอดขายตามปี
year_sales = df.groupby("Year")["Global_Sales"].sum()

plt.figure(figsize=(12,6))
year_sales.plot(kind="line", marker="o")
plt.title("Global Sales Trend by Year")
plt.ylabel("Global Sales (Millions)")
plt.xlabel("Year")
plt.grid(True)
plt.show()


# %%
# แสดงกราฟแท่งของยอดขายรวมตามแพลตฟอร์ม
genre_sales = df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
genre_sales.plot(kind="bar", color="lightgreen")
plt.title("Total Global Sales by Platform")
plt.ylabel("Global Sales (Millions)")
plt.xlabel("Platform")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

