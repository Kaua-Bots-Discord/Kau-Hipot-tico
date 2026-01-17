# 🆕 Novas Funcionalidades v3 - Kauã Hipotético

Este documento descreve as novas funcionalidades adicionadas na versão 3 do bot.

## 1️⃣ Seleção Dinâmica de Emojis

### O que é?

Agora você pode **escolher quais timers usar** ao criar uma mensagem de timer. Em vez de sempre ter os 6 emojis disponíveis, você pode selecionar apenas os que deseja.

### Como usar?

Use o parâmetro `emojis` no comando `/criar`:

```
/criar descricao: Votação emojis: 10,20,30
```

### Opções disponíveis:

| Código | Emoji | Duração |
|--------|-------|---------|
| `10` | ⏱️ | 10 minutos |
| `20` | ⏲️ | 20 minutos |
| `30` | ⌛ | 30 minutos |
| `40` | ⏰ | 40 minutos |
| `60` | 🕐 | 1 hora |
| `cancelar` | ❌ | Não vai responder |

### Exemplos práticos:

```
/criar descricao: Votação rápida emojis: 10,20
/criar descricao: Reunião longa emojis: 30,40,60
/criar descricao: Presença emojis: 10,cancelar
```

### Benefícios:

- **Menos confusão**: Apenas os timers relevantes são mostrados
- **Customização**: Adapte o timer para cada situação
- **Clareza**: Usuários veem apenas as opções válidas

---

## 2️⃣ Suporte a Imagens

### O que é?

Agora você pode **enviar uma imagem junto com a mensagem do timer**. A imagem aparecerá no embed da mensagem inicial.

### Como usar?

Use o parâmetro `imagem` no comando `/criar`:

```
/criar descricao: Pausa para café imagem: https://exemplo.com/imagem.jpg
```

### Exemplos de URLs válidas:

- URLs do Discord: `https://media.discordapp.net/attachments/...`
- URLs de sites: `https://exemplo.com/imagem.jpg`
- URLs de serviços: `https://imgur.com/...`

### Exemplo prático:

```
/criar descricao: Votação de atividade emojis: 10,20,30 imagem: https://media.discordapp.net/attachments/...
```

### Benefícios:

- **Contexto Visual**: A imagem ajuda a entender o propósito do timer
- **Atratividade**: Mensagens mais visuais e interessantes
- **Comunicação**: Transmita informações de forma mais clara

---

## 3️⃣ Imagem de Notificação (Goku)

### O que é?

Quando um timer expira, o bot **envia uma imagem do Goku** junto com a notificação de fim de timer. Essa imagem aparece tanto na **DM privada** quanto na **mensagem do canal**.

### Como funciona?

1. Você cria um timer com `/criar`
2. Você reage com um emoji
3. Quando o timer expira, você recebe:
   - Uma **DM privada** com a notificação e a imagem do Goku
   - Uma **mensagem no canal** mencionando você com a imagem do Goku

### Arquivo de imagem:

A imagem está armazenada em `assets/goku_timer_end.jpg`.

### Benefícios:

- **Diversão**: A imagem do Goku torna a notificação mais interessante
- **Notificação Clara**: Você vê claramente que o timer expirou
- **Redundância**: Se a imagem não carregar, a mensagem de texto ainda aparece

### Customização:

Se você quiser usar uma imagem diferente:

1. Substitua o arquivo `assets/goku_timer_end.jpg` por sua imagem
2. Certifique-se de que o arquivo tem o mesmo nome
3. Reinicie o bot

---

## 4️⃣ Comando `/presente` - Lista de Presença

### O que é?

Um novo comando que cria uma **lista de presença** onde usuários podem confirmar sua presença reagindo com ✅. A lista é atualizada automaticamente a cada 15 segundos.

### Como usar?

```
/presente descricao: Presença na reunião de hoje
```

### Como funciona?

1. O bot cria uma mensagem com o emoji ✅
2. Usuários reagem com ✅ para confirmar presença
3. A mensagem é atualizada automaticamente mostrando:
   - Quantas pessoas confirmaram
   - Quem confirmou (lista de menções)

### Exemplo de resultado:

```
✅ Lista de Presença
Presença na reunião de hoje

Presentes (5)
✅ @Alice
✅ @Bob
✅ @Charlie
✅ @Diana
✅ @Eve
```

