import pygame
from constants import *
from pygame.locals import *

class Button():
    text_col =  (0, 0, 0)
    button_col = (255, 255, 255)
    hover_col = (217, 217, 217)
    click_col = (150, 150, 150)
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self, screen):

        clicked = False
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
                action = True
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, "black", (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, "black", (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, "black", (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, "black", (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)


        # add text to button
        text_img = FONT.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


#     def draw(self, screen):
#         # create pygame Rect object for the button
#         button_rect = Rect(self.x, self.y, self.width, self.height)
#
#         pygame.draw.line(screen, "white", (self.x, self.y), (self.x + self.width, self.y), 2)
#         pygame.draw.line(screen, "white", (self.x, self.y), (self.x, self.y + self.height), 2)
#         pygame.draw.line(screen, "black", (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
#         pygame.draw.line(screen, "black", (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
#
#
#
#
#         # add text to button
#         text_img = FONT.render(self.text, True, self.text_col)
#         text_len = text_img.get_width()
#         screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
#
#
#     def check_click(self, screen):
#         action = False
#         clicked = False
#
#         # get mouse position
#         pos = pygame.mouse.get_pos()
#
#         # create pygame Rect object for the button
#         button_rect = Rect(self.x, self.y, self.width, self.height)
#
#         # check mouseover and clicked conditions
#         if button_rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1:
#                 clicked = True
#                 pygame.draw.rect(screen, self.click_col, button_rect)
#             elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
#                 clicked = False
#                 action = True
#             else:
#                 pygame.draw.rect(screen, self.hover_col, button_rect)
#         else:
#             pygame.draw.rect(screen, self.button_col, button_rect)
#         return action
#