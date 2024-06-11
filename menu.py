from db import*


from cone import conexao
conbd=conexao()
while 1>0:
    op=menu()
    if op==1:
        op=menu2()
        if op==1:
            
            
            
            Nome = input("digite o nome do produto:")
            Descricao = input("digite a descrição do produto: ")
            Preco = float(input("digite o preço do produto: "))
            quantEstoque = float(input("Digite a quantidade: "))
            cadastrarproduto(conbd,Nome,Descricao,Preco,quantEstoque,)
        if op==2:
            Nome = input("digite o nome do cliente: ")
            Sobrenome = input("digite a sobrenome do cliente: ")
            Endereco = input("digite o endereço do cliente: ")
            Cidade = input("digite a cidade do cliente: ")
            CodigoPostal = input("digite o código postal do cliente: ")
            cadastrarcliente(conbd,Nome,Sobrenome,Endereco,Cidade,CodigoPostal)
        if op==3:
            Nome = input("Digite o nome do fornecedor: ")
            Contato = input("Digite o Email do fornecedor: ")
            Endereco = input("Digite o endereço do fornecedor: ")
            cadastrarfornecedor(conbd,Nome,Contato,Endereco)
        if op==4:
            Nome = input("Digite o nome do funcionário: ")
            Cargo = input("Digite o cargo do funcionário: ")
            Departamento = input("Digite o departamento do funcionário: ")
            cadastrarfuncionarios(conbd,Nome,Cargo,Departamento)
            
        
            
    