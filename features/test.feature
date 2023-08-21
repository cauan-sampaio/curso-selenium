Feature: Login

        Scenario: Fazer login na conta
            Given Que eu esteja na página 
            When Quando eu clickar nos inputs de user-name e senha
            """
            {
                "nome": "cauan",
                "senha":"123"
            }
            """
            Then O usuário poderá logar!    