import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

load_dotenv(ROOT / ".env")

clean_data = ROOT / "data" / "clean" / "healthcare_clean_data.csv"

df = pd.read_csv(clean_data)

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

df.to_sql(
    'patients',
    engine,
    if_exists='replace',
    index=False
)
