from flask import Flask, app, render_template, request, redirect, url_for, abort, jsonify, flash
from Empresa import Empresa
from Database import Database
from Usuario import Usuario
from Desenvolvedor import Desenvolvedor
from flask_wtf import FlaskForm, RecaptchaField
import requests
from datetime import datetime
from Evento import Evento
import sys
from Projeto import Projeto
import json
import pymongo


app = Flask(__name__, template_folder="templates")
emailsessao=''
emp = Empresa()
evt = Evento()
dev = Desenvolvedor()
db = Database()
us=Usuario()
pjt = Projeto()
app.config["SECRET_KEY"] = "mysecretkey"
app.config["RECAPTCHA_PUBLIC_KEY"] = '6Lfi1XcmAAAAAG6go6mUbSpX_01xHunP7wgn9StD'
app.config["RECAPTCHA_PRIVATE_KEY"] = '6Lfi1XcmAAAAANyI3-604hr8oKpQkRuH1A0XI9kw'

class Widgets(FlaskForm):
    recaptcha = RecaptchaField()
#Rotas 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/editar_perfil', methods=['GET'])
def editarp():
    if tipo == True:
        return render_template('editar_perfil.html', nome=dev.getNome(), contabancaria=dev.getConta(), sobrenome=dev.getSobrenome(), 
                           telefone=dev.getTelefone(), descricao=dev.getDescricao())
    
    else:
        return render_template('editar_perfil_emp.html', razaosocial=emp.getRazaoSocial(), contabancaria=emp.getConta(), 
                           telefone=emp.getTelefone(), descricao=emp.getAreaNegocio())

@app.route('/signup_dev', methods=['GET'])
def regdv():
    return render_template('RegisterDesenvolvedor.html') 

@app.route('/signup_emp', methods=['GET'])
def regem():
    return render_template('RegisterEmpresa.html')

@app.route('/authlogin', methods=['GET', 'POST'])
def login():
    form = Widgets()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            flash('Por favor, preencha todos os campos.')
            return redirect(url_for('login'))
        
        elif 'g-recaptcha-response' not in request.form:
            flash('Por favor, marque a caixa de verificação reCaptcha.')
            return redirect(url_for('login'))
        
        elif dev.iniciaSessao(email, password):
            global tipo # tipo == True desenvolvedor. tipo == false Empresa
            tipo=dev.verificaUsuario()
            if tipo:
                dev.capturaEmail(email)
                return redirect(url_for('feed'))
            else:
                emp.capturaEmail(email)
                return redirect(url_for('feed'))
        else:
            flash('***EMAIL OU SENHA INCORRETOS***')
            return redirect(url_for('login'))

@app.route('/lista_projetos', methods=['GET'])
def lista_projetos():
    return render_template('lista-projetos.html')

@app.route('/perfil', methods=['GET'])
def perfil():
   if tipo == True:
        saldo = Usuario().verificarSaldo(True, dev.getCodigo())
        return render_template('perfil_dev.html', nome=dev.getNome(), sobrenome=dev.getSobrenome(), descricao=dev.getDescricao(), email=dev.getEmail(), saldo=saldo)
   else:
       saldo = Usuario().verificarSaldo(False, emp.getCodigo())
       return render_template('perfil_dev.html', nome=emp.getRazaoSocial(), descricao=emp.getAreaNegocio(), email=emp.getEmail(), saldo=saldo)

@app.route('/criar_Projeto', methods=['GET'])
def criar_projeto():
    return render_template('criarProjeto.html')

@app.route('/feed', methods=['GET'])
def feed():
    if tipo == True:
        return render_template('pagina_inicial.html', nome=dev.getNome(), sobrenome=dev.getSobrenome(), descricao=dev.getDescricao())
    else:
        return render_template('pagina_inicial.html', nome=emp.getRazaoSocial(), descricao=emp.getAreaNegocio())

#metodos 
    
@app.route('/pesquisa_usuario', methods=['GET'])
def pesquisaUsuario():
    #nome = request.form.get('nome')
    nome = request.args.get('nome')
    tipoUsuario = tipo
    # if tipoUsuario:
    #     codUsuario = dev.getCodigo()
    # else:
    #     codUsuario = emp.getCodigo()
    resultado = Usuario().pesquisaUsuario(nome, tipoUsuario)
    return jsonify(resultado)
    #print(resultado)

@app.route('/copiarURL', methods=['GET'])
    
