from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de produtos
produtos = []

# Rota principal - exibe a lista de produtos cadastrados

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/inicio')
def home():
    return render_template('inicio.html')


# Rota para adicionar um novo produto
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        codigo = request.form['codigo']
        valor = request.form['valor']
        produto = {'id': len(produtos), 'nome': nome, 'codigo': codigo, 'valor': valor}
        produtos.append(produto)
        return redirect('/')
    return render_template('cadastrarProdu.html')

# Rota para editar um produto
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    produto = next((produto for produto in produtos if produto['id'] == id), None)
    if produto:
        if request.method == 'POST':
            produto['nome'] = request.form['nome']
            produto['codigo'] = request.form['codigo']
            produto['valor'] = request.form['valor']
            return redirect('/')
        return render_template('editarProdu.html', produto=produto)
    return "produto não encontrado."

# Rota para excluir um produto
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    del produtos[id]
    return redirect('/')

if __name__ == '__main__':
    app.run()
