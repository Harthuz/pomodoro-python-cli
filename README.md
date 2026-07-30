# Pomodoro Script

Script em Python para gestão de tempo com a técnica Pomodoro diretamente no terminal.

![Demonstração do Pomodoro CLI](assets/screenshot.png)

## Como Executar

Você pode executar o script diretamente via Python ou de forma global em qualquer terminal após configurar o `PATH`.

### Execução Direta

Execute o script utilizando o Python 3:

```bash
python pomodoro.py [argumentos]
```

### Execução Global no Terminal (via `pomodoro.bat`)

Após adicionar a pasta do projeto ao `PATH` do Windows, você poderá rodar o comando simplificado em qualquer diretório:

```bash
pomodoro [argumentos]
```

---

## Configuração do PATH no Windows

Adicionar o diretório do projeto à variável de ambiente `PATH` permite executar o comando `pomodoro` de qualquer pasta no Prompt de Comando (CMD) ou PowerShell.

### Opção 1: Via Interface Gráfica (Recomendado)

1. Pressione as teclas `Win + R`, digite `sysdm.cpl` e pressione **Enter**.
2. Na janela que abrir, vá até a aba **Avançado** e clique no botão **Variáveis de Ambiente...**.
3. Na seção **Variáveis do usuário** (ou **Variáveis do sistema**), selecione a variável `Path` e clique em **Editar...**.
4. Clique no botão **Novo** no canto direito.
5. Cole o caminho absoluto do diretório do projeto (exemplo: `C:\Users\Nutis\Documents\Hernandes\Pomodoro`).
6. Clique em **OK** em todas as janelas abertas para salvar.
7. **Reinicie o terminal** (CMD ou PowerShell) para carregar a nova configuração.

### Opção 2: Via PowerShell (Linha de Comando)

Abra o PowerShell e execute o comando abaixo (substituindo pelo caminho real da sua pasta):

```powershell
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\Nutis\Documents\Hernandes\Pomodoro", "User")
```

> **Nota:** Após executar o comando acima, feche e abra o terminal para aplicar a alteração.

---

## Argumentos Disponíveis

- `-f`, `--foco`: Tempo de foco em minutos (padrão: 25)
- `-pc`, `--pausa-curta`: Tempo de pausa curta em minutos (padrão: 5)
- `-pl`, `--pausa-longa`: Tempo de pausa longa em minutos (padrão: 15)
- `-c`, `--ciclos`: Número de ciclos de foco antes de uma pausa longa (padrão: 4)
- `-v`, `--volume`: Nível do volume/intensidade sonora do alarme: 0 a 100 (padrão: 50)
- `-a`, `--auto`: Inicia os próximos ciclos automaticamente sem perguntar

### Exemplos de Uso

**Executar com configurações padrão:**
```bash
pomodoro
```
*(ou `python pomodoro.py`)*

**Executar com foco de 50 minutos, pausa de 10 minutos, pausa longa de 20 minutos, volume alto (80) e início automático:**
```bash
pomodoro -f 50 -pc 10 -pl 20 -v 80 -a
```

**Execução rápida de teste (ex: foco de 10s e pausa de 5s):**
```bash
pomodoro -f 0.16 -pc 0.08 -pl 0.16
```
