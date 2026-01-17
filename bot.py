import discord
from discord.ext import commands, tasks
from discord import app_commands
import asyncio
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import random
print("🚀 Bot iniciando no Railway") 

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Dicionários para armazenar dados
active_user_timers = {}
active_timer_messages = {}
active_presence_messages = {}
user_crit_streak = {} # {user_id: {"streak": 0, "last_roll": 0, "perfect_count": 0}}

# Emojis e suas durações em minutos
TIMER_EMOJIS = {
    "⏱️": 10,
    "⏲️": 20,
    "⌛": 30,
    "⏰": 40,
    "🕐": 60,
    "❌": 0
}

EMOJI_DESCRIPTIONS = {
    "⏱️": "10 minutos",
    "⏲️": "20 minutos",
    "⌛": "30 minutos",
    "⏰": "40 minutos",
    "🕐": "1 hora",
    "❌": "Não vai responder este turno / Cancelar"
}

# Caminho para a imagem de notificação (apenas para DM)
GOKU_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "assets", "goku_timer_end.jpg")

# --- Dados do Comando /crítico ---
CRIT_DATA = {
    # Base (Streak 0)
    0: {
        1: ("É o seu fim.", "https://c.tenor.com/0EERvw7z2aEAAAAd/tenor.gif"),
        (2, 5): ("O teste falhou completamente. Nada saiu como o planejado.", "https://i.pinimg.com/originals/3a/b7/19/3ab71952c94481683f397b533c2f0820.gif"),
        (6, 10): ("Você errou… mas admita: podia ter sido muito pior.", "https://i.pinimg.com/originals/36/05/31/36053168f906146ecca193c762417f63.gif"),
        (11, 16): ("Não foi dessa vez. O destino não se curvou ao seu golpe.", "https://i.pinimg.com/originals/56/33/0f/56330f99dc697e0cb5b8a288de9e3912.gif"),
        17: ("Foi por pouco. Muito pouco. Mas ainda assim… falhou.", "https://i.pinimg.com/originals/88/46/ea/8846eaf78dec660c7b8524dbda463d3a.gif"),
        (18, 19): ("Você sentiu o instante exato em que tudo se alinhou. Um crítico perfeito surge diante de você.", "https://i.pinimg.com/originals/5e/47/8a/5e478a0f48d4798c7df3a12a23988e4b.gif"),
        20: ("As chamas do destino ardem ao seu redor, guiando sua mão. Você atinge um perfeito absoluto.", "https://i.pinimg.com/originals/f2/12/83/f21283042ce025fb4fbcc67813bc792a.gif"),
    },
    # Streak 1 (Tentando o 2º crítico)
    1: {
        (1, 16): ("", "https://i.pinimg.com/1200x/94/66/50/94665094581145ec6ad9584ea40ed758.jpg"),
        (17, 19): ("De novo. Você fez de novo. O segundo crítico consecutivo ecoa como um trovão — você está esquentando.", "https://i.pinimg.com/originals/74/cb/d3/74cbd301f3babfda58f3c822c4d127e4.gif"),
        20: ("Nada pode conter o fluxo de poder à sua volta. Você atinge um crítico perfeito, transcendendo o impossível.", "https://i.pinimg.com/originals/73/4a/eb/734aebc14d9a69fc0c4582ec82375506.gif"),
    },
    # Streak 2 (Tentando o 3º crítico)
    2: {
        (1, 14): ("Dois críticos impressionantes, mas na terceira tentativa, o brilho se apagou.", "https://i.pinimg.com/736x/e1/05/e5/e105e553c998f035cb7812dd60a09290.jpg"),
        (15, 19): ("O terceiro golpe crítico consecutivo rasga o silêncio. Agora já não é sorte, é domínio absoluto.", "https://c.tenor.com/sFoO37BKxlgAAAAd/tenor.gif"),
        20: ("Mais uma vez, perfeição pura. O terceiro crítico é perfeito faz o mundo tremer ao seu redor.", "https://c.tenor.com/FILnhw_rozUAAAAd/tenor.gif"),
    },
    # Streak 3 (Tentando o 4º crítico)
    3: {
        (1, 11): ("Você estava imparável, três críticos seguidos. Mas o quarto não veio. O destino decidiu cobrar seu preço.", "https://i.pinimg.com/736x/85/15/de/8515deea342342feeb33c36a61b6e6a7.jpg"),
        (12, 19): ("O quarto crítico consecutivo é simplesmente impressionante. Você acaba de estabelecer um novo recorde.", "https://i.pinimg.com/originals/2a/20/73/2a2073496e77970cbcacf686cc2383e6.gif"),
        20: ("Um quarto crítico perfeito consecutivo. Perfeição absoluta, incontestável — um feito digno de ser registrado em crônicas.", "https://i.pinimg.com/originals/f2/12/83/f21283042ce025fb4fbcc67813bc792a.gif"),
    },
    # Streak 4 (Tentando o 5º crítico)
    4: {
        (1, 10): ("Quatro críticos consecutivos… algo lendário. Mas ao buscar o quinto, o destino finalmente disse 'não'.", "https://i.pinimg.com/736x/ea/6b/16/ea6b1690c002debcd6ed817a77283d8c.jpg"),
        (11, 19): ("Cinco críticos consecutivos. Inacreditável. Sua lenda se escreve sozinha enquanto você avança.", "https://c.tenor.com/L9gZo3fb2YQAAAAd/tenor.gif"),
        20: ("O quinto crítico perfeito consecutivo explode, você é um monstro.", "https://i.pinimg.com/originals/0d/e4/2a/0de42aea0739dfe7dd3aa0f45277347c.gif"),
    },
}

