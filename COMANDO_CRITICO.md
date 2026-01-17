# 🎲 Comando `/crítico` - Sistema de Sorteio Crítico

## O que é?

O comando `/crítico` é um sistema de sorteio que simula um sistema de crítico em RPGs. Quando você executa o comando, o bot sorteia um número de 1 a 20 e exibe uma mensagem temática com um GIF/vídeo correspondente.

## Como usar?

Simplesmente digite o comando no Discord:

```
/crítico
```

O bot responderá com um embed contendo:
- O número sorteado (1-20)
- Uma mensagem temática baseada no resultado
- Um GIF ou vídeo relacionado ao resultado
- Informações sobre sequência de críticos (se aplicável)

## 🎯 Sistema de Sequência de Críticos

O bot rastreia sua sequência de críticos consecutivos. Quanto mais críticos você acertar seguidos, mais impressionantes ficam as mensagens!

### Fases do Sistema

**Fase 1: Base (Sem Sequência)**

Quando você não tem nenhum crítico consecutivo:

| Resultado | Mensagem | Tipo |
|-----------|----------|------|
| 1 | "É o seu fim." | Falha Crítica |
| 2-5 | "O teste falhou completamente. Nada saiu como o planejado." | Falha |
| 6-10 | "Você errou… mas admita: podia ter sido muito pior." | Falha |
| 11-16 | "Não foi dessa vez. O destino não se curvou ao seu golpe." | Falha |
| 17 | "Foi por pouco. Muito pouco. Mas ainda assim… falhou." | Falha |
| 18-19 | "Você sentiu o instante exato em que tudo se alinhou. Um crítico perfeito surge diante de você." | **Crítico** ✅ |
| 20 | "As chamas do destino ardem ao seu redor, guiando sua mão. Você atinge um perfeito absoluto." | **Crítico Perfeito** 🔥 |

**Fase 2: Segundo Crítico Consecutivo**

Quando você acerta 1 crítico e tenta o segundo:

| Resultado | Mensagem |
|-----------|----------|
| 1-16 | "Você havia acertado o primeiro crítico… mas o segundo escapou pelos seus dedos." |
| 17-19 | "De novo. Você fez de novo. O segundo crítico consecutivo ecoa como um trovão — você está esquentando." |
| 20 | "Nada pode conter o fluxo de poder à sua volta. Você atinge um crítico perfeito, transcendendo o impossível." |

**Fase 3: Terceiro Crítico Consecutivo**

Quando você acerta 2 críticos e tenta o terceiro:

| Resultado | Mensagem |
|-----------|----------|
| 1-14 | "Dois críticos impressionantes, mas na terceira tentativa, o brilho se apagou." |
| 15-19 | "O terceiro golpe crítico consecutivo rasga o silêncio. Agora já não é sorte, é domínio absoluto." |
| 20 | "Mais uma vez, perfeição pura. O terceiro crítico é perfeito faz o mundo tremer ao seu redor." |

**Fase 4 e 5: Quarto e Quinto Críticos Consecutivos**

O padrão continua, com os requisitos de sucesso ficando cada vez menores (mais fácil manter a sequência).

**Fase 6+: Críticos Ilimitados**

Após o quinto crítico consecutivo, o sistema continua indefinidamente, repetindo o padrão do quinto crítico mas atualizando o número (sexto, sétimo, oitavo, etc.).

## 📊 Tabela de Sequências

| Sequência | Requisito Mínimo para Acertar | Requisito para Crítico Perfeito |
|-----------|-------------------------------|--------------------------------|
| 1º Crítico | 18+ | 20 |
| 2º Crítico | 17+ | 20 |
| 3º Crítico | 15+ | 20 |
| 4º Crítico | 12+ | 20 |
| 5º+ Crítico | 11+ | 20 |

## 🔥 Exemplos de Uso

### Exemplo 1: Primeira Tentativa

```
/crítico
→ Você rolou um 19!
→ "Você sentiu o instante exato em que tudo se alinhou. Um crítico perfeito surge diante de você."
→ Sequência: 🔥 1º Crítico Consecutivo!
```

### Exemplo 2: Mantendo a Sequência

```
/crítico
→ Você rolou um 18!
→ "De novo. Você fez de novo. O segundo crítico consecutivo ecoa como um trovão — você está esquentando."
→ Sequência: 🔥 2º Crítico Consecutivo!
```

### Exemplo 3: Quebrando a Sequência

```
/crítico
→ Você rolou um 16!
→ "Você estava imparável, três críticos seguidos. Mas o quarto não veio. O destino decidiu cobrar seu preço."
→ Sequência Quebrada: A sequência de 3 críticos foi quebrada.
```

## 🎨 Características Visuais

Cada resultado é acompanhado por:
- **GIFs/Vídeos Temáticos**: Cenas de anime e ação que correspondem ao resultado
- **Cores de Embed**: Vermelho para críticos, azul para falhas
- **Informações de Sequência**: Mostra sua sequência atual de críticos

## 💡 Dicas

1. **Quanto mais críticos você acertar, mais fácil fica manter a sequência**: Após o 5º crítico, você só precisa de 11+ para acertar.

2. **Críticos Perfeitos (20) sempre contam**: Independentemente da sequência, um 20 sempre é um crítico perfeito.

3. **Sua sequência é rastreada por usuário**: Cada pessoa tem sua própria sequência independente.

4. **As sequências persistem enquanto o bot estiver online**: Se o bot reiniciar, as sequências são resetadas.

## 🎲 Probabilidades

| Resultado | Probabilidade | Tipo |
|-----------|---------------|------|
| 1 | 5% | Falha Crítica |
| 2-20 | 95% | Outros |
| 18-19 | 10% | Crítico (Fase 1) |
| 20 | 5% | Crítico Perfeito |

## 📝 Notas Importantes

- O sistema de sequência é **apenas para diversão** e não afeta nenhuma mecânica do servidor.
- Cada usuário tem sua própria sequência independente.
- As sequências são **resetadas quando o bot reinicia**.
- O comando está disponível para **todos os membros do servidor**.

---

**Divirta-se rolando críticos! 🎲✨**
