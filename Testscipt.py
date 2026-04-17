import pandas as pd
import numpy as np

# 1. Inladen van een externe dataset
# Vervang 'dataset.csv' door het daadwerkelijke bestandspad
try:
    df = pd.read_csv('dataset.csv')
    print("Bestand succesvol geladen.\n")
except FileNotFoundError:
    print("Fout: Bestand niet gevonden.")
    # Dummy data voor demonstratie als bestand ontbreekt
    data = {
        'waarde': [10, 20, np.nan, 40, 50],
        'categorie': ['A', 'B', 'A', 'B', 'A']
    }
    df = pd.DataFrame(data)

# 2. Opschonen van de data
# Verwijder rijen met lege waarden of vul ze in
df_cleaned = df.dropna().copy()

# 3. Basisstatistieken berekenen
stats = {
    'Gemiddelde': df_cleaned.mean(numeric_only=True),
    'Mediaan': df_cleaned.median(numeric_only=True),
    'Standaarddeviatie': df_cleaned.std(numeric_only=True)
}

# 4. Output genereren
print("--- Beschrijvende Statistiek ---")
for key, value in stats.items():
    print(f"\n{key}:")
    print(value)

# 5. Opslaan van de opgeschoonde data
df_cleaned.to_csv('cleaned_dataset.csv', index=False)
print("\nOpgeschoonde data opgeslagen als 'cleaned_dataset.csv'")