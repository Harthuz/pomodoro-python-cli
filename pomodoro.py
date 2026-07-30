import time
import sys
import argparse
import winsound

# Definições de frequências para sons
FREQ_DESCANSO = 600   # Tom mais grave para descanso
FREQ_TRABALHO = 1000  # Tom mais agudo para voltar ao trabalho

def tocar_bip(tipo, volume):
    """
    Toca o som correspondente.
    tipo: 'descanso' ou 'trabalho'
    volume: nível de 0 (mudo) a 100 (máximo)
    """
    if volume <= 0:
        return

    # winsound.Beep não tem controle de volume nativo.
    # Simulamos o volume ajustando o número de bipes (de 1 a 5)
    bipes = max(1, int(volume / 20))

    frequencia = FREQ_DESCANSO if tipo == 'descanso' else FREQ_TRABALHO
    
    if tipo == 'descanso':
        # Bip de descanso com duração de 2 segundos (2000ms)
        duracao = 2000
        for _ in range(bipes):
            winsound.Beep(frequencia, duracao)
            time.sleep(0.2)
    else:
        # Bip de trabalho com duração total de 3 segundos: 1.4s de som, 0.2s de silêncio, 1.4s de som
        for _ in range(bipes):
            winsound.Beep(frequencia, 1400)
            time.sleep(0.2)
            winsound.Beep(frequencia, 1400)
            time.sleep(0.2)

def formatar_tempo(segundos):
    mins, segs = divmod(int(segundos), 60)
    return f"{mins:02d}:{segs:02d}"

def executar_timer(duracao_minutos, mensagem, som_tipo, volume):
    segundos_totais = int(duracao_minutos * 60)
    print(f"\nIniciando: {mensagem} ({duracao_minutos} min)")
    
    for s in range(segundos_totais, 0, -1):
        tempo_formatado = formatar_tempo(s)
        progresso = int((segundos_totais - s) / segundos_totais * 20)
        barra = "#" * progresso + "-" * (20 - progresso)
        sys.stdout.write(f"\r[{barra}] {tempo_formatado} restante")
        sys.stdout.flush()
        time.sleep(1)
        
    sys.stdout.write(f"\r[####################] 00:00 - Concluído!\n")
    sys.stdout.flush()
    
    tocar_bip(som_tipo, volume)

def validar_volume(valor):
    ivalor = int(valor)
    if ivalor < 0 or ivalor > 100:
        raise argparse.ArgumentTypeError(f"O volume deve estar entre 0 e 100. Recebido: {valor}")
    return ivalor

def main():
    parser = argparse.ArgumentParser(description="Cronômetro Pomodoro em Python")
    parser.add_argument("-f", "--foco", type=float, default=25.0, help="Tempo de foco em minutos (padrão: 25)")
    parser.add_argument("-pc", "--pausa-curta", type=float, default=5.0, help="Tempo de pausa curta em minutos (padrão: 5)")
    parser.add_argument("-pl", "--pausa-longa", type=float, default=15.0, help="Tempo de pausa longa em minutos (padrão: 15)")
    parser.add_argument("-c", "--ciclos", type=int, default=4, help="Número de ciclos de foco antes de uma pausa longa (padrão: 4)")
    parser.add_argument("-v", "--volume", type=validar_volume, default=50, help="Nível do volume do alarme de 0 a 100 (padrão: 50)")
    parser.add_argument("-a", "--auto", action="store_true", help="Inicia os próximos ciclos automaticamente sem perguntar")
    
    args = parser.parse_args()
    
    ciclo = 1
    try:
        while True:
            print(f"\n=== Ciclo {ciclo} ===")
            # 1. Foco
            executar_timer(args.foco, "Foco no Trabalho!", "descanso", args.volume)
            
            # Se atingir a quantidade de ciclos definidos, faz uma pausa longa, senão pausa curta
            if ciclo % args.ciclos == 0:
                executar_timer(args.pausa_longa, "Pausa Longa para Descanso!", "trabalho", args.volume)
            else:
                executar_timer(args.pausa_curta, "Pausa Curta para Descanso!", "trabalho", args.volume)
                
            ciclo += 1
            if not args.auto:
                input("\nPressione Enter para iniciar o próximo ciclo (ou Ctrl+C para sair)...")
            else:
                print("\nIniciando o próximo ciclo automaticamente em 3 segundos... (Ctrl+C para sair)")
                time.sleep(3)
            
    except KeyboardInterrupt:
        print("\n\nPomodoro finalizado pelo usuário. Bom descanso!")

if __name__ == "__main__":
    main()
