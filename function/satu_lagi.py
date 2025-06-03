import pandas as pd

data = {
    "nama": ["Rina", "Joko", "Sari", "Dedi"],
    "usia": [17, 25, 15, 30]
}

df = pd.DataFrame(data)

df["status_usia"] = df["usia"].apply(lambda x: "dewasa" if x >= 18 else "anak-anak")

print(df)