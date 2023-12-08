from app import db

#Definição dos modelos das tabelas no banco de dados
#Cada classe representa uma tabela
#As funções "__repr__" e "as_dict" são responsáveis pela representação e serialização (respectivamente) dos objetos

#Tabela de categoria dos vinhos:
class Tbcategoria(db.Model):
    pkcodigocat = db.Column(db.Integer, primary_key=True) #Definindo a primary key da tabela
    nomecat = db.Column(db.String(50), nullable=False) #E aqui definindo um atributo onde ele não pode ser null

    def __repr__(self):
        return f"Tbcategoria('{self.nomecat}')"

    def as_dict(self):
        return {'pkcodigocat': self.pkcodigocat, 'nomecat': self.nomecat}

#Tabela de tipo dos vinhos:
class Tbtipo(db.Model):
    pkcodigotip = db.Column(db.Integer, primary_key=True)
    nometip = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Tbtipo('{self.nometip}')"

    def as_dict(self):
        return {'pkcodigotip': self.pkcodigotip, 'nometip': self.nometip}

#Tabela dos vinhos:
class Tbvinho(db.Model):
    pkcodigovin = db.Column(db.Integer, primary_key=True)
    nomevin = db.Column(db.String(50), nullable=False)
    precovin = db.Column(db.Float, nullable=False)
    anovin = db.Column(db.Integer, nullable=False)
    paisvin = db.Column(db.String(50), nullable=False)
    estoquevin = db.Column(db.Integer)


    #Relacionamento com Tbtipo:
    fkcodigotip = db.Column(db.Integer, db.ForeignKey('tbtipo.pkcodigotip')) #Aqui eu defino uma fk conectada ao pk da tabela de tipo
    tipo = db.relationship('Tbtipo', backref=db.backref('vinhos', lazy=True)) #Já aqui eu crio um relacionamento bidirecional entre as tabelas

    #Relacionamento com Tbcategoria:
    fkcodigocat = db.Column(db.Integer, db.ForeignKey('tbcategoria.pkcodigocat'))
    categoria = db.relationship('Tbcategoria', backref=db.backref('vinhos', lazy=True))

    def __repr__(self):
        return f"Tbvinho('{self.nomevin}', '{self.precovin}', '{self.anovin}', '{self.paisvin}', '{self.estoquevin}')"

    def as_dict(self):
        return {
            'pkcodigovin': self.pkcodigovin,
            'nomevin': self.nomevin,
            'precovin': self.precovin,
            'anovin': self.anovin,
            'paisvin': self.paisvin,
            'estoquevin': self.estoquevin,
            'fkcodigotip': self.fkcodigotip,
            'fkcodigocat': self.fkcodigocat
        }

#Tabela dos clientes:
class Tbcliente(db.Model):
    pkcodigocli = db.Column(db.Integer, primary_key=True)
    cpfcli = db.Column(db.String(11), nullable=False)
    nomecli = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Cliente ('{self.nomecli}', '{self.cpfcli}')"

    def as_dict(self):
        return {'pkcodigocli': self.pkcodigocli, 'cpfcli': self.cpfcli, 'nomecli': self.nomecli}

#Tabela dos carrinhos feitos pelos clientes:
class Tbcarrinho(db.Model):
    pkcodigocar = db.Column(db.Integer, primary_key=True)
    estadocar = db.Column(db.String(20), nullable=False)

    #Relacionamento com Tbcliente:
    fkcodigocli = db.Column(db.Integer, db.ForeignKey('tbcliente.pkcodigocli'))
    cliente = db.relationship('Tbcliente', backref=db.backref('carrinhos', lazy=True))

    def __repr__(self):
        return f"Carrinho ('{self.pkcodigocar}', do cliente '{self.fkcodigocli}')"

    def as_dict(self):
        return {'pkcodigocar': self.pkcodigocar, 'estadocar': self.estadocar, 'fkcodigocli': self.fkcodigocli}

#Tabela que armazena os vinhos presentes no carrinho
class Tbvinhosdocarrinho(db.Model):
    pkcodigovincar = db.Column(db.Integer, primary_key=True)

    #Relacionamento com Tbvinho:
    fkcodigovin = db.Column(db.Integer, db.ForeignKey('tbvinho.pkcodigovin'))
    vinho = db.relationship('Tbvinho', backref=db.backref('vinhos_do_carrinho', lazy=True))

    #Relacionamento com Tbcarrinho:
    fkcodigocar = db.Column(db.Integer, db.ForeignKey('tbcarrinho.pkcodigocar'))
    carrinho = db.relationship('Tbcarrinho', backref=db.backref('vinhos_do_carrinho', lazy=True))

    def __repr__(self):
        return f"Vinho ('{self.fkcodigovin}', do carrinho '{self.fkcodigocar}')"

    def as_dict(self):
        return {'pkcodigovincar': self.pkcodigovincar, 'fkcodigovin': self.fkcodigovin, 'fkcodigocar': self.fkcodigocar}