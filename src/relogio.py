"""
Prova do Relogio - Memory Model
Autor: Anthony William Staiger, com apoio do Claude (Anthropic)

O que este script mostra:
  1. Calcula o intervalo entre duas mensagens (o "gap").
  2. Classifica a pausa (mesma conversa, pausa curta, pausa longa...).
  3. Mede o intervalo numa escala em "graus" (logaritmo), para o tempo
     ocupar poucos tokens em vez de virar texto corrido.
  4. Testa o caso real da demo: 21:44:06 -> 22:02:27 (deve dar 18min 21s).

Como rodar:  python relogio.py
"""

import math
from datetime import datetime

# Formato das datas: dia/mes/ano hora:minuto:segundo
FORMATO = "%d/%m/%Y %H:%M:%S"


def intervalo_em_segundos(inicio, fim):
    """Devolve quantos segundos passaram entre duas datas (texto)."""
    a = datetime.strptime(inicio, FORMATO)
    b = datetime.strptime(fim, FORMATO)
    return int((b - a).total_seconds())


def formatar(segundos):
    """Transforma segundos em texto legivel, ex.: '18min 21s'."""
    dias, resto = divmod(segundos, 86400)
    horas, resto = divmod(resto, 3600)
    minutos, seg = divmod(resto, 60)
    partes = []
    if dias:
        partes.append(f"{dias}d")
    if horas:
        partes.append(f"{horas}h")
    if minutos:
        partes.append(f"{minutos}min")
    if seg or not partes:
        partes.append(f"{seg}s")
    return " ".join(partes)


def classificar(segundos):
    """Diz que tipo de pausa foi. Os limites sao um ponto de partida."""
    if segundos < 10 * 60:
        return "mesma conversa"
    if segundos < 6 * 3600:
        return "pausa curta"
    if segundos < 3 * 86400:
        return "pausa longa"
    return "volta depois de muito tempo"


def grau(segundos):
    """Escala logaritmica: 1 minuto = 0, 10 min = 1, 100 min = 2, e assim por diante."""
    minutos = max(segundos / 60, 1)
    return round(math.log10(minutos), 1)


def relatorio(inicio, fim):
    s = intervalo_em_segundos(inicio, fim)
    return {
        "intervalo": formatar(s),
        "tipo": classificar(s),
        "grau": grau(s),
        "segundos": s,
    }


if __name__ == "__main__":
    casos = [
        ("Caso real da demo (22/06/2026)", "22/06/2026 21:44:06", "22/06/2026 22:02:27"),
        ("Conversa continua", "17/10/2026 20:06:58", "17/10/2026 20:09:10"),
        ("Do dia para a manha", "17/10/2026 20:06:58", "18/10/2026 13:56:10"),
        ("Um mes depois", "17/09/2026 20:00:00", "17/10/2026 20:00:00"),
    ]

    print("=== PROVA DO RELOGIO ===\n")
    for nome, ini, fim in casos:
        r = relatorio(ini, fim)
        print(f"{nome}")
        print(f"  de {ini} ate {fim}")
        print(f"  intervalo: {r['intervalo']} | tipo: {r['tipo']} | grau: {r['grau']}\n")

    # Teste automatico: se o calculo estiver errado, o programa avisa.
    real = relatorio("22/06/2026 21:44:06", "22/06/2026 22:02:27")
    assert real["segundos"] == 1101, "Erro: o gap real deveria ser 1101 segundos"
    assert real["intervalo"] == "18min 21s", "Erro: texto do gap incorreto"
    print("TESTE OK: o gap real da demo deu 18min 21s, como registrado.")
