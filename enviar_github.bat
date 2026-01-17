@echo off
title Enviar para o GitHub
echo ==========================================
echo    Enviando Kaua Bot V4 para o GitHub
echo ==========================================
echo.

:: Verifica se o Git esta instalado
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Git nao encontrado! Por favor, instale o Git: https://git-scm.com/
    pause
    exit /b
)

set /p repo_url="Cole a URL do seu repositorio do GitHub (ex: https://github.com/usuario/repositorio.git): "

if "%repo_url%"=="" (
    echo [ERRO] URL do repositorio nao pode ser vazia.
    pause
    exit /b
)

echo.
echo Inicializando repositorio local...
git init

echo.
echo Adicionando arquivos...
git add .

echo.
echo Criando primeiro commit...
git commit -m "Initial commit: Kaua Bot V4 com sistema de criticos corrigido"

echo.
echo Configurando branch principal...
git branch -M main

echo.
echo Conectando ao repositorio remoto...
git remote add origin %repo_url%

echo.
echo Enviando arquivos (pode ser solicitado login)...
git push -u origin main

echo.
echo ==========================================
echo    Processo concluido! Verifique seu GitHub.
echo ==========================================
pause
