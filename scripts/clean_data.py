import pandas as pd
from pathlib import Path
from word2number import w2n

ROOT = Path(__file__).resolve().parent.parent

messy_data = ROOT / "data" / "raw" / "healthcare_messy_data.csv"
clean_data = ROOT / "data" / "clean" / "healthcare_clean_data.csv"

df = pd.read_csv(messy_data)

#Convert all columns to snake case
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#Capitalize first and last names as well as remove extra spaces
df['patient_name'] = df['patient_name'].str.strip().str.title()

#Change written ages to integers
def convert_age(x):
    if pd.isna(x):
        return pd.NA

    if isinstance(x, int):
        return x

    if isinstance(x, str):
        x = x.strip()

        try:
            return int(x)
        except ValueError:
            try:
                return w2n.word_to_num(x)
            except ValueError:
                return pd.NA   # or return x if you want to preserve invalid values

    return pd.NA

df["age"] = df["age"].apply(convert_age).astype("Int64")

#Title case for medication column
df['medication'] = df['medication'].str.strip().str.title()

#Standardize the format of visit_date column
df["visit_date"] = pd.to_datetime(df["visit_date"], errors="coerce")
df["visit_date"] = df["visit_date"].dt.strftime("%Y-%m-%d")

df.to_csv(clean_data, index=False)