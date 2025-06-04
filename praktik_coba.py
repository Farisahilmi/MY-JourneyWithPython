import pandas as pd
data = {
    "nama" : ["ari", "budi", "cici"],
    "umur" : [25, 30, 22],
    "nilai": [85, 90, 95]
}

df = pd.DataFrame(data)
print(df["nama"])
print(df.loc[1])
print(df.iloc[1])

print(df.iloc[2])

df["kota"] = ["jakarta", "bandung", "surabaya"]

df = df.drop(index=1)
df = df.rename(columns={"nilai": "skor"})

print(df.info())

