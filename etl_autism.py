import pandas as pd

print("--- Starting Autism Diagnosis Timeline ETL (Explained) ---")

timeline_data = [
    {
        "Year": 1943,
        "Authority": "Leo Kanner",
        "Definition": "Early Infantile Autism",
        "Context": "Rare condition defined by 'insistence on sameness' & social isolation.",
        "Prevalence": "1 in 10,000",
        "Est_US_Cases": "< 15,000",
        "Symptoms": "• <b>Extreme aloneness:</b> Profound lack of interest in others or social interaction.<br>• <b>Delayed echolalia:</b> Repetition of words/phrases heard previously, often out of context.<br>• <b>Hypersensitivity:</b> Extreme adverse reaction to loud noises or bright lights."
    },
    {
        "Year": 1980,
        "Authority": "DSM-III",
        "Definition": "Infantile Autism",
        "Context": "Officially recognized as distinct from schizophrenia. Strict onset criteria.",
        "Prevalence": "1 in 2,000",
        "Est_US_Cases": "~100,000",
        "Symptoms": "• <b>Social responsiveness:</b> Failure to cuddle or make eye contact.<br>• <b>Language deficit:</b> Failure to develop speech or use it for communication.<br>• <b>Onset:</b> Symptoms must appear before 30 months of age."
    },
    {
        "Year": 1994,
        "Authority": "DSM-IV",
        "Definition": "Asperger's & Spectrum",
        "Context": "Major expansion. Included high-functioning cases (Asperger's).",
        "Prevalence": "1 in 150",
        "Est_US_Cases": "~1.5 Million",
        "Symptoms": "• <b>Restricted interests:</b> Intense focus on specific topics (e.g., trains, math).<br>• <b>Asperger's distinction:</b> No significant delay in language or cognitive development, unlike classic autism."
    },
    {
        "Year": 2013,
        "Authority": "DSM-5",
        "Definition": "Autism Spectrum Disorder",
        "Context": "Merged all diagnoses into a single spectrum with severity levels (1-3).",
        "Prevalence": "1 in 59",
        "Est_US_Cases": "~3.5 Million",
        "Symptoms": "• <b>Sensory processing:</b> Over or under-sensitivity to pain, temperature, or sound.<br>• <b>Social-emotional reciprocity:</b> Difficulty with back-and-forth conversation or sharing interests."
    },
    {
        "Year": 2025,
        "Authority": "CDC / Current Status",
        "Definition": "The Current Epidemic",
        "Context": "Highest recorded prevalence. Debate continues on environmental drivers.",
        "Prevalence": "1 in 31",
        "Est_US_Cases": "~5.4 Million+",
        "Symptoms": "• <b>Broad Spectrum:</b> Includes non-verbal individuals requiring 24/7 care to high-IQ professionals.<br>• <b>Co-occurring conditions:</b> High rates of GI issues, seizures, and anxiety."
    }
]

df = pd.DataFrame(timeline_data)
df.to_csv("autism_diagnosis_timeline.csv", index=False)
print("--- SUCCESS: Enriched Autism Data with Definitions ---")