@app.route('/signup_developer', methods=['POST'])
def regdev():
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        genero = request.form.get('genero')
        data_nascimento = request.form.get('data_nascimento')
        telefone = request.form.get('telefone')
        conta = request.form.get('conta')
        senha = request.form.get('senha')
        #rNovaSenha = request.form.get('rNovaSenha')
        descricao = request.form.get('descricao')
        tag = request.form.get('tag')
    #funcao para o backend
        dev.criaDesenvolvedor(nome, sobrenome, cpf, email, genero, data_nascimento, telefone, conta, senha, descricao, tag)
        print(email)
        print(senha)
        return redirect(url_for('home'))
    
    
@app.route('/signup_enterprise', methods=['POST'])
def regEmp():
    cnpj = request.form.get('cnpj')
    razao_social = request.form.get('razao_social')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    conta = request.form.get('conta')
    senha = request.form.get('senha')
    cep = request.form.get('cep')
    #confirm_password = request.form.get('confirm_password')
    area_negocio = request.form.get('area_negocio')

    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    if requisicao.status_code == 200:
        #funcao para o backend
        emp.criaEmpresa(cnpj, razao_social, email, telefone, conta, senha, area_negocio, cep)
        return render_template('home.html')
    else:
        flash("CEP inválido!")
        return redirect(url_for('regem'))

@app.route('/delete_conta', methods=['GET'])
def delete_conta():
    if tipo:
        dev.deletaUsuario(tipo, dev.getEmail())
    else:
        emp.deletaUsuario(tipo, emp.getEmail())
    return render_template('home.html')

@app.route('/edita_perfil', methods=['POST'])
def edita_perfil():
    if tipo == True:
        name = request.form.get('name')
        sobrenome = request.form.get('sobrenome')
        descricao = request.form.get('descricao')
        contabancaria = request.form.get('contabancaria')
        telefone = request.form.get('telefone')
        hashtags = request.form.get('hashtags')
        genero = request.form.get('genero')
        password = request.form.get('password')

        dev.setNome(name)
        dev.setSobrenome(sobrenome)
        dev.setDescricao(descricao)
        dev.setConta(contabancaria)
        dev.setTelefone(telefone)
        dev.setGenero(genero)
        dev.setTag(hashtags)
        dev.setSenha(password)

        return redirect(url_for('perfil'))

    else:
        contabancaria = request.form.get('contabancaria')
        telefone = request.form.get('telefone')
        password = request.form.get('password')
        areanegocio = request.form.get('areanegocio')
        razaosocial = request.form.get('razaosocial')

        emp.setRazaoSocial(razaosocial)
        emp.setConta(contabancaria)
        emp.setTelefone(telefone)
        emp.setAreaNegocio(areanegocio)
        emp.setSenha(password)

        return redirect(url_for('perfil'))

@app.route('/criarProjeto', methods=['POST'])
def criarProjeto():
    if tipo == False: 
        cod_empresa = emp.getCodigo()
        nome_projeto = request.form.get('nome_projeto')
        numero_devs = request.form.get('numero_devs')
        tag_projeto = request.form.get('tag_projeto')
        valor_orcamento = request.form.get('valor_orcamento')
        prazo = request.form.get('prazo')
        especificacao = request.form.get('especificacao')
        status_projeto = "A fazer"
        pjt.criaProjeto(cod_empresa, especificacao, valor_orcamento, prazo, status_projeto, tag_projeto, nome_projeto, numero_devs)
        return render_template('pagina_inicial.html')
    else:
        return render_template('pagina_inicial.html')
  
@app.route('/follow', methods=['POST'])
def follow():
    Id = request.json['Id']
    Usuario.Follow(Id)
    return jsonify(success=True)

@app.route('/unfollow', methods=['POST'])
def unfollow():
    Id = request.json['Id']
    Usuario.Unfollow(Id)
    return jsonify(success=True)

@app.route("/calendario", methods=["GET", "POST"])
def index():
  return render_template("S4A_calendar.html")

@app.route("/get/", methods=["POST"])
def get():
    data = dict(request.form)
    if dev.verificaUsuario():
        events = evt.getEvento(int(data["month"]), int(data["year"]), dev.getCodigo(), True)
    else:
        events = evt.getEvento(int(data["month"]), int(data["year"]), emp.getCodigo(), False)
    # print(events)
    return "{}" if events is None else events

