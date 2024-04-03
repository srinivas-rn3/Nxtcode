import csv

input_file = r"C:\Users\srini\OneDrive\Documents\pythonFiles\sales1.csv" 
output_file = r"C:\Users\srini\OneDrive\Documents\pythonFiles\etl_csv.csv"


def extract_csv(input_file):
    """
    Extract data from a CSV file.
    """
    data = []
    with open(input_file,"r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def transform_data(data):
    """
    Transform data by converting it to uppercase.
    """
    trasform_data = []
    for row in data:
        transform_row = [cell.upper() for cell in row]
        trasform_data.append(transform_row)
    return trasform_data

def load_data(output_csv,data):
    """
    Load transformed data into a CSV file.
    """
    with open(output_csv,'w',newline='') as outcsvfile:
        writer = csv.writer(outcsvfile)
        writer.writerows(data)

if __name__ =='__main__':
    input_file =  input_file 
    output_file = output_file 

    # Extract data
    data1 = extract_csv(input_file)

    # Transform data
    transformed_data = transform_data(data1)

    # Load data
    load_data(output_file,transformed_data)
