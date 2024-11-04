# 왼/오른쪽 방향키,대쉬,타이머
#잠,대기,달리기,빨리 달리기
# Game object class here

from pico2d import load_image


class Grass:
    def __init__(self,depth):
        self.image = load_image('grass.png')
        self.y = 90
        if depth == 0:
            self.y = 50
        else:
            self.y = 30
    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass


