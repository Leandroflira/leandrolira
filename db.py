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
        
