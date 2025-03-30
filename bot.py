import discord
from discord import app_commands
from discord.ext import commands
import json
import os

# Configure bot intents
intents = discord.Intents.default()
intents.guilds = True  # Enable access to guild (server) information
intents.members = True  # Enable access to member information

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Path to the blacklist file
BLACKLIST_FILE = 'blacklist.json'

# Function to load the blacklist from a JSON file
def load_blacklist():
    if os.path.exists(BLACKLIST_FILE):  # Check if the blacklist file exists
        with open(BLACKLIST_FILE, 'r') as f:  # Open the file in read mode
            return json.load(f)  # Load and return the blacklist as a Python list
    return []  # Return an empty list if the file does not exist

# Function to save the blacklist to a JSON file
def save_blacklist(blacklist):
    with open(BLACKLIST_FILE, 'w') as f:  # Open the file in write mode
        json.dump(blacklist, f, indent=4)  # Save the blacklist with indentation for readability

# Load the blacklist into memory when the bot starts
blacklist = load_blacklist()

# Command to add a member to the blacklist and ban them from all servers
@bot.tree.command(name="blacklist", description="Blacklist a member and ban them from all servers")
@app_commands.describe(member="The member to blacklist")  # Describe the command parameter
async def blacklist_member(interaction: discord.Interaction, member: discord.Member):
    if member.id not in blacklist:  # Check if the member is not already blacklisted
        blacklist.append(member.id)  # Add the member's ID to the blacklist
        save_blacklist(blacklist)  # Save the updated blacklist to the file
        for guild in bot.guilds:  # Iterate through all servers the bot is in
            try:
                await guild.ban(member, reason="Blacklisted")  # Attempt to ban the member
            except discord.Forbidden:
                # Send a message if the bot lacks permissions to ban the member
                await interaction.response.send_message(f"Unable to ban {member.mention} in the server {guild.name}", ephemeral=True)
            except discord.HTTPException as e:
                # Send a message if an HTTP error occurs during the ban
                await interaction.response.send_message(f"Error when banning {member.mention} in the server {guild.name}: {str(e)}", ephemeral=True)
        # Confirm the member has been blacklisted and banned
        await interaction.response.send_message(f"{member.mention} has been blacklisted and banned from all servers.", ephemeral=True)
    else:
        # Inform the user that the member is already blacklisted
        await interaction.response.send_message(f"{member.mention} is already blacklisted.", ephemeral=True)

# Command to remove a member from the blacklist and unban them from all servers
@bot.tree.command(name="unblacklist", description="Remove a member from the blacklist and unban them from all servers")
@app_commands.describe(member="The member to be removed from the blacklist")  # Describe the command parameter
async def unblacklist_member(interaction: discord.Interaction, member: discord.User):
    if member.id in blacklist:  # Check if the member is in the blacklist
        blacklist.remove(member.id)  # Remove the member's ID from the blacklist
        save_blacklist(blacklist)  # Save the updated blacklist to the file
        for guild in bot.guilds:  # Iterate through all servers the bot is in
            try:
                await guild.unban(member, reason="Unblacklisted")  # Attempt to unban the member
            except discord.Forbidden:
                # Send a message if the bot lacks permissions to unban the member
                await interaction.response.send_message(f"Unable to unban {member.mention} in the server {guild.name}", ephemeral=True)
            except discord.HTTPException as e:
                # Send a message if an HTTP error occurs during the unban
                await interaction.response.send_message(f"Error when unbanning {member.mention} in the server {guild.name}: {str(e)}", ephemeral=True)
        # Confirm the member has been removed from the blacklist and unbanned
        await interaction.response.send_message(f"{member.mention} has been removed from the blacklist and unbanned from all servers.", ephemeral=True)
    else:
        # Inform the user that the member is not in the blacklist
        await interaction.response.send_message(f"{member.mention} is not in the blacklist.", ephemeral=True)

# Event triggered when a member joins a server
@bot.event
async def on_member_join(member):
    if member.id in blacklist:  # Check if the member is in the blacklist
        try:
            await member.guild.ban(member, reason="Blacklisted")  # Attempt to ban the member
        except discord.Forbidden:
            # Log a message if the bot lacks permissions to ban the member
            print(f"Unable to ban {member.mention} in the server {member.guild.name}")
        except discord.HTTPException as e:
            # Log a message if an HTTP error occurs during the ban
            print(f"Error when banning {member.mention} in the server {member.guild.name}: {str(e)}")

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Synchronize slash commands with Discord
    print(f'Bot connected as {bot.user}')  # Log a confirmation message

# Run the bot with the token
bot.run('YOUR_BOT_TOKEN_HERE')