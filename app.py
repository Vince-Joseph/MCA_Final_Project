from flask import Flask, render_template, request, json, jsonify
from process import processBlock

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


@app.route('/results', methods=['GET', 'POST'])
def resultsPage():
    content =  request.get_json()
    data = request.get_json()

    if request.is_json:
        # process each block of text
        for block in data['content']:
            processBlock(block)
            # print(block, "\n\n")

        return render_template('results.html', data=data['content'][0])
    
    return render_template('results.html', data=[])
    
if __name__ == "__main__":
    app.run(debug=True)


