import subprocess
from flask import Flask
from os import environ
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return "On"
print("Running index.py")
processbot = subprocess.Popen(['python3.7', 'index.py'])


@bot.command()
async def emoji(ctx, emoji:discord.Emoji):
  await ctx.send(emoji)
  print(emoji)