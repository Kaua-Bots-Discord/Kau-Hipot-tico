# 📚 Guia Completo de Setup - Kauã Hipotético

Este guia passo a passo ajudará você a configurar o bot Kauã Hipotético no Discord.

## Passo 1: Criar uma Aplicação no Discord Developer Portal

1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Faça login com sua conta Discord
3. Clique no botão **"New Application"** (canto superior direito)
4. Digite o nome: **Kauã Hipotético**
5. Aceite os termos e clique em **"Create"**

## Passo 2: Configurar o Bot

1. Na página da aplicação, clique na aba **"Bot"** (menu esquerdo)
2. Clique em **"Add Bot"**
3. Você verá a seção "TOKEN" - clique em **"Copy"** para copiar o token
4. **⚠️ Guarde este token em um local seguro** - você precisará dele

## Passo 3: Ativar Intents Necessários

Ainda na aba "Bot", role para baixo até a seção **"GATEWAY INTENTS"** e ative:

- ✅ **PRESENCE INTENT**
- ✅ **SERVER MEMBERS INTENT**
- ✅ **MESSAGE CONTENT INTENT**

Clique em **"Save Changes"**

## Passo 4: Configurar Permissões

1. Vá para a aba **"OAuth2"** (menu esquerdo)
2. Clique em **"URL Generator"** (sub-menu)

### Selecione os Scopes:
- ✅ `bot`

### Selecione as Permissões:
- ✅ Send Messages
- ✅ Embed Links
- ✅ Add Reactions
- ✅ Read Messages/View Channels
- ✅ Read Message History
- ✅ Manage Messages

3. Uma URL será gerada no final da página
4. Copie essa URL e abra em seu navegador
5. Selecione o servidor onde deseja adicionar o bot
6. Clique em **"Authorize"**

## Passo 5: Configurar o Arquivo .env

1. Abra o arquivo `.env` na pasta do projeto
2. Substitua `seu_token_aqui` pelo token que você copiou no Passo 2:

```
DISCORD_BOT_TOKEN=seu_token_copiado_aqui
```

3. Salve o arquivo

## Passo 6: Instalar Dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

## Passo 7: Executar o Bot

### Opção 1: Usando o script de inicialização

```bash
./start.sh
```

### Opção 2: Executar diretamente

```bash
python bot.py
```

Você deverá ver:
```
✅ Bot Kauã Hipotético#0000 conectado com sucesso!
✅ 3 comando(s) sincronizado(s)
```

## Passo 8: Testar o Bot

1. Vá para um canal de texto no seu servidor Discord
2. Digite `/criar` e pressione Enter
3. Você verá as opções de comando
4. Complete com uma descrição (ex: "Pausa para café")
5. Pressione Enter para executar

O bot enviará uma mensagem com os emojis de timer!

## 🎨 Configurar Foto de Perfil (Opcional)

1. Volte ao [Discord Developer Portal](https://discord.com/developers/applications)
2. Selecione sua aplicação "Kauã Hipotético"
3. Na aba "General Information", procure por "APP ICON"
4. Clique em "Upload Image"
5. Selecione o arquivo `assets/kaua_profile.jpg`
6. Clique em "Save Changes"

O avatar do bot será atualizado em breve no Discord.

## ✅ Checklist Final

- [ ] Aplicação criada no Developer Portal
- [ ] Bot adicionado à aplicação
- [ ] Intents ativados
- [ ] Permissões configuradas
- [ ] Bot adicionado ao servidor
- [ ] Token configurado no arquivo `.env`
- [ ] Dependências instaladas
- [ ] Bot iniciado com sucesso
- [ ] Comandos funcionando

## 🆘 Problemas Comuns

### "Bot não aparece no servidor"
- Verifique se você clicou em "Authorize" na URL do OAuth2
- Certifique-se de que tem permissão para adicionar bots ao servidor

### "Comando não aparece"
- Reinicie o bot
- Aguarde alguns minutos para sincronização
- Verifique se o bot tem permissão para enviar mensagens

### "Token inválido"
- Copie o token novamente do Developer Portal
- Certifique-se de que não há espaços em branco
- Não compartilhe seu token com ninguém

### "Intents não ativados"
- Volte ao Developer Portal
- Aba "Bot" → "GATEWAY INTENTS"
- Ative os três intents mencionados acima

## 📞 Suporte

Para mais informações:
- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Documentation](https://discord.com/developers/docs)

---

**Pronto para usar! 🚀**
