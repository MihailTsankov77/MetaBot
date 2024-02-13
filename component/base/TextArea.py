import pygame


class TextArea:
    def __init__(self):
        ...

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                print(event.text)
            
        
    def draw(self):
        ...
        
