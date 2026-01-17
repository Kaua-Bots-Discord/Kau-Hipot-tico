# 🆕 Novas Funcionalidades - Kauã Hipotético

Este documento descreve as novas funcionalidades adicionadas ao bot Kauã Hipotético.

## 1️⃣ Sexta Opção: Emoji ❌ (Não vai responder este turno)

### O que é?

Adicionamos uma sexta opção de reação com o emoji **❌** que permite aos usuários indicar que **não vão responder neste turno** ou que desejam **cancelar sua participação**.

### Como usar?

Ao ver uma mensagem de timer criada, você pode reagir com **❌** para indicar que não vai participar. O bot confirmará sua escolha com uma mensagem na DM.

### Exemplos de uso:

- **Sessão de Jogo**: Você está ocupado e não pode jogar neste turno
- **Reunião**: Você não pode participar neste momento
- **Pausa**: Você precisa fazer uma pausa e não quer ser notificado

---

## 2️⃣ Notificação no Canal (além da DM)

### O que é?

Agora, quando um timer expira, o bot **notifica não apenas a DM do usuário**, mas também **envia uma mensagem no canal de origem** onde o timer foi criado.

### Como funciona?

1. Você cria um timer com `/criar descricao: Pausa para café`
2. Você reage com ⏱️ (10 minutos)
3. Após 10 minutos, você recebe:
   - Uma **DM privada** do bot com a notificação
   - Uma **mensagem no canal** mencionando você e informando que o timer expirou

### Benefícios:

- **Visibilidade**: Todos no servidor veem quando os timers expiram
- **Rastreabilidade**: Há um registro no canal de quem foi notificado e quando
- **Redundância**: Se a DM falhar, você ainda será notificado no canal

### Exemplo de mensagem no canal:

```
@Usuario, seu timer de 10 minutos acabou!
```

---

## 3️⃣ Visualização de Usuários por Reação

### O que é?

A mensagem do timer agora é **atualizada automaticamente a cada 30 segundos** para mostrar **quais usuários reagiram a cada opção**.

### Como funciona?

1. Você cria um timer com `/criar descricao: Votação`
2. O embed mostra:
   ```
   ⏱️ 10 minutos
   Usuários: @Alice, @Bob, @Charlie
   
   ⏲️ 20 minutos
   Usuários: @Diana, @Eve
   
   ⌛ 30 minutos
   Usuários: Ninguém reagiu ainda.
   ```

3. Conforme mais pessoas reagem, a lista é atualizada automaticamente

### Benefícios:

- **Transparência**: Todos veem quem escolheu qual opção
- **Monitoramento**: Você pode acompanhar as escolhas em tempo real
- **Votação**: Perfeito para votações e decisões em grupo

### Atualização automática:

O bot atualiza o embed a cada **30 segundos** para refletir as reações mais recentes. Isso garante que as informações estejam sempre atualizadas sem sobrecarregar o servidor.

---

## 4️⃣ Múltiplos Timers no Mesmo Embed

### O que é?

Agora você pode **criar múltiplos timers** usando o mesmo embed, sem precisar criar mensagens separadas.

### Como funciona?

1. Você cria um timer com `/criar descricao: Votação de Atividade`
2. Vários usuários reagem a diferentes emojis
3. Cada reação cria um timer **independente** para aquele usuário
4. O embed mostra **todos os timers e quem reagiu a cada um**

### Exemplo prático:

```
⏱️ 10 minutos
Usuários: @Alice, @Bob

⏲️ 20 minutos
Usuários: @Charlie

⌛ 30 minutos
Usuários: @Diana, @Eve

⏰ 40 minutos
Usuários: Ninguém reagiu ainda.

🕐 1 hora
Usuários: @Frank

❌ Não vai responder
Usuários: @Grace
```

Cada usuário tem seu próprio timer independente, mas todos são gerenciados no mesmo embed.

### Benefícios:

- **Eficiência**: Uma única mensagem para múltiplos timers
- **Organização**: Tudo em um único lugar
- **Escalabilidade**: Suporta muitos usuários simultaneamente

---

## 📊 Comparação: Antes vs Depois

