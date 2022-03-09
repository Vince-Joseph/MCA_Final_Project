from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    data = request.get_json()
    # data.get('data')
    # print(request.get_data())
    # print(request.get_json())
    content =  request.get_json()
    print(content)
    # resultsPage(content)
    # results = {'processed': request.method}
    # return jsonify(results)
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
    # print("from results page", content)
    content =  request.get_json()
    # print(content)
    data = request.get_json()
    print (request.is_json)
    if request.is_json:
        print(data)
        return render_template('results.html', data=data)
    
    return render_template('results.html', data=[])
    
if __name__ == "__main__":
    app.run(debug=True)


