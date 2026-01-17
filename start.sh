#!/bin/bash

# Script para iniciar o bot Kauã Hipotético

echo "🤖 Iniciando Kauã Hipotético..."
echo ""

# Verificar se o arquivo .env existe
if [ ! -f .env ]; then
    echo "❌ Erro: Arquivo .env não encontrado!"
    echo "📋 Criando .env a partir do exemplo..."
    cp .env.example .env
    echo "⚠️  Configure seu DISCORD_BOT_TOKEN no arquivo .env"
    exit 1
fi

# Verificar se o token foi configurado
if grep -q "seu_token_aqui" .env; then
    echo "❌ Erro: DISCORD_BOT_TOKEN ainda não foi configurado!"
    echo "📋 Edite o arquivo .env e adicione seu token"
    exit 1
fi

# Carregar variáveis de ambiente
export $(cat .env | xargs)

# Verificar se as dependências estão instaladas
echo "📦 Verificando dependências..."
pip install -q -r requirements.txt

echo ""
echo "✅ Iniciando o bot..."
echo "🔗 Pressione Ctrl+C para parar"
echo ""

python bot.py
