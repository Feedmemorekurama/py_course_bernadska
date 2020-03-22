attack_wolf = ["sheep","sheep","sheep","wolf","sheep"]

attack_wolf.reverse()
for i in attack_wolf: 
    if attack_wolf.index("sheep") == 0 and attack_wolf.index("wolf") == 1:
        print("Oi! Sheep number 1! You are about to be eaten by a wolf!")
        break
    else:
        print("Wolf will eat another sheep")