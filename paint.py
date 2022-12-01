import time
import pygame
import datetime

class Paint(object):
    def __init__(self):
        self.martix = []
        self.timing = ""

    # 绘制选择窗口
    def PaintSelected(self, selected_form, move_x, move_y):
        img = pygame.image.load('image.png')
        selected_form.blit(img, (0, 0))

        pygame.font.init()

        selected_font = pygame.font.SysFont('Arial', 60, True)
        easy_text = selected_font.render('Welcome to Sudoku', True, (0, 0, 0))
        selected_form.blit(easy_text, (40, 100))

        selected_font = pygame.font.SysFont('Arial', 50, True)
        easy_text = selected_font.render('Select Game Mode:', True, (0, 0, 0))
        selected_form.blit(easy_text, (90, 280))

        # part_1: easy
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 0, 260, 100))
        selected_font = pygame.font.SysFont('Arial', 25, True)
        easy_text = selected_font.render('EASY', True, (0, 0, 0))
        pygame.draw.rect(selected_form, (120, 120, 0), (100, 410, 95, 50))
        pygame.draw.rect(selected_form, (255, 255, 255), (105, 415, 85, 40))
        pygame.draw.rect(selected_form, (255, 120, 0), (110, 420, 75, 30))
        # pygame.draw.rect(selected_form, (100, 128, 128), (20, 20, 240, 80))
        selected_form.blit(easy_text, (120, 420))

        # part_2: medium
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 100, 260, 100))

        medium_text = selected_font.render('MEDIUM', True, (0, 0, 0))
        pygame.draw.rect(selected_form, (120, 120, 0), (225, 410, 115, 50))
        pygame.draw.rect(selected_form, (255, 255, 255), (230, 415, 105, 40))
        pygame.draw.rect(selected_form, (255, 120, 0), (235, 420, 95, 30))
        selected_form.blit(medium_text, (240, 420))

        # part_3: hard
        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 200, 260, 100))
        hard_text = selected_font.render('HARD', True, (0, 0, 0))
        pygame.draw.rect(selected_form, (120, 120, 0), (365, 410, 90, 50))
        pygame.draw.rect(selected_form, (255, 255, 255), (370, 415, 80, 40))
        pygame.draw.rect(selected_form, (255, 120, 0), (375, 420, 70, 30))
        selected_form.blit(hard_text, (380, 420))

        """ Mouse movement event """
        if 120 < move_x < 180 and 420 < move_y < 450:
            easy_text = selected_font.render('EASY', True, (255, 255, 255))
            selected_form.blit(easy_text, (120, 420))
        elif 240 < move_x < 325 and 420 < move_y < 450:
            medium_text = selected_font.render('MEDIUM', True, (255, 255, 255))
            selected_form.blit(medium_text, (240, 420))
        elif 380 < move_x < 440 and 420 < move_y < 450:
            hard_text = selected_font.render('HARD', True, (255, 255, 255))
            selected_form.blit(hard_text, (380, 420))

    # Draw the main window
    def PaintForm(self, form, start_time, block_size, block_gap,
                  move_x, move_y, press_x, press_y, martix, empty, is_same, issuccess, reset):

        form.fill((220, 220, 220))


        pygame.font.init()

        title_font = pygame.font.SysFont('Arial', 50, True)
        title_text = title_font.render('Welcome to Sudoku', True, (0, 0, 0))
        form.blit(title_text, (15, 30))

        # Time:  0:00:00
        pygame.draw.rect(form, (100, 200, 200), (420, 25, 130, 70))
        time_font = pygame.font.SysFont('Arial', 28, True)
        time_text = time_font.render('Time', True, (0, 0, 0))
        form.blit(time_text, (430, 30))

        tmp = round(time.time() - int(start_time), 0)
        self.time = str(datetime.timedelta(seconds=tmp))
        digtial_time = time_font.render(str(self.time), True, (255, 250, 250))
        form.blit(digtial_time, (455, 60))

        # time.sleep(1)


        tips_font = pygame.font.SysFont('Arial', 20 ,True)
        # tips_text = tips_font.render('Using logic and reasoning, fill in the other blanks with numbers 1-9.', True, (0, 0, 0))
        # form.blit(tips_text, (25, 70))
        #
        # tips_text = tips_font.render('Make each number 1-9 appear only once in each row, column, and boxes.', True, (0, 0, 0))
        # form.blit(tips_text, (25, 90))


        tips_text = tips_font.render('Restart', True, (0, 0, 0))
        form.blit(tips_text, (20, 110))

        tips_text = tips_font.render('Reset', True, (0, 0, 0))
        form.blit(tips_text, (85, 110))

        tips_text = tips_font.render('Exit', True, (0, 0, 0))
        form.blit(tips_text, (140, 110))

        if 17 < move_x < 77 and 110 < move_y < 135:
            tips_text = tips_font.render('Restart', True, (255, 255, 255))
            pygame.draw.rect(form, (128, 128, 128), (17, 110, 63, 25))
            form.blit(tips_text, (20, 110))
        elif 80 < move_x < 133 and 110 < move_y < 135:
            tips_text = tips_font.render('Reset', True, (255, 255, 255))
            pygame.draw.rect(form, (128, 128, 128), (80, 110, 53, 25))
            form.blit(tips_text, (85, 110))
        elif 136 < move_x < 176 and 110 < move_y < 135:
            tips_text = tips_font.render('Exit', True, (255, 255, 255))
            pygame.draw.rect(form, (128, 128, 128), (136, 110, 40, 25))
            form.blit(tips_text, (140, 110))



        pygame.draw.rect(form, (65, 105, 225), (5, 140, 550, 550))  # Blue background
        pygame.draw.rect(form, (65, 105, 225), (5, 140, 185, 185))
        pygame.draw.rect(form, (65, 105, 225), (370, 140, 185, 185))
        pygame.draw.rect(form, (65, 105, 225), (188, 322, 185, 185))
        pygame.draw.rect(form, (65, 105, 225), (5, 505, 185, 185))
        pygame.draw.rect(form, (65, 105, 225), (370, 505, 185, 185))

        for i in range(9):
            for j in range(9):
                # (x, y) The initial position of the block
                x = j * block_size + (j + 1) * block_gap
                y = i * block_size + (i + 1) * block_gap

                """ Mouse movement event """
                # Mouse keys corresponding to the box, the box color changes
                if x + 5 < press_x < x + 5 + block_size and y + 140 < press_y < y + 140 + block_size and [i, j] in empty:
                    pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))
                else:
                    pygame.draw.rect(form, (255, 255, 255), (x + 5, y + 140, block_size, block_size))

                """ Mouse press event """
                # if x + 5 < press_x < x + 5 + block_size and 140 < press_y < 690:
                #     pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))
                # #
                # if y + 140 < press_y < y + 140 + block_size and 5 < press_x < 555:
                #     pygame.draw.rect(form, (220, 220, 220), (x + 5, y + 140, block_size, block_size))

                # Draw numbers
                num_font = pygame.font.SysFont('Arial', 45, True)
                if martix[i][j] != 0:
                    if [i, j] not in empty and [i, j] not in is_same:
                        num_text = num_font.render(str(martix[i][j]), True, (0, 0, 0))
                    elif [i, j] not in empty and [i, j] in is_same:
                        num_text = num_font.render(str(martix[i][j]), True, (0, 0, 0))
                        # num_text = num_font.render(str(martix[i][j]), True, (255, 0, 0))
                    else:
                        num_text = num_font.render(str(martix[i][j]), True, (65, 105, 225))
                        # num_text = num_font.render(str(martix[i][j]), True, (65, 105, 225))
                    # if martix[i][j] == 0:
                    #     num_text = num_font.render(str(martix[i][j]), True, (255, 255, 255))
                    # else:
                    #     num_text = num_font.render(str(martix[i][j]), True, (0, 0, 0))
                    form.blit(num_text, (x + 22, y + 150))



    # Draw Selection window
    def Paint_return(self, success_form, text, button_text, move_x, move_y):

        img = pygame.image.load('image.png')
        success_form.blit(img,(0,0))

        pygame.font.init()


        # pygame.draw.rect(self.selected_form, (128, 128, 128), (0, 0, 260, 100))
        selected_font = pygame.font.SysFont('Arial', 50, True)
        easy_text = selected_font.render(text, True, (0, 0, 0))
        success_form.blit(easy_text, (160, 250))


        selected_font = pygame.font.SysFont('Arial', 35, True)
        easy_text = selected_font.render(button_text, True, (0, 0, 0))
        if button_text == 'EXIT':
            pygame.draw.rect(success_form, (128, 128, 128), (220, 380, 90, 40))
        else:
            pygame.draw.rect(success_form, (128, 128, 128), (220, 380, 150, 40))
        success_form.blit(easy_text, (230, 380))

        if button_text == 'EXIT':
            if 220 < move_x < 310 and 380 < move_y < 420:
                pygame.draw.rect(success_form, (128, 128, 128), (220, 380, 90, 40))
                easy_text = selected_font.render(button_text, True, (255, 255, 255))
                success_form.blit(easy_text, (230, 380))
        else:
            if 220 < move_x < 370 and 380 < move_y < 420:
                pygame.draw.rect(success_form, (128, 128, 128), (220, 380, 150, 40))
                easy_text = selected_font.render(button_text, True, (255, 255, 255))
                success_form.blit(easy_text, (230, 380))


        # if 0 < move_x < 260 and 0 < move_y < 100:
        #     pygame.draw.rect(selected_form, (128, 128, 128), (0, 0, 260, 100))
        #     easy_text = selected_font.render('EASY', True, (255, 255, 255))
        #     selected_form.blit(easy_text, (90, 30))