@app.route("/save/", methods=["POST"])
def save():
    data = dict(request.form)
    if dev.verificaUsuario():
        ok = evt.criaEventoDev(data["s"], data["e"], data["t"], data["c"], data["b"], dev.getCodigo(), True)
        us.enviarEmailReuniaoCriada(dev.getEmail(), dev.getNome(), data["s"])
    else:
        ok = evt.criaEventoEmp(data["s"], data["e"], data["t"], data["c"], data["b"], emp.getCodigo(), False)
        us.enviarEmailReuniaoCriada(emp.getEmail(), emp.getRazaoSocial(), data["s"])
    msg = "OK" 
    return 'Reunião criada com sucesso!'
    # if ok:
    #     return make_response(msg, 500)

@app.route("/delete/", methods=["POST"])
def delete():
  data = dict(request.form)
  dataEvento = evt.getDataEvento(data["id"])
#   date_time = datetime(dataEvento)
  dataEvento.strftime('%d/%m/%Y %H:%M:%S')
  ok = evt.deletaEvento(data["id"])
  if dev.verificaUsuario():
      us.enviarEmailReuniaoExcluida(dev.getEmail(), dev.getNome(), dataEvento)
  else:
      us.enviarEmailReuniaoExcluida(emp.getEmail(), emp.getRazaoSocial(), dataEvento)
  msg = "OK"
  return 'Reunião excluída com sucesso!' 
#   if ok:
#     #else sys.last_value
#     return make_response(msg, 500)

@app.route('/deposito', methods=['POST'])
def deposito():
    tipoUsuario = tipo
    if tipoUsuario:
        codUsuario = dev.getCodigo()
    else:
        codUsuario = emp.getCodigo()
    valor = request.form.get('valor')
    valor = valor.replace(',', '.')
    if Usuario().Depositar(tipoUsuario, codUsuario, valor):
        flash("Depósito realizado com sucesso!")
        return redirect(url_for('perfil'))
    else:
        flash("Erro ao realizar depósito!")
        return redirect(url_for('perfil'))

@app.route('/saque', methods=['POST'])
def saque():
    tipoUsuario = tipo
    if tipoUsuario:
        codUsuario = dev.getCodigo()
    else:
        codUsuario = emp.getCodigo()
    valor = request.form.get('valor')
    valor = valor.replace(',', '.')
    if Usuario().Sacar(tipoUsuario, codUsuario, valor):
        flash("Saque realizado com sucesso!")
        return redirect(url_for('perfil'))
    else:
        flash("Erro ao realizar saque!")
        return redirect(url_for('perfil'))


@app.route('/transacao', methods=['POST'])
def transacao():
    if tipo == False:
        codEmpresa = emp.getCodigo()
        codDesenvolvedor = request.form.get('codDev')
        valor = request.form.get('valor')
        valor = valor.replace(',', '.')
        descricao = request.form.get('descricao')
        if Usuario().realizarTransacao(codEmpresa, codDesenvolvedor, valor, descricao, tipo):
            flash("Transação realizada com sucesso!")
            return redirect(url_for('perfil'))
        else:
            flash("Erro ao realizar transação!")
            return redirect(url_for('perfil'))
    else:
        flash("Erro ao realizar transação!")
        return redirect(url_for('perfil'))


@app.route('/carteira', methods=['GET'])
def carteira():
    if tipo:
        saldo = Usuario().verificarSaldo(True, dev.getCodigo())
    else:
        saldo = Usuario().verificarSaldo(False, emp.getCodigo())
    return render_template('carteira.html', saldo=saldo)

@app.route('/perfil/<selectedUser>')
def exibir_perfil(selectedUser):
    selectedUser = json.loads(selectedUser)
    nomePesquisado = selectedUser["nome"]
    sobrenomePesquisado = selectedUser["sobrenome"]
    emailPesquisado = selectedUser["email"]
    descricaoDevPesquisado = selectedUser["descricao"]
    #descricaoEmpPesquisado = selectedUser["area_negocio"]
    print(nomePesquisado)
    print(selectedUser)
    return render_template('perfil-default.html', selectedUser=selectedUser, nome=nomePesquisado, sobrenome=sobrenomePesquisado, email=emailPesquisado, descricao=descricaoDevPesquisado)

@app.route('/url', methods=['POST'])
def get_url():
    data = request.get_json()
    url = data['url']
    # Faça o que quiser com a URL aqui, como armazená-la em um banco de dados
    print(url)
    return 'URL recebida com sucesso'


VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
 
    
def main():
    from Database import Database
    
if __name__ == "__main__":
    main()
    app.run()