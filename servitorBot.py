# hexarchate bot, by Ursula
# jeng-zai cards and meanings from Yoon Ha Lee's list at http://clockwiki.yoonhalee.com/index.php?title=Jeng-zai

import random
import discord
from discord.ext import commands

#insert the token for your Discord app here
TOKEN = ''

# @servitor-bot to send a command
bot = commands.Bot(command_prefix=commands.when_mentioned)

#test: returns "flashing lights affirmatively"

@bot.command()
async def test(ctx):
    msg = '{0.author.mention} *flashing lights affirmatively*'.format(ctx)
    await ctx.send(msg)

#number: returns a random number between 1 and the provided value, inclusive (defaults to 6)

@bot.command()
async def number(ctx, max="6"):
    num = random.randint(1, int(max))
    num_msg = '{0.author.mention} ' + str(num)
    await ctx.send(num_msg.format(ctx))

#faction: choose a random faction (hexarchate by default, add any term to get heptarchate)

@bot.command()
async def faction(ctx, archate="hexarchate"):
    faction_list = [
        'Andan', 'Nirai', 'Vidona', 'Rahal', 'Kel', 'Shuos'
    ]
    if archate!="hexarchate":
        faction_list.append('Liozh')
    name_msg = '{0.author.mention} '+random.choice(faction_list)
    await ctx.send(name_msg.format(ctx))

#jz: choose a random jeng-zai card
#the keywords "meaning" or "up" will return the meaning of the upright card
#the keywords "read" or "updown" will choose an upright or inverted card randomly

