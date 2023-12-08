from flask import request, jsonify, abort, render_template
from app import app, db
from models import Tbcliente, Tbvinho, Tbtipo, Tbcategoria, Tbcarrinho, Tbvinhosdocarrinho

#Rotas definidas para interagir com o banco de dados
#Cada rota manipula dados relacionados a uma tabela específica

#Rota para renderizar a página inicial com os botões de GET
@app.route("/")
def index():
    return render_template("index.html")

#Rota para renderizar a página de formulários com os métodos POST das tabelas
@app.route("/forms")
def forms():
    return render_template("forms.html")

#Rotas para clientes
@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "GET":
        #Obtém todos os clientes no banco de dados e os converte para uma lista de dicionários:
        with app.app_context():
            list_clientes = Tbcliente.query.all()
        clientes_dict_list = [cliente.as_dict() for cliente in list_clientes]
        return jsonify(clientes_dict_list)

    elif request.method == "POST":
        #Adiciona um novo cliente ao banco de dados:
        data = request.get_json()
        nome = data.get("nome")
        cpf = data.get("cpf")

        new_cliente = Tbcliente(nomecli=nome, cpfcli=cpf)
        db.session.add(new_cliente)
        db.session.commit()

        return jsonify(new_cliente.as_dict())

    else:
        abort(404)

@app.route("/cliente/<int:pkcodigocli>", methods=["GET", "PUT", "DELETE"])
def cliente(pkcodigocli):
    if request.method == "GET":
        with app.app_context():
            client = Tbcliente.query.get(pkcodigocli)
        if client:
            return jsonify(client.as_dict())
        else:
            return jsonify({"message": "Cliente não encontrado"}), 404

    elif request.method == "PUT":
        with app.app_context():
            client = Tbcliente.query.get(pkcodigocli)
            if client:
                #Aqui pega os valores novos inseridos no body do request e os adiciona no cliente específicado
                data = request.get_json()
                client.nomecli = data.get("nome", client.nomecli)
                client.cpfcli = data.get("cpf", client.cpfcli)
                db.session.commit()
                return jsonify(client.as_dict())
            else:
                return jsonify({"message": "Cliente não encontrado"}), 404

    elif request.method == "DELETE":
        with app.app_context():
            client = Tbcliente.query.get(pkcodigocli)
            if client:
                #Aqui deleta o cliente especificado no request caso seja encontrado:
                db.session.delete(client)
                db.session.commit()
                return jsonify({"message": "Cliente deletado com sucesso!"})
            else:
                return jsonify({"message": "Cliente não encontrado"}), 404

    else:
        abort(404)

#Rotas para categorias
@app.route("/categorias", methods=["GET", "POST"])
def categorias():
    if request.method == "GET":
        with app.app_context():
            list_categorias = Tbcategoria.query.all()
        categorias_dict_list = [categoria.as_dict() for categoria in list_categorias]
        return jsonify(categorias_dict_list)

    elif request.method == "POST":
        data = request.get_json()
        nomecat = data.get("nomecat")

        new_categoria = Tbcategoria(nomecat=nomecat)
        db.session.add(new_categoria)
        db.session.commit()

        return jsonify(new_categoria.as_dict())

    else:
        abort(404)

@app.route("/categoria/<int:pkcodigocat>", methods=["GET", "PUT", "DELETE"])
def categoria(pkcodigocat):
    if request.method == "GET":
        with app.app_context():
            cat = Tbcategoria.query.get(pkcodigocat)
        if cat:
            return jsonify(cat.as_dict())
        else:
            return jsonify({"message": "Categoria não encontrada"}), 404

    elif request.method == "PUT":
        with app.app_context():
            cat = Tbcategoria.query.get(pkcodigocat)
            if cat:
                data = request.get_json()
                cat.nomecat = data.get("nomecat", cat.nomecat)
                db.session.commit()
                return jsonify(cat.as_dict())
            else:
                return jsonify({"message": "Categoria não encontrada"}), 404

    elif request.method == "DELETE":
        with app.app_context():
            cat = Tbcategoria.query.get(pkcodigocat)
            if cat:
                db.session.delete(cat)
                db.session.commit()
                return jsonify({"message": "Categoria deletada com sucesso!"})
            else:
                return jsonify({"message": "Categoria não encontrada"}), 404
    else:
        abort(404)

#Rotas para tipos:
@app.route("/tipos", methods=["GET", "POST"])
def tipos():
    if request.method == "GET":
        with app.app_context():
            list_tipos = Tbtipo.query.all()
        tipos_dict_list = [tipo.as_dict() for tipo in list_tipos]
        return jsonify(tipos_dict_list)

    elif request.method == "POST":
        data = request.get_json()
        nometip = data.get("nometip")

        new_tipo = Tbtipo(nometip=nometip)
        db.session.add(new_tipo)
        db.session.commit()

        return jsonify(new_tipo.as_dict())

    else:
        abort(404)

