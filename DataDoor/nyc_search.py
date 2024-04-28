###########################This one works
import pandas as pd
from rapidfuzz import process

def get_nyc(data):

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('city_NewYorkCity_2024.csv')

    # Define a function to perform the fuzzy search
    def fuzzy_search(query, choices, limit=1):
        results = process.extract(query, choices, limit=limit)
        return results

    # Get the search query from the user
    query = data

    choices_name = df['name'].tolist()
    choices_summary = df['summary'].tolist()
    choices = [(name + " " + summary) for name, summary in zip(choices_name, choices_summary)]


    # Perform the fuzzy search
    results = fuzzy_search(query, choices)

    # Define a function to format the matched row as a dictionary
    def format_row_as_dict(row):
        return {
            'name': row['name'],
            'summary': row['summary'],
            'url': row['url']
        }

    # Print the most relevant matches
    for result in results:
        match = result[0]
        match_score = result[1]
        matched_row = df[(df['name'] + " " + df['summary']) == match].iloc[0]  # Get the first row if there are multiple matches
        formatted_row = format_row_as_dict(matched_row)
        # print("Matched row:")
        # print(formatted_row)
        # print("Match score:", match_score)
        # print()
    print("NYC done!")
    return formatted_row