| Funcionalidade | Antes | Depois |
|---|---|---|
| Opções de Timer | 5 emojis | 6 emojis (+ ❌) |
| Notificação | Apenas DM | DM + Canal |
| Visualização de Reações | Não | Sim (atualizado a cada 30s) |
| Múltiplos Timers | Não | Sim (no mesmo embed) |
| Opção de Cancelamento | Não | Sim (❌) |

---

## 🔧 Configuração Técnica

### Intents Necessários

Para que a visualização de usuários funcione, certifique-se de que a seguinte intent está ativada no Discord Developer Portal:

- **Server Members Intent**: Permite ao bot buscar a lista de membros que reagiram

### Atualização Automática do Embed

A tarefa `update_timer_message` executa a cada 30 segundos e:

1. Busca todas as mensagens de timer ativas
2. Obtém as reações de cada mensagem
3. Lista os usuários que reagiram a cada emoji
4. Atualiza o embed com as informações mais recentes

### Armazenamento de Dados

O bot mantém dois dicionários em memória:

- **`active_user_timers`**: Armazena os timers individuais de cada usuário
- **`active_timer_messages`**: Armazena as informações das mensagens de timer para atualização

---

## 🚀 Exemplos de Uso Avançado

### Exemplo 1: Votação em Grupo

```
/criar descricao: Qual atividade fazer? (10m = Jogo, 20m = Filme, 30m = Conversa, ❌ = Não participo)
```

Todos reagem e veem em tempo real quem escolheu o quê.

### Exemplo 2: Pausa em Sessão de Trabalho

```
/criar descricao: Pausa de 15 minutos (10m = Café, 20m = Exercício, ❌ = Continuo trabalhando)
```

O gerente vê quem vai fazer pausa e quem continua.

### Exemplo 3: Disponibilidade para Reunião

```
/criar descricao: Reunião em 30 minutos (10m = Vou chegar cedo, 30m = Vou na hora, ❌ = Não consigo)
```

Todos sabem quem vai estar disponível e quando.

---

## ⚙️ Configuração Personalizada

### Modificar o Intervalo de Atualização

No arquivo `bot.py`, procure por:

```python
@tasks.loop(seconds=30)
async def update_timer_message():
```

Altere o valor `30` para o intervalo desejado em segundos. Por exemplo, `60` para atualizar a cada minuto.

### Adicionar Mais Emojis

Edite os dicionários `TIMER_EMOJIS` e `EMOJI_DESCRIPTIONS`:

```python
TIMER_EMOJIS = {
    "⏱️": 10,
    "⏲️": 20,
    "⌛": 30,
    "⏰": 40,
    "🕐": 60,
    "❌": 0,
    "🎮": 15,  # Novo emoji
}

EMOJI_DESCRIPTIONS = {
    "⏱️": "10 minutos",
    "⏲️": "20 minutos",
    "⌛": "30 minutos",
    "⏰": "40 minutos",
    "🕐": "1 hora",
    "❌": "Não vai responder este turno / Cancelar",
    "🎮": "15 minutos - Jogo",  # Descrição do novo emoji
}
```

---

## 🐛 Troubleshooting

### Não vejo quem reagiu

**Problema**: O embed não mostra os usuários que reagiram.

**Solução**: Certifique-se de que a **Server Members Intent** está ativada no Discord Developer Portal.

### Notificação não chega no canal

**Problema**: O timer expira mas não há mensagem no canal.

**Solução**: Verifique se o bot tem permissão para enviar mensagens no canal.

### Embed não atualiza

**Problema**: A lista de usuários não muda mesmo após novas reações.

**Solução**: A atualização acontece a cada 30 segundos. Aguarde um pouco. Se persistir, reinicie o bot.

---

## 📝 Notas Importantes

1. **Timezone**: O bot usa o timezone local do servidor para calcular os timers.
2. **Persistência**: Os timers são armazenados em memória. Se o bot reiniciar, os timers ativos serão perdidos.
3. **Performance**: Com muitos timers simultâneos, a atualização do embed pode levar alguns segundos.
4. **Limite de Reações**: Discord permite até 20 reações diferentes por mensagem, então você pode ter até 20 emojis diferentes.

---

**Aproveite as novas funcionalidades! 🎉**
