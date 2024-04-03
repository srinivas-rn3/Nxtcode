# Importing necessary libraries
import pandas as pd 

# Step 1: Extract data
def extract_data(file_path):
    """
    Extracts data from a CSV file and returns a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found.Please cehck the file path:")
        return None 
    except Exception as e:
        print("An error occurred during data extraction:",str(e))
        return None

# Step 2: Transform data
def transform_data(data):
    """
    Transforms the data by performing some operations.
    """
    try:
        # Example transformation: converting date string to datetime
        data['Date'] = pd.to_datetime(data['Date'])
        # Example transformation: adding a new column
        data['Year'] = data['Date'].dt.year
        return data 
    except Exception as e:
        print("An Error occured during data transfromation:",str(e))
        return None

'''
def transform_data(data):
    """
    Transforms the data by performing some operations.
    """
     # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Extract year from 'Date' and create a new 'Year' column
    data['Year'] = data['Date'].dt.year
    
    return data
'''
# Step 3: Load data
def load_data(data):
    """
    Loads the transformed data into a new CSV file.
    """
    try:
        data.to_csv(r"C:\Users\srini\OneDrive\Documents\pythonFiles\transform_data.csv",index=False)
        print("Data Successfully loaded.")
    except Exception as e:
        print("An error occurred  during data transfromation:", str(e))
        return None

# Main function to orchestrate the ETL process
def main():
    # Extracted Data
    file_path = r"C:\Users\srini\OneDrive\Documents\pythonFiles\new_csv.csv" # Path to your CSV file
    extracted_data = extract_data(file_path)
    if extracted_data is not None:
        # Transform data
        transformed_data = transform_data(extracted_data)
        
        if transform_data is not None:
            # Load data
            load_data(transformed_data)

# Calling the main function to start the ETL process
if __name__ == '__main__':
    main()