from constants import RotationType

START_POSITION = [0, 0, 0]


class Box:
    def __init__(self, name, length, width, height, way, locate, package, state, weight):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.way = way
        self.locate = locate
        self.package = package
        self.state = state
        self.weight = weight
        self.rotation_type = 0  # 初始旋转类型：（x,y,x）-->（l,w,h）
        self.position = START_POSITION  # 初始位置：（0，0，0）

    def get_volume(self):
        '''
        获取该货品箱子的体积
        :return:
        '''
        return self.length * self.weight * self.height

    def get_dimension(self):
        '''
        获取维度，共六种维度变换方式
        :return:
        '''
        if self.rotation_type == RotationType.RT_LWH:
            dimension = [self.length, self.width, self.height]
        elif self.rotation_type == RotationType.RT_HLW:
            dimension = [self.height, self.length, self.width]
        elif self.rotation_type == RotationType.RT_HWL:
            dimension = [self.height, self.width, self.length]
        elif self.rotation_type == RotationType.RT_WHL:
            dimension = [self.width, self.height, self.length]
        elif self.rotation_type == RotationType.RT_WLH:
            dimension = [self.width, self.length, self.height]
        elif self.rotation_type == RotationType.RT_LHW:
            dimension = [self.length, self.height, self.width]
        else:
            dimension = []

        return dimension

    def string(self):
        return