from dados import podologia, reflexologia, triagem_info

def preco_podologia():
    return podologia["preco"]

def preco_reflexo():
    return reflexologia["preco"]["espaco"]

def horario_podologia():
    return podologia["horario"]

def horario_reflexo():
    return reflexologia["horario"]

def localizacao():
    return podologia["localizacao"]

def domicilio():
    return podologia["domicilio"]

def agendar():
    return (
        "Atendo somente com hora marcada 😊\n"
        "Envie seu nome por gentileza."
    )

def resposta_triagem(cond):
    return triagem_info.get(cond, "Informação registrada!")
