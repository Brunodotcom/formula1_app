import fastf1

fastf1.Cache.enable_cache('cache')


#Função para listar os pilotos
def listar_pilotos(ano: int, gp: str):

    #Criando a sessão com os argumentos passados na função
    evento = fastf1.get_event(ano, gp)
    session = evento.get_session('R') #Selecionando "race" que é a corrida
    #Baixando os dados
    session.load()

    #coletando dados dos pilotos e criando uma lista para inserir as informações
    pilotos = session.drivers
    dados_pilotos = []

    #iterando pelo obejeto e coletando os dados desejados
    for piloto in pilotos:
        info = session.get_driver(piloto)
        dados_pilotos.append(
            {
                'codigo': piloto,
                'nome': info.FullName,
                'equipe': info.TeamName,
                'posicao_final': info.ClassifiedPosition,
                'tempo_total': str(info.Time),
                'abbr': info.Abbreviation
            }
        )
    
    #Retornando os dados formatados
    return ''.join(f'{p["posicao_final"]} - {p["abbr"]} - {p["nome"]} - {p["equipe"]}\
    - Tempo: {p["tempo_total"]}\n' for p in dados_pilotos)



print(listar_pilotos(2025, 'Austin'))