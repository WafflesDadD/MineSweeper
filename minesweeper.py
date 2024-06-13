import pygame as pg
import sys
import time
import random
from pygame.locals import *

won = False
lost = False

TW= 50
TH= 50

boardX=12
boardY=12
mineCount=28
board = [[0 for i in range(boardX)] for j in range(boardY)]
isFlagged = [[0 for i in range(boardX)] for j in range(boardY)]
isChecked = [[0 for i in range(boardX)] for j in range(boardY)]
width = (TW * boardX)
height = (TH * boardY) + TH

isPlaying = False
screen = 'menu'
mode = 'nothing'

pg.init()
fps = 20
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((300,400), 0, 32)
pg.display.set_caption("MineSweeper")
 

menu_window = pg.image.load("BaseGameStart.png")
easy_tab = pg.image.load("EasyGameStart.png")
mid_tab = pg.image.load("MediumGameStart.png")
hard_tab = pg.image.load("HardGameStart.png")
lose_screen = pg.image.load("loseScreen.png")
win_screen = pg.image.load("winScreen.png")
black = pg.image.load("black.png")

menu_window = pg.transform.scale(menu_window, (300,400))
easy_tab = pg.transform.scale(easy_tab, (300,400))
mid_tab = pg.transform.scale(mid_tab, (300,400))
hard_tab = pg.transform.scale(hard_tab, (300,400))
lose_screen = pg.transform.scale(lose_screen, (300,400))
win_screen = pg.transform.scale(win_screen, (300,400))

tile_img = pg.image.load("tile_modified.png")
flag_img = pg.image.load("flag_modified.png")
mine_img = pg.image.load("mine_modified.png")
boom_img = pg.image.load("boom_modified.png")
clear_img = pg.image.load("clear_tile_modified.png")
menu_img = pg.image.load("menu_tile.png")
restart_img = pg.image.load("restart_tile.png")
continue_img = pg.image.load("continue_tile.png")

tile_img = pg.transform.scale(tile_img, (TW, TH))
flag_img = pg.transform.scale(flag_img, (TW, TH))
mine_img = pg.transform.scale(mine_img, (TW, TH))
boom_img = pg.transform.scale(boom_img, (TW, TH))
clear_img = pg.transform.scale(clear_img, (TW, TH))
menu_img = pg.transform.scale(menu_img, (TW, TH))
restart_img = pg.transform.scale(restart_img, (TW, TH))
continue_img = pg.transform.scale(continue_img, (TW, TH))

tile1_img = pg.image.load("1_tile.png")
tile2_img = pg.image.load("2_tile.png")
tile3_img = pg.image.load("3_tile.png")
tile4_img = pg.image.load("4_tile.png")
tile5_img = pg.image.load("5_tile.png")
tile6_img = pg.image.load("6_tile.png")
tile7_img = pg.image.load("7_tile.png")
tile8_img = pg.image.load("8_tile.png")

tile1_img = pg.transform.scale(tile1_img, (TW, TH))
tile2_img = pg.transform.scale(tile2_img, (TW, TH))
tile3_img = pg.transform.scale(tile3_img, (TW, TH))
tile4_img = pg.transform.scale(tile4_img, (TW, TH))
tile5_img = pg.transform.scale(tile5_img, (TW, TH))
tile6_img = pg.transform.scale(tile6_img, (TW, TH))
tile7_img = pg.transform.scale(tile7_img, (TW, TH))
tile8_img = pg.transform.scale(tile8_img, (TW, TH))



