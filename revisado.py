adms = [{"nome": "Lucas", "email": "admteste@gmail.com", "senha": "123"}]
clientes = []
dentistas = []
salas = []
consultas = []
id_dentista = 1
id_sala = 1
id_consulta = 1
aberto = True


while aberto:
    print("\n=== CLÍNICA ===\n1 - Paciente\n2 - Administração\n0 - Sair")
    inicio = input("Escolha: ")


    if inicio == "1":
        cpf = input("CPF (11 números): ").strip()
        paciente = None
        if not cpf.isdigit() or len(cpf) != 11: print("CPF inválido.")
        else:
            for cliente in clientes:
                if cliente["cpf"] == cpf: paciente = cliente
            if paciente is None:
                print("CPF não cadastrado. Faça seu cadastro.")
                nome = input("Nome: ").strip()
                senha = input("Crie uma senha: ").strip()
                telefone = input("Telefone: ").strip()
                if nome != "" and senha != "" and telefone != "":
                    paciente = {"nome": nome, "cpf": cpf, "senha": senha,
                                "telefone": telefone, "observacoes": "", "alergias": ""}
                    clientes.append(paciente)
                    print("Cadastro concluído.")
                else: print("Preencha todos os campos.")
            else:
                senha = input("Senha: ")
                if senha != paciente["senha"]:
                    print("Senha incorreta.")
                    paciente = None
                else: print("Bem-vindo(a),", paciente["nome"])

            if paciente is not None:
                menu_paciente = True
                while menu_paciente:
                    print("\n=== PACIENTE ===\n1 - Dentistas\n2 - Agendar\n3 - Minhas consultas\n4 - Cancelar consulta\n0 - Voltar")
                    opcao = input("Escolha: ")

                    if opcao == "1":
                        if len(dentistas) == 0: print("Nenhum dentista cadastrado.")
                        for dentista in dentistas:
                            sala_nome = "Sem consultório"
                            for sala in salas:
                                if sala["dentista_id"] == dentista["id"]: sala_nome = sala["nome"]
                            print(dentista["id"], dentista["nome"],
                                  dentista["especialidade"], sala_nome)

                    elif opcao == "2":
                        if len(dentistas) == 0 or len(salas) == 0: print("Ainda não há dentistas e salas disponíveis.")
                        else:
                            for dentista in dentistas:
                                for sala in salas:
                                    if sala["dentista_id"] == dentista["id"]:
                                        print(dentista["id"], dentista["nome"],
                                              dentista["especialidade"], sala["nome"])
                            escolha_id = input("ID do dentista: ")
                            escolhido = None
                            sala_escolhida = None
                            for dentista in dentistas:
                                if str(dentista["id"]) == escolha_id: escolhido = dentista
                            if escolhido is not None:
                                for sala in salas:
                                    if sala["dentista_id"] == escolhido["id"]: sala_escolhida = sala
                            if escolhido is None or sala_escolhida is None: print("Dentista não encontrado ou sem sala.")
                            else:
                                hoje = input("Data de hoje AAAA-MM-DD: ")
                                data = input("Data da consulta AAAA-MM-DD: ")
                                hora_agora = input("Hora atual HH:MM: ")
                                hora = input("Horário desejado HH:MM: ")
                                if len(hoje) != 10 or len(data) != 10 or len(hora) != 5: print("Confira o formato da data e do horário.")
                                elif data < hoje: print("A data já passou.")
                                elif data == hoje and hora <= hora_agora: print("Escolha um horário futuro.")
                                else:
                                    ocupado = False
                                    for consulta in consultas:
                                        if (consulta["status"] == "Agendada"
                                            and consulta["data"] == data
                                            and consulta["hora"] == hora
                                            and (consulta["dentista_id"] == escolhido["id"]
                                                 or consulta["sala_id"] == sala_escolhida["id"])):
                                            ocupado = True
                                    if ocupado: print("Dentista ou sala já ocupados nesse horário.")
                                    else:
                                        consultas.append({"id": id_consulta,
                                            "cpf": paciente["cpf"], "dentista_id": escolhido["id"],
                                            "sala_id": sala_escolhida["id"], "data": data,
                                            "hora": hora, "status": "Agendada"})
                                        id_consulta += 1
                                        print("Consulta agendada.")

                    elif opcao == "3":