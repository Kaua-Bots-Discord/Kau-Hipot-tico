# 📖 Exemplos de Uso - Kauã Hipotético

Este documento mostra exemplos práticos de como usar o bot Kauã Hipotético.

## Exemplo 1: Criar um Timer Simples

### Passo 1: Usar o comando
```
/criar descricao: Pausa para café
```

### Resultado
O bot envia uma mensagem como esta:

```
⏱️ Timer Criado
Pausa para café

Reaja com um emoji para iniciar o timer:
⏱️ → 10 minutos
⏲️ → 20 minutos
⌛ → 30 minutos
⏰ → 40 minutos
🕐 → 1 hora

Criado por seu_nome
```

### Passo 2: Reagir ao emoji
Você clica no emoji ⏱️ para iniciar um timer de 10 minutos.

### Resultado
Você recebe uma DM do bot:

```
⏱️ Timer Iniciado
Você será notificado em 10.0 minutos
```

### Passo 3: Aguardar
Após 10 minutos, você recebe:

```
⏰ Timer Finalizado!
Seu timer de 10 minutos expirou!
```

---

## Exemplo 2: Timer com Tempo Parcial

### Cenário
- Mensagem criada às 10:00
- Você reage ao emoji ⏲️ (20 minutos) às 10:05

### Resultado
Como 5 minutos já passaram, você será notificado em **15 minutos** (às 10:20).

**Mensagem recebida:**
```
⏱️ Timer Iniciado
Você será notificado em 15.0 minutos
```

---

## Exemplo 3: Múltiplos Timers

### Passo 1: Criar primeiro timer
```
/criar descricao: Primeira tarefa
```
Você reage com ⏱️ (10 minutos)

### Passo 2: Criar segundo timer
```
/criar descricao: Segunda tarefa
```
Você reage com ⏲️ (20 minutos)

### Passo 3: Listar timers
```
/timers
```

### Resultado
```
⏱️ Seus Timers Ativos

Timer de 10 minutos
Tempo restante: 8.5 minutos

Timer de 20 minutos
Tempo restante: 18.3 minutos
```

---

## Exemplo 4: Cancelar Timers

### Passo 1: Você tem 2 timers ativos
```
/timers
```

### Passo 2: Cancelar todos
```
/cancelar
```

### Resultado
```
✅ Timers Cancelados
2 timer(s) cancelado(s) com sucesso
```

---

## Exemplo 5: Timer de 1 Hora

### Uso
```
/criar descricao: Sessão de trabalho
```
Você reage com 🕐 (1 hora)

### Resultado
Após 1 hora, você recebe a notificação de conclusão.

---

## Casos de Uso Práticos

### 📚 Estudar
```
/criar descricao: Sessão de estudo - Matemática
```
Reaja com ⏲️ (20 minutos) para uma sessão curta.

### 💼 Trabalho
```
/criar descricao: Reunião em 30 minutos
```
Reaja com ⌛ (30 minutos) para ser notificado.

### 🍳 Cozinhar
```
/criar descricao: Tempo de cozimento do arroz
```
Reaja com ⏱️ (10 minutos) para não queimar.

### 🏃 Exercício
```
/criar descricao: Intervalo entre séries
```
Reaja com ⏱️ (10 minutos) para descansar.

### 🎮 Gaming
```
/criar descricao: Pausa para lanche
```
Reaja com ⏲️ (20 minutos) para relaxar.

---

## Dicas e Truques

### ✅ Dica 1: Reutilizar Mensagens
Você pode reagir múltiplas vezes à mesma mensagem de timer, mas apenas uma reação por usuário será ativa.

### ✅ Dica 2: Descrições Descritivas
Use descrições claras para lembrar o que o timer é:
- ❌ Ruim: `/criar descricao: timer`
- ✅ Bom: `/criar descricao: Pausa para café - volta às 14:30`

### ✅ Dica 3: Monitorar Timers
Use `/timers` frequentemente para acompanhar seus timers ativos.

### ✅ Dica 4: Cancelamento Rápido
Se você errou, use `/cancelar` para remover todos os timers de uma vez.

### ✅ Dica 5: Notificações
Certifique-se de que você tem DMs ativadas para receber as notificações do bot.

---

## Troubleshooting

### ❓ "Não recebi a notificação"
- Verifique se suas DMs estão abertas
- Certifique-se de que o bot tem permissão para enviar mensagens
- Reinicie o Discord

### ❓ "O emoji não funciona"
- Certifique-se de que está usando os emojis corretos
- Tente remover a reação e adicionar novamente

### ❓ "Não consigo usar o comando"
- Verifique se o bot está online
- Certifique-se de que o bot tem permissão para enviar mensagens no canal
- Tente digitar `/` novamente para atualizar a lista de comandos

---

## Resumo dos Comandos

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `/criar` | Cria um novo timer | `/criar descricao: Pausa para café` |
| `/timers` | Lista seus timers ativos | `/timers` |
| `/cancelar` | Cancela todos os seus timers | `/cancelar` |

---

**Divirta-se usando o Kauã Hipotético! 🚀**
