import pandas as pd

print("--- Starting Autism Diagnosis Timeline ETL (Enriched) ---")

timeline_data = [
    {
        "Year": 1943,
        "Authority": "Leo Kanner",
        "Definition": "Early Infantile Autism",
        "Context": "Rare condition defined by 'insistence on sameness' & social isolation.",
        "Prevalence": "1 in 10,000",
        "Est_US_Cases": "< 15,000",
        "Symptoms": "• Extreme aloneness\n• Delayed echolalia\n• Hypersensitivity to stimuli"
    },
    {
        "Year": 1980,
        "Authority": "DSM-III",
        "Definition": "Infantile Autism",
        "Context": "Officially recognized as distinct from schizophrenia. Strict onset criteria.",
        "Prevalence": "1 in 2,000",
        "Est_US_Cases": "~100,000",
        "Symptoms": "• Lack of social responsiveness\n• Deficits in language\n• Onset before 30 months"
    },
    {
        "Year": 1994,
        "Authority": "DSM-IV",
        "Definition": "Asperger's & Spectrum",
        "Context": "Major expansion. Included high-functioning cases (Asperger's).",
        "Prevalence": "1 in 150",
        "Est_US_Cases": "~1.5 Million",
        "Symptoms": "• Impaired social interaction\n• Restricted interests\n• No general language delay (Asperger's)"
    },
    {
        "Year": 2013,
        "Authority": "DSM-5",
        "Definition": "Autism Spectrum Disorder",
        "Context": "Merged all diagnoses into a single spectrum with severity levels (1-3).",
        "Prevalence": "1 in 59",
        "Est_US_Cases": "~3.5 Million",
        "Symptoms": "• Deficits in social communication\n• Repetitive patterns of behavior\n• Sensory processing issues"
    },
    {
        "Year": 2025,
        "Authority": "CDC / Current Status",
        "Definition": "The Current Epidemic",
        "Context": "Highest recorded prevalence. Debate continues on environmental drivers.",
        "Prevalence": "1 in 31",
        "Est_US_Cases": "~5.4 Million+",
        "Symptoms": "• Broad spectrum covering non-verbal to high IQ\n• Co-occurring conditions (ADHD, Anxiety)\n• GI issues frequently reported"
    }
]

df = pd.DataFrame(timeline_data)
df.to_csv("autism_diagnosis_timeline.csv", index=False)
print("--- SUCCESS: Enriched Autism Data Saved ---")
