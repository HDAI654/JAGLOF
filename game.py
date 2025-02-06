import pygame
import sys
import data
import random
import menu
#MAIN
class game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        #DISPLAY
        self.window=pygame.display.set_mode((572, 614))
        pygame.display.set_caption(" ")
        self.clock=pygame.time.Clock()
        self.game_place=True
        #GROUND
        self.ground=pygame.image.load(f"assets\\image\\ground\\{data.ground_choose}.png")
        self.ground_y=0
        #WATCHER
        self.watcher_number=0
        self.watcher=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\watcher\\BARBAR_{self.watcher_number}.png").convert_alpha(), 0, 0.5)
        self.watcher_flip=pygame.transform.flip(self.watcher, True, False)
        self.watcher_timer=pygame.USEREVENT
        pygame.time.set_timer(self.watcher_timer, 60)
        #PLAYER
        self.player_number=1
        self.player_direction="c"
        self.player_speed=0
        self.player_x=200
        self.player_y=300
        self.player_address=data.player_info[data.player_choose]["address"]
        self.player=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\player\\{self.player_address}_wizard\\{self.player_direction}{self.player_number}.png").convert_alpha(), 0, data.player_info[data.player_choose]["scale"])
        self.player_timer=pygame.USEREVENT
        pygame.time.set_timer(self.player_timer, 60)
        self.player_mask=pygame.mask.from_surface(self.player)
        #ENEMY
        self.wood_number=8
        self.wood_sc=0.7
        self.wood_a=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\enemy\\w{self.wood_number}.png").convert_alpha(), 0, self.wood_sc)
        self.wood_b=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\enemy\\w{self.wood_number}.png").convert_alpha(), 0, self.wood_sc)
        self.wood_c=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\enemy\\w{self.wood_number}.png").convert_alpha(), 0, self.wood_sc)
        self.woods_place=[[15, -584], [150, -414], [200, -264]]
        self.wood_timer=pygame.USEREVENT
        pygame.time.set_timer(self.wood_timer, 60)
        self.wood_a_mask=pygame.mask.from_surface(self.wood_a)
        self.wood_b_mask=pygame.mask.from_surface(self.wood_b)
        self.wood_c_mask=pygame.mask.from_surface(self.wood_c)
        #GAME SOUND
        if data.sound==True:
            self.sound="GAMING_SOUND.mp3"
            pygame.mixer.music.load(f"assets\\sound\\{self.sound}")
            pygame.mixer.music.play(-1)
            self.end_sound=pygame.USEREVENT+1
            pygame.mixer.music.set_endevent(self.end_sound)
        #TIMER
        self.record=data.record
        self.timer_font=pygame.font.Font("assets\\font\\ALGER.ttf", 40)
        self.timer=self.timer_font.render(str(int(self.record/1000)), (0, 0, 0), True)
    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #END THE GAME SOUND
                if data.sound==True:
                    if event.type==self.end_sound:
                        pygame.mixer.music.play()
                #ANIMATION FOR WATCHER AND PLAYER AND WOODS
                #WATCHER
                if event.type==self.watcher_timer:
                    self.watcher_number+=1
                #PLAYER
                if event.type==self.player_timer:
                    self.player_number+=1
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.player_direction="l"
                        self.player_speed=-5
                    if event.key==pygame.K_RIGHT:
                        self.player_direction="r"
                        self.player_speed=5
                if event.type==pygame.KEYUP:
                    self.player_direction="c"
                    self.player_speed=0
                #WOODS
                if event.type==self.wood_timer:
                    self.wood_number-=1
                    #TIMER
                    data.record+=60
            #GROUND
            self.window.blit(self.ground, (0, self.ground_y))
            self.window.blit(self.ground, (0, self.ground_y-data.ground[data.ground_choose]["height"]))
            if self.ground_y>data.ground[data.ground_choose]["height"]:
                self.ground_y=0
            self.ground_y+=5
            #WATCHER
            if self.watcher_number>6:
                self.watcher_number=0
            self.watcher=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\watcher\\BARBAR_{self.watcher_number}.png").convert_alpha(), 0, 0.5)
            self.watcher_flip=pygame.transform.flip(self.watcher, True, False)
            #LEFT
            self.window.blit(self.watcher, (data.ground[data.ground_choose]["watchers_left_x"], self.ground_y+data.ground[data.ground_choose]["watcher_left_y"][0]))
            self.window.blit(self.watcher, (data.ground[data.ground_choose]["watchers_left_x"], self.ground_y+data.ground[data.ground_choose]["watcher_left_y"][1]))
            self.window.blit(self.watcher, (data.ground[data.ground_choose]["watchers_left_x"], self.ground_y+data.ground[data.ground_choose]["watcher_left_y"][2]))
            self.window.blit(self.watcher, (data.ground[data.ground_choose]["watchers_left_x"], self.ground_y+data.ground[data.ground_choose]["watcher_left_y"][3]))
            #RIGHT
            self.window.blit(self.watcher_flip, (data.ground[data.ground_choose]["watchers_right_x"], self.ground_y+data.ground[data.ground_choose]["watcher_right_y"][0]))
            self.window.blit(self.watcher_flip, (data.ground[data.ground_choose]["watchers_right_x"], self.ground_y+data.ground[data.ground_choose]["watcher_right_y"][1]))
            self.window.blit(self.watcher_flip, (data.ground[data.ground_choose]["watchers_right_x"], self.ground_y+data.ground[data.ground_choose]["watcher_right_y"][2]))
            self.window.blit(self.watcher_flip, (data.ground[data.ground_choose]["watchers_right_x"], self.ground_y+data.ground[data.ground_choose]["watcher_right_y"][3]))
            #PLAYER
            if self.player_number>8:
                self.player_number=1
            self.player=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\player\\{self.player_address}_wizard\\{self.player_direction}{self.player_number}.png").convert_alpha(), 0, data.player_info[data.player_choose]["scale"])
            self.window.blit(self.player, (self.player_x, self.player_y))
            self.player_x+=self.player_speed
            #ENEMY
            if self.wood_number<1:
                self.wood_number=8
            self.window.blit(self.wood_a, self.woods_place[0])
            self.window.blit(self.wood_b, self.woods_place[1])
            self.window.blit(self.wood_c, self.woods_place[2])
            self.wood_a=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\enemy\\w{self.wood_number}.png").convert_alpha(), 0, self.wood_sc)
            self.wood_b=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\enemy\\w{self.wood_number}.png").convert_alpha(), 0, self.wood_sc)
            self.wood_c=pygame.transform.rotozoom(pygame.image.load(f"assets\\image\\enemy\\w{self.wood_number}.png").convert_alpha(), 0, self.wood_sc)
            self.woods_place[0][1]+=6
            self.woods_place[1][1]+=6
            self.woods_place[2][1]+=6
            if self.woods_place[0][1]>680:
                self.woods_place[0][1]=-584
                self.woods_place[0][0]=random.randint(15, 30)
            if self.woods_place[1][1]>680:
                self.woods_place[1][1]=-414
                self.woods_place[1][0]=random.randint(140, 170)
            if self.woods_place[2][1]>680:
                self.woods_place[2][1]=-264
                self.woods_place[2][0]=random.randint(180, 200)
            #CRASH
            offset_a=(self.woods_place[0][0]-self.player_x, self.woods_place[0][1]-self.player_y)
            offset_b=(self.woods_place[1][0]-self.player_x, self.woods_place[1][1]-self.player_y)
            offset_c=(self.woods_place[2][0]-self.player_x, self.woods_place[2][1]-self.player_y)
            if self.player_mask.overlap(self.wood_a_mask, offset_a) or self.player_mask.overlap(self.wood_b_mask, offset_b) or self.player_mask.overlap(self.wood_c_mask, offset_c):
                #BACK TO MENU
                pygame.quit()
                mc=menu.menu()
                mc.play()
                sys.exit()
            #TIMER
            self.window.blit(self.timer, (20, 20))
            self.record=data.record
            self.timer=self.timer_font.render(str(int(self.record/1000)), (0, 0, 0), True)
            #UPDATE THE DISPLAY
            pygame.display.update()
            self.clock.tick(90)
