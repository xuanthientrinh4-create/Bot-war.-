import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("❌ Chưa set DISCORD_TOKEN trong .env")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[OK] Bot online: {bot.user}")

@bot.command()
async def war(ctx, *, name: str):
    path = "reo.txt"

    if not os.path.exists(path):
        await ctx.send("❌ Không tìm thấy file reo.txt")
        return

    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    await ctx.send(f"🔥 WAR BẮT ĐẦU: **{name}** 🔥")

    for line in lines:
        msg = line.replace("{name}", name)
        await ctx.send(msg)
        await asyncio.sleep(0.8)

    await ctx.send("✅ WAR KẾT THÚC")

bot.run(TOKEN)
