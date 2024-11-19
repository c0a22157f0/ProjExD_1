import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像Surfaceを作成する
    bg_img2 = pg.transform.flip(bg_img, True, False) #背景画像左右反転
    kk_img = pg.image.load("fig/3.png") #こうかとん画像Surfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとんを左右反転させる
    kk_rct= kk_img.get_rect() #こうかとんrectを取得する
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        yoko = 0
        tate = 0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            yoko = 0
            tate = -1
        elif key_lst[pg.K_DOWN]:
            yoko = 0
            tate = 1
        elif key_lst[pg.K_LEFT]:
            yoko = -1
            tate = 0
        elif key_lst[pg.K_RIGHT]:
            yoko = 1
            tate = 0
        else:
            yoko = -1
            tate = 0
        kk_rct.move_ip((yoko, tate))

        x = -(tmr%3200)
        
        screen.blit(bg_img, [x, 0]) #screanSurfaceに背景画像Surfaceを張り付ける [0,0]は画面の一番左上に張りつける
        screen.blit(bg_img2, [x+1600, 0]) #左右反転の背景画像
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()