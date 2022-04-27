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
uu = 1
page_set = False

@app.route('/results', methods=['GET', 'POST'])
def resultsPage():
    global uu
    global files
    global page_set

    # print(uu)

    # if page_set:
    if(uu<3):
        # remove all existing sub directories from downloads folder
        shutil.rmtree('static/downloads/')
        os.mkdir('static/downloads')
        # print("helo ------------------------------------")
    else:
        uu = 1
        page_set = True
    # else:
    #     if(uu<3):
    #         # remove all existing sub directories from downloads folder
    #         shutil.rmtree('static/downloads/')
    #         os.mkdir('static/downloads')
    #     else:
    #         uu = 2

    uu += 1


    files = []

    # accept the json request from client
    data = request.get_json()

    i = 1
    if request.is_json:
        # process each block of text
        i=1
        for block in data['content']:
            print(block, "\n\n")
            processBlock(block)
            i += 1           
        
    files = getDirectoryDetails()
    return render_template('results.html', data=files, num=3)

def filesLength(files):
    l = 0
    for x in files:
        l += len(x)
    return l

def getDirectoryDetails():
    # entries = os.listdir('static/downloads/') # get details of all folder names under static/downloads
    files = [] # initialize the list of files to empty
    folder_files = os.listdir('static/downloads/')

    i = 1
    # for singleFile in files:
    #     # extension has not been added, but it's still working!!
    #     os.rename('static/downloads/'+singleFile, 'static/downloads/'+str(i))
    #     i += 1

    files = ['static/downloads/'+x for x in folder_files]
    print(files)
    # i=1
    # # loop via the list of folders
    # for folder in entries:
    #     # get the names of inidividual files from each folder
    #     folder_files = os.listdir('static/downloads/'+folder+'/')
    #     for singleFile in folder_files:
    #         # extension has not been added, but it's still working!!
    #         os.rename('static/downloads/'+folder+'/'+singleFile, 'static/downloads/'+folder+'/'+str(i))
    #         i += 1

    #     folder_files = os.listdir('static/downloads/'+folder+'/')
    #     # format it and append to the files list
    #     files.append(['static/downloads/'+folder+'/'+x for x in folder_files])

    return files

if __name__ == "__main__":
    app.run(debug=True)