def menu_screen():
    global boardX, boardY, mineCount, board, mode, isFlagged, width, height, MCR, TR
    go = True
    easy = False
    mid = False
    hard = False
    screen = pg.display.set_mode((300,400), 0, 32)
    screen.blit(menu_window, (0, 0))
    pg.display.update()
    while go:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                event.button
                x, y = pg.mouse.get_pos()
                if x > 60 and x < 240 and y > 260 and y < 310:
                        go = False
                if easy == False and mid == False and hard == False:
                    if x > 40 and x < 260 and y > 85 and y < 125:
                        easy = True
                    elif x > 40 and x < 260 and y > 125 and y < 175:
                        mid = True
                    elif x > 40 and x < 260 and y > 175 and y < 215:
                        hard = True
        x, y = pg.mouse.get_pos()
        if easy == False and mid == False and hard == False:
            if x > 40 and x < 260 and y > 85 and y < 125:
                screen.blit(easy_tab, (0, 0))
                pg.display.update()
            elif x > 40 and x < 260 and y > 125 and y < 175:
                screen.blit(mid_tab, (0, 0))
                pg.display.update()
            elif x > 40 and x < 260 and y > 175 and y < 215:
                screen.blit(hard_tab, (0, 0))
                pg.display.update()
             
        if easy:
            boardX=16
            boardY=12
            mineCount=22
            mode='Easy'
        elif mid:
            boardX=18
            boardY=14
            mineCount=36
            mode='Medium'
        elif hard:
            boardX=20
            boardY=16
            mineCount=60
            mode='Advanced'
            
        pg.display.update()
        CLOCK.tick(fps)
    start()

def start():
    global boardX, boardY, mineCount, board, isFlagged, isChecked, width, height, MCR, TR, won, lost
    won = False
    lost = False
    MCR= mineCount
    TR = (boardX*boardY) - mineCount
    board = [[0 for i in range(boardX)] for j in range(boardY)]
    isFlagged = [[0 for i in range(boardX)] for j in range(boardY)]
    isChecked = [[0 for i in range(boardX)] for j in range(boardY)]
    width = (TW * boardX)
    height = (TH * boardY) + TH
    screen = pg.display.set_mode((width, height), 0, 32)

    for i in range(boardX):
        for j in range(boardY):
            screen.blit(tile_img, (i*TW,j*TH))
    
    draw_status()
    mine_placing()



def win(): #needs work
    global won
    won = True
    go1 = True
    go2 = True
    draw_status()
    while go1:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                event.button
                x, y = pg.mouse.get_pos()
                if x > (2*width/3)-50 and x < (2*width/3)+50 and y > height-TH and y < height:
                    screen = pg.display.set_mode((300,400), 0, 32)
                    screen.blit(win_screen, (0, 0))
                    pg.display.update()
                    go1 = False
                elif x > (width/3)-50 and x < (width/3)+50 and y > height-TH and y < height:
                    menu_screen()
                    go1 = False
                    go2 = False

        pg.display.update()
        CLOCK.tick(fps)
    while go2:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                event.button
                x, y = pg.mouse.get_pos()
                if x > 50 and x < 250 and y > 270 and y < 315:
                    start()
                    go2 = False
                elif x > 50 and x < 250 and y > 330 and y < 375:
                    menu_screen()
                    go2 = False
        pg.display.update()
        CLOCK.tick(fps)



def lose(): #needs work
    global lost
    lost = True
    go1 = True
    go2 = True
    draw_status()
    while go1:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                event.button
                x, y = pg.mouse.get_pos()
                if x > (2*width/3)-50 and x < (2*width/3)+50 and y > height-TH and y < height:
                    screen = pg.display.set_mode((300,400), 0, 32)
                    screen.blit(lose_screen, (0, 0))
                    pg.display.update()
                    go1 = False
                elif x > (width/3)-50 and x < (width/3)+50 and y > height-TH and y < height:
                    menu_screen()
                    go1 = False
                    go2 = False
        pg.display.update()
        CLOCK.tick(fps)
    
    while go2:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                event.button
                x, y = pg.mouse.get_pos()
                if x > 50 and x < 250 and y > 270 and y < 315:
                    start()
                    go2 = False
                elif x > 50 and x < 250 and y > 330 and y < 375:
                    menu_screen()
                    go2 = False
        pg.display.update()
        CLOCK.tick(fps)



