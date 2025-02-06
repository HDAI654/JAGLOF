import pygame
import sys
import data
import game
class menu:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        #DISPLAY
        self.window=pygame.display.set_mode((572, 614))
        pygame.display.set_caption(" ")
        self.clock=pygame.time.Clock()
        self.menu_place=True
        #BACKGROUND
        self.menu_background=data.menu["background"]
        self.background=pygame.image.load(f"assets\\image\\menu\\{self.menu_background}.png")
    def play(self):
        while self.menu_place:
            #MOUSE PRESS AND PLACE
            mouse_place=pygame.mouse.get_pos()
            mouse_press=pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #BACKGROUND
            self.menu_background=data.menu["background"]
            self.background=pygame.image.load(f"assets\\image\\menu\\{self.menu_background}.png")
            self.window.blit(self.background, (0, 0))
            #CHANGE THE MENU
            #SETTING
            if mouse_place[0]>390 and mouse_place[0]<558 and mouse_place[1]>528 and mouse_place[1]<588:
                pygame.draw.line(self.window, (0, 0, 255), (389, 585), (557, 585), width=5)
                if mouse_press[0]==1:
                    data.menu["background"]="setting_menu"
            #START
            if mouse_place[0]>10 and mouse_place[0]<276 and mouse_place[1]>530 and mouse_place[1]<584:
                pygame.draw.line(self.window, (0, 0, 255), (9, 583), (275, 583), width=5)
                if mouse_press[0]==1:
                    data.menu["background"]="start_menu"
            #SETTING MENU SETTING
            if data.menu["background"]=="setting_menu":
                pygame.draw.line(self.window, (255, 255, 255), data.menu["setting_menu"][data.player_choose+"_under_line_place"][0], data.menu["setting_menu"][data.player_choose+"_under_line_place"][1], width=5)
                pygame.draw.line(self.window, (255, 255, 255), data.menu["setting_menu"][data.ground_choose+"_under_line_place"][0], data.menu["setting_menu"][data.ground_choose+"_under_line_place"][1], width=5)
                if data.sound==True:
                    pygame.draw.line(self.window, (255, 255, 255), (449, 295), (520, 295), width=5)
                if data.sound==False:
                    pygame.draw.line(self.window, (255, 255, 255), (289, 293), (344, 293), width=5)
                #MOUSE ON IMAGE
                #WIZARD
                if mouse_place[0]>449 and mouse_place[0]<513 and mouse_place[1]>51 and mouse_place[1]<131:
                    pygame.draw.line(self.window, (0, 0, 255), data.menu["setting_menu"]["wizard_under_line_place"][0], data.menu["setting_menu"]["wizard_under_line_place"][1], width=5)
                    if mouse_press[0]==1:
                        data.player_choose="wizard"
                #ELECTRO WIZARD
                if mouse_place[0]>231 and mouse_place[0]<295 and mouse_place[1]>50 and mouse_place[1]<137:
                    pygame.draw.line(self.window, (0, 0, 255), data.menu["setting_menu"]["electro_wizard_under_line_place"][0], data.menu["setting_menu"]["electro_wizard_under_line_place"][1], width=5)
                    if mouse_press[0]==1:
                        data.player_choose="electro_wizard"
                #ICE WIZARD
                if mouse_place[0]>336 and mouse_place[0]<402 and mouse_place[1]>46 and mouse_place[1]<135:
                    pygame.draw.line(self.window, (0, 0, 255), data.menu["setting_menu"]["ice_wizard_under_line_place"][0], data.menu["setting_menu"]["ice_wizard_under_line_place"][1], width=5)
                    if mouse_press[0]==1:
                        data.player_choose="ice_wizard"
                #GREEN GROUND
                if mouse_place[0]>424 and mouse_place[0]<520 and mouse_place[1]>321 and mouse_place[1]<424:
                    pygame.draw.line(self.window, (0, 0, 255), data.menu["setting_menu"]["green_ground_under_line_place"][0], data.menu["setting_menu"]["green_ground_under_line_place"][1], width=5)
                    if mouse_press[0]==1:
                        data.ground_choose="green_ground"
                #GRAY GROUND
                if mouse_place[0]>273 and mouse_place[0]<368 and mouse_place[1]>322 and mouse_place[1]<424:
                    pygame.draw.line(self.window, (0, 0, 255), data.menu["setting_menu"]["gray_ground_under_line_place"][0], data.menu["setting_menu"]["gray_ground_under_line_place"][1], width=5)
                    if mouse_press[0]==1:
                        data.ground_choose="gray_ground"
                #SOUND
                if mouse_place[0]>449 and mouse_place[0]<500 and mouse_place[1]>219 and mouse_place[1]<290:
                    pygame.draw.line(self.window, (0, 0, 255), (449, 295), (520, 295), width=5)
                    if mouse_press[0]==1:
                        data.sound=True
                if mouse_place[0]>283 and mouse_place[0]<339 and mouse_place[1]>222 and mouse_place[1]<296:
                    pygame.draw.line(self.window, (0, 0, 255), (289, 293), (344, 293), width=5)
                    if mouse_press[0]==1:
                        data.sound=False
            #START MENU SETTING
            if data.menu["background"]=="start_menu":
                #START
                if mouse_place[0]>292 and mouse_place[0]<500 and mouse_place[1]>81 and mouse_place[1]<163:
                    pygame.draw.line(self.window, (255, 255, 255), (292, 163), (500, 163), width=5)
                    if mouse_press[0]==1:
                        pygame.quit()
                        cg=game.game()
                        cg.play()
                        sys.exit()
                #EXIT
                if mouse_place[0]>328 and mouse_place[0]<460 and mouse_place[1]>239 and mouse_place[1]<325:
                    pygame.draw.line(self.window, (255, 255, 255), (328, 325), (460, 325), width=5)
                    if mouse_press[0]==1:
                        pygame.quit()
                        sys.exit()

            #UPDATE THE DISPLAY
            self.clock.tick(90)
            pygame.display.update()