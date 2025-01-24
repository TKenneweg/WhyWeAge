
def getMortalityData(file_path):
    # Initialize lists for Single-Year Ages Code and Crude Rate
    single_year_ages_code = []
    crude_rate = []

    # Read the file and process each line
    with open(file_path, "r") as file:
        for line in file:
            # Split the line by tabs
            columns = line.strip().split("\t")

            # Check if the line has the expected number of columns
            if len(columns) >= 5:
                try:
                    # Extract Single-Year Ages Code and Crude Rate
                    age_code = columns[1].strip().strip('"')
                    rate = columns[4].strip().strip('"')

                    # Only add numeric values to the lists
                    if age_code.isdigit() and rate.replace(".", "").isdigit():
                        single_year_ages_code.append(int(age_code))
                        crude_rate.append(float(rate)/1e5)
                except ValueError:
                    continue  # Skip lines with invalid data
    
    return single_year_ages_code, crude_rate
    # Output the results
    # print("Single-Year Ages Code:", single_year_ages_code)
    print("Crude Rate:", crude_rate)
