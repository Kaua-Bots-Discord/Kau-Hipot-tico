# 🤖 Kauã Hipotético - Discord Timer Bot v4

Um bot de Discord avançado que permite criar timers customizáveis, listas de presença e um sistema de sorteio crítico com temática de RPG.

## ✨ Funcionalidades

**Timers Avançados (Admin Only):**
- **Comando `/criar`**: Cria um novo timer com descrição, emojis customizáveis e imagem opcional.
- **Seleção Dinâmica de Emojis**: Escolha quais timers usar (ex: apenas 10 e 20 minutos).
- **Suporte a Imagens**: Envie uma imagem junto com a mensagem do timer.
- **Notificação com Imagem**: Receba uma imagem (Goku) **apenas na DM privada** quando o timer expira.
- **Notificações Duplas**: Notificação via DM (com imagem) e no canal de origem (sem imagem).
- **Visualização de Reações**: A mensagem é atualizada para mostrar quem reagiu a cada opção.
- **Múltiplos Timers**: Suporte a múltiplos usuários no mesmo embed.

**Timers Disponíveis:**
- ⏱️ 10 minutos
- ⏲️ 20 minutos
- ⌛ 30 minutos
- ⏰ 40 minutos
- 🕐 1 hora
- ❌ Não vai responder este turno / Cancelar

**Listas de Presença (Admin Only):**
- **Comando `/presente`**: Cria uma lista de presença onde usuários reagem com ✅ para confirmar presença.
- **Listagem Numerada**: Os usuários aparecem em formato numerado (1- @user, 2- @user, etc.).
- **Atualização Automática**: A lista é atualizada a cada 15 segundos.
- **Contagem de Presentes**: Mostra quantas pessoas confirmaram presença.

**Sistema de Crítico (Para Todos):**
- **Comando `/crítico`**: Sorteia um número de 1 a 20 com mensagens e GIFs temáticos.
- **Sequência de Críticos**: Rastreia críticos consecutivos com mensagens cada vez mais épicas.
- **Sistema de Fases**: Quanto mais críticos você acerta, mais fácil fica manter a sequência.
- **Temática RPG**: Mensagens e GIFs de anime/ação que correspondem a cada resultado.

**Gerenciamento:**
- **Comando `/timers`**: Lista seus timers ativos com tempo restante.
- **Comando `/cancelar`**: Cancela todos os seus timers.

## 📋 Requisitos

- Python 3.8+
- `discord.py` 2.3.2+
- `python-dotenv` 1.0.0+
- Um servidor Discord para testes
- Um token de bot Discord válido

## 🚀 Instalação

### 1. Clonar ou baixar o projeto

```bash
cd /home/ubuntu/kaua_bot
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar o token do bot

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione seu token:

```
DISCORD_BOT_TOKEN=seu_token_aqui
```

### 4. Criar um Bot no Discord Developer Portal

1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application" e dê um nome (ex: "Kauã Hipotético")
3. Vá para a aba "Bot" e clique em "Add Bot"
4. Copie o token sob "TOKEN"
5. **Ative as seguintes Intents**:
   - **Message Content Intent**
   - **Server Members Intent** (Crucial para o bot ver quem reagiu)
   - **Reaction Intent**

### 5. Configurar permissões do bot

Na seção "OAuth2" → "URL Generator":

**Scopes:**
- `bot`

**Permissions:**
- Send Messages
- Embed Links
- Add Reactions
- Read Messages/View Channels
- Read Message History
- Manage Messages

Copie a URL gerada e acesse em seu navegador para adicionar o bot ao seu servidor.

## 📖 Como Usar

### Comando: `/criar` (Admin Only)

Cria um novo timer com opções customizáveis:

```
/criar descricao: Pausa para café emojis: 10,20 imagem: https://exemplo.com/imagem.jpg
```

**Parâmetros:**
- `descricao`: Descrição do timer (obrigatório)
- `emojis`: Quais timers usar, separados por vírgula (opcional, padrão: todos)
  - Opções: `10`, `20`, `30`, `40`, `60`, `cancelar`
- `imagem`: URL de uma imagem para enviar junto (opcional)

### Comando: `/presente` (Admin Only)

Cria uma lista de presença:

```
/presente descricao: Presença na reunião de hoje
```

Todos que reagirem com ✅ aparecerão na lista em formato numerado.

### Comando: `/crítico` (Para Todos)

Sorteia um número de 1 a 20 com resultado temático:

```
/crítico
```

O bot exibe uma mensagem épica e um GIF correspondente ao resultado. Sua sequência de críticos é rastreada automaticamente!

### Comando: `/timers`

Lista todos os seus timers ativos com o tempo restante:

```
/timers
```

### Comando: `/cancelar`

Cancela todos os seus timers ativos:

```
/cancelar
```

## ▶️ Executar o Bot

```bash
python bot.py
```

Você deverá ver:
```
✅ Bot Kauã Hipotético#0000 conectado com sucesso!
✅ 5 comando(s) sincronizado(s)
```

## 📁 Estrutura do Projeto

```
kaua_bot/
├── bot.py                      # Arquivo principal do bot (v4)
├── requirements.txt            # Dependências do projeto
├── .env.example               # Exemplo de arquivo de configuração
├── README.md                  # Este arquivo
├── GUIA_ATUALIZACAO.md        # Guia para atualizar o código
├── COMANDO_CRITICO.md         # Documentação do comando /crítico
├── assets/
│   ├── kaua_profile.jpg       # Foto de perfil do bot
│   └── goku_timer_end.jpg     # Imagem de notificação de fim de timer
└── logs/                      # Pasta para logs (opcional)
```

## 🔐 Restrições de Permissão

- **`/criar`**: Apenas administradores podem usar
- **`/presente`**: Apenas administradores podem usar
- **`/crítico`**: Todos os membros podem usar

## 🐛 Troubleshooting

### Bot não mostra quem reagiu

Certifique-se de que a **Server Members Intent** está ativada no Discord Developer Portal.

### Notificação não chega no canal

Verifique se o bot tem permissão para enviar mensagens no canal de origem.

### Imagem do Goku não aparece na DM

Certifique-se de que o arquivo `goku_timer_end.jpg` existe em `assets/`.

### Como atualizar o código?

Consulte o arquivo **`GUIA_ATUALIZACAO.md`** para instruções detalhadas.

### Quero entender o sistema de crítico

Consulte o arquivo **`COMANDO_CRITICO.md`** para documentação completa.

## 📄 Licença

Este projeto é fornecido como está para uso pessoal.

## 🤝 Suporte

Para problemas ou sugestões, verifique:
- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- Arquivo `GUIA_ATUALIZACAO.md` para problemas de atualização
- Arquivo `COMANDO_CRITICO.md` para dúvidas sobre o sistema de crítico

---

**Desenvolvido com ❤️ para Discord**
