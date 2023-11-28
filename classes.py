import pygame

# Cell Class
class Cell :
    def __init__(self, row_num, CELL_WIDTH, CELL_HEIGHT, CELL_BG) -> None:
        self.surf = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        self.surf.fill(CELL_BG)
        self.rect = self.surf.get_rect()
        
        self.row_num = row_num

        self.note = 0
        self.inst = None

        self.fx1_num = 0
        self.fx1_amt = 0
        self.fx2_num = 0
        self.fx2_amt = 0

    def get_info(self) :
        if self.inst == None :
            return f'{self.row_num:2}|{self.note:3}|--|{self.fx1_num:1}:{self.fx1_amt:2}'
        else :
            return f'{self.row_num:2}|{self.note:3}|{self.inst:2}|{self.fx1_num:1}:{self.fx1_amt:2}'
# -- End of Cell class