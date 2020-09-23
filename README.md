<h1>PythonTesteJunto</h1>

<h3> Teste Junto Seguros </h3>

- Utilizando Python Versão 3.8


Para Instalar:

    ''' Console
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt
    '''

Projeto:

    - Utilizando Framework Flask
    - Criado Crud e Autenticação com JWT para testar no Postman ou Insomnia
    - Utilizando BD SqLite
    - Pacotes utilizados no Projeto estão no Requirements-dev.txt

Exemplo de Request:

 - Post_user

        {
            "name" : "teste",
            "username": "teste1",
            "password": "password",
            "email": "teste@hotmail.com"
        }
    
 - Update_user

        {
            "name" : "testeXX",
            "username": "testeXX",
            "password": "passwordX",
            "email": "testeXX@hotmail.com"
        }
        
 - Get_user || - Get_users

        {
        }
        
 - Delete_User

        {
        }
 
 - Token JWT
 
        - Type : Basic Auth
        - Username : testeXX
        - password : passwordX