def draw_status(): #needs work
    global TH
    font = pg.font.Font(None, 30)
    if won:
        text = font.render("You Won!", 1, (55, 255, 55))
    elif lost:
        text = font.render("You Lost", 1, (255, 55, 55))
    else:
        text = font.render("Sweep It", 1, (255, 255, 255))
    mode_text = font.render(mode, 1, (255, 255, 255))
    MCmessage = font.render(str(MCR), 1, (255, 255, 255))
    black_img = pg.transform.scale(black, (width,TH))

    text_rect = text.get_rect(center=(width/2, height-(TH/2)))
    menu_rect = menu_img.get_rect(center=((width/3), height-(TH/2)))
    restart_rect = restart_img.get_rect(center=((2*width/3), height-(TH/2)))
    mineCount_rect = MCmessage.get_rect(center=(width-75, height-(TH/2)))
    mode_rect = text.get_rect(center=(75, height-(TH/2)))
    refresh_rect = black_img.get_rect(center=(width/2, height-(TH/2)))

    screen.blit(black_img, refresh_rect)
    screen.blit(text, text_rect)
    screen.blit(menu_img, menu_rect)
    if won or lost:
        screen.blit(continue_img, restart_rect)
    else:
        screen.blit(restart_img, restart_rect)
    screen.blit(MCmessage, mineCount_rect)
    screen.blit(mode_text, mode_rect)

    pg.display.update()
    


def mine_placing():
    first = True
    mineSpots = []
    mineSpots2 = []
    dupeList = []

    for i in range(mineCount):
        x = random.randint(0,boardX-1)
        y = random.randint(0,boardY-1)
        mineSpots.append((x,y))


    while True:

        for i in range(len(mineSpots)):
            k = i + 1
            for j in range(k,len(mineSpots)):
                if mineSpots[i] == mineSpots[j] and mineSpots[i] not in dupeList:
                    dupeList.append(mineSpots[j])

        if len(dupeList) == 0 and first is False:
            break

        for i in range(len(dupeList)):
            if dupeList[i] in mineSpots:
                mineSpots.remove(dupeList[i])

        for i in range(len(mineSpots)):
            mineSpots2.append(mineSpots[i])

        for i in range(len(dupeList)):
            x = random.randint(0,boardX-1)
            y = random.randint(0,boardY-1)
            mineSpots2.append((x,y))

        mineSpots = []
        for i in range(len(mineSpots2)):
            mineSpots.append(mineSpots2[i])
        
        dupeList = []
        mineSpots2 = []
        
       
        for i in range(len(mineSpots)):
            t = mineSpots[i]
            x = t[0]
            y = t[1]
            board[y][x] = 9
        first = False
    
    for i in range(boardY):
        print(board[i])
    print()
    number_tiles()



def number_tiles():
    for i in range(boardY):
        for j in range(boardX):
            if board[i][j] != 9:
                if (j-1) >= 0:
                    if board[i][j-1] == 9:
                        board[i][j] = (board[i][j] + 1)

                if (j+1) < boardX:
                    if board[i][j+1] == 9:
                        board[i][j] = (board[i][j] + 1)
                
                if (i-1) >= 0:  
                    if board[i-1][j] == 9:
                        board[i][j] = (board[i][j] + 1)

                    if (j-1) >= 0:
                        if board[i-1][j-1] == 9:
                            board[i][j] = (board[i][j] + 1)

                    if (j+1) < boardX:  
                        if board[i-1][j+1] == 9:
                            board[i][j] = (board[i][j] + 1)

                if (i+1) < boardY:
                    if board[i+1][j] == 9:
                        board[i][j] = (board[i][j] + 1)

                    if (j-1) >= 0:
                        if board[i+1][j-1] == 9:
                            board[i][j] = (board[i][j] + 1)

                    if (j+1) < boardX:
                        if board[i+1][j+1] == 9:
                            board[i][j] = (board[i][j] + 1)
    
    for i in range(boardY):
        print(board[i])
    

