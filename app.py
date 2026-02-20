from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")  # set your API key in env

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    argument = request.form['argument']
    
    prompt = f"Identify any logical fallacies in the following argument and classify them (e.g., strawman, slippery slope, ad hominem):\n\n\"{argument}\""

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0
    )

    result = response.choices[0].text.strip()
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

