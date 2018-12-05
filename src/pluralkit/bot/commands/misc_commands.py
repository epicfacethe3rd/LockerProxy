import io
import json
import os
from discord.utils import oauth_url

from pluralkit.bot import help
from pluralkit.bot.commands import *


async def help_root(ctx: CommandContext):
    if ctx.match("commands"):
        await ctx.reply(help.all_commands)
    elif ctx.match("proxy"):
        await ctx.reply(help.proxy_guide)
    else:
        await ctx.reply(help.root)


async def invite_link(ctx: CommandContext):
    client_id = os.environ["CLIENT_ID"]

    permissions = discord.Permissions()

    # So the bot can actually add the webhooks it needs to do the proxy functionality
    permissions.manage_webhooks = True

    # So the bot can respond with status, error, and success messages
    permissions.send_messages = True

    # So the bot can delete channels
    permissions.manage_messages = True

    # So the bot can respond with extended embeds, ex. member cards
    permissions.embed_links = True

    # So the bot can send images too
    permissions.attach_files = True

    # (unsure if it needs this, actually, might be necessary for message lookup)
    permissions.read_message_history = True

    # So the bot can add reactions for confirm/deny prompts
    permissions.add_reactions = True

    url = oauth_url(client_id, permissions)
    await ctx.reply_ok("Use this link to add PluralKit to your server: {}".format(url))


async def export(ctx: CommandContext):
    system = await ctx.ensure_system()

    members = await system.get_members(ctx.conn)
    accounts = await system.get_linked_account_ids(ctx.conn)
    switches = await system.get_switches(ctx.conn, 999999)

    data = {
        "name": system.name,
        "id": system.hid,
        "description": system.description,
        "tag": system.tag,
        "avatar_url": system.avatar_url,
        "created": system.created.isoformat(),
        "members": [
            {
                "name": member.name,
                "id": member.hid,
                "color": member.color,
                "avatar_url": member.avatar_url,
                "birthday": member.birthday.isoformat() if member.birthday else None,
                "pronouns": member.pronouns,
                "description": member.description,
                "prefix": member.prefix,
                "suffix": member.suffix,
                "created": member.created.isoformat()
            } for member in members
        ],
        "accounts": [str(uid) for uid in accounts],
        "switches": [
            {
                "timestamp": switch.timestamp.isoformat(),
                "members": [member.hid for member in await switch.fetch_members(ctx.conn)]
            } for switch in switches
        ]  # TODO: messages
    }

    f = io.BytesIO(json.dumps(data).encode("utf-8"))
    await ctx.message.channel.send(content="Here you go!", file=discord.File(fp=f, filename="system.json"))
