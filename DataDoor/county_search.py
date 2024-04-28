import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_website_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.text if soup.title else 'No Title'
    summary = soup.find('meta', {'name': 'description'})
    # summary = summary['content'] if summary else 'No Summary'
    summary = summary['content'].strip() if summary else 'No Summary'
    
    return title, summary

def score_website(url, summary):
    score = 0
    
    # Check if the URL contains indicators of data hubs or Open Data portals
    if 'data' in url.lower() or 'opendata' in url.lower() or 'data.gov' in url.lower()or 'dataset' in url.lower():
        score += 3
    
    # Check if the summary exists
    if summary != "No Summary":
        score += 10
    
    return score

def custom_google_search_county(query, county, state):
    search_query = f'{query} open "data" AND "county" of {county} {state} OR site:.gov OR inurl:data OR site:arcgis.com OR site:.org'
    results = search(search_query, num_results=1)
    return results

# def custom_google_search_state(query, state):
#     search_query = f'{query} open "data" AND {state} OR site:.gov OR inurl:data OR site:arcgis.com OR site:.org'
#     results = search(search_query, num_results=2)
#     return results

# def custom_google_search_fed(query):
#     search_query = f'{query} open "data" AND united states AND site:data.gov'
#     results = search(search_query, num_results=2)
#     return results

def get_county(data, address_dict):


    # Example usage:
    query = data
##    municipality = address_dict["City"]
    county = address_dict["County"]
    state = address_dict["State"]

    ###########County
    results_county = custom_google_search_county(query, county, state)

    # Dictionary to store search results along with their scores
    result_scores_county = {}

    for link in results_county:
        title, summary = get_website_info(link)
        score = score_website(link, summary)
        result_scores_county[link] = {'title': title, 'summary': summary, 'score': score}

    # Sort the results based on their scores in descending order
    sorted_results_county = sorted(result_scores_county.items(), key=lambda x: x[1]['score'], reverse=True)

    result_dict_county={}
    # Print the sorted results
    for link, info in sorted_results_county:
        result_dict_county["name"] = info['title']
        result_dict_county["summary"] = info['summary']
        result_dict_county["url"] = link
        break

##    ###########Muni
## 
##    results_muni = custom_google_search_muni(query, municipality, state)
##
##    # Dictionary to store search results along with their scores
##    result_scores_muni = {}
##
##    for link in results_muni:
##        title, summary = get_website_info(link)
##        score = score_website(link, summary)
##        result_scores_muni[link] = {'title': title, 'summary': summary, 'score': score}
##
##    # Sort the results based on their scores in descending order
##    sorted_results_muni = sorted(result_scores_muni.items(), key=lambda x: x[1]['score'], reverse=True)
##
##    result_dict_muni={}
##    # Print the sorted results
##    for link, info in sorted_results_muni:
##        result_dict_muni["name"] = info['title']
##        result_dict_muni["summary"] = info['summary']
##        result_dict_muni["url"] = link
##        break


    return(result_dict_county)
