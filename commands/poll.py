import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import asyncio


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='poll')
    async def poll_(self, ctx, *, title="Untitled"):
        choices = ["yes", "no", "unsure", "finish"]
        yesvote = []
        novote = []
        unsurevote = []

        yesbutton = Button(style="3", label="Yes", custom_id="yes")
        nobutton = Button(style="4", label="No", custom_id="no")
        unsurebutton = Button(style="1", label="Not Sure", custom_id="unsure")
        finish = Button(style="2", label="Finish", custom_id="finish")

        useryes = "-" if not yesvote else "<@" + ">\n<@".join(yesvote) + ">"
        userno = "-" if not novote else "<@" + ">\n<@".join(novote) + ">"
        userunsure = "-" if not unsurevote else "<@" + ">\n<@".join(unsurevote) + ">"

        embedmsg = discord.Embed(
            title=title,
            description=f"Poll created by {ctx.author.mention}",
            color=discord.Color.random())
        embedmsg.set_thumbnail(url=ctx.author.avatar_url)
        embedmsg.insert_field_at(index=0,
                                 name="Status",
                                 value="Voting is currently open.",
                                 inline=False)
        embedmsg.insert_field_at(index=1,
                                 name=f"✅User Yes ({len(yesvote)})",
                                 value=useryes,
                                 inline=True)
        embedmsg.insert_field_at(index=2,
                                 name=f"❌User No ({len(novote)})",
                                 value=userno,
                                 inline=True)
        embedmsg.insert_field_at(index=3,
                                 name=f"🤷‍♂️User Unsure ({len(unsurevote)})",
                                 value=userunsure,
                                 inline=True)

        message = await ctx.send(
            embed=embedmsg,
            components=[[yesbutton, nobutton, unsurebutton, finish]])

        def check(msg):
            return msg.custom_id in choices and msg.message.id == message.id

        while True:
            try:
                interaction = await self.bot.wait_for("button_click",
                                                      check=lambda i: check(i),
                                                      timeout=30)
            except:
                await interaction.respond(type=6)
                embedmsg.set_field_at(index=0,
                                 name="Status",
                                 value="Voting is Closed.",
                                 inline=False)
                await message.edit(embed=embedmsg, components=[])
                break

            if interaction.custom_id == "yes":
                await interaction.respond(type=6)
                if str(interaction.author.id) in novote:
                    novote.remove(str(interaction.author.id))
                if str(interaction.author.id) in unsurevote:
                    unsurevote.remove(str(interaction.author.id))
                if str(interaction.author.id) not in yesvote:
                    yesvote.append(str(interaction.author.id))
                useryes = "-" if not yesvote else "<@" + ">\n<@".join(
                    yesvote) + ">"
                userno = "-" if not novote else "<@" + ">\n<@".join(
                    novote) + ">"
                userunsure = "-" if not unsurevote else "<@" + ">\n<@".join(
                    unsurevote) + ">"
                embedmsg.set_field_at(index=1,
                                      name=f"✅User Yes ({len(yesvote)})",
                                      value=useryes,
                                      inline=True)
                embedmsg.set_field_at(index=2,
                                      name=f"❌User No ({len(novote)})",
                                      value=userno,
                                      inline=True)
                embedmsg.set_field_at(
                    index=3,
                    name=f"🤷‍♂️User Unsure ({len(unsurevote)})",
                    value=userunsure,
                    inline=True)
                await message.edit(embed=embedmsg)
            elif interaction.custom_id == "no":
                await interaction.respond(type=6)
                if str(interaction.author.id) not in novote:
                    novote.append(str(interaction.author.id))
                if str(interaction.author.id) in unsurevote:
                    unsurevote.remove(str(interaction.author.id))
                if str(interaction.author.id) in yesvote:
                    yesvote.remove(str(interaction.author.id))
                useryes = "-" if not yesvote else "<@" + ">\n<@".join(
                    yesvote) + ">"
                userno = "-" if not novote else "<@" + ">\n<@".join(
                    novote) + ">"
                userunsure = "-" if not unsurevote else "<@" + ">\n<@".join(
                    unsurevote) + ">"
                embedmsg.set_field_at(index=1,
                                      name=f"✅User Yes ({len(yesvote)})",
                                      value=useryes,
                                      inline=True)
                embedmsg.set_field_at(index=2,
                                      name=f"❌User No ({len(novote)})",
                                      value=userno,
                                      inline=True)
                embedmsg.set_field_at(
                    index=3,
                    name=f"🤷‍♂️User Unsure ({len(unsurevote)})",
                    value=userunsure,
                    inline=True)
                await message.edit(embed=embedmsg)
            elif interaction.custom_id == "unsure":
                await interaction.respond(type=6)
                if str(interaction.author.id) in novote:
                    novote.remove(str(interaction.author.id))
                if str(interaction.author.id) not in unsurevote:
                    unsurevote.append(str(interaction.author.id))
                if str(interaction.author.id) in yesvote:
                    yesvote.remove(str(interaction.author.id))
                useryes = "-" if not yesvote else "<@" + ">\n<@".join(
                    yesvote) + ">"
                userno = "-" if not novote else "<@" + ">\n<@".join(
                    novote) + ">"
                userunsure = "-" if not unsurevote else "<@" + ">\n<@".join(
                    unsurevote) + ">"
                embedmsg.set_field_at(index=1,
                                      name=f"✅User Yes ({len(yesvote)})",
                                      value=useryes,
                                      inline=True)
                embedmsg.set_field_at(index=2,
                                      name=f"❌User No ({len(novote)})",
                                      value=userno,
                                      inline=True)
                embedmsg.set_field_at(
                    index=3,
                    name=f"🤷‍♂️User Unsure ({len(unsurevote)})",
                    value=userunsure,
                    inline=True)
                await message.edit(embed=embedmsg)
            elif (interaction.custom_id == "finish") and (interaction.author.id
                                                          == ctx.author.id):
                await interaction.respond(type=6)
                embedmsg.set_field_at(index=0,
                                 name="Status",
                                 value="Voting is Closed.",
                                 inline=False)
                await message.edit(embed=embedmsg, components=[])
                break
            else:
                await interaction.respond(type=6)


def setup(bot):
    bot.add_cog(Poll(bot))
