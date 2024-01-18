from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
from open_ai_chat import get_response_output,check_api

app = Flask(__name__)


csv_data = None
user_api_key= None
# Function to check API key validity
def check_api_key(api_key):
    try:
        api_return=check_api(api_key)
        return api_return
    except:
        return False

    

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    column_info = None
    global csv_data
    global user_api_key
    if request.method == 'POST':
        api_key = request.form['api_key']
        csv_file = request.files['csv_file']
        user_api_key=api_key

        if not check_api_key(api_key):
            error = "Invalid API Key."
        else:
            if csv_file and csv_file.filename.endswith('.csv'):
                # Read CSV file and get column names with datatypes
                csv_data = pd.read_csv(csv_file)
                column_info = csv_data.dtypes.to_dict()
                
            else:
                error = "Invalid file or file format. Please upload a CSV file."

    return render_template('index.html', error=error, column_info=column_info)

@app.route('/start_chat', methods=['GET'])
def start_chat():
    return render_template('chat_UI.html')

@app.route('/get_initial_bot_response', methods=['POST'])
def get_initial_bot_response():
    # Logic to generate the initial bot response
    initial_bot_response = "Hello! Welcome to Tabular ChatBot! Let's chat with your data to reveal its hidden stories."
    
    return jsonify({'bot_response': initial_bot_response})


@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_input = request.json.get('userInput')

    # Here, you'd implement your logic to generate the bot's response based on user input
    # For demonstration, let's return a simple hardcoded response
    bot_response = get_response_output(user_api_key,user_input,csv_data)
    
    return jsonify({'bot_response': bot_response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int('3000'))