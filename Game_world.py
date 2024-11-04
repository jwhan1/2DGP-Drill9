class Game_world():
    # world[0] : 백그라운드 객체
    # worle[1] : 전면 객체
    
    def __init__(self):
        self.world = [[],[]]

    def add_object(self,e, depth):#객체, 레이어
        
        self.world[depth].append(e)

    def update(self):
        for layer in self.world:
            for o in layer:
                o.update()

    def render(self):
        for layer in self.world:
            for o in layer:
                o.draw()

    def remove_object(self,o):#객체
        for layer in self.world:
            if o in layer:
                layer.remove(o)
                return
        print(f'CRITICAL : 존재하지 않는 객체{o}를 지우려고 합니다.')