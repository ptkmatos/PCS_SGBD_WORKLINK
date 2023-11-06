from Database import Database
#from Empresa import Empresa
# OS GETTERS VÃO SER CONSULTAS NO BANCO DE DADOS PEDINDO AQUELA VARIAVEL
class Projeto():    
    def criaProjeto(self, cod_empresa,especificacao, valor_orcamento, prazo, status_projeto, tag_projeto, nome_projeto, numero_devs):
        values = (cod_empresa, especificacao, valor_orcamento, prazo, status_projeto, tag_projeto, nome_projeto, numero_devs)
        #tipo = True
        Database.connect(self)
        Database.insertProjeto(self, values)

    # GETTERS
    def getEspecificacaoProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        return Database.selectProjeto(self, 'especificacao',cod_empresa, nome_projeto)
    
    def getOrcamentoProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        return Database.selectProjeto(self, 'valor_orcamento',cod_empresa, nome_projeto)
    
    def getPrazoProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        return Database.selectProjeto(self, 'prazo',cod_empresa, nome_projeto)
    
    def getRequisitoProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        return Database.selectProjeto(self, 'requisito_tecnico',cod_empresa, nome_projeto)
    
    def getStatusProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        return Database.selectProjeto(self, 'status_projeto',cod_empresa, nome_projeto)
    
    def getTagProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        return Database.selectProjeto(self, 'tag_projeto',cod_empresa, nome_projeto)
    
    def getNomeProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        return Database.selectProjeto(self, 'nome_projeto',cod_empresa, nome_projeto)
    
    # SETTERS - ADICIONAR NOME_PROJETO COMO PARAMETRO RECEBIDO
    def setEspecificacaoProjeto(self, espec, cod_empresa, nome_projeto) :
        Database.connect(self)
        Database.updateProjeto(self, 'especificacao', espec, cod_empresa, nome_projeto)
        return True

    def setOrcamentoProjeto(self, espec, cod_empresa, nome_projeto) :
        Database.connect(self)
        Database.updateProjeto(self, 'valor_orcamento', espec, cod_empresa, nome_projeto)
        return True

    def setPrazoProjeto(self, espec, cod_empresa, nome_projeto) :
        Database.connect(self)
        Database.updateProjeto(self, 'prazo', espec, cod_empresa, nome_projeto)
        return True

    def setRequisitoProjeto(self, espec, cod_empresa, nome_projeto) :
        Database.connect(self)
        Database.updateProjeto(self, 'requisito_tecnico', espec, cod_empresa, nome_projeto)
        return True
    
    def setStatusProjeto(self, espec, cod_empresa, nome_projeto) :
        Database.connect(self)
        Database.updateProjeto(self, 'status_projeto', espec, cod_empresa, nome_projeto)
        return True

    def setTagProjeto(self, espec, cod_empresa, nome_projeto) :
        Database.connect(self)
        Database.updateProjeto(self, 'tag_projeto', espec, cod_empresa, nome_projeto)
        return True

    def setNomeProjeto(self, espec, cod_empresa, nome_projeto) :
        Database.connect(self)
        Database.updateProjeto(self, 'nome_projeto', espec, cod_empresa, nome_projeto)
        return True
    
    def listaProjetos(self, cod_empresa):
        Database.connect(self)
        Database.listaProjetos(self, cod_empresa)
        return True

    def deletaProjeto(self, cod_empresa, nome_projeto):
        Database.connect(self)
        Database.deleteProjeto(self, cod_empresa, nome_projeto)