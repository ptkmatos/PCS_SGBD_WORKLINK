import Usuario
from Database import Database
class Empresa(Usuario.Usuario):
    def criaEmpresa(self, cnpj, razao_social, email, telefone, conta, senha, area_negocio, cep):
        values = (cnpj, razao_social, email, telefone, conta, senha, area_negocio, cep)
        tipo = False
        Database.connect(self)
        Database.insert(self, values, tipo)

    # GETTERS
    def getCnpj(self):
        Database.connect(self)
        #return Database.select(self, 'EMPRESA', 'CNPJ', self.email)
    
    def getRazaoSocial(self):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'razao_social', self.email)
    
    def getEmail(self):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'email', self.email)
    
    def getTelefone(self):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'telefone', self.email)
    
    def getCodigo(self):
        Database.connect(self)
        self.codigo = Database.select(self, 'EMPRESA', 'cod_empresa', self.email)
        return Database.select(self, 'EMPRESA', 'cod_empresa', self.email)
    
    def getConta(self):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'conta_bancaria', self.email)
    
    def getSenha(self):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'senha', self.email)
    
    def getAreaNegocio(self):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'area_negocio', self.email)
    
    # SETTERS
    def setCnpj(self, cnpj):
        Database.connect(self)
        Database.update(self, 'CNPJ', cnpj, 'EMPRESA', self.email)
        return True

    def setRazaoSocial(self, razao_social):
        Database.connect(self)
        Database.update(self, 'razao_social', razao_social, 'EMPRESA', self.email)
        return True

    def setEmail(self, email_novo):
        Database.connect(self)
        Database.update(self, 'email', email_novo, 'EMPRESA', self.email)
        return True

    def setTelefone(self, telefone):
        Database.connect(self)
        Database.update(self, 'telefone', telefone, 'EMPRESA', self.email)
        return True

    def setConta(self, conta):
        Database.connect(self)
        Database.update(self, 'conta_bancaria', conta, 'EMPRESA', self.email)
        return True

    def setSenha(self, senha):
        Database.connect(self)
        Database.update(self, 'senha', senha, 'EMPRESA', self.email)
        return True

    def setAreaNegocio(self, area_negocio):
        Database.connect(self)
        Database.update(self, 'area_negocio', area_negocio, 'EMPRESA', self.email)
        return True

    #def setRazaoSocial(self, razao_social):
        #SELECT RAZAO_SOC FROM EMPRESA WHERE EMAIL = XXXX -- UPDATE
    #    pass
    #def publicarProjeto(self, projeto):
    #    self.projetos.append(projeto)
    
    #def visualizarProjetos(self, status):
    #    for projeto in self.projetos:
    #        if projeto.status == status:
    #            print(projeto)
    
    #def seguirDesenvolvedor(self, desenvolvedor):
    #    self.desenvolvedores_seguidos.append(desenvolvedor)
    
    #def pesquisarDesenvolvedores(self):
    #    self.cursor.execute(f'SELECT * FROM desenvolvedor') # Tenta achar o cara com essas credenciais
    #    self.con.commit()
    #    return str(self.cursor.fetchall())
    
    
    #def inserirDinheiroCarteira(self, valor):
    #    self.saldo_carteira += valor
    
    #def realizarPagamento(self, desenvolvedor, valor):
    #    self.saldo_carteira -= valor
    #    desenvolvedor.saldo_carteira += valor
    
    #def marcarReuniao(self, desenvolvedor, data, hora):
    #    reuniao = Reuniao(desenvolvedor, data, hora) # Usar integração com Calendar
    #    self.reunioes_agendadas.append(reuniao)

    #def avaliarDesenvolvedor(self, desenvolvedor, avaliacao):
    #    desenvolvedor.avaliacoes.append(avaliacao)

    #def listarProjetosEmAndamento(self):
    #    for projeto in self.projetos:
    #        if projeto.status == "Em andamento":
    #            print(projeto)

    #def listarProjetosConcluidos(self):
    #    for projeto in self.projetos:
    #        if projeto.status == "Concluído":
    #            print(projeto)

    #def exibirInformacoes(self):
    #    print("Razão Social:", self.razao_social)
    #    print("Email:", self.email)
    #    print("Telefone:", self.telefone)