def check_mine(col,row):
    global TR
    posX = (col) * TW
    posY = (row) * TH
    print(col,row)
    print(board[row][col])
    if isFlagged[row][col] == 0 or isFlagged[row][col] == 2:
        isFlagged[row][col] = 2
        if (board[row][col]) == 9:
            screen.blit(boom_img, (posX, posY))
            lose()
        elif (board[row][col]) == 0 and isChecked[row][col] == 0:
            isFlagged[row][col] = 2
            clear_empty(col,row)
            
        elif (board[row][col]) == 1 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile1_img, (posX, posY))
            TR = TR-1
        elif (board[row][col]) == 2 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile2_img, (posX, posY))
            TR = TR-1
        elif (board[row][col]) == 3 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile3_img, (posX, posY))
            TR = TR-1
        elif (board[row][col]) == 4 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile4_img, (posX, posY))
            TR = TR-1
        elif (board[row][col]) == 5 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile5_img, (posX, posY))
            TR = TR-1
        elif (board[row][col]) == 6 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile6_img, (posX, posY))
            TR = TR-1
        elif (board[row][col]) == 7 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile7_img, (posX, posY))
            TR = TR-1
        elif (board[row][col]) == 8 and isChecked[row][col] == 0:
            isChecked[row][col] = 1
            screen.blit(tile8_img, (posX, posY))
            TR = TR-1
    elif isFlagged[row][col] == 1:
        drawFlag(col,row)

    pg.display.update()
    if TR == 0:
        win()

    draw_status()



def check_mine2(NZclearedTiles):
    global TR
    for i in NZclearedTiles:
        global TR
        col = i[1]
        row = i[0]
        posX = (col) * TW
        posY = (row) * TH
        if isFlagged[row][col] == 0 or isFlagged[row][col] == 2:
            global TR
            isFlagged[row][col] = 2
            if (board[row][col]) == 9:
                screen.blit(boom_img, (posX, posY))
                lose()
            elif (board[row][col]) == 0 and isChecked[row][col] == 0:
                isFlagged[row][col] = 2
                isChecked[row][col] = 1
                clear_empty(col,row)
            elif (board[row][col]) == 1 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile1_img, (posX, posY))
                TR = TR-1
            elif (board[row][col]) == 2 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile2_img, (posX, posY))
                TR = TR-1
            elif (board[row][col]) == 3 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile3_img, (posX, posY))
                TR = TR-1
            elif (board[row][col]) == 4 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile4_img, (posX, posY))
                TR = TR-1
            elif (board[row][col]) == 5 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile5_img, (posX, posY))
                TR = TR-1
            elif (board[row][col]) == 6 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile6_img, (posX, posY))
                TR = TR-1
            elif (board[row][col]) == 7 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile7_img, (posX, posY))
                TR = TR-1
            elif (board[row][col]) == 8 and isChecked[row][col] == 0:
                isChecked[row][col] = 1
                screen.blit(tile8_img, (posX, posY))
                TR = TR-1

    pg.display.update()
    if TR == 0:
        win()

    draw_status()
 


