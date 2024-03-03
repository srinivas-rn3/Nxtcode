import pandas as pd
import time

try:
    start_time = time.time()

    # Read the CSV file
    df = pd.read_csv(r'C:/Users/srini/Downloads/Sundar Code/dino.csv')

    # Drop rows with NaN values in the 'species' column
    df = df.dropna(subset=['species'])

    # Use a dictionary comprehension to group dinosaurs with the same sorted letters
    dino_groups = {}
    for dino_name in df['species']:
        if isinstance(dino_name, str):
            sorted_name = ''.join(sorted(dino_name.lower()))
            key = tuple(sorted_name)  # Convert list to tuple for using it as a key
            if key in dino_groups:
                dino_groups[key].append(dino_name)
            else:
                dino_groups[key] = [dino_name]

    # Extract the values from the dictionary to get the list of lists of dinosaur names
    result = list(dino_groups.values())

    # Print the result
    print(result)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

except pd.errors.ParserError as e:
    print("Error parsing CSV file:", e)
except FileNotFoundError:
    print("CSV file not found.")
except Exception as e:
    print("An error occurred:", e)

