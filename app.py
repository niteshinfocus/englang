from flask import *
import openai
import os
from script import engScript, hinScript

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    msg=hinScript
    return render_template('index.html', translated=msg)


@app.route('/search', methods=['POST'])
def result():
    # getting input from html page
    text = request.form['msg']
    userInput = '{}'.format(text)

    #generating response
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "compare this sentence '" + userInput +" '" + " with '" + engScript + " ' "+ " and find the areas in which first sentence is wrong with respect to second sentence. Tell in 2-3 lines"}])
    aiMsg = completion.choices[0].message.content

    
    return render_template('result.html', userInput=userInput, aiMsg=aiMsg, random_script=engScript)



if __name__ == '__main__':
    app.run(debug=True)
