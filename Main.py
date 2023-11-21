import nextcord
from nextcord.ext import commands
from openai import OpenAI

chat_log = []
client = OpenAI(api_key=open("apiKey.txt", "r").read())

token = open("token.txt", "r").read()

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is now running!')

@bot.slash_command(description="Chat With ChatGPT!", force_global=True, dm_permission=True)
async def chat(interaction: nextcord.Interaction, prompt: str = nextcord.SlashOption(description = "Enter a prompt", required = True)):
    await interaction.response.defer()
    chat_log.append({"role":"user","content":prompt.strip()})
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
    )
    await interaction.followup.send(chat_completion.choices[0].message.content)

if __name__ == '__main__':
    bot.run(token)