from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Aqui você poderia implementar:
        # 1. Envio de email
        # 2. Salvar em banco de dados
        # 3. Verificações de segurança
        
        return jsonify({
            'status': 'success',
            'message': 'Formulário recebido com sucesso!'
        })

if __name__ == '__main__':
    app.run(debug=True)