# Textos extras para múltiplos críticos perfeitos consecutivos
PERFECT_STREAK_TEXTS = {
    2: ("Dois críticos perfeitos seguidos… é como se os céus observassem cada gesto seu. Algo grandioso desperta em você.", "https://i.pinimg.com/originals/96/a4/f0/96a4f01690e1c5be2fb8db2ecd0e7c45.gif"),
    3: ("Três críticos perfeitos seguidos… nenhum guerreiro comum alcança isso. Você pisa no território dos lendários.", "https://i.pinimg.com/originals/13/9b/5b/139b5bbe1665f8390006105e5fcfe8c9.gif"),
}

# --- Funções Auxiliares ---

def get_crit_result(roll: int, streak: int, perfect_count: int) -> tuple:
    """Retorna o texto e o GIF/URL para o resultado do crítico."""
    
    # Lógica para streaks acima de 4 (repetir o texto do 5º, substituindo o número)
    if streak >= 5:
        # Lógica de falha
        if roll <= 10:
            ordinal = get_ordinal(streak + 1)
            text = f"{streak} críticos consecutivos… algo lendário. Mas ao buscar o {ordinal}, o destino finalmente disse 'não'."
            gif = "https://i.pinimg.com/736x/ea/6b/16/ea6b1690c002debcd6ed817a77283d8c.jpg"
            return text, gif, False, 0
        # Lógica de acerto comum
        elif roll <= 19:
            ordinal = get_ordinal(streak + 1)
            text = f"{ordinal.capitalize()} críticos consecutivos. Inacreditável. Sua lenda se escreve sozinha enquanto você avança."
            gif = "https://c.tenor.com/L9gZo3fb2YQAAAAd/tenor.gif"
            return text, gif, True, 0
        # Lógica de 20
        else:
            ordinal = get_ordinal(streak + 1)
            text = f"O {ordinal} crítico perfeito consecutivo explode, você é um monstro."
            gif = "https://i.pinimg.com/originals/0d/e4/2a/0de42aea0739dfe7dd3aa0f45277347c.gif"
            return text, gif, True, 1
    
    # Lógica para streaks 0 a 4
    data = CRIT_DATA.get(streak, CRIT_DATA[0])
    
    for key, (text, gif) in data.items():
        if isinstance(key, tuple):
            if key[0] <= roll <= key[1]:
                # Determinar se é crítico
                if streak == 0:
                    is_crit = roll >= 18
                elif streak == 1:
                    is_crit = roll >= 17
                elif streak == 2:
                    is_crit = roll >= 15
                elif streak == 3:
                    is_crit = roll >= 12
                elif streak == 4:
                    is_crit = roll >= 11
                else:
                    is_crit = roll >= 11
                
                is_perfect = roll == 20
                
                # Verificar se precisa de texto extra para múltiplos perfeitos
                if is_perfect and perfect_count > 0 and streak > 0:
                    extra_text, extra_gif = get_perfect_streak_text(perfect_count + 1, streak)
                    if extra_text:
                        return extra_text, extra_gif, is_crit, 1
                
                return text, gif, is_crit, 1 if is_perfect else 0
        elif key == roll:
            # Determinar se é crítico para valores exatos
            if streak == 0:
                is_crit = roll >= 18
            elif streak == 1:
                is_crit = roll >= 17
            elif streak == 2:
                is_crit = roll >= 15
            elif streak == 3:
                is_crit = roll >= 12
            elif streak == 4:
                is_crit = roll >= 11
            else:
                is_crit = roll >= 11
                
            is_perfect = roll == 20
            
            # Verificar se precisa de texto extra para múltiplos perfeitos
            if is_perfect and perfect_count > 0 and streak > 0:
                extra_text, extra_gif = get_perfect_streak_text(perfect_count + 1, streak)
                if extra_text:
                    return extra_text, extra_gif, is_crit, 1
            
            return text, gif, is_crit, 1 if is_perfect else 0
            
    # Fallback (não deve acontecer)
    return "Resultado desconhecido.", "https://c.tenor.com/0EERvw7z2aEAAAAd/tenor.gif", False, 0

