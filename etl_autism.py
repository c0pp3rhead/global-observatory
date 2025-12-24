import pandas as pd

print("--- Starting Autism Diagnosis Timeline ETL ---")

# Data based on historical psychiatric records and the referenced view
# Mapping the shift from "Rare Psychosis" to "Common Spectrum"
timeline_data = [
    {
        "Year": 1911,
        "Authority": "Eugen Bleuler",
        "Role": "Swiss Psychiatrist",
        "Definition": "Coined 'Autism'",
        "Context": "Defined as a symptom of Schizophrenia (withdrawal from reality). Not a distinct disorder.",
        "Est_Prevalence": "Unknown"
    },
    {
        "Year": 1925,
        "Authority": "Grunya Sukhareva",
        "Role": "Soviet Psychiatrist",
        "Definition": "Schizoid Psychopathy",
        "Context": "First detailed description of autistic traits in children. Largely ignored by the West.",
        "Est_Prevalence": "Unknown"
    },
    {
        "Year": 1943,
        "Authority": "Leo Kanner",
        "Role": "Johns Hopkins Psychiatrist",
        "Definition": "Early Infantile Autism",
        "Context": "Defined as a rare, severe condition differing from schizophrenia. Characterized by 'insistence on sameness'.",
        "Est_Prevalence": "1 in 10,000"
    },
    {
        "Year": 1944,
        "Authority": "Hans Asperger",
        "Role": "Austrian Pediatrician",
        "Definition": "Autistic Psychopathy",
        "Context": "Described 'little professors' with high intelligence but social deficits. Findings lost until 1981.",
        "Est_Prevalence": "Unknown"
    },
    {
        "Year": 1967,
        "Authority": "Bruno Bettelheim",
        "Role": "Psychologist",
        "Definition": "Refrigerator Mother Theory",
        "Context": "False theory blaming cold parenting. Caused decades of stigma and institutionalization.",
        "Est_Prevalence": "Rare"
    },
    {
        "Year": 1980,
        "Authority": "APA (DSM-III)",
        "Role": "Diagnostic Manual",
        "Definition": "Infantile Autism",
        "Context": "OFFICIAL RECOGNITION. Separated from schizophrenia. Required onset before 30 months.",
        "Est_Prevalence": "1 in 2,000"
    },
    {
        "Year": 1987,
        "Authority": "APA (DSM-III-R)",
        "Role": "Diagnostic Manual",
        "Definition": "Autistic Disorder",
        "Context": "Broadened criteria. Removed the 30-month onset requirement.",
        "Est_Prevalence": "1 in 1,400"
    },
    {
        "Year": 1994,
        "Authority": "APA (DSM-IV)",
        "Role": "Diagnostic Manual",
        "Definition": "Asperger's & PDD-NOS",
        "Context": "MAJOR EXPANSION. Added 'Asperger Syndrome' and 'Pervasive Developmental Disorder'. The 'Spectrum' is born.",
        "Est_Prevalence": "1 in 150"
    },
    {
        "Year": 2013,
        "Authority": "APA (DSM-5)",
        "Role": "Diagnostic Manual",
        "Definition": "Autism Spectrum Disorder (ASD)",
        "Context": "Merged all sub-diagnoses into one 'Spectrum' with support levels (1, 2, 3).",
        "Est_Prevalence": "1 in 59"
    },
    {
        "Year": 2025,
        "Authority": "Sec. Robert F. Kennedy Jr.",
        "Role": "HHS Secretary",
        "Definition": "The Autism 'Emergency'",
        "Context": "Declared an epidemic driven by environmental toxins, rejecting 'better diagnosis' as the sole cause.",
        "Est_Prevalence": "1 in 31"
    }
]

df = pd.DataFrame(timeline_data)
df.to_csv("autism_diagnosis_timeline.csv", index=False)
print("--- SUCCESS: Generated Diagnosis Timeline ---")
print(df[['Year', 'Authority', 'Definition']])
