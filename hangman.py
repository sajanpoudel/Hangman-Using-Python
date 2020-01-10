import string
import random

WORDS = [
    'cres',
    'adult',
    'advice',
    'arrangement',
    'attempt',
    'august',
    'autumn',
    'border',
    'breeze',
    'brick',
    'calm',
    'canal',
    'casey',
    'cast',
    'chose',
    'claws',
    'coach',
    'constantly',
    'contrast',
    'cookies',
    'customs',
    'damage',
    'danny',
    'deeply',
    'depth',
    'discussion',
    'doll',
    'donkey',
    'egypt',
    'ellen',
    'essential',
    'exchange',
    'exist',
    'explanation',
    'facing',
    'film',
    'finest',
    'fireplace',
    'floating',
    'folks',
    'fort',
    'garage',
    'grabbed',
    'grandmother',
    'habit',
    'happily',
    'harry',
    'heading',
    'hunter',
    'illinois',
    'image',
    'independent',
    'instant',
    'January',
    'kids',
    'label',
    'lee',
    'lungs',
    'manufacturing',
    'Martin',
    'mathematics',
    'melted',
    'memory',
    'mill',
    'mission',
    'monkey',
    'mount',
    'mysterious',
    'neighborhood',
    'norway',
    'nuts',
    'occasionally',
    'official',
    'ourselves',
    'palace',
    'pennsylvania',
    'philadelphia',
    'plates',
    'poetry',
    'policema',
    'positive',
    'possibly',
    'practical',
    'pride',
    'promised',
    'recall',
    'relationship',
    'remarkable',
    'require',
    'rhyme',
    'rocky',
    'rubbed',
    'rush',
    'sale',
    'satellites',
    'satisfied',
    'scared',
    'selection',
    'shake',
    'shaking',
    'shallow',
    'shout',
    'silly',
    'simplest',
    'slight',
    'slip',
    'slope',
    'soap',
    'solar',
    'species',
    'spin',
    'stiff',
    'swung',
    'tales',
    'thumb',
    'tobacco',
    'toy',
    'trap',
    'treated',
    'tune',
    'university',
    'vapor',
    'vessels',
    'wealth',
    'wolf',
    'zoo',
]


def print_banner():
    """Show the welcome message and the rules of the game."""
    print("**********************************WELCOME TO HANGMAN***************************************************")
    print("*                                                                                                     *")
    print("*                            SAMPLE EXAMPLE BY SAJAN POUDEL                                           *")
    print("*                                                                                                     *")
    print("*                                                                                                     *")
    print("*******************************************************************************************************")
    print("\n""\n" "YOU HAVE TO GUESS THE WORDS IN 3 attempt")


userdata = ''

MAX_ATTEMPTS = 3
BLANK = '_'


MAX_ATTEMPTS = 3
BLANK = '_'


def main():

    randomstring = random.choice(WORDS)
    res = list(randomstring)
    a = len(randomstring)
    e = [BLANK] * a

    print(e) # Print The Empty Array at First

    count = MAX_ATTEMPTS # attempts left to complete the puzzle

    while count > 0:
        if e == res:
            break
        else:
            userdata = input("\nPLEASE GUESS THE WORD > ")
            truecount = 0
            for i in range(a):
                if res[i] == userdata:
                    e[i] = userdata
                    truecount = truecount + 1

            if truecount < 1:
                count = count - 1
                print('Worng Word. Try Again \n')

            print(e)

    if e == res:
        print("YOUR GUESS {} WAS RIGHT: ".format(randomstring))

    else:
        print("NEXT TRY!!! \n the correct answer was: {}".format(randomstring))


print_banner()
main()
