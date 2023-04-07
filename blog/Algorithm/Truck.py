
class Truck:
    def __init__(self,name,length,width,height):
        self.name = name
        self.length = length
        self.width =width
        self.height = height
        self.total_box = 0  #一个箱子中的总项目数
        self.boxes = [] #一个箱子里的物品，最初是一个空白列表
        self.unplaced_boxes = []
        self.unfitted_boxes = []

    def get_volume(self):
        '''
        获取箱子体积
        :return:
        '''
        return self.length*self.width*self.height

    def get_total_weight(self):
        '''
        获取总重量
        :return:
        '''
        total_weight = 0

        for box in self.boxes:
            total_weight += box.weight

        return total_weight

    def get_filling_ratio(self):
        '''
        获取填充率
        :return:
        '''
        total_filling_volume = 0

        for box in self.boxes:
            total_filling_volume += box.get_volume()

        total_filling_ratio = total_filling_volume/self.get_volume()
        return total_filling_ratio