def get_perfect_streak_text(perfect_count: int, streak: int) -> tuple:
    """Retorna texto extra para múltiplos críticos perfeitos consecutivos."""
    if perfect_count in PERFECT_STREAK_TEXTS:
        return PERFECT_STREAK_TEXTS[perfect_count]
    return None, None

def get_ordinal(n: int) -> str:
    """Retorna o número ordinal em português."""
    ordinals = {
        1: "primeiro", 2: "segundo", 3: "terceiro", 4: "quarto", 5: "quinto",
        6: "sexto", 7: "sétimo", 8: "oitavo", 9: "nono", 10: "décimo",
        11: "décimo primeiro", 12: "décimo segundo", 13: "décimo terceiro",
        14: "décimo quarto", 15: "décimo quinto"
    }
    return ordinals.get(n, f"{n}º")

# --- Eventos ---

@bot.event
async def on_ready():
    """Evento disparado quando o bot está pronto"""
    print(f"✅ Bot {bot.user} conectado com sucesso!")
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} comando(s) sincronizado(s)")
    except Exception as e:
        print(f"❌ Erro ao sincronizar comandos: {e}")
    
    update_timer_message.start()
    update_presence_message.start()

# --- Comandos ---

@bot.tree.command(name="criar", description="Cria um timer com opções de duração customizáveis")
@app_commands.default_permissions(administrator=True) # Restrição para Administradores
@app_commands.describe(
    descricao="Descrição do timer (ex: Pausa para café)",
    emojis="Emojis a usar (ex: 10,20 para usar apenas 10 e 20 minutos)",
    imagem="URL da imagem a enviar junto com o timer (opcional)"
)
async def criar_timer(
    interaction: discord.Interaction, 
    descricao: str = "Timer",
    emojis: str = "10,20,30,40,60,cancelar",
    imagem: str = None
):
    """Comando slash para criar um timer com emojis customizáveis"""
    
    emoji_keys = parse_emoji_selection(emojis)
    
    if not emoji_keys:
        await interaction.response.send_message(
            "❌ Opções de emojis inválidas! Use: 10, 20, 30, 40, 60 ou cancelar",
            ephemeral=True
        )
        return
    
    # Criar embed inicial
    embed = discord.Embed(
        title="⏱️ Timer Criado",
        description=descricao,
        color=discord.Color.blue(),
        timestamp=datetime.now()
    )
    
    embed.set_footer(text=f"Criado por {interaction.user.name}")
    
    # Adicionar imagem se fornecida
    if imagem:
        embed.set_image(url=imagem)
    
    await interaction.response.send_message(embed=embed)
    message = await interaction.original_response()
    
    active_timer_messages[message.id] = {
        "channel_id": message.channel.id,
        "description": descricao,
        "creator_id": interaction.user.id,
        "creation_time": message.created_at,
        "emoji_keys": emoji_keys,
        "image_url": imagem
    }
    
    for emoji_key in emoji_keys:
        try:
            await message.add_reaction(emoji_key)
        except Exception as e:
            print(f"❌ Erro ao adicionar reação {emoji_key}: {e}")

