import discord
from discord.ext import commands
import datetime
import time
import youtube_dl
import os
import requests
import json

from urllib import parse, request
import re
import random

bot = commands.Bot(command_prefix='z!', description="hola")
bot.remove_command('help')

players = {}


    
@bot.command()
async def ping(ctx):
    await ctx.send(f' ¡Pong! :ping_pong: ``{round(bot.latency * 1000)}ms. `` <a:verifed:766640990500945971>')
    
@bot.event
async def on_ready():
  await bot.change_presence(activity = discord.Game(name='z!help'), status=discord.Status.do_not_disturb)
  print("EL BOT ESTA ON")

  
@bot.command()
async def reset(ctx):
    if ctx.author.id == 718530241081114776:
      embed = discord.Embed(title="¡Apagando!", description=f"**{ctx.author.name}** Se a reiniciado el bot <a:verifed:766640990500945971>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
      embed.set_thumbnail(url="https://cdn.discordapp.com/icons/747608450607087726/15d4c0a190974cc213c29961b73d3357.webp?size=1024")   
      borrar = await ctx.send(embed=embed)
      time.sleep(3)
      await borrar.delete()
      await ctx.bot.logout()
      print(f'El bot a sido reiniciado por: "{ctx.author.name}" ')
    else:
      print(f'"{ctx.author.name}" a intentado reiniciar el bot')
      embed = discord.Embed(title="¡Error!", description=f"**{ctx.author.name}** No tienes permisos para eso <a:error:692564815025274881>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
      embed.set_thumbnail(url="https://cdn.discordapp.com/icons/747608450607087726/15d4c0a190974cc213c29961b73d3357.webp?size=1024")   
      borrar = await ctx.send(embed=embed)
      time.sleep(3)
      await borrar.delete()
      
@bot.command()
async def reload(ctx):
    if ctx.author.id == 718530241081114776:
      embed = discord.Embed(title="¡Apagando!", description=f"**{ctx.author.name}** Se a reiniciado el bot <a:verifed:766640990500945971>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
      embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7_IWEHjEt_1GoOtDjU5lB1ndWy3vHqtPtmzgxOvhZXA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/687630553931186276/70db4a578ad928fe488a30d3da5edb67.png?width=300&height=300")   
      borrar= await ctx.send(embed=embed)
      time.sleep(3)
      await borrar.delete()
      await ctx.bot.logout()
      print(f'El bot a sido reiniciado por: "{ctx.author.name}" ')

    else:
      print(f'"{ctx.author.name}" a intentado reiniciar el bot')
      embed = discord.Embed(title="¡Error!", description=f"**{ctx.author.name}** No tienes permisos para reiniciar el bot <a:error:692564815025274881>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
      embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7_IWEHjEt_1GoOtDjU5lB1ndWy3vHqtPtmzgxOvhZXA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/687630553931186276/70db4a578ad928fe488a30d3da5edb67.png?width=300&height=300")   
      borrar = await ctx.send(embed=embed)
      time.sleep(3)
      await borrar.delete()
    
@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Informacion del servidor", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="El servidor se creo el", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del servidor", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del servidor", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    #embed.set_thumbnail(url="https://media.discordapp.net/attachments/597081131438833665/687239997702799394/54_9_351_806-8803_20200308_011826.jpg?width=443&height=443")

    await ctx.send(embed=embed)
    
@bot.command()
async def ip(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Informacion del servidor", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="<a:verifed:766640990500945971> Direccion IP del servidor", value=f" <a:tuercs:766641422370603038> **MANTENIMIENTO**")
    embed.add_field(name="<:web:766645670274400266> Pagina WEB del servidor", value=f"[Web](https://leeproleplay.ga/)")
    embed.add_field(name="<:ts3:766645995899453480> TS3 del servidor", value=f"<a:tuercs:766641422370603038> **MANTENIMIENTO**")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    #embed.set_thumbnail(url="https://media.discordapp.net/attachments/597081131438833665/687239997702799394/54_9_351_806-8803_20200308_011826.jpg?width=443&height=443")

    await ctx.send(embed=embed)
	
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    
    embed = discord.Embed(title="Title", timestamp=ctx.message.created_at)
    
    embed.set_author(name=f"Inforacion del usuario = {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Comando ejecutado por: {ctx.author}", icon_url=ctx.author.avatar_url)
    
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nombre:", value=member.display_name)
    
    embed.add_field(name="Cuenta creada el:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Se unio el:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    
    embed.add_field(name="¿Es un bot?", value=member.bot)
    
    await ctx.send(embed=embed)
   

    
@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title=f"**<a:info:766641465425264650>Informacion del bot**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="<a:dev:766641485252263987> Dueño del bot", value=f"**TRUX_YT#4686**")
    embed.add_field(name="<a:prefix:766641915437252628> Prefix", value=f"**z!**")
    embed.add_field(name="<a:tuercs:766641422370603038>ID del bot", value=f"**766498141709008947**")
    embed.add_field(name="Estoy en", value=f"**{len(bot.guilds)}** Servidores")
    embed.add_field(name="<a:info:766641465425264650> Programado en", value=f"<:python:766640748091015168> **Python**")
    embed.add_field(name=f"Links", value=f"<:links:766641637904220171> [Discord](https://discord.gg/3bebsbJ)\n<:links:766641637904220171> [Web](https://leeproleplay.ga/)")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/747608450607087726/15d4c0a190974cc213c29961b73d3357.webp?size=1024")

    await ctx.send(embed=embed)

    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=16):
    await ctx.channel.purge(limit=amount)
    borrar = await ctx.send('<a:verifed:766640990500945971>¡Se han borrado ``{} mensajes``!'.format(amount))
    time.sleep(3)
    await borrar.delete()
@clear.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title="¡Mal!", description=f"**{ctx.author.name}** Se a reiniciado el bot <a:verifed:766640990500945971>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7_IWEHjEt_1GoOtDjU5lB1ndWy3vHqtPtmzgxOvhZXA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/687630553931186276/70db4a578ad928fe488a30d3da5edb67.png?width=300&height=300")   
        borrar = await ctx.send(embed=emed)
        await ctx.guild.owner.send(f'{ctx.author.name} a intentado borrar mensajes  en el servidor {ctx.guild.name}')
  
  
  
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Menciona a un usuario")
        return
    await member.kick()
    await ctx.send(f"**{member.name}** a sido kickeado por **{ctx.author.name}**")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title="¡Apagando!", description=f"**{ctx.author.name}** Se a reiniciado el bot <a:verifed:766640990500945971>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7_IWEHjEt_1GoOtDjU5lB1ndWy3vHqtPtmzgxOvhZXA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/687630553931186276/70db4a578ad928fe488a30d3da5edb67.png?width=300&height=300")   
        borrar = await ctx.send(embed=embed)
        time.sleep(3)
        await borrar.delete()
        await ctx.guild.owner.send(f'{ctx.author.name} a intentado kickear gente en el servidor {ctx.guild.name}')
 

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Menciona a un usuario")
        return
    await member.ban()
    await ctx.send(f"**{member.name}** a sido baneado por **{ctx.author.name}**")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.guild.owner.send(f'{ctx.author.name} a intentado banear gente en el servidor {ctx.guild.name}')
        embed = discord.Embed(title="¡Apagando!", description=f"**{ctx.author.name}** Se a reiniciado el bot <a:verifed:766640990500945971>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7_IWEHjEt_1GoOtDjU5lB1ndWy3vHqtPtmzgxOvhZXA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/687630553931186276/70db4a578ad928fe488a30d3da5edb67.png?width=300&height=300")   
        borrar = await ctx.send(embed=embed)
        time.sleep(3)
        await borrar.delete()
        
        
@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Menciona a un usuario")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    role2 = discord.utils.get(ctx.guild.roles, name="Crying Child")
    await member.remove_roles(role2)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.guild.owner.send(f'"{ctx.author.name}" a intentado banear gente')
        embed = discord.Embed(title="¡Apagando!", description=f"**{ctx.author.name}** Se a reiniciado el bot <a:verifed:766640990500945971>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7_IWEHjEt_1GoOtDjU5lB1ndWy3vHqtPtmzgxOvhZXA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/687630553931186276/70db4a578ad928fe488a30d3da5edb67.png?width=300&height=300")   
        borrar = await ctx.send(embed=embed)
        time.sleep(3)
        await borrar.delete()
    
    
@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Menciona a un usuario")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    role2 = discord.utils.get(ctx.guild.roles, name="Crying Child")
    await member.add_roles(role2)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title="¡Apagando!", description=f"**{ctx.author.name}** Se a reiniciado el bot <a:verifed:766640990500945971>", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/7_IWEHjEt_1GoOtDjU5lB1ndWy3vHqtPtmzgxOvhZXA/%3Fsize%3D2048/https/cdn.discordapp.com/avatars/687630553931186276/70db4a578ad928fe488a30d3da5edb67.png?width=300&height=300")   
        borrar = await ctx.send(embed=embed)
        time.sleep(3)
        await borrar.delete()
        
@bot.command(pass_context=True)
async def ball(ctx):
  await ctx.send(random.choice(["La verdad es que no -_- :8ball:",
                                   "¿Tú qué crees? :8ball:",
                                   "Yo digo que sí, pero tu destino dice que no >u< :8ball:",
                                   "No estés tan seguro de eso. :8ball:",
                                   "Es probable uwu :8ball:",
                                   "¡Sin lugar a dudas! :8ball:",
                                   "¿Por qué la pregunta? :8ball:",
                                   "Pregunta en otro momento. :8ball:",
                                   "No digas eso... :8ball:",
                                   "Estoy seguro de que se hará realidad. ^.^/ :8ball:",
                                   "No ¬¬ :8ball:",
                                   "No estés tan seguro de eso. :8ball:",
                                   "Eso es imposible. :8ball:",
                                   "¡Claro! :D :8ball:",
                                   "No... :8ball:",
                                   "Eso es interesante o.o :8ball:",
                                   "No creo :8ball:",
                                   "Es posible o.o :8ball:",
                                   "Sí <3 :8ball:",
                                   "Falso",
                                   "Verdadero",
                                   "¡Sin lugar a dudas!",
                                   "Se supone que sí.",
                                   "Si... :8ball:",
                                   "No hay duda acerca de ello.",
                                   "Teóricamente, sí :8ball:",
                                   "Definitivamente. :8ball:",
                                   "Cierto :8ball:",
                                   "Tal vez en un año >.< :8ball:",
                                   "Tal vez en un mes >.< :8ball:",
                                   "Tal vez mañana >.< :8ball:",
                                   "¿Crees que sí? Yo creo que no ._. :8ball:",
                                   "Probablemente no. :8ball:",
                                   "No entiendo o.O :8ball:",
                                   "¡Por supuesto que no! >.< :8ball:"]))
  
@bot.command(pass_context=True)
async def sn(ctx):
  await ctx.send(random.choice(["Si",
                                   "No",
                                   "Si.",
                                   "No.",
                                   "Si..",
                                   "No..."]))
  
  
@bot.command(pass_context=True)
async def pruebacorona(ctx):
  await ctx.send(random.choice(["Tu prueba de <:corona:766649156868898816>**CORONAVIRUS**<:corona:766649156868898816> es: **Positivo**",
                                "Tu prueba de <:corona:766649156868898816>**CORONAVIRUS**<:corona:766649156868898816> es: **Negativo**"]))


@bot.command()
async def prueba(ctx):
  await ctx.guild.owner.send(f'"{ctx.guild.name}" ')
                                     
@bot.command()
async def kiss(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** A besado a **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/399448944889036801/664504450723086336/3285c96d-72cd-460e-942a-414729bc4dcc.gif?width=400&height=225")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
async def lag(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Tiene lag", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/399448944889036801/644205502712119308/085a601660918d7426fee0287436d93d.gif?width=400&height=225")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)
    
@bot.command()
async def fail(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Está fallando", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/399448944889036801/664051845643370496/a4708958c14d6f933f98ed509b61d2b7.gif?width=400&height=225")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
async def cry(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Está llorando", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/399448944889036801/650318672321052682/8T101PL.gif?width=400&height=224")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    
    embed = discord.Embed(title=f"**{member.name}** Avatar Image", timestamp=ctx.message.created_at)
    embed.set_image(url=f"{member.avatar_url}")
    embed.set_footer(text="2020")
    
    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_nsfw()
async def fuck(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** se a follado a **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/602747804418572289/688858895166341226/11.gif?width=400&height=224")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_nsfw()
async def suck(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** Chupa el miembro de **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/602747804418572289/688863692355272848/5.gif?width=400&height=225")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
      
    
@bot.command()
@commands.is_nsfw()
async def undress(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se desnuda", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/602747804418572289/688857115674411026/24.gif?width=400&height=224")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
    
@bot.command()
@commands.is_nsfw()
async def lick(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** Lame el miembro de **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/602747804418572289/688863681102086148/2.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_nsfw()
async def cum(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se vino en **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/541290399155748867/575436663744888883/006_1000.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_nsfw()
async def masturbate(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se esta masturbando", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/602747804418572289/688857038901477451/17.gif?width=400&height=300")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
    

@bot.command()
async def happy(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Está feliz", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://images-ext-2.discordapp.net/external/Cqux_xcvPvjJgwLE9u6YH06uVhny8rgS8xq_irZ21as/https/cdn.weeb.sh/images/rkTDVJYwW.gif?width=400&height=225")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
    
@bot.command(pass_context=True)
async def help(ctx):
    await ctx.author.send('Hola mi nombre es dark y esta es mi lista de comandos.\nSi necesitas mas informacion entra a la pagina web:  https://darkness-smile.glitch.me\n\n**<a:info:692591881896591380> MODERACION:**\n\n ``z!clear``  ``z!ban`` ``z!kick`` ``z!mute`` ``z!unmute`` \n\n**<a:info:692591881896591380> INFORMATIVOS:**\n\n ``z!ping`` ``z!casos`` ``z!comandos`` ``z!contagiar`` ``z!userinfo`` ``z!botinfo`` ``z!casos`` ``z!serverinfo``\n\n **<a:info:692591881896591380> DIVERTIDOS:**\n\n``z!ball`` ``z!carcel`` ``z!whisky``  ``z!matar`` ``z!bob`` ``z!comermocos`` ``z!mascarilla`` ``z!barbijo`` ``z!tapabocas`` ``z!sn`` ``z!happy`` ``z!lag`` ``z!coronavirus`` ``z!ahogarse`` ``z!cafe`` ``z!pruebacorona`` ``z!pelearse`` ``z!cry`` ``z!avatar`` ``z!lag`` ``z!kiss`` ``z!fail``\n\n **<a:info:692591881896591380> NSFW:**\n\n``z!suck`` ``z!fuck`` ``z!lick`` ``z!masturbate`` ``z!cum`` ``z!undress``')
    await ctx.send(f'¡Mira al md **{ctx.author.name}**!')
    
@bot.command(pass_context=True)
async def comandos(ctx):
    await ctx.send('**<a:info:766641465425264650> MODERACION:**\n\n ``z!clear``  ``z!ban`` ``z!kick`` ``z!mute`` ``z!unmute`` \n\n**<a:info:766641465425264650> INFORMATIVOS:**\n\n ``z!ping`` ``z!casos`` ``z!comandos`` ``z!contagiar`` ``z!userinfo`` ``z!casos`` ``z!botinfo`` ``z!serverinfo``\n\n **<a:info:766641465425264650> DIVERTIDOS:**\n\n``z!ball`` ``z!carcel`` ``z!comermocos`` ``z!matar`` ``z!mascarilla`` ``z!barbijo`` ``z!tapabocas`` ``z!sn`` ``z!happy`` ``z!lag`` ``z!coronavirus`` ``z!whisky`` ``z!ahogarse`` ``z!cafe`` ``z!pruebacorona`` ``z!bob`` ``z!pelearse`` ``z!cry`` ``z!avatar`` ``z!lag`` ``z!kiss`` ``z!fail``\n\n **<a:info:766641465425264650> NSFW:**\n\n``z!suck`` ``z!fuck`` ``z!lick`` ``z!masturbate`` ``z!cum`` ``z!undress``')

    
@bot.command()
async def coronavirus(ctx):
    embed=discord.Embed(title="Usa el comando z!casos [pais]")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)


@bot.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)
      
       
@bot.command(aliases=['corona', 'elcorona'])
async def casos(ctx, pais=None):
    if pais is None:
      await ctx.send("Indica un pais o pon ``z!mundo`` para ver todos los casos en total <a:corona2:692543653167628318>")
      return
    else:
      if pais == "mundo":
        embed=discord.Embed(title="Coronavirus en el mundo")
        r = requests.get("https://corona.lmao.ninja/v2/all")
        dou = r.json()
        embed.add_field(name="Infectados:", value=dou["cases"], inline=False)
        embed.add_field(name="Muertes:", value=dou["deaths"], inline=False)
        embed.add_field(name="Recuperados:", value=dou["recovered"], inline=False)
        embed.set_footer(text=f"Comando ejecutado por {ctx.author.name}", icon_url=ctx.author.avatar_url)
      else:
        r = requests.get("https://corona.lmao.ninja/v2/countries/" + pais)
        if r.text == "Country not found":
          await ctx.send("El pais o comando ingresado no existe.")
          return
        else:

          dou = r.json()
          embed=discord.Embed(title="Coronavirus en " + dou["country"] + ":")
        


        
          embed.add_field(name="Infectados totales:", value=dou["cases"], inline=True)
          embed.add_field(name="Muertes totales:", value=dou["deaths"], inline=True)
          embed.add_field(name="Infectados de hoy:", value=dou["todayCases"], inline=True)
          embed.add_field(name="Muertes de hoy:", value=dou["todayDeaths"], inline=True)
          embed.add_field(name="Recuperados:", value=dou["recovered"], inline=True)
          if dou["critical"] == 0:
            embed.add_field(name="Casos Criticos:", value="Ninguno", inline=True)
          else:
            embed.add_field(name="Casos Criticos", value=dou["critical"], inline=True)
          embed.set_footer(text=f"Comando ejecutado por {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    
    
    
    
    
    
    
@bot.command(aliases=['coronavi', 'pirus'])
async def cases(ctx, pais=None):
    if pais is None:
      await ctx.send("Indicate a country or enter ``z!world`` to look all of the cases in total  <a:corona2:692543653167628318>")
      return
    else:
      if pais == "world":
        embed=discord.Embed(title="Coronavirus in the world")
        r = requests.get("https://corona.lmao.ninja/v2/all")
        dou = r.json()
        embed.add_field(name="Infected:", value=dou["cases"], inline=False)
        embed.add_field(name="Deaths:", value=dou["deaths"], inline=False)
        embed.add_field(name="Recovered :", value=dou["recovered"], inline=False)
        embed.set_footer(text=f"Command executed by {ctx.author.name}", icon_url=ctx.author.avatar_url)
      else:
        r = requests.get("https://corona.lmao.ninja/v2/countries/" + pais)
        if r.text == "Country not found":
          await ctx.send("The country or command entered does not exist")
          return
        else:

          dou = r.json()
          embed=discord.Embed(title="Coronavirus in " + dou["country"] + ":")
        


        
          embed.add_field(name="Infected total:", value=dou["cases"], inline=True)
          embed.add_field(name="Deaths totales:", value=dou["deaths"], inline=True)
          embed.add_field(name="Infected today:", value=dou["todayCases"], inline=True)
          embed.add_field(name="Deaths today:", value=dou["todayDeaths"], inline=True)
          embed.add_field(name="Recovered:", value=dou["recovered"], inline=True)
          if dou["critical"] == 0:
            embed.add_field(name="Critical cases:", value="None", inline=True)
          else:
            embed.add_field(name="Critical cases", value=dou["critical"], inline=True)
          embed.set_footer(text=f"Command executed by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    
    
    

@bot.command()
async def mascarilla(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se a puesto una mascarilla", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://i.imgur.com/QlRNL54.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)  
    
@bot.command()
async def barbijo(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se a puesto un barbijo", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://i.imgur.com/QlRNL54.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
async def tapabocas(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se a puesto un tapabocas", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://i.imgur.com/QlRNL54.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
async def contagiar(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** A contagiado de coronavirus a **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.tenor.com/images/5047aa0102643a1c6780479f2536bf65/tenor.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
async def comermocos(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se come los mocos", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://thumbs.gfycat.com/DistantBiodegradableGrayling-max-1mb.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)  
    
@bot.command()
async def ahogarse(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se ahoga", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://img.buzzfeed.com/buzzfeed-static/static/2015-03/9/12/enhanced/webdr11/anigif_enhanced-24407-1425918025-2.gif?output-quality=auto&output-format=auto&downsize=360")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)  
    
@bot.command()
async def cafe(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se esta tomando un cafe", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://i.pinimg.com/originals/9e/f0/c8/9ef0c82905fd4fba11cd85fa7c69ca54.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)  
    
@bot.command()
async def whisky(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se esta tomando un whisky", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media.giphy.com/media/77ZhcbrGHqQSY/giphy.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)  
    
@bot.command()
async def pelearse(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** Se esta dando a vergasos con **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media1.tenor.com/images/bc5468a43f56d60cacde958f1388128d/tenor.gif?itemid=6185033ñ")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
async def matar(ctx, member:discord.Member = None):
    embed = discord.Embed(description=f"**{ctx.author.name}** Le esta disparando a **{member.name}**", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://media1.tenor.com/images/3948a1b0d2419b57e2a22ed5099189d8/tenor.gif?itemid=12188033")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
    
@bot.command()
async def carcel(ctx):
    embed = discord.Embed(description=f"**{ctx.author.name}** Esta en la carcel", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://www.laguiadelvaron.com/wp-content/uploads/2017/01/chacar.gif")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed) 
    
@bot.command()
async def bob(ctx):
  r = requests.get("https://pastebin.com/raw/gu2nUvMs")
  await ctx.send(r.text)

    
    
        
bot.run('NzY2NDk4MTQxNzA5MDA4OTQ3.X4kPBQ.hHSdM2Rog-Wa1-1L8sDcjrXW7e8')



