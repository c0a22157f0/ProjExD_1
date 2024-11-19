import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像Surfaceを作成する
    kk_img = pg.image.load("fig/3.png") #こうかとん画像Surfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとんを左右反転させる
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) #screanSurfaceに背景画像Surfaceを張り付ける [0,0]は画面の一番左上に張りつける
        screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()