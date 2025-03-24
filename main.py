import discord
from discord.ext import commands

# Tworzymy intents
intents = discord.Intents.default()
intents.message_content = True  # Wymagane do czytania wiadomości

# Tworzymy bota z intents
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Zalogowano jako: {bot.user}')

@bot.command()
async def hello(ctx):
    """Bot odpowiada przywitaniem."""
    await ctx.send(f'🚀 Cześć, {ctx.author.mention}! Jestem {bot.user}!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    """Generuje wiadomość z 'he' powtórzonym określoną ilość razy."""
    if count_heh < 1 or count_heh > 100:
        await ctx.send("❌ Wybierz liczbę między 1 a 100.")
    else:
        await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    """Wysyła obrazek jako podgląd zamiast pliku do pobrania."""
    file_path = "recykling_smieci.jpg"  # Ścieżka do pliku

    try:
        with open(file_path, "rb") as f:
            picture = discord.File(f, filename="recykling_smieci.jpg")
            embed = discord.Embed(title="♻️ Recykling śmieci!")
            embed.set_image(url=f"attachment://recykling_smieci.jpg")  # Osadzamy obrazek
            await ctx.send(embed=embed, file=picture)  # Wysyłamy osadzenie + plik
    except FileNotFoundError:
        await ctx.send("❌ Nie znaleziono pliku `recykling_smieci.jpg`!")
    except Exception as e:
        await ctx.send(f"❌ Wystąpił błąd: {e}")


bot.run("TU_WPISZ_SWÓJ_TAJNY_KOD")
