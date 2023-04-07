from Box import Box

class Packer:
    def __init__(self):
        self.trucks = []    #集装箱
        self.unplaced_boxes = []    #还未放置的箱子
        self.placed_boxes = []  #已经放置完成的箱子
        self.unfit_boxes = []   #不适合的箱子
        self.total_boxes = 0    #箱子总数

    def add_truck(self,truck):
        '''
        添加集装箱
        :param truck:
        :return:
        '''
        return self.trucks.append(truck)

    def add_box(self,name,num,length,width,height,way,locate,package,state,weight):
        '''
        添加货品
        :param name:
        :param num:
        :param length:
        :param width:
        :param height:
        :param way:
        :param locate:
        :param package:
        :param state:
        :param weight:
        :return:
        '''
        self.total_boxes += num
        for i in range(num):
            self.unplaced_boxes.append(Box(name,length,width,height,way,locate,package,state,weight))