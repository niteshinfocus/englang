from flask import *
import openai
import os
from script import random_script
from englisttohindi.englisttohindi import EngtoHindi

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    msg=random_script
    trans = EngtoHindi(message=msg)
    return render_template('index.html', translated=trans.convert)


@app.route('/search', methods=['POST'])
def result():
    # getting input from html page
    text = request.form['msg']
    userInput = '{}'.format(text)

    #generating response
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "compare this sentence '" + userInput +" '" + " with '" + random_script + " ' "+ " and find the areas in which first sentence is wrong"}])
    aiMsg = completion.choices[0].message.content

    hindi_feedback = EngtoHindi(message=aiMsg)
    t = hindi_feedback.convert
    
    return render_template('result.html', userInput=userInput, hiMsg=t, aiMsg=aiMsg, random_script=random_script)



if __name__ == '__main__':
    app.run(debug=True)