import random
import time
print("Hi! What is your name? ")
name = input()
print("Hi,", name)
print("Do you like Warrior Cats?")
print(" Type 'y' or 'n' and push Enter")
answer = input()
if answer == "n":
    from time import sleep
    print("OK... ", end='')
    sleep(1)
    print("""
    |\---/|
    | o_o |
     \_^_/ """)
    print("By, ",  end='')
    sleep(2)
    print("then...")
    sleep(2)
    input("\n\nPress the Enter key to exit")
elif answer == "y":
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
    print("Great! \nThen you probably want to play my game.")
    sleep(1)
    print("As you know, there are five WC tribes")
    sleep(1)
    print("Try to guess, wich of WC tribes i'm thinking about?")
    sleep(1)
    print()


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
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
""")
input("\n\nPress the Enter key to exit")