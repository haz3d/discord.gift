import pyfiglet

import random

import string

import requests

banner = pyfiglet.figlet_format("DNGen", font="slant")

print(banner)

num_links = int(input("How many Discord Nitro links would you like to generate? "))

def generate_discord_nitro_link(num_chars):

    link = "https://discord.gift/"

    for n in range(num_chars):

        link += random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)

    return link

for i in range(num_links):

    link = generate_discord_nitro_link(16)

    url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + link.split("/")[-1] + "?with_application=false&with_subscription_plan=true"

    response = requests.get(url)

    if response.status_code == 200:

        print("[✅] The Discord Nitro Link is Valid: " + link)

    elif response.status_code == 400:

        print("[❗] The Discord Nitro Link is Used: " + link)

    else:

        print("[❌] The Discord Nitro Link is Invalid: " + link)

