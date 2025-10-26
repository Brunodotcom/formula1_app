import fastf1

fastf1.Cache.enable_cache('cache')


sessao = fastf1.get_session(2020, 'Monaco', 'R')
sessao.load()
pilotos = sessao.drivers

for piloto in pilotos:
    info = sessao.get_driver(piloto)
    print(f'Piloto: {info.Abbreviation} - {info.FullName}\nEquipe: {info.TeamName}')