
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
