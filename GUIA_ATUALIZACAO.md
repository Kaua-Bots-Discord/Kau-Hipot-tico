# 📚 Guia de Atualização do Código - Kauã Hipotético

Este guia explica como atualizar o código do bot Kauã Hipotético em sua máquina local.

## 🔄 Processo de Atualização

### Opção 1: Substituição Simples (Recomendado)

Se você já tem o bot funcionando e deseja atualizar para a versão mais recente:

#### Passo 1: Fazer Backup

Antes de qualquer coisa, faça um backup do seu arquivo `.env` (que contém seu token):

```bash
cp /caminho/para/seu/kaua_bot/.env /caminho/para/backup/.env.backup
```

#### Passo 2: Baixar a Nova Versão

Baixe o arquivo ZIP mais recente (`kaua_bot_v3.zip` ou a versão atual).

#### Passo 3: Descompactar

Descompacte o arquivo ZIP em um local temporário:

```bash
unzip kaua_bot_v3.zip -d /caminho/temporario/
```

#### Passo 4: Substituir os Arquivos

Copie os novos arquivos para sua pasta do projeto, **exceto o arquivo `.env`**:

```bash
# Copiar o novo bot.py
cp /caminho/temporario/kaua_bot/bot.py /seu/projeto/kaua_bot/bot.py

# Copiar o novo README.md
cp /caminho/temporario/kaua_bot/README.md /seu/projeto/kaua_bot/README.md

# Copiar outros arquivos de documentação
cp /caminho/temporario/kaua_bot/*.md /seu/projeto/kaua_bot/

# Copiar a nova imagem de notificação
cp /caminho/temporario/kaua_bot/assets/goku_timer_end.jpg /seu/projeto/kaua_bot/assets/
```

#### Passo 5: Atualizar Dependências

Se houver novas dependências, atualize-as:

```bash
cd /seu/projeto/kaua_bot
pip install -r requirements.txt
```

#### Passo 6: Reiniciar o Bot

Pare o bot atual (Ctrl+C) e reinicie:

```bash
python bot.py
```

### Opção 2: Atualização Manual (Para Usuários Avançados)

Se você fez modificações personalizadas no código e deseja mesclar as atualizações:

#### Passo 1: Comparar Versões

Use uma ferramenta de comparação de código (como `diff` no Linux/Mac ou `fc` no Windows) para ver as diferenças:

```bash
diff /seu/projeto/kaua_bot/bot.py /caminho/temporario/kaua_bot/bot.py
```

#### Passo 2: Aplicar Mudanças Seletivas

Abra ambos os arquivos em um editor de texto e aplique manualmente as mudanças que deseja manter.

#### Passo 3: Testar

Execute os testes para garantir que tudo funciona:

```bash
python test_bot.py
```

## 📋 Checklist de Atualização

Após atualizar, verifique:

- [ ] Arquivo `.env` ainda contém seu token
- [ ] Arquivo `bot.py` foi substituído pela nova versão
- [ ] Arquivo `requirements.txt` foi atualizado
- [ ] Dependências foram instaladas (`pip install -r requirements.txt`)
- [ ] Imagem `goku_timer_end.jpg` está em `assets/`
- [ ] Bot inicia sem erros (`python bot.py`)
- [ ] Comandos `/criar`, `/presente`, `/timers` e `/cancelar` funcionam

## 🆕 Novas Funcionalidades na v3

A versão 3 do bot inclui:

1. **Seleção Dinâmica de Emojis**: Escolha quais timers usar no comando `/criar`
2. **Suporte a Imagens**: Envie uma imagem junto com o timer
3. **Imagem de Notificação**: Receba uma imagem do Goku quando o timer expira
4. **Comando `/presente`**: Crie listas de presença com reações

### Exemplos de Uso das Novas Funcionalidades

#### Usar Apenas Alguns Emojis

```
/criar descricao: Votação emojis: 10,20 imagem: https://exemplo.com/imagem.jpg
```

Isso criará um timer com apenas os emojis de 10 e 20 minutos.

#### Criar Lista de Presença

```
/presente descricao: Presença na reunião de hoje
```

Todos que reagirem com ✅ aparecerão na lista.

## 🐛 Troubleshooting

### "Erro: módulo não encontrado"

Se você receber um erro como `ModuleNotFoundError: No module named 'discord'`, reinstale as dependências:

```bash
pip install -r requirements.txt
```

### "Bot não inicia"

Verifique se:
1. O token no arquivo `.env` está correto
2. O arquivo `bot.py` não tem erros de sintaxe
3. As dependências foram instaladas

Execute:

```bash
python -m py_compile bot.py
```

Se não houver erro, a sintaxe está correta.

### "Imagem não aparece na notificação"

Certifique-se de que o arquivo `goku_timer_end.jpg` existe em `assets/`:

```bash
ls -la assets/goku_timer_end.jpg
```

Se não existir, baixe-o novamente ou copie-o do arquivo ZIP.

## 📝 Mantendo Suas Personalizações

Se você fez modificações no código, aqui está como manter suas mudanças durante a atualização:

### Passo 1: Identificar Suas Mudanças

Anote quais partes do código você modificou (ex: cores dos embeds, mensagens personalizadas, etc.).

### Passo 2: Criar um Arquivo de Patch

Crie um arquivo separado com suas personalizações:

```python
# meus_customizacoes.py
CORES_PERSONALIZADAS = {
    "timer": 0xFF5733,  # Cor vermelha personalizada
    "presenca": 0x33FF57  # Cor verde personalizada
}

MENSAGENS_PERSONALIZADAS = {
    "timer_iniciado": "⏱️ Seu timer começou!",
    "timer_finalizado": "⏰ Tempo acabou!"
}
```

### Passo 3: Aplicar Personalizações

Após atualizar, reaplique suas personalizações ao novo código.

## 🔐 Segurança

**Nunca** compartilhe seu arquivo `.env` ou seu token com ninguém. Ao fazer backup ou compartilhar código, sempre remova o token.

Para remover o token de um arquivo antes de compartilhar:

```bash
sed 's/DISCORD_BOT_TOKEN=.*/DISCORD_BOT_TOKEN=seu_token_aqui/' .env > .env.public
```

## 📞 Suporte

Se tiver problemas durante a atualização:

1. Consulte o arquivo `README.md` para instruções gerais
2. Verifique o arquivo `NOVAS_FUNCIONALIDADES.md` para entender as mudanças
3. Consulte a documentação do [discord.py](https://discordpy.readthedocs.io/)

---

**Atualização concluída com sucesso! 🎉**
