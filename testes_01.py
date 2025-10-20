import fastf1


#Criando uma pasta "cache" para que os dados não sejam baixados sempre
fastf1.Cache.enable_cache('cache')


#Criando uma sessão e baixando os dados
session = fastf1.get_session(2025, 'Austin', 'R')
session.load()


#Exibindo os pilotos
print(session.drivers)


#Coletando dados de um piloto
verstappen = session.laps.pick_driver('VER')

#Mostrando o tempo de volta mais rápida do piloto
fastest = verstappen.pick_fastest()
print(f'A volta mais rápida do Verstappen: Volta: {fastest['LapNumber']} - Tempo:{fastest['LapTime']}')