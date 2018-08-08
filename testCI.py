import os
map_sokoban = {
    "size_x":4,
    "size_y":4
}
player = {"x":1,"y":2}
ex = {"x":3,"y":2}
key = {"x":2,"y":1}

playing = True
is_key = False
while playing:
    os.system ('clear')
    for y in range (map_sokoban["size_y"]):
        for x in range (map_sokoban["size_x"]):
            pic = '- '
            if ex["x"] == x and ex["y"] == y:
                pic = 'E '
            if x==key['x'] and y==key['y']:
                pic = 'K '
            if x==player["x"] and y==player["y"] :
                pic = 'P '
            print (pic, end='')
            
            
        print()

    move = input ("Your move: ").upper()
    dx = 0
    dy = 0
    if move == "W":
        dy=-1
    elif move =="S":
        dy =1
    elif move == "D":
        dx =1
    elif move == "A":
        dx=-1
    elif move == "Q":
        playing = False
        break
    else :
        playing = True
        
    if 0 <= player['x'] + dx < map_sokoban['size_x'] and 0 <= player['y'] + dy < map_sokoban['size_y']:
        player['x'] += dx
        player['y'] += dy
        if player['x'] == key['x'] and player['y'] == key['y']:
            key = {'x':-1,'y':-1}
            is_key = True
        win = True
        if player["x"] != ex["x"] or player["y"] != ex["y"] or is_key != True:
            win = False
        if win == True:
            print ("You win")
            playing = False
            break