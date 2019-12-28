
print("**********************************WELCOME TO HANGMAN***************************************************")
print("*                                                                                                     *")
print("*                                 DEVELOPED BY SAJAN POUDEL                                           *")
print("*                                                                                                     *")
print("*                                                                                                     *")
print("*******************************************************************************************************")
print("\n""\n" "YOU HAVE TO GUESS THE WORDS IN 3 attempt")
import string
import random
userdata = ''

def main():

    keywords = ['cres',
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
    'zoo']
   
    randomstring = random.choice(keywords)
    #print(randomstring)
    res = []
    res[:0]= randomstring
    a = int((len(randomstring)))
    global userdata
    e=[]
    for i in range(a):
        e.insert(i,'_')

    print(e) # Print The Empty Array at First

    count=3 # attemp count to complete the puzzle 

    while(count>0):
        if(e == res):
            break
        else:
            userdata = (input("\nPLEASE GUESS THE WORD > "))
            truecount=0
            for i in range(a):
                if(res[i]==userdata):
                    e[i]=userdata
                    truecount= truecount + 1              
            
            if(truecount<1):
                count=count-1
                print('Worng Word. Try Again \n')                          
               
            truecount=0
            print(e)

       
    if (e == res):
        print("YOUR GUESS {} WAS RIGHT: ".format(randomstring))
    
    else:
        print("NEXT TRY!!! \n the correct answer was: {}".format(randomstring))
    

main()


 