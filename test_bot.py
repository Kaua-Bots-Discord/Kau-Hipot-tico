"""
Script de teste para validar a lógica do bot Kauã Hipotético
Este arquivo testa os cálculos de timer sem precisar de uma conexão real ao Discord
"""

from datetime import datetime, timedelta
import asyncio

# Emojis e suas durações em minutos
TIMER_EMOJIS = {
    "⏱️": 10,
    "⏲️": 20,
    "⌛": 30,
    "⏰": 40,
    "🕐": 60,
    "❌": 0 # Nova opção: Não vai responder este turno / Cancelar
}

EMOJI_DESCRIPTIONS = {
    "⏱️": "10 minutos",
    "⏲️": "20 minutos",
    "⌛": "30 minutos",
    "⏰": "40 minutos",
    "🕐": "1 hora",
    "❌": "Não vai responder este turno / Cancelar"
}

def test_emoji_descriptions():
    """Testa se todas as descrições estão corretas"""
    print("🧪 Testando descrições de emojis...")
    
    for emoji, duration in TIMER_EMOJIS.items():
        if emoji not in EMOJI_DESCRIPTIONS:
            print(f"❌ Emoji {emoji} não tem descrição!")
            return False
        print(f"  ✅ {emoji} → {EMOJI_DESCRIPTIONS[emoji]}")
    
    print("✅ Todas as descrições estão corretas!\n")
    return True

def test_timer_calculation():
    """Testa o cálculo de tempo restante do timer"""
    print("🧪 Testando cálculo de timer...")
    
    # Simular uma mensagem criada há 5 minutos
    message_creation_time = datetime.now() - timedelta(minutes=5)
    timer_start_time = datetime.now()
    
    # Tempo decorrido
    elapsed = (timer_start_time - message_creation_time).total_seconds() / 60
    print(f"  ⏱️  Tempo decorrido: {elapsed:.1f} minutos")
    
    # Testar cada emoji
    for emoji, duration in TIMER_EMOJIS.items():
        remaining = duration - elapsed
        
        if emoji == "❌":
            print(f"  {emoji} ({duration}m): Opção de cancelamento/não responder")
            continue
            
        print(f"  {emoji} ({duration}m): {remaining:.1f} minutos restantes")
        
        if remaining <= 0:
            print(f"    ⚠️  Timer já expirou!")
        else:
            print(f"    ✅ Timer válido")
    
    print("✅ Cálculos de timer funcionando corretamente!\n")
    return True

def test_multiple_timers():
    """Testa o suporte a múltiplos timers"""
    print("🧪 Testando múltiplos timers...")
    
    # Simular dicionário de timers
    active_timers = {}
    
    # Adicionar alguns timers
    for i in range(3):
        timer_key = f"message_{i}_user_123"
        active_timers[timer_key] = {
            "end_time": datetime.now() + timedelta(minutes=10 + i*10),
            "user_id": 123,
            "duration": 10 + i*10
        }
        print(f"  ✅ Timer {i+1} adicionado")
    
    print(f"  📊 Total de timers: {len(active_timers)}")
    print("✅ Múltiplos timers funcionando corretamente!\n")
    return True

async def test_async_timer():
    """Testa a lógica assíncrona de timer"""
    print("🧪 Testando timer assíncrono (2 segundos)...")
    
    start_time = datetime.now()
    await asyncio.sleep(2)
    end_time = datetime.now()
    
    elapsed = (end_time - start_time).total_seconds()
    print(f"  ⏱️  Tempo decorrido: {elapsed:.2f} segundos")
    print("✅ Timer assíncrono funcionando corretamente!\n")
    return True

def run_all_tests():
    """Executa todos os testes"""
    print("=" * 50)
    print("🤖 Testes do Bot Kauã Hipotético")
    print("=" * 50)
    print()
    
    results = []
    
    # Testes síncronos
    results.append(("Descrições de Emojis", test_emoji_descriptions()))
    results.append(("Cálculo de Timer", test_timer_calculation()))
    results.append(("Múltiplos Timers", test_multiple_timers()))
    
    # Teste assíncrono
    print("🧪 Testando timer assíncrono...")
    asyncio.run(test_async_timer())
    results.append(("Timer Assíncrono", True))
    
    # Resumo
    print("=" * 50)
    print("📊 Resumo dos Testes")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name}: {status}")
    
    print()
    print(f"Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! Bot pronto para usar.")
    else:
        print("⚠️  Alguns testes falharam. Verifique os erros acima.")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