@bot.command()
async def jz(ctx, reading="none"):
    jzdict = {'The Novice': ['New beginnings.  Innocence.', 'Ignorance.  Walking into disaster.'], 'The Poet': ['Praise.  Finding the right words.  The arts.', 'Lamentations.  At a loss for words.'], 'The Inquisitor': ['Adherence to law.  Upright morals.', 'Weak-willed.  Criminal temptations.'], 'The Hexarch': ['Power.  Mastery of those around you.', 'Falling short of your goals.'], 'The Pyre': ['Destruction.  Bad luck.', 'Self-sacrifice.  Loyalty.'], 'The Mathematician': ['The fundamental order of the universe.  Power over the natural world.', 'Disorder.  Natural disaster.'], 'The Courtesan': ['Luxury and wealth.  Romance.  Pleasurable conversation.', 'Lack of social connection.  Poverty.  Loneliness.'], 'The Drowned General:': ['Disaster.  Failure through hubris.', 'Ambition.  A high-risk, high-gain gamble.'], 'The Soldier': ['Conquest.  Success through physical strength.', 'Weakness.  Ill health.'], 'The Scholar': ['Meditation.  Pursuit of knowledge.', 'Frivolity.'], 'The Spinning Coin': ['Chance.  Good luck.', 'Rigidity.  Instability.'], 'The Magistrate': ['Austerity.  Determining the fate of others.', 'Self-indulgence.  Lack of influence.'], 'The Dragon-Horse': ['Travel to faraway place.  Rapid movement.', 'Stagnation.  Besieged.'], 'Death': ['Transformation.  The cycle of existence.', 'Decay.  Festering.'], 'The Heretic': ['Ruination.  Heterodoxy.', 'Precarious situation.  Proceed with caution.'], 'The Empty Hand': ['Potential for advancement.  New possibilities opening up.', 'Trapped in your current position.  Misunderstandings.'], 'The Feast': ['Success in material matters.  An upcoming honor.', 'Lack of recognition for your work.  Struggling to make ends meet.'], 'The Star': ['Clarity.  Hope.', 'Despair.  Calamity.  Confusion.'], 'The Moon': ['Illusion.  Self-deception.  Wishful thinking.', 'Comfort.  Self-knowledge.'], 'The Fortress': ['Protection.  Strength in numbers.', 'Isolation.  Vulnerability.'], 'Judgment': ['Remembrance.', 'Crisis.'], 'The Wheel of Worlds': ['Completion.  Harmony with your surroundings.', 'Emptiness.  Disconnect.  Lack of rapport.'], 'Ace of Gears': ['Change in the natural world.', 'Stagnation in the natural world.  Lack of opportunity.'], 'Deuce of Gears': ['A cog in the machine.  Pawn of powers beyond your control.', 'Devious plans.  Breaking past the boundaries of what is thought possible.'], 'Three of Gears': ["Celebration of the world's riches.", 'Poverty.  Turned away from something you want.'], 'Four of Gears': ['An opportunity has passed you by.  Instability in the natural world.', 'The chance to build something concrete.'], 'Five of Gears': ['An opportunity at the cost of struggle.  Colliding ambitions.', 'Conflict with peers.'], 'Six of Gears': ['Material gains.  Wealth.', 'Bad investments.  Poor planning.'], 'Seven of Gears': ['In danger of losing your wealth.', 'Risky investments.'], 'Eight of Gears': ['Obstacles to advancement.  Hard work ahead.', 'Small reward for a lot of work.'], 'Nine of Gears': ['Recovery from hard work.', 'Working at a disadvantage.'], 'Ten of Gears': ['Too many burdens.  Being taken advantage of by others.', 'Unexpected breakthrough.'], 'Page of Gears': ['Prosperity if you seize the opportunity.  A reliable friend.', 'Lost chance.   Unreliable partner.'], 'Knight of Gears': ['You must keep your world in balance to hold onto your gains.  An engineer.', 'Plans thrown askew by an unexpected event.'], 'Master of Gears': ['Material wealth.  Seeking balance.  A student of the natural world.', 'Wealth slipping away.  The envy of others.'], 'Book of Gears': ['Victory through precision.  Calculated perfection.', 'Chaos.  Lack of harmony.  Poorly thought-out plans.'], 'Ace of Doors': ['A sudden change of position or action.', 'Refusal to consider the options.'], 'Deuce of Doors': ['At a crossroads.  Two opposing possibilities.', 'Indecision.  Stagnation.  Trapped.'], 'Three of Doors': ['An opportunity to be remembered for your actions.', 'Ignominy.  Being disregarded.'], 'Four of Doors': ['A path beyond which there is no returning.  Being backed into a corner.', 'Separation from your allies.'], 'Five of Doors': ['Retreat.  Fleeing the field of battle.', 'Finding shelter.  Temporary respite.'], 'Six of Doors': ['Many fruitful opportunities.', 'Overwhelmed by possibilities.'], 'Seven of Doors': ['Labyrinth.  Betrayal.  Confusion.', 'Finding out more than you wanted to know.'], 'Eight of Doors': ['Victim.  Many doors but no way out.', 'The compassion of a stranger.  An unexpected rescue.'], 'Nine of Doors': ['Unwanted responsibility.  You regret the path you took to get here.', 'Evading responsibility.'], 'Ten of Doors': ['From every door a death, from every mouth a maw.  Utter defeat.', 'A narrow escape.'], 'Page of Doors': ['Exploration.  An inquisitive friend.', 'Getting lost.  A wrong turn taken.'], 'Knight of Doors': ['Charging ahead.  A decisive person.', 'Wrong course of action.  Impulsivity.'], 'Master of Doors': ['Avoidance of outright battle.  A person who understands the entire situation.', 'Fatalism.  Surrender.'], 'Book of Doors': ['Victory by understanding different paths to success.  A map of the situation is at hand.', 'Fundamental misunderstanding of the situation.  Obfuscation.'], 'Ace of Roses': ['A sudden change of heart.', 'Apathy.'], 'Deuce of Roses': ['Celebration.  Happy memories.', 'Disappointment.  Avoidance of the past.'], 'Three of Roses': ['Lovers or companions.  Pleasure.', 'Divorce.  Lack of rapport.'], 'Four of Roses': ['Depression.  Lack of fulfillment.', 'Daydreaming.  Lost in your hopes.'], 'Five of Roses': ['Temporary gloom.', 'Unstable mood.'], 'Six of Roses': ['Joy.  Fulfillment.', 'Unhappiness.  Lack of friends.'], 'Seven of Roses': ['Temptation.  Risk without reward.', 'Caution.  Second-guessing yourself.'], 'Eight of Roses': ['Bitter lessons.', 'Failure to learn better.'], 'Nine of Roses': ['Self-indulgence.  Complacency.', 'Lack of self-control.'], 'Ten of Roses': ['Community.  Accomplishment.', 'Failure.  Brooding.'], 'Page of Roses': ['Amusement.  A friend who listens well.', 'Irony.  Sarcasm.  Someone who ignores you.'], 'Knight of Roses': ['Pride.  An artisan.', 'Pride goes before a fall.'], 'Master of Roses': ['Emotional self-control.  A calm person.', 'A manipulator.'], 'Book of Roses': ['An artistic performance.  Good aesthetic judgment.  Emotional responsiveness.', 'Tawdriness.  Rigidity.'], 'Ace of Eyes': ['A sudden change of opinion.', 'Stubbornness.  Clinging to an outdated plan.'], 'Deuce of Eyes': ['Paradox.  Confusion.', 'Insight.  Wisdom.'], 'Three of Eyes': ['Illusion.  You wonder about a difficult situation.', 'Harsh reality.  No way out.'], 'Four of Eyes': ['Destructive obsession.  Paralysis.', 'Focus.  Intense concentration produces insight.'], 'Five of Eyes': ['Meditation.  Generation of ideas.', 'Disorganized ideas.  Distraction.'], 'Six of Eyes': ['Generosity.  Collaboration.', 'Selfishness.  Squandered opportunity.'], 'Seven of Eyes': ['Stuck in destructive patterns of thought.  Lack of wisdom.', 'Constructive thinking.  A plan comes clear.'], 'Eight of Eyes': ['The importance of being well-prepared.', 'Trying to prepare for the wrong things.'], 'Nine of Eyes': ['Prevailing through cunning.  The wisdom that comes with age.', 'Too clever for your own good.  Counterproductive scheming.'], 'Ten of Eyes': ['Knowledge.  Inspiration.', "Copying others' ideas.  Lack of originality."], 'Page of Eyes': ['Optimism.  Keeping your eyes open.  A knowledgeable friend.', 'Pessimism.  Too much information or misinformation.'], 'Knight of Eyes': ['Working toward a goal.  A strategist.', 'Your plans collapse under their own weight.'], 'Master of Eyes': ['Self-understanding.  An expert in their field.', 'Self-deception.']}
    card = random.choice(list(jzdict.keys()))
    card_msg = '{0.author.mention} ' + card
    if reading == "meaning" or reading == "up":
        card_msg = card_msg + ": " + jzdict[card][0]
    if reading == "read" or reading == "updown":
        rev = random.randint(0,1)
        if rev ==1:
            card_msg = card_msg + ", Reversed" 
        card_msg = card_msg + ": " + jzdict[card][rev]
    await ctx.send(card_msg.format(ctx))

bot.run(TOKEN)
