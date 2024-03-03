import pandas as pd
import time

try:
    start_time = time.time()
    # Read the CSV file
    df = pd.read_csv(r'C:/Users/srini/Downloads/Sundar Code/dino.csv')

    # Convert 'length' column to numeric data type
    df['length'] = pd.to_numeric(df['length'], errors='coerce')

    # Fill missing values in the 'length' column with 1.0
    df['length'].fillna(1.0, inplace=True)

    # Group by species and calculate the average length
    avg_length = df.groupby('species')['length'].mean()

    # Find the species with the largest average length
    largest_avg_length_species = avg_length.idxmax()

    print("Species with the largest average length:", largest_avg_length_species)
    
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

except pd.errors.ParserError as e:
    print("Error parsing CSV file:", e)
except ValueError as e:
    print("Error converting 'length' column to numeric:", e)
