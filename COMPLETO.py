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
                        hoje = input("Data de hoje AAAA-MM-DD: ")
                        hora_agora = input("Hora atual HH:MM: ")
                        encontrou = False
                        for consulta in consultas:
                            futura = consulta["data"] > hoje or (
                                consulta["data"] == hoje and consulta["hora"] >= hora_agora)
                            if (consulta["cpf"] == paciente["cpf"]
                                and consulta["status"] == "Agendada" and futura):
                                encontrou = True
                                nome_dentista = ""
                                for dentista in dentistas:
                                    if dentista["id"] == consulta["dentista_id"]: nome_dentista = dentista["nome"]
                                print(consulta["id"], nome_dentista,
                                      consulta["data"], consulta["hora"])
                        if not encontrou: print("Nenhuma consulta futura.")

                    elif opcao == "4":
                        id_cancelar = input("ID da consulta: ")
                        cancelou = False
                        for consulta in consultas:
                            if (str(consulta["id"]) == id_cancelar
                                and consulta["cpf"] == paciente["cpf"]
                                and consulta["status"] == "Agendada"):
                                consulta["status"] = "Cancelada pelo paciente"
                                cancelou = True
                        if cancelou: print("Sua consulta foi cancelada.")
                        else: print("Consulta ativa não encontrada para seu CPF.")
                    elif opcao == "0": menu_paciente = False
                    else: print("Opção inválida.")

    elif inicio == "2":
        email = input("E-mail do ADM: ")
        senha = input("Senha do ADM: ")
        adm_logado = None
        for adm in adms:
            if adm["email"] == email and adm["senha"] == senha: adm_logado = adm
        if adm_logado is None: print("E-mail ou senha incorretos.")
        else:
            print("Bem-vindo(a),", adm_logado["nome"])
            menu_adm = True
            while menu_adm:
                print("\n=== SECRETARIA ===\n1 - Pacientes\n2 - Dentistas\n3 - Salas\n4 - Agenda\n0 - Sair da conta")
                escolha_adm = input("Escolha: ")

                if escolha_adm == "1":
                    menu_cliente = True
                    while menu_cliente:
                        print("\n=== PACIENTES ===\n1 - Cadastrar\n2 - Listar\n3 - Buscar/atualizar\n4 - Remover\n0 - Voltar")
                        opcao_cliente = input("Escolha: ")
                        if opcao_cliente == "1":
                            nome = input("Nome: ").strip()
                            cpf_novo = input("CPF: ").strip()
                            senha_nova = input("Senha: ").strip()
                            telefone_novo = input("Telefone: ").strip()
                            cpf_repetido = False
                            for cliente in clientes:
                                if cliente["cpf"] == cpf_novo: cpf_repetido = True
                            if not cpf_novo.isdigit() or len(cpf_novo) != 11:
                                print("CPF deve ter 11 números.")
                            elif nome == "" or senha_nova == "" or telefone_novo == "":
                                print("Preencha todos os campos.")
                            elif cpf_repetido:
                                print("CPF já cadastrado.")
                            else:
                                clientes.append({"nome": nome, "cpf": cpf_novo,
                                    "senha": senha_nova, "telefone": telefone_novo,
                                    "observacoes": "", "alergias": ""})
                                print("Paciente cadastrado.")
                        elif opcao_cliente == "2":
                            if len(clientes) == 0: print("Lista vazia.")
                            for cliente in clientes:
                                print(cliente["nome"], cliente["cpf"], cliente["telefone"],
                                      "Obs:", cliente["observacoes"], "Alergias:", cliente["alergias"])
                        elif opcao_cliente == "3":
                            busca = input("Nome ou CPF: ").strip().lower()
                            encontrou = False
                            for cliente in clientes:
                                if busca in cliente["nome"].lower() or busca == cliente["cpf"]:
                                    encontrou = True
                                    print(cliente["nome"], cliente["cpf"], cliente["telefone"])
                            if encontrou:
                                cpf_editar = input("CPF para atualizar: ")
                                editar = None
                                for cliente in clientes:
                                    if cliente["cpf"] == cpf_editar: editar = cliente
                                if editar is None: print("Paciente não encontrado.")
                                else:
                                    nome_novo = input("Novo nome (Enter mantém): ").strip()
                                    telefone_novo = input("Novo telefone (Enter mantém): ").strip()
                                    obs = input("Observações (Enter mantém): ").strip()
                                    alergias = input("Alergias (Enter mantém): ").strip()
                                    if nome_novo != "": editar["nome"] = nome_novo
                                    if telefone_novo != "": editar["telefone"] = telefone_novo
                                    if obs != "": editar["observacoes"] = obs
                                    if alergias != "": editar["alergias"] = alergias
                                    print("Cadastro atualizado.")
                            else: print("Paciente não encontrado.")

                        elif opcao_cliente == "4":
                            cpf_remover = input("CPF para remover: ")
                            existe = False
                            for cliente in clientes:
                                if cliente["cpf"] == cpf_remover: existe = True
                            if existe:
                                confirmar = input("Confirma remoção? (s/n): ")
                                if confirmar.lower() == "s":
                                    clientes_novos = []
                                    for cliente in clientes:
                                        if cliente["cpf"] != cpf_remover:
                                            clientes_novos.append(cliente)
                                    clientes = clientes_novos
                                    for consulta in consultas:
                                        if consulta["cpf"] == cpf_remover and consulta["status"] == "Agendada":
                                            consulta["status"] = "Cancelada pela secretaria"
                                    print("Paciente removido.")
                            else:
                                print("Paciente não encontrado.")
                        elif opcao_cliente == "0": menu_cliente = False
                        else: print("Opção inválida.")

                elif escolha_adm == "2":
                    menu_dentista = True
                    while menu_dentista:
                        print("\n=== DENTISTAS ===\n1 - Cadastrar\n2 - Listar\n3 - Atualizar\n4 - Remover\n0 - Voltar")
                        opcao_dentista = input("Escolha: ")
                        if opcao_dentista == "1":
                            if len(dentistas) >= 2: print("Limite de 2 dentistas atingido.")
                            else:
                                nome = input("Nome: ").strip()
                                cro = input("CRO: ").strip()
                                especialidade = input("Especialidade: ").strip()
                                repetido = False
                                for dentista in dentistas:
                                    if dentista["cro"].lower() == cro.lower(): repetido = True
                                if nome == "" or cro == "" or especialidade == "": print("Preencha os campos.")
                                elif repetido: print("CRO já cadastrado.")
                                else:
                                    dentistas.append({"id": id_dentista, "nome": nome,
                                        "cro": cro, "especialidade": especialidade})
                                    id_dentista += 1
                                    print("Dentista cadastrado.")
                        elif opcao_dentista == "2":
                            if len(dentistas) == 0: print("Lista vazia.")
                            for dentista in dentistas:
                                print(dentista["id"], dentista["nome"],
                                      dentista["cro"], dentista["especialidade"])
                        elif opcao_dentista == "3":
                            id_editar = input("ID do dentista: ")
                            editar = None
                            for dentista in dentistas:
                                if str(dentista["id"]) == id_editar: editar = dentista
                            if editar is None: print("Dentista não encontrado.")
                            else:
                                nome_novo = input("Novo nome (Enter mantém): ").strip()
                                cro_novo = input("Novo CRO (Enter mantém): ").strip()
                                esp_nova = input("Nova especialidade (Enter mantém): ").strip()
                                repetido = False
                                for dentista in dentistas:
                                    if (cro_novo != "" and dentista["cro"].lower() == cro_novo.lower()
                                        and dentista["id"] != editar["id"]):
                                        repetido = True
                                if repetido: print("CRO já pertence a outro dentista.")
                                else:
                                    if nome_novo != "": editar["nome"] = nome_novo
                                    if cro_novo != "": editar["cro"] = cro_novo
                                    if esp_nova != "": editar["especialidade"] = esp_nova
                                    print("Dentista atualizado.")
                        elif opcao_dentista == "4":
                            id_remover = input("ID do dentista: ")
                            remover = None
                            for dentista in dentistas:
                                if str(dentista["id"]) == id_remover: remover = dentista
                            if remover is None: print("Dentista não encontrado.")
                            else:
                                tem_consulta = False
                                for consulta in consultas:
                                    if consulta["dentista_id"] == remover["id"]: tem_consulta = True
                                if tem_consulta: print("Dentista tem consulta registrada; não pode ser removido.")
                                else:
                                    dentistas_novos = []
                                    salas_novas = []
                                    for dentista in dentistas:
                                        if dentista["id"] != remover["id"]:
                                            dentistas_novos.append(dentista)
                                    for sala in salas:
                                        if sala["dentista_id"] != remover["id"]:
                                            salas_novas.append(sala)
                                    dentistas = dentistas_novos
                                    salas = salas_novas
                                    print("Dentista removido.")
                        elif opcao_dentista == "0": menu_dentista = False
                        else: print("Opção inválida.")

                elif escolha_adm == "3":
                    menu_sala = True
                    while menu_sala:
                        print("\n=== SALAS ===\n1 - Cadastrar/vincular\n2 - Listar\n0 - Voltar")
                        opcao_sala = input("Escolha: ")
                        if opcao_sala == "1":
                            if len(salas) >= 2: print("Limite de 2 salas atingido.")
                            elif len(dentistas) == 0: print("Cadastre dentista primeiro.")
                            else:
                                nome_sala = input("Nome da sala: ").strip()
                                repetida = False
                                for sala in salas:
                                    if sala["nome"].lower() == nome_sala.lower(): repetida = True
                                if nome_sala == "" or repetida: print("Nome vazio ou sala já cadastrada.")
                                else:
                                    print("Dentistas sem sala:")
                                    for dentista in dentistas:
                                        tem_sala = False
                                        for sala in salas:
                                            if sala["dentista_id"] == dentista["id"]: tem_sala = True
                                        if not tem_sala: print(dentista["id"], dentista["nome"])
                                    id_escolhido = input("ID do dentista: ")
                                    escolhido = None
                                    for dentista in dentistas:
                                        if str(dentista["id"]) == id_escolhido: escolhido = dentista
                                    tem_sala = False
                                    if escolhido is not None:
                                        for sala in salas:
                                            if sala["dentista_id"] == escolhido["id"]: tem_sala = True
                                    if escolhido is None: print("Dentista não encontrado.")
                                    elif tem_sala: print("Dentista já tem uma sala.")
                                    else:
                                        salas.append({"id": id_sala, "nome": nome_sala,
                                            "dentista_id": escolhido["id"]})
                                        id_sala += 1
                                        print("Sala vinculada.")
                        elif opcao_sala == "2":
                            if len(salas) == 0: print("Lista vazia.")
                            for sala in salas:
                                dentista_sala = "Não encontrado"
                                for dentista in dentistas:
                                    if dentista["id"] == sala["dentista_id"]: dentista_sala = dentista["nome"]
                                print(sala["nome"], "-", dentista_sala)
                        elif opcao_sala == "0": menu_sala = False
                        else: print("Opção inválida.")

                elif escolha_adm == "4":
                    menu_agenda = True
                    while menu_agenda:
                        print("\n=== AGENDA ===\n1 - Listar todas\n2 - Filtrar\n3 - Cancelar\n0 - Voltar")
                        opcao_agenda = input("Escolha: ")
                        if opcao_agenda == "1" or opcao_agenda == "2":
                            filtro_id = ""
                            filtro_data = ""
                            if opcao_agenda == "2":
                                print("1 - Dentista | 2 - Data")
                                filtro = input("Tipo: ")
                                if filtro == "1": filtro_id = input("ID do dentista: ")
                                elif filtro == "2": filtro_data = input("Data AAAA-MM-DD: ")
                            encontrou = False
                            for consulta in consultas:
                                mostrar = True
                                if filtro_id != "" and str(consulta["dentista_id"]) != filtro_id: mostrar = False
                                if filtro_data != "" and consulta["data"] != filtro_data: mostrar = False
                                if mostrar:
                                    encontrou = True
                                    nome_cliente = "Paciente removido"
                                    nome_dentista = "Dentista removido"
                                    for cliente in clientes:
                                        if cliente["cpf"] == consulta["cpf"]: nome_cliente = cliente["nome"]
                                    for dentista in dentistas:
                                        if dentista["id"] == consulta["dentista_id"]: nome_dentista = dentista["nome"]
                                    print(consulta["id"], nome_cliente, consulta["cpf"],
                                          nome_dentista, consulta["data"],
                                          consulta["hora"], consulta["status"])
                            if not encontrou: print("Nenhuma consulta encontrada.")
                        elif opcao_agenda == "3":
                            cancelar = input("ID da consulta: ")
                            cancelou = False
                            for consulta in consultas:
                                if str(consulta["id"]) == cancelar and consulta["status"] == "Agendada":
                                    consulta["status"] = "Cancelada pela secretaria"
                                    cancelou = True
                            if cancelou: print("Consulta cancelada.")
                            else: print("Consulta ativa não encontrada.")
                        elif opcao_agenda == "0": menu_agenda = False
                        else: print("Opção inválida.")
                elif escolha_adm == "0":
                    print("Você saiu da conta.")
                    menu_adm = False
                else: print("Opção inválida.")
    elif inicio == "0":
        print("Programa encerrado.")
        aberto = False
    else: print("Opção inválida.")
