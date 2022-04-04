from flask import Flask, render_template, request, json, jsonify
from process import processBlock
import os, time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    data = request.get_json()
    content =  request.get_json()
    return render_template("index.html", content = content)




    # data = request.get_json()
    # data = jsonify(data)
    # return render_template("index.html", content = data)
    # return render_template("index.html", content = request.form['myDoc'])
    # content = ""
    # if request.form :
    #     content = request.form['myDoc']
    # # return render_template(content)
    # # if request.method == "POST":

files = []
@app.before_request
def before_request():
    global files
    # content =  request.get_json()
    data = request.get_json()

    if request.is_json:
        # process each block of text
        i=1
        for block in data['content']:
            processBlock(block, i)
            i += 1           
            print(block, "\n\n")

        # return render_template('results.html', data=[1, 2,3]) # this is not working !!
    files = getDirectoryDetails()


@app.route('/results', methods=['GET', 'POST'])
def resultsPage():
    return render_template('results.html', data=files)

def getDirectoryDetails():
    entries = os.listdir('static/downloads/') # get details of all folder names under static/downloads
    files = [] # initialize the list of files to empty

    # loop via the list of folders
    for folder in entries:
        # get the names of inidividual files from each folder
        folder_files = os.listdir('static/downloads/'+folder+'/')
        # format it and append to the files list
        files.append(['static/downloads/'+folder+'/'+x for x in folder_files])

    return files

if __name__ == "__main__":
    app.run(debug=True)