@app.route("/tipo/<int:pkcodigotip>", methods=["GET", "PUT", "DELETE"])
def tipo(pkcodigotip):
    if request.method == "GET":
        with app.app_context():
            tip = Tbtipo.query.get(pkcodigotip)
        if tip:
            return jsonify(tip.as_dict())
        else:
            return jsonify({"message": "Tipo não encontrado"}), 404

    elif request.method == "PUT":
        data = request.get_json()
        nometip = data.get("nometip")

        new_tipo = Tbtipo(nometip=nometip)
        db.session.add(new_tipo)
        db.session.commit()

        return jsonify(new_tipo.as_dict())

    elif request.method == "DELETE":
        with app.app_context():
            tipo = Tbtipo.query.get(pkcodigotip)
            if tipo:
                db.session.delete(tipo)
                db.session.commit()
                return jsonify({"message": "Tipo deletado com sucesso!"})
            else:
                return jsonify({"message": "Tipo não encontrado"}), 404

    else:
        abort(404)

#Rotas para vinhos:
@app.route("/vinhos", methods=["GET", "POST"])
def vinhos():
    if request.method == "GET":
        with app.app_context():
            list_vinhos = Tbvinho.query.all()
        vinhos_dict_list = [vinho.as_dict() for vinho in list_vinhos]
        return jsonify(vinhos_dict_list)

    elif request.method == "POST":
        data = request.get_json()
        nomevin = data.get("nomevin")
        precovin = data.get("precovin")
        anovin = data.get("anovin")
        paisvin = data.get("paisvin")
        estoquevin = data.get("estoquevin")
        fkcodigotip = data.get("fkcodigotip")
        fkcodigocat = data.get("fkcodigocat")

        new_vinho = Tbvinho(
            nomevin=nomevin,
            precovin=precovin,
            anovin=anovin,
            paisvin=paisvin,
            estoquevin=estoquevin,
            fkcodigotip=fkcodigotip,
            fkcodigocat=fkcodigocat
        )
        db.session.add(new_vinho)
        db.session.commit()

        return jsonify(new_vinho.as_dict())

    else:
        abort(404)

@app.route("/vinho/<int:pkcodigovin>", methods=["GET", "PUT", "DELETE"])
def vinho(pkcodigovin):
    if request.method == "GET":
        with app.app_context():
            vin = Tbvinho.query.get(pkcodigovin)
        if vin:
            return jsonify(vin.as_dict())
        else:
            return jsonify({"message": "Vinho não encontrado"}), 404

    elif request.method == "PUT":
        with app.app_context():
            vinho = Tbvinho.query.get(pkcodigovin)
            if vinho:
                data = request.get_json()
                vinho.nomevin = data.get("nomevin", vinho.nomevin)
                vinho.precovin = data.get("precovin", vinho.precovin)
                vinho.anovin = data.get("anovin", vinho.anovin)
                vinho.paisvin = data.get("paisvin", vinho.paisvin)
                vinho.estoquevin = data.get("estoquevin", vinho.estoquevin)
                vinho.fkcodigotip = data.get("fkcodigotip", vinho.fkcodigotip)
                vinho.fkcodigocat = data.get("fkcodigocat", vinho.fkcodigocat)
                db.session.commit()
                return jsonify(vinho.as_dict())
            else:
                return jsonify({"message": "Vinho não encontrado"}), 404

    elif request.method == "DELETE":
        with app.app_context():
            vinho = Tbvinho.query.get(pkcodigovin)
            if vinho:
                db.session.delete(vinho)
                db.session.commit()
                return jsonify({"message": "Vinho deletado com sucesso!"})
            else:
                return jsonify({"message": "Vinho não encontrado"}), 404

    else:
        abort(404)

#Rotas para carrinhos:
@app.route("/carrinhos", methods=["GET", "POST"])
def carrinhos():
    if request.method == "GET":
        with app.app_context():
            list_carrinhos = Tbcarrinho.query.all()
        carrinhos_dict_list = [carrinho.as_dict() for carrinho in list_carrinhos]
        return jsonify(carrinhos_dict_list)


    elif request.method == "POST":
        data = request.get_json()
        estadocar = data.get("estadocar")
        fkcodigocli = data.get("fkcodigocli")

        new_carrinho = Tbcarrinho(
            estadocar=estadocar,
            fkcodigocli=fkcodigocli
        )
        db.session.add(new_carrinho)
        db.session.commit()

        return jsonify(new_carrinho.as_dict())


    else:

        abort(404)


