import discord
import main
import datetime
from discord.ext import commands
from config import TOKEN, CHANNEL_NAME, COMMAND_PREFIX

product_title = main.hypeboost_product_title
product_picture = main.product_picture
hypeboost_sizes = main.hypeboost_prices
hypeboost_product_url = main.hypeboost_product_url
stockx_product_url = main.stockx_url
restocks_product_url = main.restocks_url
goat_product_url = main.product_goat

if not TOKEN:
    raise ValueError("The Bot-Token was not included in the config.py file")

if not CHANNEL_NAME:
    raise ValueError("The Channel-Name was not included in the config.py file")

if not COMMAND_PREFIX:
    raise ValueError("The Command-Prefix was not included in the config.py file")

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Scraping! (Payout Hypeboost)'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.channel.name == CHANNEL_NAME:
    if message.content.startswith(COMMAND_PREFIX):
      await message.channel.send("Scraping...")

      if COMMAND_PREFIX in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX, '')
        SKU = SKU_raw.replace(" ", "")
        product_title_output = product_title(SKU)
        product_picture_output = product_picture(SKU)
        hypeboost_sizes_output = hypeboost_sizes(SKU)
        hypeboost_product_url_output = hypeboost_product_url(SKU)
        stockx_product_url_output = stockx_product_url(SKU)
        restocks_product_url_output = restocks_product_url(SKU)
        goat_product_url_output = goat_product_url(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=hypeboost_product_url_output,
          color=0x3498db
        )
        embed.set_author(
          name="Hypeboost Payout Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://consumersiteimages.trustpilot.net/business-units/610a587f2b259a001d8d9b5f-198x149-1x.jpg"
          )
        embed.set_thumbnail(
          url=product_picture_output
        )
        embed.add_field(
          name="Payout Prices:",
          value=hypeboost_sizes_output
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_product_url_output})      " f"[[Restocks]]({restocks_product_url_output})      " f"[[Hypeboost]]({hypeboost_product_url_output})      " f"[[GOAT]]({goat_product_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Hypeboost-Payout      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Payout Scraping Successful!')


bot.run(TOKEN)
c
