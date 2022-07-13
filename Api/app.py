
from modul import answerRule,answerKnowledg

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/knowledge', methods=['POST', 'GET'])
def qa():
    question = request.args.get('question')
    context = request.args.get('context')
    render_template('form.html')
    if request.method == 'POST':
        question = request.form['question']
        context = request.form['context']
        if not question or not context:
            return render_template('form.html')
        return render_template('form.html', answerKnowledg_v=answerKnowledg(question, context))
    else:

        return render_template('form.html')


@app.route('/rule', methods=['POST', 'GET'])
def qax():
    question = request.args.get('question')
    classification = request.args.get('classification')
    render_template('form.html')
    if request.method == 'POST':
        question = request.form['question']
        classification = request.form['classification']
        if not question or not classification:
            return render_template('form.html')
        return render_template('form.html', answerKnowledg_v=answerRule(question, classification))
    else:

        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)