# discord-bot-blacklist

# Discord Blacklist Bot

A Discord bot that allows server administrators to manage a blacklist of users. The bot can ban blacklisted users from all servers it is in and unban them when removed from the blacklist.

## Features

- **Blacklist Command**: Add a user to the blacklist and ban them from all servers.
- **Unblacklist Command**: Remove a user from the blacklist and unban them from all servers.
- **Automatic Ban**: Automatically bans blacklisted users who join a server.
- **Persistent Blacklist**: The blacklist is stored in a JSON file for persistence.

## Prerequisites

- Python 3.8 or higher
- A Discord bot token (create one at the [Discord Developer Portal](https://discord.com/developers/applications))

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/LimsDev-code/discord-blacklist-bot.git
   cd discord-blacklist-bot

2. pip install -r requirements.txt

3. Replace YOUR_BOT_TOKEN_HERE in bot.py with your actual bot token.

4. run : python bot.py

