import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

xsmb = pd.read_csv("XSMB.csv")

xsmb_clone = xsmb.copy()


xsmb_clone["odd"]= xsmb_clone["KQ"].apply(lambda x:0 if x%2==0 else 1)

xsmb_odd = xsmb_clone.groupby("odd").count().reset_index()
# print(xsmb_odd)
sns.barplot(data=xsmb_odd,x="odd",y="KQ")
plt.show()


xsmb["last2digit"]=xsmb["KQ"].apply(lambda x: int(str(x)[-2:]))

# last2digit = xsmb["last2digit"].value_counts()

xsmb_last2digit = xsmb.groupby("last2digit").count().reset_index()
print(xsmb_last2digit)

plt.plot(xsmb_last2digit["last2digit"],xsmb_last2digit["KQ"])
# sns.displot(xsmb["last2digit"],height=5,aspect=3)
plt.show()

