import sys
import time
thu = """It's Thunderclan!
    s+`                   `+s  
    mMmo.               -sNMh  
    mMMMNy:          `:hNMMMh  
    mMMMMMNdhyyyyyyyhdNMMMMMh  
    :ymMMMMMMMMMMMMMMMMMMMMMh  
      .+hNMMNNMMMMMMMMMMMMMMh  
        `-smh:yNMMMMMMMMMMMMh  
    `      `-  .omMMMMMMMMMMh  
    ys:`         `/hNdNMMMMMh  
    mMMmy:`  ..`    :.-smMMMh  
    mMMMMMmy/sNds/.`  ` .+mMh  
    mMMMMMMMMMMMMMMdy/ys:``/o  
    mMMMMMMMMMMMMMMMMMMMMms-   
    ooooooooooooooooooooooooo
    """
riv = """It's Riverclan
    *                       * 
    -Ns-                  -sN- 
    dMMmo`              :hMMM- 
    dMMMMNs-         `+mMMMMM- 
    dMMMMMMMMMMMMMMMMMMMMMMMM- 
    dMMMMMMMMMMMMMMMMMMMMMMMM- 
    dMMMMMmyo/yMMMMMNdyoNMMMM- 
    dmy+-```  omhs/-`  `hdhhh. 
    ` ./ymMo    ./ydNo/::/+sy. 
    +dMMMMMMdyhNMMMMMMMMMMMMM- 
    dMMMMMMmhsdMMMMMMMdyNMMMM- 
    dMmy+-`   oMNds/-` `mNNmm- 
    -` -+ymo  ```-+yh/-..-:/+` 
    :yNMMMMNs+shNMMMMMMMMMMMM- 
    :////////////////////////: 
    """
win = """It's Windclan!
    .                        . 
    sm+`                  `+my 
    sMMNs.              .oNMMy 
    sMMMMMh:          -yNMMMMy 
    sMMMMMMMNNNNNNNNNNMMMMMMMy 
    sMMMMMMMMMMNmdddNMMMMMMMMy 
    sMMMMMMMMd./hmNmy//dMMMMMy 
    sMMMMMMMMm:/yyyMMM+`NMMMMy 
    sMMMMMMMMMMMNNMMMN-.NMMMMy 
    -///+oydNMMMMMMmo``shhyyho 
        ```  `://:`            
    /dmMMMMmy+-`   `-/shmmdho. 
    sMMMMMMMMMMMNmNMMMMMMMMMMy 
    sMMMMMMMMMMMMMMMMMMMMMMMMy 
    :oooooooooooooooooooooooo: 
    """
sha = """It's Shadowclan!
     \s                      /s
    +MNy-                 `omMd
    +MMMMh:             -sNMMMd
    +MMMMMMmo++++++++++hMMMMMMd
    +MMMMMMMMMMMMMMMMMMMMMMMMMd
    +MMMMMMMMMMMMMMMMMMMMMMMMMd
    +MMMMMMMMMMMMMMMMMMMMMMMMMd
    +MMN/::::yMMMMMMN/...-sMMMd
    +MMMmo++yMMMMMMMMNyoodMMMMd
    +MMMMMMMMMMMMMMMMMMMMMMMMMd
    +MMMMMMMMMMMMMMMMMMMMMMMMMd
    +MMMMMMMMMNho//oyNMMMMMMMMd
    +MMMMMMMMh.      `sMMMMMMMd
    +MMMMMMMN`         dMMMMMMd
    """
sta = """It's Starclan!
    |-                      -|  
    hMh/                  :hMh  
    hMMMm+`            `+mMMMh  
    hMMMMMNs::::::::::sNMMMMMh  
    hMMMMMMMMMMMMMMMMMMMMMMMMh  
    hMMMMMMMMMMMMMMMMMMMMMMMMh  
    hMMMMMMMMMMMNdMMMMMMMMMMMh  
    hMMMMMMMMMMN:`dMMMMMMMMMMh  
    hMMmhhhhhhh:  `syyyyyydMMh  
    hMMMd/`             -yNMMh  
    hMMMMMmo.        `/dMMMMMh  
    hMMMMMMd.        `oMMMMMMh  
    hMMMMMs`           :mMMMMh  
    hMMMm:              `yMMMh  
    .:::`                 :::.  
    """
