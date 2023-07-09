import json

def combine_data(iteration):
    start = 1
    end = 90
    # List of file names
    file_names = [f'results/iteration-{iteration}/results/{i}to{i+9}.json' for i in range(start, end, 10)]

    # Create an empty dictionary to store the combined data
    combined_data = {}

    # Read each file and add its data to the combined dictionary
    for file_name in file_names:
        with open(file_name) as file:
            data = json.load(file)
            combined_data.update(data)

    # Save the combined data to a new JSON file
    output_file = f'Results/iteration-{iteration}/final/{start}to{end}.json'
    with open(output_file, 'w') as file:
        json.dump(combined_data, file, indent=4)

    print(f"Combined data saved to '{output_file}'.")

# Example usage: combining data from 1 to 50
combine_data(4)
