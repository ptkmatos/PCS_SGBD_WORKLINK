import Usuario
from Database import Database
# OS GETTERS VÃO SER CONSULTAS NO BANCO DE DADOS PEDINDO AQUELA VARIAVEL
class Desenvolvedor(Usuario.Usuario):    
    def criaDesenvolvedor(self, nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, descricao, tag):
        values = (nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, descricao, tag)
        tipo = True
        Database.connect(self)
        Database.insert(self, values, tipo)

    # GETTERS
    def getNome(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'nome', self.email)
    
    def getSobrenome(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'sobrenome', self.email)
    
    def getCPF(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'CPF', self.email)
    
    def getEmail(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'email', self.email)
    
    def getGenero(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'genero', self.email)
    
    def getDataNascimento(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'data_nascimento', self.email)
    
    def getTelefone(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'telefone', self.email)
    
    def getConta(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'conta_bancaria', self.email)
    
    def getNome(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'nome', self.email)
    
    def getSenha(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'senha', self.email)
    
    def getDescricao(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'descricao', self.email)
    
    def getCodigo(self):
        Database.connect(self)
        self.codigo = Database.select(self, 'DESENVOLVEDOR', 'cod_desenvolvedor', self.email)
        return Database.select(self, 'DESENVOLVEDOR', 'cod_desenvolvedor', self.email)
    
    def getTag(self):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'tag', self.email)
    
    # SETTERS
    def setNome(self, nome):
        Database.connect(self)
        Database.update(self, 'nome', nome, 'DESENVOLVEDOR', self.email)
        return True

    def setSobrenome(self, sobrenome):
        Database.connect(self)
        Database.update(self, 'sobrenome', sobrenome, 'DESENVOLVEDOR', self.email)
        return True

    def setCpf(self, CPF):
        Database.connect(self)
        Database.update(self, 'CPF', CPF, 'DESENVOLVEDOR', self.email)
        return True

    def setEmail(self, email_novo):
        Database.connect(self)
        Database.update(self, 'email', email_novo, 'DESENVOLVEDOR', self.email)
        return True

    def setGenero(self, genero):
        Database.connect(self)
        Database.update(self, 'genero', genero, 'DESENVOLVEDOR', self.email)
        return True

    def setDataNascimento(self, data_nascimento):
        Database.connect(self)
        Database.update(self, 'data_nascimento', data_nascimento, 'DESENVOLVEDOR', self.email)
        return True

    def setTelefone(self, telefone):
        Database.connect(self)
        Database.update(self, 'telefone', telefone, 'DESENVOLVEDOR', self.email)
        return True

    def setConta(self, conta):
        Database.connect(self)
        Database.update(self, 'conta_bancaria', conta, 'DESENVOLVEDOR', self.email)
        return True
        
    def setSenha(self, senha):
        Database.connect(self)
        Database.update(self, 'senha', senha, 'DESENVOLVEDOR', self.email)
        return True

    def setDescricao(self, descricao):
        Database.connect(self)
        Database.update(self, 'descricao', descricao, 'DESENVOLVEDOR', self.email)
        return True

    def setTag(self, tag):
        Database.connect(self)
        Database.update(self, 'tag_desenvolvedor', tag, 'DESENVOLVEDOR', self.email)
        return True
    
    #def candidataProjeto(self, projeto):
        # INSERIR NO BD O PROJETO QUE O CARA SE CANDIDATOU
    #    pass
    
    #def visualizaProjetos(self, status):
    #    for projeto in self.projetos:
    #        if projeto.status == status:
    #            print(projeto)
    
    #def segueEmpresa(self, empresa):
    #    self.empresas_seguidas.append(empresa)
    
    #def pesquisaProjetos(self, tags):
    #    projetos_encontrados = []
    #    for projeto in self.projetos:
    #        if any(tag in projeto.tags for tag in tags):
    #            projetos_encontrados.append(projeto)
    #    return projetos_encontrados
    
    #def guardaDinheiroCarteira(self, valor):
    #    self.saldo_carteira += valor
    
    #def marcaReuniao(self, empresa, data, hora):
    #    reuniao = Reuniao(empresa, data, hora) # Usar integração com Calendar
    #    self.reunioes_agendadas.append(reuniao)
    
    #def pesquisaEmpresa(self, razao_social):
    #    for empresa in self.empresas:
    #        if empresa.razao_social == razao_social:
    #            return empresa
    #    return None

    #def avaliaEmpresa(self, empresa, avaliacao):
    #    empresa.avaliacoes.append(avaliacao)

    
    
