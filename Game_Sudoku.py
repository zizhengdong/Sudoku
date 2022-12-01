import os
import sys
import time
import pygame
import numpy as np

from paint import Paint
from Generate import Generate


class Game_Sudoku(object):
    def __init__(self, screen_width, screen_height, selected_width, selected_height,
                 block_gap, block_size, level):

        self.screen_width = screen_width  # Width of window
        self.screen_height = screen_height  # Height of window
        self.block_gap = block_gap  # Gap of blocks
        self.block_size = block_size  #
        self.form = ''

        self.martix = []

        self.x, self.y = 0, 0
        self.row, self.col = 0, 0  #


        self.tmp = 0
        self.time = ""
        self.start_time = ""
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.empty = []
        self.is_same = []
        self.issuccess = False
        self.start = True

        """ font """
        self.title_font = ''
        self.time_font = ''
        self.tips_font = ''
        self.font = ''


        self.selected_form = ""
        self.selected_width = selected_width
        self.selected_height = selected_height

        self.selected_font = ""

        self.move_x, self.move_y = 0, 0
        self.press_x, self.press_y = 0, 0

        self.level = level
        self.counts = [30, 40, 50]


    def Form(self):
        """
        :return:
        """
        pygame.init()
        pygame.display.set_caption("Game_Sudoku")
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.form = pygame.display.set_mode([self.screen_width, self.screen_height], 0, 0)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        self.start_time = time.time()


        self.init()

        while True:
            self.Action()
            pygame.display.update()


    def SelectedForm(self):
        """
        :return:
        """
        pygame.init()
        pygame.display.set_caption("Game_Sudoku")
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.selected_form = pygame.display.set_mode([self.selected_width, self.selected_height], 0, 0)

        while True:
            self.SelectedAction()
            pygame.display.update()


    def ReturnForm(self,is_success):
        """
        :return:
        """
        pygame.init()
        pygame.display.set_caption("Game_Sudoku")
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.returnForm = pygame.display.set_mode([560, 692], 0, 0)
        if is_success:
            text = "Game Won!"
            button_text = "EXIT"
        else:
            text = "Game Over :("
            button_text = "RESTART"
        while True:
            self.ReturnAction(text,button_text)
            pygame.display.update()


    def Action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.move_x, self.move_y = pos[0], pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.press_x, self.press_y = pos[0], pos[1]
                self.row, self.col = (self.press_y - 140 - 1) // 61, (self.press_x - 5 - 1) // 61
            elif event.type == pygame.MOUSEBUTTONUP:
                if 17 < self.press_x < 77 and 110 < self.press_y < 135:
                    self.SelectedForm()
                elif 80 < self.press_x < 133 and 110 < self.press_y < 135:
                    self.reset()
                elif 136 < self.press_x < 176 and 110 < self.press_y < 135:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                """
                pygame.KEYDOWN 
                pygame.KEYUP 
                """
                """ 
                K_ESCAPE: ESC
                """
                if event.key == pygame.K_SPACE:
                    self.start = True
                    self.start_time = time.time()
                elif 0 < event.key < 1114111 and chr(event.key) in self.nums and 0 <= self.row <= 8 and 0 <= self.col <= 8 \
                        and [self.row, self.col] in self.empty:
                    self.IsRight(chr(event.key))
                    self.martix[self.row][self.col] = chr(event.key)
                elif event.key == pygame.K_BACKSPACE:
                    if [self.row, self.col] in self.empty:
                        self.martix[self.row][self.col] = 0

        paint = Paint()
        paint.PaintForm(self.form, self.start_time, self.block_size, self.block_gap,
                        self.move_x, self.move_y, self.press_x, self.press_y, self.martix,
                        self.empty, self.is_same, self.issuccess, self.start)


        if self.is_full():
            self.IsSuccess()


    def SelectedAction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.move_x, self.move_y = pos[0], pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.press_x, self.press_y = pos[0], pos[1]
                if 120 < self.press_x < 180 and 420 < self.press_y < 450:
                    self.level = 0
                    self.Form()
                elif 240 < self.press_x < 325 and 420 < self.press_y < 450:
                    self.level = 1
                    self.Form()
                elif 380 < self.press_x < 440 and 420 < self.press_y < 450:
                    self.level = 2
                    self.Form()


        paint = Paint()
        paint.PaintSelected(self.selected_form, self.move_x, self.move_y)


    def ReturnAction(self,text,button_text):
        paint = Paint()
        paint.Paint_return(self.selected_form, text ,button_text, self.move_x, self.move_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.move_x, self.move_y = pos[0], pos[1]
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                self.press_x, self.press_y = pos[0], pos[1]
                if 220 < self.press_x < 370 and 380 < self.press_y < 420 and button_text == 'RESTART':
                    self.SelectedForm()
                elif 220 < self.press_x < 310 and 380 < self.press_y < 420 and button_text == 'EXIT':
                    sys.exit()
        paint = Paint()
        paint.Paint_return(self.selected_form, text, button_text, self.move_x, self.move_y)


    def init(self):
        self.empty = []

        g = Generate(self.counts[self.level])
        self.martix = g.build_martix()


        for i in range(9):
            for j in range(9):
                if self.martix[i][j] == 0:
                    self.empty.append([i, j])




    def IsRight(self, num):
        rowset = self.martix[self.row, :]
        colset = self.martix[:, self.col]
        blockset = self.martix[self.row // 3 * 3: self.row // 3 * 3 + 3,
                   self.col // 3 * 3: self.col // 3 * 3 + 3].reshape(9)

        num = int(num)
        self.is_same = []
        if num in rowset or num in colset or num in blockset:
            pos = np.where(self.martix == num)
            pos_x, pos_y = pos[0], pos[1]
            for i in range(len(pos_x)):
                self.is_same.append([pos_x[i], pos_y[i]])


    def IsSuccess(self):
        if  not self.is_same:
            self.empty = []
            self.issuccess = True
            self.ReturnForm(self.issuccess)
        else:
            self.issuccess = False
            self.ReturnForm(self.issuccess)

    def reset(self):
        for i, j in self.empty:
            self.martix[i][j] = 0;
        return self.martix

    def is_full(self):
        for i,j in self.empty:
            if self.martix[i][j] == 0:
                return False
        return True