#عمل data cleaning
import pandas as pd 
data = pd.read_csv("challenge_data.csv")
#مسح الخانه الفارغه في sereis FullName
data.dropna(subset=['FullName'],inplace=True)
#تحويل sereis JoinDate لي تواريخ و ملئ القيم Nat  ب اقرب تريخ
data['JoinDate'] = pd.to_datetime(data['JoinDate'],errors='coerce')
data['JoinDate'] = data['JoinDate'].fillna(method='ffill')
#تحويل sereis Age لي float64 و التعامل مع القيم الغلك ب None  و ملئ القيم None  ب متوسط العمر
#تحويل العمود Age لي float64  و القيم غير قابله لي تحويل اجعله NaN و ملئ القيم الفارغه ب متوسط العمر
data['Age'] = pd.to_numeric(data['Age'],errors='coerce')
age_mean = data['Age'].mean()
data['Age'] = data['Age'].fillna(age_mean.round())
#تحويل series Income  لي float64 و القيم الغير قابله لتغير حوله لي NaN  ثم ملئ القيم الفارغه بالمتوسط 
data['Income'] = pd.to_numeric(data['Income'],errors='coerce') 
income_mean = data['Income'].mean()
data['Income'] = data['Income'].fillna(income_mean)
# ملئ القيم الفارغه ب اكثر قيمه مكرره في series City
city_mode = data['City'].mode()[0]
data['City'] = data['City'].fillna(city_mode)
#تحويل تنسيق الكتابه موحد و ملئ القيم الفارغه ب اكثر قيمه مكرره 
data['Membership'] = data['Membership'].str.strip().str.lower()
membership_mode = data['Membership'].mode()[0]
data['Membership'] = data['Membership'].fillna(membership_mode)
#تحويل sereis LastPurchase لي تاريخ و تحويل القيم الغير صحيحه لي Nat  و ملئ القيم الفارغه ب ffill
data['LastPurchase'] = pd.to_datetime(data['LastPurchase'],errors='coerce')
data['LastPurchase'] = data['LastPurchase'].fillna(method='ffill')
#تصدير المف باسم challenge_data_cleaned
data.to_csv("challenge_data_cleaned.csv",index=False)
#Exploratory
print(data)
print(f"\n{data.head()}\n")
print(data.info())