import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row  # Store entire row as value
    
    return dictionary

def main():
    # Read the products CSV into a dictionary
    products_dict = read_dictionary('products.csv', 0)
    print("Products Dictionary:", products_dict)  # Print the dictionary to verify
    
    # Open and process the request CSV
    with open('request.csv', mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        
        print("\nRequested Items:")
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            if product_number in products_dict:
                product_name = products_dict[product_number][1]
                product_price = float(products_dict[product_number][2])
                
                print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
            else:
                print(f"Product {product_number} not found in catalog.")

if __name__ == "__main__":
    main()
