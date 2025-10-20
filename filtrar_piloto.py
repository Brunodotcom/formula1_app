import fastf1

fastf1.Cache.enable_cache('cache')

def filtrar_piloto(ano: int, gp: str, abbr:str):
    evento = fastf1.get_event(ano, gp)
    session = evento.get_session('R')
    session.load()
    fastest_lap = session.laps.pick_fastest(abbr)
    piloto = session.get_driver(abbr)


    return ''.join(f'{evento.EventName}\n{piloto.Abbreviation} - {piloto.FullName} - {piloto.TeamName}\n\
    Volta mais rápida: {fastest_lap["LapTime"]}\nPontos conquistados: {piloto.Points}\n\
    Posição final: {piloto.ClassifiedPosition}')



print(filtrar_piloto(2025, 'Austin', 'VER'))