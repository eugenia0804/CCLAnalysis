import json

def format_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    pretty_json = json.dumps(data, indent=4)

    with open(file_path, 'w') as file:
        file.write(pretty_json)

# Example usage
file_path = 'results/iteration-1/final/1to90.json'
format_json(file_path)