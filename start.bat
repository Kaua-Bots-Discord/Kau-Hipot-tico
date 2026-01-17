@echo off
title Kaua Bot V4 - Windows
echo ==========================================
echo    Iniciando Kaua Bot V4 no Windows
echo ==========================================
echo.

:: Verifica se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! Por favor, instale o Python e adicione ao PATH.
    pause
    exit /b
)

:: Verifica se o arquivo .env existe
if not exist .env (
    echo [AVISO] Arquivo .env nao encontrado!
    echo Criando um arquivo .env de exemplo...
    echo DISCORD_BOT_TOKEN=seu_token_aqui > .env
    echo [AVISO] Por favor, edite o arquivo .env e coloque seu token do Discord.
    pause
    exit /b
)

:: Instala as dependencias se necessario
echo Instalando/Atualizando dependencias...
python -m pip install -r requirements.txt

echo.
echo Iniciando o bot...
echo.
python bot.py

pause
