import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")


print("Given DataFrame :\n", df)
print("\nIterating over rows using iterrows() method :\n")

for index, row in df.iterrows():
    print(row["name"], row["dollar_price"], row["local_price"])


print("Given Dataframe :\n", df)
print("\nIterating over rows using apply function :\n")

print(df.apply(lambda row: row['name'] + " " +
               str(row["dollar_price"]) + " " + 
               str(row["currency_code"]), axis=1))