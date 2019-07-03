from flask import Flask, render_template, request, redirect
import random

earned_gold = 0

app=Flask(__name__)
@app.route("/")
def ninja_gold():
    return render_template('index.html',score = earned_gold)

@app.route('/process_gold', methods=['POST'])
def process_gold():

    if request.form['whichbutton'] == 'farm':
        add_gold(int(random.random()*10)+10)
    if request.form['whichbutton'] == 'casino':
        add_gold(int(random.random()*100))


    
    return redirect('/')

def add_gold(gold):
    global earned_gold 
    earned_gold += gold

if __name__ == "__main__":
    
    app.run(debug=True)