def clear_empty(col,row):
    global TR
    clearedTiles = [(row,col)]
    NZclearedTiles = []
    print(col,row)
    while True:
        length = len(clearedTiles)
        for i in clearedTiles:
            x = i[1]
            y = i[0]
            
            if (x-1) >= 0:
                if board[y][x-1] == 0 and (y,x-1) not in clearedTiles and (y,x-1) not in NZclearedTiles:
                    clearedTiles.append((y,x-1))
                elif board[y][x-1] != 0 and (y,x-1) not in clearedTiles and (y,x-1) not in NZclearedTiles:
                    NZclearedTiles.append((y,x-1))


            if (x+1) < boardX:
                if board[y][x+1] == 0 and (y,x+1) not in clearedTiles and (y,x+1) not in NZclearedTiles:
                    clearedTiles.append((y,x+1))
                elif board[y][x+1] != 0 and (y,x+1) not in clearedTiles and (y,x+1) not in NZclearedTiles:
                    NZclearedTiles.append((y,x+1))


            if (y-1) >= 0:  
                if board[y-1][x] == 0 and (y-1,x) not in clearedTiles and (y-1,x) not in NZclearedTiles:
                    clearedTiles.append((y-1,x))
                elif board[y-1][x] != 0 and (y-1,x) not in clearedTiles and (y-1,x) not in NZclearedTiles:
                    NZclearedTiles.append((y-1,x))

                if (x-1) >= 0:
                    if board[y-1][x-1] == 0 and (y-1,x-1) not in clearedTiles and (y-1,x-1) not in NZclearedTiles:
                        clearedTiles.append((y-1,x-1))
                    elif board[y-1][x-1] != 0 and (y-1,x-1) not in clearedTiles and (y-1,x-1) not in NZclearedTiles:
                        NZclearedTiles.append((y-1,x-1))

                if (x+1) < boardX:  
                    if board[y-1][x+1] == 0 and (y-1,x+1) not in clearedTiles and (y-1,x+1) not in NZclearedTiles:
                        clearedTiles.append((y-1,x+1))
                    elif board[y-1][x+1] != 0 and (y-1,x+1) not in clearedTiles and (y-1,x+1) not in NZclearedTiles:
                        NZclearedTiles.append((y-1,x+1))


            if (y+1) < boardY:
                if board[y+1][x] == 0 and (y+1,x) not in clearedTiles and (y+1,x) not in NZclearedTiles:
                    clearedTiles.append((y+1,x))
                elif board[y+1][x] != 0 and (y+1,x) not in clearedTiles and (y+1,x) not in NZclearedTiles:
                    NZclearedTiles.append((y+1,x))

                if (x-1) >= 0:
                    if board[y+1][x-1] == 0 and (y+1,x-1) not in clearedTiles and (y+1,x-1) not in NZclearedTiles:
                        clearedTiles.append((y+1,x-1))
                    elif board[y+1][x-1] != 0 and (y+1,x-1) not in clearedTiles and (y+1,x-1) not in NZclearedTiles:
                        NZclearedTiles.append((y+1,x-1))

                if (x+1) < boardX:
                    if board[y+1][x+1] == 0 and (y+1,x+1) not in clearedTiles and (y+1,x+1) not in NZclearedTiles:
                        clearedTiles.append((y+1,x+1))
                    elif board[y+1][x+1] != 0 and (y+1,x+1) not in clearedTiles and (y+1,x+1) not in NZclearedTiles:
                        NZclearedTiles.append((y+1,x+1))
     
        if len(clearedTiles) == length:
            break
        

    print(clearedTiles)
    print(NZclearedTiles)
    for i in clearedTiles:
        if isChecked[i[0]][i[1]] == 0:
            isChecked[i[0]][i[1]] = 1
            TR = TR-1
            screen.blit(clear_img, (i[1]*TW, i[0]*TH))
            pg.display.update()
    check_mine2(NZclearedTiles)
    NZclearedTiles = []



def drawFlag(col, row):
    global MCR
    posX = (col) * TW
    posY = (row) * TH
    if isChecked[row][col] == 0:
        if isFlagged[row][col] == 0 or isFlagged[row][col] == 2:
            screen.blit(flag_img, (posX, posY))
            MCR = MCR-1
            isFlagged[row][col] = 1
            pg.display.update()
            draw_status()
        elif isFlagged[row][col] == 1:
            screen.blit(tile_img, (posX, posY))
            MCR = MCR+1
            isFlagged[row][col] = 0
            pg.display.update()
            draw_status()



def user_click(button):
    x, y = pg.mouse.get_pos()
    run = 0
    if x > (2*width/3)-50 and x < (2*width/3)+50 and y > height-TH and y < height:
        run = 1
        start()
        
    if x > (width/3)-50 and x < (width/3)+50 and y > height-TH and y < height:
        run = 1
        menu_screen()

    for i in range(boardX):
        if(x < (width / boardX * (i+1))):
            col = i
            break
    if run == 0:
        for i in range(boardY):
            if(y < ((height) / (boardY+1) * (i+1))):
                row = i
                break
        try:
            if col < boardX and row < boardY:
                if button == 1:
                    check_mine(col,row)
                elif button == 3:
                    drawFlag(col,row)
        except:
            pass
 

 
menu_screen()
 
while(True):

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click(event.button)
    pg.display.update()
    CLOCK.tick(fps)