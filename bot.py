from matcher import match
import flow
import responses

estado = None
triagem_atual = None
servico_atual = None

print(flow.menu_inicial())

while True:
    user = input("> ").lower().strip()

    if user in ["sair", "exit", "quit"]:
        print("Bot encerrado.")
        break

    # MENU INICIAL
    if estado is None:
        if user == "1":
            estado = "podologia_triagem"
            servico_atual = "Podologia"
            print(flow.flow_podologia())
            continue

        elif user == "2":
            estado = "reflexologia"
            servico_atual = "Reflexologia Podal"
            print(flow.flow_reflexo())
            continue

        else:
            print("Opção inválida. Digite 1 ou 2.")
            continue

    # TRIAGEM
    if estado == "podologia_triagem":
        if user == "1":
            triagem_atual = "Nenhuma"
        elif user == "2":
            triagem_atual = "Diabetes"
        elif user == "3":
            triagem_atual = "Idoso acamado"
        elif user == "4":
            triagem_atual = "Anticoagulante"
        elif user == "5":
            triagem_atual = "Outro"
        else:
            print("Opção inválida. Escolha 1-5.")
            continue

        print(responses.resposta_triagem(triagem_atual.lower()))
        print("\nO que deseja?\n1) Preço\n2) Horário\n3) Localização\n4) Domicílio\n5) Agendar")
        estado = "podologia_menu"
        continue

    # MENU PODOLÓGICO
    if estado == "podologia_menu":
        if user == "1":
            print(responses.preco_podologia())
        elif user == "2":
            print(responses.horario_podologia())
        elif user == "3":
            print(responses.localizacao())
        elif user == "4":
            print(responses.domicilio())
        elif user == "5":
            print(responses.agendar())
            estado = "aguardando_nome"
            continue
        else:
            print("Escolha 1 | 2 | 3 | 4 | 5")

    # REFLEXOLOGIA
    if estado == "reflexologia":
        if user == "1":
            print(responses.preco_reflexo())
        elif user == "2":
            print(responses.horario_reflexo())
        elif user == "3":
            print(responses.localizacao())
        elif user == "4":
            print(responses.domicilio())
        elif user == "5":
            print(responses.agendar())
            estado = "aguardando_nome"
            continue
        else:
            print("Escolha 1 | 2 | 3 | 4 | 5")

    # CAPTURA NOME + LOG
    if estado == "aguardando_nome":
        nome = user.strip().title()

        with open("atendimentos.txt", "a", encoding="utf-8") as f:
            f.write(f"Nome: {nome}\n")
            f.write(f"Serviço: {servico_atual}\n")
            f.write(f"Triagem: {triagem_atual}\n")
            f.write("-" * 30 + "\n")

        print(f"Obrigada, {nome}! 😊")
        print("A podóloga vai te chamar no WhatsApp para combinar dia e horário.\n")
        
        estado = None
        print("Se quiser atendimento novamente:\n1) Podologia\n2) Reflexologia")
