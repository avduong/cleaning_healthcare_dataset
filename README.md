# Healthcare Dataset ETL Pipeline Using Python and PostgreSQL

This was an exercise in cleaning commonly found data entry issues in healthcare datasets. Conditions and medications did not align for many records, such as metformin for heart disease. However, medical accuracy is not the purpose of this exercise.

## Project Structure
    /data
        /clean
            healthcare_clean_data.csv
        /raw
            healthcare_messy_data.csv

    /scripts
        clean_data.py
        load_data.py

    /sql
        data_validation.sql

    README.md

## Data Sources
URL: https://github.com/eyowhite/Messy-dataset/blob/main/healthcare_messy_data.csv

## Data Cleaning
1. Original dataset kept in cleaning_healthcare_dataset/data/raw/healthcare_messy_data.csv
2. Reviewed columns one at a time and altered if needed. Cleaning script located in cleaning_healthcare_dataset/scripts/clean_data.py. The script saved the resulting cleaned dataset to cleaning_healthcare_dataset/data/clean/healthcare_clean_data.csv. For categories like age, there is no empty string values, since everybody has an age. People can be missing a phone number, though, so the null values and empty strings were left as they are.
3. Cleaned dataset was loaded to postgres. Script can be found in cleaning_healthcare_dataset/scripts/load_data.py

## Notes
-The phone_number column includes a mix of NULL values as well as empty string values. Column was left as is, since phone number can be unknown or nonexistant.
-Columns such as age do not have empty strings since every record is expected to have an age value.

## Data Validation
-Total records: 1000
-Records with no null values in any column: 37