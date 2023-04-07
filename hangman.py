import random
import time
import io

fails = 0
word_bank = ["about","account","across","addition","adjustment","advertisement","after","again","against","agreement","almost","among","amount","amusement","angle","angry","animal","answer","apparatus","apple","approval","argument","attack","attempt","attention","attraction","authority","automatic","awake","balance","basin","basket","beautiful","because","before","behaviour","belief","berry","between","birth","bitter","black","blade","blood","board","boiling","bottle","brain","brake","branch","brass","bread","breath","brick","bridge","bright","broken","brother","brown","brush","bucket","building","burst","business","butter","button","camera","canvas","carriage","cause","certain","chain","chalk","chance","change","cheap","cheese","chemical","chest","chief","church","circle","clean","clear","clock","cloth","cloud","collar","colour","comfort","committee","common","company","comparison","competition","complete","complex","condition","connection","conscious","control","copper","cotton","cough","country","cover","crack","credit","crime","cruel","crush","current","curtain","curve","cushion","damage","danger","daughter","death","decision","degree","delicate","dependent","design","desire","destruction","detail","development","different","digestion","direction","dirty","discovery","discussion","disease","disgust","distance","distribution","division","doubt","drain","drawer","dress","drink","driving","early","earth","education","effect","elastic","electric","engine","enough","equal","error","event","every","example","exchange","existence","expansion","experience","expert","false","family","father","feather","feeble","feeling","female","fertile","fiction","field","fight","finger","first","fixed","flame","flight","floor","flower","foolish","force","forward","frame","frequent","friend","front","fruit","future","garden","general","glass","glove","government","grain","grass","great","green","group","growth","guide","hammer","hanging","happy","harbour","harmony","healthy","hearing","heart","history","hollow","horse","hospital","house","humour","important","impulse","increase","industry","insect","instrument","insurance","interest","invention","island","jelly","jewel","journey","judge","kettle","knife","knowledge","language","laugh","learning","leather","letter","level","library","light","limit","linen","liquid","little","living","loose","machine","manager","market","married","match","material","measure","medical","meeting","memory","metal","middle","military","minute","mixed","money","monkey","month","morning","mother","motion","mountain","mouth","muscle","music","narrow","nation","natural","necessary","needle","nerve","night","noise","normal","north","number","observation","offer","office","operation","opinion","opposite","orange","order","organization","ornament","other","owner","paint","paper","parallel","parcel","paste","payment","peace","pencil","person","physical","picture","place","plane","plant","plate","please","pleasure","plough","pocket","point","poison","polish","political","porter","position","possible","potato","powder","power","present","price","print","prison","private","probable","process","produce","profit","property","prose","protest","public","punishment","purpose","quality","question","quick","quiet","quite","range","reaction","reading","ready","reason","receipt","record","regret","regular","relation","religion","representative","request","respect","responsible","reward","rhythm","right","river","rough","round","scale","school","science","scissors","screw","second","secret","secretary","selection","sense","separate","serious","servant","shade","shake","shame","sharp","sheep","shelf","shirt","shock","short","silver","simple","sister","skirt","sleep","slope","small","smash","smell","smile","smoke","smooth","snake","sneeze","society","solid","sound","south","space","spade","special","sponge","spoon","spring","square","stage","stamp","start","statement","station","steam","steel","stick","sticky","stiff","still","stitch","stocking","stomach","stone","store","story","straight","strange","street","stretch","strong","structure","substance","sudden","sugar","suggestion","summer","support","surprise","sweet","system","table","taste","teaching","tendency","theory","there","thick","thing","thought","thread","throat","through","through","thumb","thunder","ticket","tight","tired","together","tomorrow","tongue","tooth","touch","trade","train","transport","trick","trouble","trousers","winter","woman","wound","writing","wrong","yellow","yesterday","young"]

def render():
    global fails
    if fails == 1:
        print("""
         ==============
         |      |
         |     _|_
         |    /   \\
         |    \\___/
         |
         |
         |
         |
         |
         |
         |
        ==================
        """)
    elif fails == 2:
        print("""
         ==============
         |      |
         |     _|_
         |    /   \\
         |    \\___/
         |      |
         |      |
         |      |
         |      |
         |
         |
         |
        ==================
        """)
    elif fails == 3:
        print("""
         ==============
         |      |
         |     _|_
         |    /   \\
         |    \\___/
         |      |
         |   ---|
         |      |
         |      |
         |
         |
         |
        ==================
        """)
    elif fails == 4:
        print("""
         ==============
         |      |
         |     _|_
         |    /   \\
         |    \\___/
         |      |
         |   ---|---
         |      |
         |      |
         |
         |
         |
        ==================
        """)
    elif fails == 5:
        print("""
         ==============
         |      |
         |     _|_
         |    /   \\
         |    \\___/
         |      |
         |   ---|---
         |      |
         |      |
         |     /
         |    /
         |
        ==================
        """)
    elif fails == 6:
        print("""
         ~~~~ RIP ~~~~
         ==============
         |      |
         |     _|_
         |    /X X\\
         |    \\___/
         |      |
         |   ---|---
         |      |
         |      |
         |     / \\
         |    /   \\
         |
        ==================
        """)

def play_hangman():
    global fails
    guesses = []
    try:
        f = open("./hangman.txt")
        word = f.readline().strip()
        cur_str = ["_" for i in range(len(word))]
        prev_guesses = f.readline().strip()
        for g in prev_guesses:
            guesses.append(g)
            indices = [i for i in range(len(word)) if word[i] == g]
            for x in indices:
                cur_str[x] = g
        fails = int(f.readline())
        f.close()
        f = open("./hangman.txt", "w")
        f.close()
        print("\nContinuing saved game state.")
        print(f"Current word: {cur_str}")
    except io.UnsupportedOperation:
        word = random.choice(word_bank)
        cur_str = ["_" for i in range(len(word))]
    except FileNotFoundError:
        word = random.choice(word_bank)
        cur_str = ["_" for i in range(len(word))]
    print(f"Your word has {len(word)} letters.")
    while True:
        guess = input("Guess a letter (# to quit)\n")
        if guess == "#":
            f = open("./hangman.txt", "w")
            f.write(word + "\n")
            for g in guesses:
                f.write(g)
            f.write("\n")
            f.write(str(fails))
            f.close()
            print("Progress saved.")
            time.sleep(2)
            break
        elif len(guess) > 1 or not guess.isalpha():
            print("Please enter a valid guess (one letter long)")
            continue
        else:
            if guess in word:
                guesses.append(guess)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for x in indices:
                    cur_str[x] = guess
            else:
                fails += 1
            print(f"\nCurrent word: {cur_str}")
            render()
            if fails == 6:
                print("You lose!\n")
                break
            if "_" not in cur_str:
                print("You win!\n")
                break
            time.sleep(1)