@bot.tree.command(name="presente", description="Cria uma lista de presença com reações")
@app_commands.default_permissions(administrator=True) # Restrição para Administradores
@app_commands.describe(
    descricao="Descrição da lista de presença (ex: Presença na reunião)"
)
async def comando_presente(interaction: discord.Interaction, descricao: str = "Lista de Presença"):
    """Comando para criar uma lista de presença"""
    
    embed = discord.Embed(
        title="✅ Lista de Presença",
        description=descricao,
        color=discord.Color.green(),
        timestamp=datetime.now()
    )
    
    embed.add_field(
        name="Reaja com ✅ para confirmar sua presença",
        value="Clique no emoji ✅ para aparecer na lista",
        inline=False
    )
    
    embed.set_footer(text=f"Criada por {interaction.user.name}")
    
    await interaction.response.send_message(embed=embed)
    message = await interaction.original_response()
    
    active_presence_messages[message.id] = {
        "channel_id": message.channel.id,
        "description": descricao,
        "creator_id": interaction.user.id,
        "creation_time": message.created_at,
        "users": set()
    }
    
    try:
        await message.add_reaction("✅")
    except Exception as e:
        print(f"❌ Erro ao adicionar reação: {e}")

@bot.tree.command(name="crítico", description="Sorteia um número de 1 a 20 e aplica o sistema de crítico")
async def comando_critico(interaction: discord.Interaction):
    """Comando para sortear um número de 1 a 20 e aplicar o sistema de crítico"""
    
    user_id = interaction.user.id
    roll = random.randint(1, 20)
    
    # Obter o streak atual do usuário
    streak_data = user_crit_streak.get(user_id, {"streak": 0, "last_roll": 0, "perfect_count": 0})
    current_streak = streak_data["streak"]
    perfect_count = streak_data.get("perfect_count", 0)
    
    # Obter o resultado do crítico
    text, gif_url, is_crit, is_perfect = get_crit_result(roll, current_streak, perfect_count)
    
    # Atualizar o streak
    if is_crit:
        new_streak = current_streak + 1
        new_perfect_count = perfect_count + is_perfect
    else:
        new_streak = 0
        new_perfect_count = 0
        
    user_crit_streak[user_id] = {"streak": new_streak, "last_roll": roll, "perfect_count": new_perfect_count}
    
    # Criar embed
    embed = discord.Embed(
        title=f"🎲 Rolagem de Crítico: {roll}",
        description=f"{interaction.user.mention} rolou um **{roll}**!",
        color=discord.Color.red() if is_crit else discord.Color.blue(),
        timestamp=datetime.now()
    )
    
    if text:
        embed.add_field(name="Resultado", value=text, inline=False)
    
    # Adicionar GIF/URL
    if gif_url:
        embed.set_image(url=gif_url)
        
    # Adicionar informação de streak
    if is_crit and new_streak > 1:
        embed.add_field(name="Sequência", value=f"🔥 {new_streak}º Crítico Consecutivo!", inline=False)
    elif not is_crit and current_streak > 0:
        embed.add_field(name="Sequência Quebrada", value=f"A sequência de {current_streak} críticos foi quebrada.", inline=False)
        
    await interaction.response.send_message(embed=embed)

# --- Tarefas de Fundo e Lógica de Reação ---

def parse_emoji_selection(emojis_str: str) -> list:
    """
    Parseia a string de emojis e retorna os emojis correspondentes
    """
    emoji_mapping = {
        "10": "⏱️",
        "20": "⏲️",
        "30": "⌛",
        "40": "⏰",
        "60": "🕐",
        "cancelar": "❌"
    }
    
    try:
        selections = [s.strip().lower() for s in emojis_str.split(",")]
        result = []
        
        for selection in selections:
            if selection in emoji_mapping:
                result.append(emoji_mapping[selection])
        
        return result if result else list(TIMER_EMOJIS.keys())
    except:
        return list(TIMER_EMOJIS.keys())

