from flask import Flask, render_template, request
from functionalities import input_handel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_page', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        days_off = request.form.get('days_off')
        long_travel = request.form.get('long_travel')
        type_of_prefer = request.form.getlist('type_of_prefer')
        budget = request.form.get('budget')

        checkbox_data = input_handel.process_checkbox_data(type_of_prefer)
        recommendation_html = generate_html(days_off, long_travel, type_of_prefer, budget, checkbox_data)

        # Pass recommendation HTML to the template
        return render_template('recommendation.html', recommendation=recommendation_html)
    else:
        return render_template('predict_page.html')

@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')

def generate_html(days_off, long_travel, type_of_prefer, budget, checkbox_data):
    html_content = f'''
    <h1>Here is ours recommendation for what you have select</h1>
    <ul>
        <li>Your amount of Days off: {days_off}</li>
        <li>Your Budget: {budget}</li>
        <li>Your Reference(s): {type_of_prefer}</li>
        <li>Long Travel: {long_travel}</li>
        <li>Recommendation:
            <ol>
    '''
    
    for preference in type_of_prefer:
        if checkbox_data[preference]:
            html_content += f'<li>{preference}</li>'
    
    html_content += '''
            </ol>
        </li>
    </ul>
    '''
    
    return html_content

if __name__ == '__main__':
    app.run(debug=True)