"""
Author: Buddhi W
Date: 07/25/2024
Main script that runs the web UI for the AI agent.
"""

from flask import Flask, request, render_template
from assistant_utils import run_assistant

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        user_query = request.form['question']

        if not user_query:
            output = "Empty query"
        else:
            output = run_assistant(user_query)

        return render_template('index.html', answer=output)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
