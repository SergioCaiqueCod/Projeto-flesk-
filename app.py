from flask import Flask,render_template,request,redirect,url_for

app= Flask(__name__)
# Nome,Idade,Email,Rg , id
alunos=[
    {
    'nome':'Gabriel',
    'idade':26,
    'email':'gabrielvieira@gmail.com',
    'RG':'11932-1294',
    'id':'11'
},
{   
   'nome':'sergio',
    'idade':17,
    'email':'sergiocaique@gmail.com',
    'RG':'11932-1374',
    'id':'12'
}
]

@app.route('/')
def index():
    return render_template('register.html',pessoa=alunos)

@app.route('/adicionar',methods=['POST'])
def adicionar():
    nome=request.form['nome']
    idade=request.form['idade']
    email=request.form['email']
    RG=request.form['RG']
    id=request.form['id']

    alunos.append({'nome':nome,'idade':idade,'email':email,'RG':RG,'id':id})
    return redirect(url_for('index'))

app.run(debug=True)