@app.route("/carrinho/<int:pkcodigocar>", methods=["GET", "PUT", "DELETE"])
def carrinho(pkcodigocar):
    if request.method == "GET":
        with app.app_context():
            carrinho = Tbcarrinho.query.get(pkcodigocar)
        if carrinho:
            return jsonify(carrinho.as_dict())
        else:
            return jsonify({"message": "Carrinho não encontrado"}), 404

    elif request.method == "PUT":
        with app.app_context():
            carrinho = Tbcarrinho.query.get(pkcodigocar)
            if carrinho:
                data = request.get_json()
                carrinho.estadocar = data.get("estadocar", carrinho.estadocar)
                carrinho.fkcodigocli = data.get("fkcodigocli", carrinho.fkcodigocli)
                db.session.commit()
                return jsonify(carrinho.as_dict())
            else:
                return jsonify({"message": "Carrinho não encontrado"}), 404

    elif request.method == "DELETE":
        with app.app_context():
            carrinho = Tbcarrinho.query.get(pkcodigocar)
            if carrinho:
                db.session.delete(carrinho)
                db.session.commit()
                return jsonify({"message": "Carrinho deletado com sucesso!"})
            else:
                return jsonify({"message": "Carrinho não encontrado"}), 404

    else:
        abort(404)

#Rotas para os vinhos do carrinho:
@app.route("/vinhosdocarrinho", methods=["GET", "POST"])
def vinhosdocarrinho():
    if request.method == "GET":
        with app.app_context():
            list_vinhosdocarrinho = Tbvinhosdocarrinho.query.all()
        vinhosdocarrinho_dict_list = [vinhodocarrinho.as_dict() for vinho in list_vinhosdocarrinho]
        return jsonify(vinhosdocarrinho_dict_list)

    elif request.method == "POST":
        data = request.get_json()
        fkcodigovin = data.get("fkcodigovin")
        fkcodigocar = data.get("fkcodigocar")

        new_vinhodocarrinho = Tbvinhosdocarrinho(
            fkcodigovin=fkcodigovin,
            fkcodigocar=fkcodigocar
        )
        db.session.add(new_vinhodocarrinho)
        db.session.commit()

        return jsonify(new_vinhodocarrinho.as_dict())

    else:
        abort(404)


@app.route("/vinhodocarrinho/<int:pkcodigovincar>", methods=["GET", "PUT", "DELETE"])
def vinhodocarrinho(pkcodigovincar):
    if request.method == "GET":
        with app.app_context():
            vinhodocarrinho = Tbvinhosdocarrinho.query.get(pkcodigovincar)
        if vinhodocarrinho:
            return jsonify(vinhodocarrinho.as_dict())
        else:
            return jsonify({"message": "Vinho do carrinho não encontrado"}), 404

    elif request.method == "PUT":
        with app.app_context():
            vinhodocarrinho = Tbvinhosdocarrinho.query.get(pkcodigovincar)
            if vinhodocarrinho:
                data = request.get_json()
                vinhodocarrinho.fkcodigovin = data.get("fkcodigovin", vinhodocarrinho.fkcodigovin)
                vinhodocarrinho.fkcodigocar = data.get("fkcodigocar", vinhodocarrinho.fkcodigocar)
                db.session.commit()
                return jsonify(vinhodocarrinho.as_dict())
            else:
                return jsonify({"message": "Vinho do carrinho não encontrado"}), 404

    elif request.method == "DELETE":
        with app.app_context():
            vinhodocarrinho = Tbvinhosdocarrinho.query.get(pkcodigovincar)
            if vinhodocarrinho:
                db.session.delete(vinhodocarrinho)
                db.session.commit()
                return jsonify({"message": "Vinho do carrinho deletado com sucesso!"})
            else:
                return jsonify({"message": "Vinho do carrinho não encontrado"}), 404

    else:
        abort(404)

#Rota com o join da Tbvinho com a Tbcategoria e Tbtipo:
@app.route("/vinhos_com_info", methods=["GET"])
def vinhos_com_info():
    if request.method == "GET":
        with app.app_context():
            # Realiza um join nas tabelas Tbvinho, Tbcategoria e Tbtipo
            query_result = db.session.query(
                Tbvinho,
                Tbcategoria.nomecat.label("categoria_nome"),
                Tbtipo.nometip.label("tipo_nome")
            ).join(Tbcategoria).join(Tbtipo).all()

            # Converte o resultado da consulta para um formato de dicionário
            vinhos_info_list = [
                {
                    "1 - vinho": {
                        "pkcodigovin": vinho.pkcodigovin,
                        "nomevin": vinho.nomevin,
                        "precovin": vinho.precovin,
                        "anovin": vinho.anovin,
                        "paisvin": vinho.paisvin,
                        "estoquevin": vinho.estoquevin,
                        "fkcodigotip": vinho.fkcodigotip,
                        "fkcodigocat": vinho.fkcodigocat
                    },
                    "2 - categoria_nome": categoria_nome,
                    "3 - tipo_nome": tipo_nome
                }
                for vinho, categoria_nome, tipo_nome in query_result
            ]

            return jsonify(vinhos_info_list)

    else:
        abort(404)