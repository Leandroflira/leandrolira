def menu():
    print(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<")
    print("             MENU")
    print(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<")
    print("1-Cadastrar")
    print("2-Deletar")
    print("3-Realizar Pedido")
    print("-"*20)
    res=int(input("Digite o que deseja: "))
    print("-"*20)
    return res
def menu2():
    print("1-produto")
    print("2-cliente")
    print("3-fornecedor")
    print("4-funcionarios")
    print("-"*20)
    res=int(input("digite o que deseja: "))
    print("-"*20)
    return res



def cadastrarproduto(conbd, Nome, Descricao, Preco, quantEstoque):
    mycursor = conbd.cursor()
    sql = "INSERT INTO Produtos (Nome, Descricao, Preco) VALUES (%s, %s, %s)"
    valores = (Nome, Descricao, Preco)
    mycursor.execute(sql, valores)
    #ID_Produto = mycursor.fetchone()[0]
    #int(ID_Produto)
    ID_Produto = mycursor.lastrowid
    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUES(%s, %s)"
    val1 = (ID_Produto, quantEstoque)
    mycursor.execute(sql1, val1)
    conbd.commit()
    print("Produto cadastrado com sucesso")
    mycursor.close()
    ID_Categoria = mycursor.lastrowid
    sql2 = "INSERT INTO categoriasprodutos (ID_Categoria, Nome, Descricao) VALUES(%s, %s, %s)"
    val2 = (ID_Categoria, Nome, Descricao)
    mycursor.execute(sql2, val2)
    conbd.commit()
    print("Produto cadastrado com sucesso")
    mycursor.close()
   
def cadastrarcliente(conbd, Nome, sobrenome, endereco, cidade, codigopostal):
    mycursor = conbd.cursor()
    valores = (Nome, sobrenome, endereco, cidade, codigopostal)
    sql = "INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s)"

    mycursor.execute(sql, valores)
    conbd.commit()
    print("cliente cadastrado com sucesso")
    mycursor.close()
    
def cadastrarfornecedor(conbd, nome, contato, endereco):
    mycursor = conbd.cursor()
    valores = (nome, contato, endereco)
    sql = "INSERT INTO fornecedores( Nome, Contato, Endereco) VALUES (%s, %s, %s)"
    
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Fornecedor cadastrado com sucesso")
    mycursor.close()
    
def cadastrarfuncionarios(conbd, nome, cargo, departamento):
    mycursor = conbd.cursor()
    valores = (nome, cargo, departamento)
    sql = "INSERT INTO funcionarios(Nome, Cargo, Departamento) VALUES (%s, %s, %s)"
    
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Funcionário cadastrao com sucesso")
    mycursor.close()
    
def obterProdutoID(conbd,nome):
    try:
        with conbd.cursor() as cursor:
            sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
            cursor.execute(sql,(nome,))
            resultado = cursor.fetchone()
            if resultado:
                    return resultado[0]
            else:
                print("Produto com nome '{nome}' não encontrado")
                return None
    except Exception as e:
        print("Ocorreu um erro ao obter o ID do produto:{e}")
        return None
    
    
def deletarProduto(conbd, nome_produto):
    try:
        produto_id = obterProdutoID(conbd, nome_produto)
        if not produto_id:
            return
        
        conbd.start_transaction()
        with conbd.cursor() as cursor:
            sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
             
        cursor.execute(sql_detalhes_pedido, (produto_id,)) 
        with conbd.cursor() as cursor: 
            sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
            cursor.execute(sql_estoque, (produto_id,))
        with conbd.cursor() as cursor:
            sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
            cursor.execute(sql_produto, (produto_id,))
        conbd.commit()
        print("Produto e suas referencias deletadas com sucesso")
        
    except Exception as e :
        conbd.rollback()
        print(f"Ocorreu um erro ao deletar o produto: {e}")
        
    finally:
        conbd.close()

def encontrarcliente(conbd,):
    while true:
        active = "off"
        mycursor = conbd.cursor()
        cliente = input("Digite o nome do cliente :")
        sql = "select*from cliente where Nome = %s"
        val = (cliente,)
        mycursor.execute(sql,val)
        resultados = mycursor
        for linha in resultados:
            if cliente in linha[1]:
                id_cliente = linha[0]
                active = "on"

        if active == "off":
            inputclientes(conbd)
        if active == "on":
            break
    return id-cliente


def comprarproduto(conbd,):
    res = 0
    mycursor = conbd.cursor()
    produto = input("Digite o qual produto: ")
    sql = "select*frfron produtos"
    mycursor.execute(sql,)
    resultados = mycursor
    for linha in resultados:
        if produto in linha[1]:
            print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|preço:",linha[3])
    id_produto = int(input("Para confirmar digite o id do produto: "))
    sql2 ="select*from produtos where id_produto = %s"
    val2 = (id_produto,)
    mycursor.execute(sql2,val2,)
    resultados = mycursor
    for linha in resultados:
        preço = linha[3]
    quantidade = int(input("Quantidade: "))
    pg = input("Digite o método de pagamento: ")
    valor = preco = quantidade
    res = valor
    print("Compra realizada! Total :",res)
    avaliacao = int(input("De 1 a 5 o quão satisfeito está com o produto :"))
    coment = input("Digite seu comentário sobre o produto: ")

    return id_produto, res, quantidade, pg, preco, avaliacao, coment
        
def criarpedido(conbd,):
    data = date.today()
    mycursor = condb.mycursor()
    id_cliente = encontrarcliente(conbd,)
    dentro = comprarproduto(conbd,)
    id_produto = dentro[0]
    valor =  dentro[1]
    quantidade = dentro[2]
    pg = dentro[3]
    avaliacao = dentro[4]
    coment = dentro[5]
    sql = "insert into pedidos(data_pedido, id_cliente, total) values (%s, %s, %s)"
    val = (data, id_cliente, valor,)
    mycursor.execute(sql,val)
    id_pedido = mycursor.lastrowid
    sql1 = "insert into detalhespedido(ID_pedido, ID_produto, Quantidade) values (%s, %s, %s)"
    val1 = (id_pedido, id_produto, quantidade)
    mycursor.execute(sql1, val1)
    sql2 = "insert into vendas(data, id_cliente, metodopagamento, total) values (%s, %s, %s, %s)"
    val2 = (data, id_cliente,pg, valor)
    mycursor.execute(sql2, val2)
    id_venda = mycursor.lastrowid
    sql3 = "insert into pagamentos(ID_venda, data, valor) values (%s, %s, %s)"
    val3 = (id_venda, data, valor)
    mycursor.execute(sql3, val3)
    sql4 = "insert into comentariosavaliacoes(ID_produto, id_cliente, comentario, avaliacao, data) values (%s, %s, %s, %s, %s)"
    val4 = (id_produto, id_cliente, comentario, avaliacao, data)
    mycursor.execute(sql4, val4)
    print("compra realizada com sucesso")
    conbd.commit()
    mycursor.close()

def inputclientes(conbd,):
    nome = input("Digite o nome do cliente: ")
    sobrenome = input("Digite o sobrenome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    codigopostal = int(input("Digite o código postal do cliente"))
    cadastrarcliente(conbd, nome, sobrenome, endereco, cidade, codigopostal) 
    