sky = """It's Skyclan!
    *                        *   
    :y-                    :y:`  
    :ddy-                -yddo/  
    :dddds--------------sdddds/  
    :dddddddddddhhhdddddddddds/  
    :dddddddddyyyo:oddddddddds/  
    :ddddddhhyo+`   oyhdddddds/  
    :dddddyys:.      `.oddddds/  
    :dddddyo           +ddddds/  
    :ddddhy+           -ydddds/  
    :ddddoh.            .dddds/  
    :dddds:        `   `+dddds/  
    :ddddddo+oy.   os+ohddddds/  
    :hyhhhhhhhss`  .+yhhhhhhhs/  
    """
clans = [thu, riv, win, sha, sta, sky]
print("Hi! What is your name? ")
name = input()
print("Hi,", name, '!', sep='')
print("Do you like Warrior Cats?")
print("Type 'y' or 'n' and press Enter")
answer = input()
if answer == "y":
    import pyglet

    sound = pyglet.media.load('mysound.mp3', streaming=False)
    sound.play()
    pyglet.app.run()
    while answer == "y":
        from time import sleep
        print("""
           _.---.._             _.---...__
        .-'   /\   \          .'  /\     /
        `.   (  )   \        /   (  )   /
          `.  \/   .'\      /`.   \/  .'
            ``---''   )    (   ``---''
                    .';.--.;`.
                  .' /_...._\ `.
                .'   `.a  a.'   `.
               (        \/        )
                `.___..-'`-..___.'
                   \          /
                    `-.____.-'
        """)
        print("Great!")
        sleep(1)
        print("Let's play Warrior Guess!")
        sleep(3)
        print("As you know, there are six WC clans.")
        sleep(3)
        print("Try to guess, wich one i'm thinking about?")
        sleep(3)

        from time import sleep
        loading = 'You only have three attempts!'
        for i in range(29):
            print(loading[i], end='', flush=True);
            sleep(0.1)
        import random
        guess = random.choice(clans)
        print("""
              Press:
              1 for Thunderclan
              2 for Riverclan
              3 for Windclan
              4 for Shadowclan
              5 for Starclan
              6 for Skyclan
               """)
        # print(guess) Test guess = random.choice(clans)
        attempt = 0
        while attempt < 3:
            answer_guess = int(input())
            if answer_guess - 1 == clans.index(guess):
                print("Yeah!")
                print(guess)
                attempt = 3
            else:
                print("Nope! Try again!")
                attempt += 1
                if attempt == 3:
                    from time import sleep
                    loading = "You loose!"
                    for i in range(10):
                        print(loading[i], end='', flush=True)
                        sleep(0.2)
                    print("""
                               .'\   /`.
                             .'.-.`-'.-.`.
                        ..._:   .-. .-.   :_...
                      .'    '-.(o ) (o ).-'    `.
                     :  _    _ _`~(_)~`_ _    _  :
                    :  /:   ' .-=_   _=-. `   ;\  :
                    :   :|-.._  '     `  _..-|:   :
                     :   `:| |`:-:-.-:-:'| |:'   :
                      `.   `.| | | | | | |.'   .'
                        `.   `-:_| | |_:-'   .'
                          `-._   ````    _.-'
                              ``-------''
                    """)
        print("Shall we play again?")
        print("Type 'y' or 'n' and press Enter")
        answer = input()
elif answer == "n":
    from time import sleep
    print("OK... ", end='')
    sleep(1)
    print("""
    |\---/|
    | o_o |
     \_^_/ """)
    print("By, ",  end='')
    sleep(1)
    print("then...")
    sleep(2)
    input("\n\nPress the Enter key")
else:
    print("Learn to read and come to play with me!")
    from time import sleep
    sleep(4)
# sys.exit()
# print("\a")
print("""
     *        |\___/|               *
              )     (             .    *          '
        *    =\     /=    .
               )===(       *
            . /     \           *            *
     .        |     |                 .
             /       \     
             \       /
      _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
      |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
      |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
      |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
      |W |A |R |R |I |O |R |  |G |U |E |S |S |  |
""")
input("\n\nPress the Enter key to exit")