

from flask import Flask, render_template, request, redirect, url_for
from geocode import get_location
from muni_county_search import get_muni_county
from fed_search import get_fed
from state_search import get_state



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def handle_form_submission():
    if request.method == 'POST':
        # Retrieve the form data
        data = request.form.get('data')
        zip_code = request.form.get('zip_code')

        # Sample data
        placeholder_name = "Placeholder Dataset"
        placeholder_url = "data.gov"
        placeholder_summary = "Summary"

        # Truncate placeholder_name to 30 characters
        def truncate_name(name):
            truncated_name = name[:30] + '...' if len(name) > 30 else name
            return(truncated_name)
            
        # Truncate placeholder_summary to 100 characters
        def truncate_summary(summary):
            truncated_summary = summary[:120] + '...' if len(summary) > 100 else summary
            return(truncated_summary)

         # Truncate placeholder_url to 50 characters
        def truncate_url(url):
            truncated_url = url[:50] + '...' if len(url) > 50 else url
            return(truncated_url)


        #####Geocode
 
        import certifi
        import ssl
        import geopy

        # Disable SSL certificate verification
        ctx = ssl._create_unverified_context(cafile=certifi.where())
        geopy.geocoders.options.default_ssl_context = ctx

        address_dict = get_location(zip_code)

        #####Fed
        fed_dict = get_fed(data)
        fed_dict["name"] = truncate_name(fed_dict["name"])
        fed_dict["summary"] = truncate_summary(fed_dict["summary"])
        fed_dict["url"] = truncate_summary(fed_dict["url"])

        #####State
        state_dict = get_state(data,address_dict["State"])
        state_dict["name"] = truncate_name(state_dict["name"])
        state_dict["summary"] = truncate_summary(state_dict["summary"])
        state_dict["url"] = truncate_url(state_dict["url"])

        #####County and Muni
        county_dict, muni_dict = get_muni_county(data, address_dict)
        county_dict["name"] = truncate_name(county_dict["name"])
        county_dict["summary"] = truncate_summary(county_dict["summary"])
        county_dict["url"] = truncate_url(county_dict["url"])

        muni_dict["name"] = truncate_name(muni_dict["name"])
        muni_dict["summary"] = truncate_summary(muni_dict["summary"])
        muni_dict["url"] = truncate_url(muni_dict["url"])

        #####Placeholder
        truncated_summary = truncate_summary(placeholder_summary)
        truncated_name = truncate_name(placeholder_name)
        truncated_url = truncate_url(placeholder_url)

        print(county_dict)

        return render_template('search.html', 
                               muni_name=muni_dict["name"],
                               muni_url=muni_dict["url"],
                               muni_summary=muni_dict["summary"],
                               county_name=county_dict["name"],
                               county_url=county_dict["url"],
                               county_summary=county_dict["summary"],
                               state_name=state_dict["name"],
                               state_url=state_dict["url"],
                               state_summary=state_dict["summary"],
                               fed_name=fed_dict["name"],
                               fed_url=fed_dict["url"],
                               fed_summary=fed_dict["summary"],
                               data=data, 
                               zip_code=zip_code)
    

    else:
        data = request.form.get('data', '')  # Get the value from the form input
        zip_code = request.form.get('zip_code', '')  # Get the value from the form input
        return render_template('search.html', data=data, zip_code=zip_code)


if __name__ == '__main__':
    app.run(debug=True)


