text = '''
def function():
    print("Hello World!")

bob.__x = 10

bob.y = function
'''


class Test:
    def __init__(self):
        self.__x = 0
        


# detect __ or _ in the beginning of a variable name
# detect 

bob = Test()

exec(text)



print(bob.__x)



# import pygame_gui

#  hello_button = pygame_gui.elements.UITextBox(
#             html_text='Hello World!\n\nThis is a text box\nIt can be used to display text\nIt can also be used to display HTML\n<font color=#FF0000>Like this</font>',
#             relative_rect=pygame.Rect((350, 275), (200, 500)),
#             manager=self.manager)


#  if event.type == pygame_gui.UI_BUTTON_PRESSED:
#                     if event.ui_element == hello_button:
#                          print('Hello World!')

#                 self.manager.process_events(event)

# self.manager.update(time_delta)
#             self.manager.draw_ui(self.screen)
