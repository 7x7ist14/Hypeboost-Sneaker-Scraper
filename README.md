# Hypeboost-Sneaker-Scraper
A web Scraper for Sneaker Prices on Hypeboost with discord message.
The Scraper will Scrape Price informations for all listed Sizes on Hypeboost and return
you a list of them in your discord server.
The message also includes the Hypeboost Product URL, StockX Product URL and Restocks Product URL for the Scraped Product.
A Product Photo is also added to the return message.




# How to use:

1. Check or install following libraries:

+ requests (pip install requests)
+ json (pip install json)
+ BeautifulSoup (pip install beautifulsoup4)
+ Discord (pip install discord.py)

to install them just write the pip install... in your Terminal

2. Open "Config" file and input your Discord Bot Token and the name of the channel were you want to use the scraper in.


3. Open and run the "discord_embed" file. (best for this is VS-Code in my opinion)

4. Write the keyword ($scrape) + SKU in your discord server (you have to write the message in the same channel that you added to the config file!)
   format: $scrape SKU --> (example: $scrape CW1590-100)


The Scraper will now send you all listed sizes and their prices in the discord channel.
Also the Hypeboost Product URL is in the blue title.
At the bottom of the discord message you can also find the StockX and Restocks Product URL to the Scraped Product.




# Notes:
This is my first Github Project and the code might not be the best or the simplest,
if you have any questions just ask them and i will try to help.



# Return Message Example:
The return message looks like this:



![Discord-Message-new](https://user-images.githubusercontent.com/103487648/221413654-7a80159a-7493-44f9-8d77-45048b356df8.png)