@bot.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    """Evento disparado quando alguém reage a uma mensagem"""
    
    if user.bot:
        return
    
    emoji = str(reaction.emoji)
    message_id = reaction.message.id
    
    # Só processa se for um emoji de timer E a mensagem for um timer ativo
    if emoji in TIMER_EMOJIS and message_id in active_timer_messages:
        await handle_timer_reaction(reaction, user, emoji)
    elif emoji == "✅" and message_id in active_presence_messages:
        # A lógica de presença é tratada na tarefa de fundo
        pass

async def handle_timer_reaction(reaction: discord.Reaction, user: discord.User, emoji: str):
    """Trata reações de timer"""
    
    message_id = reaction.message.id
    duration_minutes = TIMER_EMOJIS[emoji]
    
    if emoji == "❌":
        # Apenas processa se for uma mensagem de timer válida
        if message_id not in active_timer_messages:
            return

        timer_key = f"{message_id}_{user.id}"
        
        # Se o usuário tinha um timer ativo para ESTA mensagem, cancela
        if timer_key in active_user_timers:
            del active_user_timers[timer_key]
            try:
                await user.send("✅ Opção 'Não vai responder este turno' registrada e seu timer para esta mensagem foi cancelado.")
            except:
                pass
        else:
            # Se não tinha timer, apenas confirma que ele não vai responder (opcional, mas mantido conforme lógica anterior)
            # Para evitar spam em mensagens aleatórias, já filtramos no on_reaction_add
            try:
                await user.send("✅ Opção 'Não vai responder este turno' registrada.")
            except:
                pass
        return
    
    timer_key = f"{message_id}_{user.id}"
    
    if timer_key in active_user_timers:
        try:
            await user.send("⚠️ Você já tem um timer ativo para esta mensagem!")
        except:
            pass
        return
    
    message_creation_time = reaction.message.created_at
    if message_creation_time.tzinfo is None:
        message_creation_time = message_creation_time.replace(tzinfo=datetime.now().astimezone().tzinfo)
    
    timer_start_time = datetime.now(message_creation_time.tzinfo)
    elapsed = (timer_start_time - message_creation_time).total_seconds() / 60
    remaining_minutes = duration_minutes - elapsed
    
    if remaining_minutes <= 0:
        try:
            await user.send(f"⏰ O timer de {duration_minutes} minutos já expirou!")
        except:
            pass
        return
    
    active_user_timers[timer_key] = {
        "end_time": timer_start_time + timedelta(minutes=duration_minutes),
        "user_id": user.id,
        "channel_id": reaction.message.channel.id,
        "duration": duration_minutes,
        "message_id": message_id,
        "remaining": remaining_minutes
    }
    
    try:
        embed = discord.Embed(
            title="⏱️ Timer Iniciado",
            description=f"Você será notificado em **{remaining_minutes:.1f} minutos**",
            color=discord.Color.green()
        )
        await user.send(embed=embed)
    except:
        pass
    
    asyncio.create_task(wait_and_notify(timer_key, user, remaining_minutes))

async def wait_and_notify(timer_key: str, user: discord.User, remaining_minutes: float):
    """Aguarda o tempo restante e notifica o usuário (DM com imagem, Canal sem imagem)"""
    
    try:
        wait_seconds = remaining_minutes * 60
        await asyncio.sleep(wait_seconds)
        
        if timer_key not in active_user_timers:
            return
        
        timer_data = active_user_timers[timer_key]
        del active_user_timers[timer_key]
        
        # Criar embed de notificação
        embed = discord.Embed(
            title="⏰ Timer Finalizado!",
            description=f"Seu timer de **{timer_data['duration']} minutos** expirou!",
            color=discord.Color.red(),
            timestamp=datetime.now()
        )
        
        # 1. Notificação via DM (COM IMAGEM)
        try:
            if os.path.exists(GOKU_IMAGE_PATH):
                await user.send(f"{user.mention}", embed=embed, file=discord.File(GOKU_IMAGE_PATH))
            else:
                await user.send(f"{user.mention}", embed=embed)
        except:
            pass
        
        # 2. Notificação no Canal de Origem (SEM IMAGEM)
        try:
            channel = bot.get_channel(timer_data['channel_id'])
            if channel:
                await channel.send(f"**{user.mention}**, seu timer de **{timer_data['duration']} minutos** acabou!")
        except Exception as e:
            print(f"❌ Erro ao notificar canal: {e}")
        
        print(f"✅ Timer finalizado para {user.name} ({timer_key})")
        
    except asyncio.CancelledError:
        print(f"⚠️ Timer cancelado para {user.name}")
    except Exception as e:
        print(f"❌ Erro ao notificar usuário: {e}")

