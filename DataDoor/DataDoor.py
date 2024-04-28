

from flask import Flask, render_template, request, redirect, url_for


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
        truncated_name = placeholder_name[:30] + '...' if len(placeholder_name) > 30 else placeholder_name

        # Truncate placeholder_summary to 100 characters
        truncated_summary = placeholder_summary[:100] + '...' if len(placeholder_summary) > 100 else placeholder_summary


        return render_template('search.html', 
                               placeholder_name=truncated_name, 
                               placeholder_url=placeholder_url, 
                               placeholder_summary=truncated_summary,
                               data=data, 
                               zip_code=zip_code)
    

    else:
        data = request.form.get('data', '')  # Get the value from the form input
        zip_code = request.form.get('zip_code', '')  # Get the value from the form input
        return render_template('search.html', data=data, zip_code=zip_code)


if __name__ == '__main__':
    app.run(debug=True)


