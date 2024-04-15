# cartomancy planning
'''
1. make a dictionary nested of all the cards wih meanings
2. add user input so user can pick the cards and returns the meanings 
3. add ability for user to also input a number instead of spelling the number out
4. add a way for the user to get the explanation of another card if wanted or will quit the program
'''


card_suits = {
    'spades': {
        "Ace": "Endings, misfortune",
        "Two": "Tough decisions, deceit, change",
        "Three": "Trouble in relationships, infidelity",
        "Four": "Illness, broken promises",
        "Five": "Obstacles and difficulty, eventual success",
        "Six": "Improvement, small wins, upswing",
        "Seven": "Bad advice, grief, loss",
        "Eight": "Deceit, danger, caution is advised",
        "Nine": "Bad luck, depression, anxiety",
        "Ten": "Bad news, worry, imprisonment",
        "Jack": "An unpleasant or immature young person with black hair",
        "Queen": "A dark-haired woman or widow",
        "King": "A dark-haired selfish but ambitious older man"
    },
    'hearts': {
        "Ace": "New relationships, friendship",
        "Two": " Good fortune in love and relationships, prosperity, Affection, lust, and success",
        "Three": "A new friendship or relationship, remain cautious and guarded with your words, Importance.",
        "Four": " Change is coming, possible travel, return of an old partner, or taking the next step in a relationship.",
        "Five": "Jealousy, resentment, loss of love, deceit, or illness.",
        "Six": "A pleasant surprise, a new love interest, Unexpected.",
        "Seven": "Broken promises, second chances, emotional decisions.",
        "Eight": "Invitations, surprise visitors, ending of a friendship or romance.",
        "Nine": " The wish card. Wishes, desires, and dreams are fulfilled.",
        "Ten": "Good fortune, success, fulfillment, but the possibility of family issues needing attention.",
        "Jack": "A young man you may be close with. Could be a friend, brother, or a romantic interest. May be blonde.",
        "Queen": "A kind, good-natured blonde woman who may be a friend, sister, aunt, or even a girlfriend. ",
        "King": "Represents a man who is good-natured, loving, and gives good advice. Possibly a paternal life figure."
    },
    'diamonds': {
        "Ace": "A gift, a new beginning, a message, improvement, and the beginnings of your energy work.",
        "Two": "A disagreement within a relationship, disapproval of a relationship, an affair, and making or receiving payment.",
        "Three": "Legal issues, family issues, teamwork, poor focus, and instability.",
        "Four": "Unexpected gift or inheritance, gaining financial stability, trust, and improvement.",
        "Five": "Positive energy, happy home, Improvements, and success in business ventures.",
        "Six": "Troubles, disagreements, poor communication, jealousy, issues in a second marriage.",
        "Seven": "Confusion, challenges, and problems at work.",
        "Eight": " Surprise romance or a marriage later in life. Possibility of travel and planning with caution.",
        "Nine": "New business opportunities, success, surprise money, and changes.",
        "Ten": "Positive change, success, good fortune, financial prosperity, and good luck.",
        "Jack": "An unreliable and dishonest young person. Might be a family member.",
        "Queen": "An outgoing, successful, and reliable woman.",
        "King": "An accomplished older man who holds a position of authority, Stubborn but also reliable. "
    },
    'clubs': {
        "Ace": "Happiness, good financial fortune, good news, and the possibility of a new business venture.",
        "Two": "Challenges, a new social or business correspondence that may lead to gossip from those who oppose you.",
        "Three": "Successful marriage, advancements, growth, wealthy partner, or partner with a wealthy family.",
        "Four": "Deceit or betrayal from a trusted friend, a change for the worse.",
        "Five": "New friendships, changes in work or social situation, support, marital success.",
        "Six": "Financial support, prosperity, Improvement, progress, or completion of a business or social goals.",
        "Seven": "Business success, changes, potential trouble from a romantic partner.",
        "Eight": "Trouble and turmoil in business relations, love, and personal relationships.",
        "Nine": "New opportunities, new admirer, luck, but a warning against stubbornness.",
        "Ten": "Good fortune, money from unexpected sources, travel that is possibly related to business.",
        "Jack": " A dark-haired young person, generally male, who is reliable and trustworthy.",
        "Queen": "A dark-haired woman, usually a colleague, who is charming, confident, and helpful.",
        "King": "A strong, dark-haired man, commonly older, who is kind, honest, and loving."
    }
}
# asks user for the symbol of the card


def get_symbol():
    user_symbol = input(
        "What was the suit of the card?\n Ex. Ace of Spades will be simply: Spades\n").lower()
    return str(user_symbol)

# asks user for the name of the card


def get_name():
    user_name = input(
        "What was the name of the card?\n Ex. Ace of Spades will be simply: Ace.\n If unknown press enter to enter the number shown.\n").lower()
    return str(user_name)


# asks user for number incase they do not know the name
def get_number():
    user_number = input(
        "What was the number of the card?\n For Jack = 11 \n For Queen = 12 \n For King = 13\n")
    user_digit = int(user_number)
    for suit, suit_info in card_suits.items():
        for i, num in enumerate(suit_info):
            if (i + 1) == user_digit:
                return num

symbol = get_symbol()
name = get_name()
num = get_number()

# takes in the symbol of the card and the name and then will return the card meaning
def get_description(symbol, name, num):
    for suit, suit_info in card_suits.items():
        if symbol.lower() == suit.lower():
            for card_name, card_description in suit_info.items():
                if card_name.lower() == name or card_name.lower() == num.lower():
                    return card_description


# asks user the questions for the card symbol, name, and number then returns the description

print("I found the description!\n")
print(get_description(symbol, name, num))



def user_wants_continue():
  while True:
    user_continue = input("Do you want to find out more?\n Yes/No\n")
    if user_continue == 'yes' or user_continue == 'Yes':
        return str(user_continue)
        break
    elif user_continue == 'no'or user_continue == 'No':
        return str(user_continue)
        break
    else:
        print("\nYou have to choose Yes or No")   

answer = user_wants_continue()

def another_card(answer):
  if answer.lower() == "yes":
    return print(get_description(get_symbol(), get_name(), get_number()))
  elif answer.lower() == "no":
    return quit()

print(another_card(answer))
  