@tasks.loop(seconds=30)
async def update_timer_message():
    """Tarefa de fundo para atualizar as mensagens de timer com a lista de usuários que reagiram"""
    
    if not active_timer_messages:
        return
    
    for message_id, data in list(active_timer_messages.items()):
        try:
            channel = bot.get_channel(data['channel_id'])
            if not channel:
                del active_timer_messages[message_id]
                continue
            
            message = await channel.fetch_message(message_id)
            
            new_embed = discord.Embed(
                title="⏱️ Timer Criado",
                description=data['description'],
                color=discord.Color.blue(),
                timestamp=data['creation_time']
            )
            
            creator = bot.get_user(data['creator_id'])
            new_embed.set_footer(text=f"Criado por {creator.name if creator else 'Usuário Desconhecido'}")
            
            if data.get('image_url'):
                new_embed.set_image(url=data['image_url'])
            
            for reaction in message.reactions:
                emoji = str(reaction.emoji)
                if emoji in data['emoji_keys']: # Apenas emojis selecionados
                    users = [user async for user in reaction.users() if user != bot.user]
                    description = EMOJI_DESCRIPTIONS.get(emoji, "Duração Desconhecida")
                    user_list = ", ".join([u.mention for u in users]) if users else "Ninguém reagiu ainda."
                    
                    new_embed.add_field(
                        name=f"{emoji} {description}",
                        value=f"**Usuários:** {user_list}",
                        inline=False
                    )
            
            await message.edit(embed=new_embed)
            
        except discord.NotFound:
            del active_timer_messages[message_id]
        except Exception as e:
            print(f"❌ Erro ao atualizar mensagem {message_id}: {e}")

@tasks.loop(seconds=15)
async def update_presence_message():
    """Tarefa de fundo para atualizar as mensagens de presença com listagem numerada"""
    
    if not active_presence_messages:
        return
    
    for message_id, data in list(active_presence_messages.items()):
        try:
            channel = bot.get_channel(data['channel_id'])
            if not channel:
                del active_presence_messages[message_id]
                continue
            
            message = await channel.fetch_message(message_id)
            
            users = []
            for reaction in message.reactions:
                if str(reaction.emoji) == "✅":
                    async for user in reaction.users():
                        if user != bot.user:
                            users.append(user)
            
            new_embed = discord.Embed(
                title="✅ Lista de Presença",
                description=data['description'],
                color=discord.Color.green(),
                timestamp=data['creation_time']
            )
            
            creator = bot.get_user(data['creator_id'])
            new_embed.set_footer(text=f"Criada por {creator.name if creator else 'Usuário Desconhecido'}")
            
            if users:
                # Listagem numerada
                user_list = "\n".join([f"{i+1}- {user.mention}" for i, user in enumerate(users)])
                new_embed.add_field(
                    name=f"Presentes ({len(users)})",
                    value=user_list,
                    inline=False
                )
            else:
                new_embed.add_field(
                    name="Presentes (0)",
                    value="Ninguém confirmou presença ainda",
                    inline=False
                )
            
            await message.edit(embed=new_embed)
            
        except discord.NotFound:
            del active_presence_messages[message_id]
        except Exception as e:
            print(f"❌ Erro ao atualizar mensagem de presença {message_id}: {e}")

@update_timer_message.before_loop
@update_presence_message.before_loop
async def before_loops():
    await bot.wait_until_ready()

# --- Execução ---

def run_bot(token: str):
    """Inicia o bot com o token fornecido"""
    try:
        bot.run(token)
    except Exception as e:
        print(f"❌ Erro ao iniciar o bot: {e}")

if __name__ == "__main__":
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        print("❌ Erro: DISCORD_BOT_TOKEN não foi definido")
        print("Configure a variável de ambiente no arquivo .env")
    else:
        run_bot(token)
