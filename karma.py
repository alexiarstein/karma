############ KARMA IMPLEMENTATION ##############
# Author: Alexia Michelle <alexiarstein@aol.com>
# Use: integrate as part of an existing discord bot in python
# License: GNU GPL v3 (See LICENSE / COPYING for more info)


# Karma database file
karma_file = 'karma.txt'

# Load existing karma data into a dictionary
karma_data = {}
if os.path.exists(karma_file):
    with open(karma_file, 'r') as file:
        for line in file:
            entry, score = line.strip().split(',')
            karma_data[entry] = int(score)

@bot.event
async def on_message(message):
    if message.content.startswith('!karma'):
        # Handle karma commands
        await handle_karma_command(message)
    else:
        # Update karma on valid karma messages
        update_karma(message)
    
    await bot.process_commands(message)

# Corrects !karma without args to display only the top 5 entries and not the whole database. 
# Issue: https://github.com/alexiarstein/karma/issues/2
async def handle_karma_command(message):
    if message.content == '!karma':
        # Display top 5 entries
        sorted_karma = sorted(karma_data.items(), key=lambda x: x[1], reverse=True)[:5]
        top_entries = '\n'.join([f'{entry}: {score}' for entry, score in sorted_karma])
        await message.channel.send(f'Top 5 del karma más bello:\n{top_entries}')
    else:
        # Display karma for a specific entry
        entry = message.content[len('!karma '):]
        karma_score = karma_data.get(entry, 0)
        await message.channel.send(f'Karma para {entry}: {karma_score}')



def update_karma(message):
    # Parse message for karma updates
    words = message.content.split()

    # Parse message for karma updates
    words = message.content.split()[1:]
    # define action to store the add or substraction
    action = ""
    # variable that holds the desired tech, person or thing to value
    entry = ""

    # if the content of the message contains an space, or the same
    # that is has more than one word
    if len(words) >= 2:
        action = words[-1][-2:]
        # join all words except the last one
        entry = f"{' '.join(words[:-1])} {words[-1][:-2]}"
    else:
        entry = words[0][:-2]
        action = words[0][-2:]

    if action =='++':
        karma_data[entry] = karma_data.get(entry, 0) + 1
        save_karma_data()
    elif action == '--':
        karma_data[entry] = karma_data.get(entry, 0) - 1
        save_karma_data()

def save_karma_data():
    # Save karma data to the file
    with open(karma_file, 'w') as file:
        for entry, score in karma_data.items():
            file.write(f'{entry},{score}\n')

