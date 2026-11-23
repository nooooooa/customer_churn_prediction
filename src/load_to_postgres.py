import os
import pandas as pd

from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, text

# 1. Tentukan lokasi project
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Load konfigurasi environment
load_dotenv(BASE_DIR / ".env")

# 3. Buat koneksi database
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(connection_url)

with engine.connect() as connection:
    result = connection.execute(
        text("""
            SELECT
                current_database(),
                current_schema(),
                current_user
        """)
    )

    # print("Database information:", result.fetchone())

    # tables = connection.execute(
    #     text("""
    #         SELECT table_name
    #         FROM information_schema.tables
    #         WHERE table_schema = 'public'
    #     """)
    # )

    # print("Tables in database:")
    # for table in tables:
    #     print(table[0])

try:
    # 4. Baca dataset hasil cleaning
    file_path = (
        BASE_DIR / "data" / "process"
        / "telco_customer_churn_cleaned.csv"
    )

    df = pd.read_csv(file_path)

    print("Total CSV data rows:", len(df))
    print("Missing TotalCharges:", df["TotalCharges"].isna().sum())

    # 5. Rename kolom
   
    df = df.rename(columns={
        "customerID": "customer_id",
        "gender": "gender",
        "SeniorCitizen": "senior_citizen",
        "Partner": "partner",
        "Dependents": "dependents",
        "tenure": "tenure",
        "PhoneService": "phone_service",
        "MultipleLines": "multiple_lines",
        "InternetService": "internet_service",
        "OnlineSecurity": "online_security",
        "OnlineBackup": "online_backup",
        "DeviceProtection": "device_protection",
        "TechSupport": "tech_support",
        "StreamingTV": "streaming_tv",
        "StreamingMovies": "streaming_movies",
        "Contract": "contract",
        "PaperlessBilling": "paperless_billing",
        "PaymentMethod": "payment_method",
        "MonthlyCharges": "monthly_charges",
        "TotalCharges": "total_charges",
        "Churn": "churn"
    })

    # print("Columns after renaming:")
    # print(df.columns.tolist())


    # 6. Import data dengan transaksi
    with engine.begin() as connection:

        existing_count = connection.execute(
            text("SELECT COUNT(*) FROM customers")
        ).scalar()

        if existing_count > 0:
            raise ValueError(
                "Data already exists. Import cancelled."
            )

        df.to_sql(
            name="customers",
            con=connection,
            if_exists="append",
            index=False,
            chunksize=500
        )

    # 7. Verifikasi hasil import
    with engine.connect() as connection:
        total_count = connection.execute(
            text("SELECT COUNT(*) FROM customers")
        ).scalar()

    print("Import completed!")
    print("Total rows in PostgreSQL:", total_count)

finally:
    engine.dispose()
