//Funções JavaScript para fazer requisições à API do Flask
//Cada função corresponde a um tipo específico de recurso

function getClientes() {
    //Obtém a lista de clientes
    $.get("/clientes", function(data) {
        $("#api-response").text(JSON.stringify(data, null, 2));
    });
}

function getCategorias() {
    $.get("/categorias", function(data) {
        $("#api-response").text(JSON.stringify(data, null, 2));
    });
}

function getTipos() {
    $.get("/tipos", function(data) {
        $("#api-response").text(JSON.stringify(data, null, 2));
    });
}

function getVinhos() {
    $.get("/vinhos", function(data) {
        $("#api-response").text(JSON.stringify(data, null, 2));
    });
}

function getCarrinhos() {
    $.get("/carrinhos", function(data) {
        $("#api-response").text(JSON.stringify(data, null, 2));
    });
}

function getVinhosDoCarrinho() {
    $.get("/vinhosdocarrinho", function(data) {
        $("#api-response").text(JSON.stringify(data, null, 2));
    });
}

function getVinhosComInfo() {
    $.get("/vinhos_com_info", function(data) {
        $("#api-response").text(JSON.stringify(data, null, 2));
    });
}

//Função para adicionar um novo cliente:
function adicionarCliente() {
    const nome = document.getElementById("cliente-nome").value;
    const cpf = document.getElementById("cliente-cpf").value;

    const data = { nome, cpf };

    //Envia uma requisição POST com os dados do novo cliente:
    fetch('/clientes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Cliente adicionado:', data);
        //Limpar os campos do formulário após a adição:
        document.getElementById("cliente-nome").value = "";
        document.getElementById("cliente-cpf").value = "";
    })
    .catch((error) => {
        console.error('Erro ao adicionar Cliente:', error);
    });
}

//Função para adicionar Categoria
function adicionarCategoria() {
    const nomecat = document.getElementById("categoria-nome").value;

    const data = { nomecat };

    fetch('/categorias', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Categoria adicionada:', data);
        document.getElementById("categoria-nome").value = "";
    })
    .catch((error) => {
        console.error('Erro ao adicionar Categoria:', error);
    });
}

//Função para adicionar Tipo
function adicionarTipo() {
    const nometip = document.getElementById("tipo-nome").value;

    const data = { nometip };

    fetch('/tipos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Tipo adicionado:', data);
        document.getElementById("tipo-nome").value = "";
    })
    .catch((error) => {
        console.error('Erro ao adicionar Tipo:', error);
    });
}

//Função para adicionar Vinho
function adicionarVinho() {
    const nomevin = document.getElementById("vinho-nome").value;
    const precovin = document.getElementById("vinho-precovin").value;
    const anovin = document.getElementById("vinho-anovin").value;
    const paisvin = document.getElementById("vinho-paisvin").value;
    const estoquevin = document.getElementById("vinho-estoquevin").value;
    const fkcodigotip = document.getElementById("vinho-fkcodigotip").value;
    const fkcodigocat = document.getElementById("vinho-fkcodigocat").value;

    const data = {
        nomevin,
        precovin,
        anovin,
        paisvin,
        estoquevin,
        fkcodigotip,
        fkcodigocat
    };

    fetch('/vinhos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Vinho adicionado:', data);
        document.getElementById("vinho-nome").value = "";
        document.getElementById("vinho-precovin").value = "";
        document.getElementById("vinho-anovin").value = "";
        document.getElementById("vinho-paisvin").value = "";
        document.getElementById("vinho-estoquevin").value = "";
        document.getElementById("vinho-fkcodigotip").value = "";
        document.getElementById("vinho-fkcodigocat").value = "";
    })
    .catch((error) => {
        console.error('Erro ao adicionar Vinho:', error);
    });
}

//Função para adicionar Carrinho
function adicionarCarrinho() {
    const estadocar = document.getElementById("carrinho-estadocar").value;
    const fkcodigocli = document.getElementById("carrinho-fkcodigocli").value;

    const data = {
        estadocar,
        fkcodigocli
    };

    fetch('/carrinhos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Carrinho adicionado:', data);
        document.getElementById("carrinho-estadocar").value = "";
        document.getElementById("carrinho-fkcodigocli").value = "";
    })
    .catch((error) => {
        console.error('Erro ao adicionar Carrinho:', error);
    });
}

//Função para adicionar Vinhos do Carrinho
function adicionarVinhoDoCarrinho() {
    const fkcodigovin = document.getElementById("vinhodocarrinho-fkcodigovin").value;
    const fkcodigocar = document.getElementById("vinhodocarrinho-fkcodigocar").value;

    const data = {
        fkcodigovin,
        fkcodigocar
    };

    fetch('/vinhosdocarrinho', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Vinho do Carrinho adicionado:', data);
        document.getElementById("vinhodocarrinho-fkcodigovin").value = "";
        document.getElementById("vinhodocarrinho-fkcodigocar").value = "";
    })
    .catch((error) => {
        console.error('Erro ao adicionar Vinho do Carrinho:', error);
    });
}