from gc import callbacks
from flask import Flask, render_template, request, json, jsonify
from process import processBlock
import os, time, shutil

app = Flask(__name__)

'''
    The function index() will return the index.html file when one try to access
    any one of / or /home or /index urls
'''
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")



@app.route('/loading', methods=['GET', 'POST'])
def loadingPage():
    return render_template('loading.html')

    
files = []
'''
    The function resultsPage() will return the results.html file when one try to access
    /results url
'''
@app.route('/results', methods=['GET', 'POST'])
def resultsPage():

    # remove all existing sub directories from downloads folder
    # shutil.rmtree('static/downloads/')
    # os.mkdir('static/downloads')

    global files
    files = []

    # accept the json request from client
    data = request.get_json()

    i = 1
    if request.is_json:
        # process each block of text
        i=1
        for block in data['content']:
            processBlock(block, i)
            i += 1           
            print(block, "\n\n")
        
    files = getDirectoryDetails()
    print(files)
    # lenFiles = len(files)
    # print("valueo f i", lenFiles)
    # print("\n--------------", len(files))
    # print(filesLength(files))
    return render_template('results.html', data=files)

def filesLength(files):
    l = 0
    for x in files:
        l += len(x)
    return l

def getDirectoryDetails():
    entries = os.listdir('static/downloads/') # get details of all folder names under static/downloads
    files = [] # initialize the list of files to empty

    i=1
    # loop via the list of folders
    for folder in entries:
        # get the names of inidividual files from each folder
        folder_files = os.listdir('static/downloads/'+folder+'/')
        for singleFile in folder_files:
            # extension has not been added, but it's still working!!
            os.rename('static/downloads/'+folder+'/'+singleFile, 'static/downloads/'+folder+'/'+str(i))
            i += 1

        folder_files = os.listdir('static/downloads/'+folder+'/')
        # format it and append to the files list
        files.append(['static/downloads/'+folder+'/'+x for x in folder_files])

    return files

if __name__ == "__main__":
    app.run(debug=True)

