--Number of rows: 1000
SELECT COUNT(*)
FROM patients;

--Number of rows no null values in any column: 37
SELECT COUNT(*)
FROM patients
WHERE patient_name IS NOT NULL
	AND age IS NOT NULL
	AND gender IS NOT NULL
    -- "condition" is a reserved word
	AND "condition" IS NOT NULL
	AND medication IS NOT NULL
	AND visit_date IS NOT NULL
	AND blood_pressure IS NOT NULL
	AND cholesterol IS NOT NULL
	AND email IS NOT NULL
	AND phone_number IS NOT NULL;
    