### Exemplos de uso:

```
/presente descricao: Presença no evento
/presente descricao: Confirmação para a reunião
/presente descricao: Quem vem ao jogo?
```

### Benefícios:

- **Transparência**: Todos veem quem confirmou presença
- **Automatização**: Não precisa contar manualmente
- **Rastreabilidade**: Há um registro no canal de quem confirmou

### Diferença entre `/criar` e `/presente`:

| Aspecto | `/criar` (Timer) | `/presente` (Presença) |
|--------|-----------------|----------------------|
| Propósito | Contar tempo | Confirmar presença |
| Reação | Inicia um timer | Apenas registra presença |
| Notificação | Sim, quando expira | Não |
| Atualização | A cada 30s | A cada 15s |
| Emojis | Customizáveis | Apenas ✅ |

---

## 📊 Comparação: v2 vs v3

| Funcionalidade | v2 | v3 |
|---|---|---|
| Timers Básicos | ✅ | ✅ |
| 6 Opções de Emoji | ✅ | ✅ |
| Notificação Dupla | ✅ | ✅ |
| Visualização de Reações | ✅ | ✅ |
| Múltiplos Timers | ✅ | ✅ |
| Seleção Dinâmica de Emojis | ❌ | ✅ |
| Suporte a Imagens | ❌ | ✅ |
| Imagem de Notificação | ❌ | ✅ |
| Comando `/presente` | ❌ | ✅ |

---

## 🔧 Configuração Técnica

### Intents Necessários

Para que tudo funcione corretamente, certifique-se de que as seguintes intents estão ativadas:

- **Message Content Intent**: Para ler reações
- **Server Members Intent**: Para buscar usuários que reagiram
- **Reaction Intent**: Para detectar reações

### Tarefas de Fundo

O bot executa duas tarefas de fundo:

1. **`update_timer_message`**: Atualiza as mensagens de timer a cada 30 segundos
2. **`update_presence_message`**: Atualiza as listas de presença a cada 15 segundos

---

## 🚀 Exemplos de Uso Avançado

### Exemplo 1: Votação com Imagem

```
/criar descricao: Qual atividade fazer? emojis: 10,20,30 imagem: https://exemplo.com/atividades.jpg
```

Todos veem a imagem e votam em qual atividade fazer.

### Exemplo 2: Reunião com Presença

```
/presente descricao: Reunião de planejamento - 14h
```

Todos confirmam presença antes da reunião.

### Exemplo 3: Timer Rápido

```
/criar descricao: Pausa de 10 minutos emojis: 10
```

Apenas a opção de 10 minutos é mostrada.

### Exemplo 4: Evento com Múltiplas Opções

```
/criar descricao: Quando vocês podem? emojis: 10,20,30,40,60 imagem: https://exemplo.com/evento.jpg
```

Usuários votam em qual horário preferem.

---

## 🐛 Troubleshooting

### Imagem não aparece no timer

**Problema**: A imagem não é exibida na mensagem do timer.

**Solução**: Certifique-se de que a URL é válida e acessível. Tente usar uma URL direta de imagem.

### Lista de presença não atualiza

**Problema**: A lista de presença não mostra as novas reações.

**Solução**: A atualização acontece a cada 15 segundos. Aguarde um pouco. Se persistir, reinicie o bot.

### Emojis customizados não funcionam

**Problema**: Ao usar `emojis: 10,20`, apenas alguns emojis aparecem.

**Solução**: Certifique-se de que está usando os valores corretos: `10`, `20`, `30`, `40`, `60`, `cancelar`.

### Imagem de Goku não aparece na notificação

**Problema**: O timer expira mas a imagem não é enviada.

**Solução**: Certifique-se de que o arquivo `assets/goku_timer_end.jpg` existe e está no local correto.

---

## 📝 Notas Importantes

1. **Limite de Reações**: Discord permite até 20 reações diferentes por mensagem.
2. **Tamanho de Imagem**: Imagens muito grandes podem levar tempo para carregar.
3. **Persistência**: Os timers são armazenados em memória. Se o bot reiniciar, os timers ativos serão perdidos.
4. **Performance**: Com muitos timers simultâneos, a atualização pode levar alguns segundos.

---

**Aproveite as novas funcionalidades! 🎉**
