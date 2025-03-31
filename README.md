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
   
##Commands:

/blacklist
Description: Blacklist a member and ban them from all servers.
Usage: /blacklist <member>
Permissions: Requires the bot to have Ban Members permission in all servers.
/unblacklist
Description: Remove a member from the blacklist and unban them from all servers.
Usage: /unblacklist <member>
Permissions: Requires the bot to have Ban Members permission in all servers.


## Notes:

Ensure the bot has the necessary permissions (Ban Members) in all servers it is added to.
The bot must be invited with the appropriate OAuth2 scopes to use slash commands.

## Disclaimer

Use this bot responsibly. Ensure you comply with Discord's Terms of Service and Community Guidelines.
