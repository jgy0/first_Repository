class Person:
    sum_number=0
    @classmethod
    def sum_num(cls):
        return  cls.sum_number
    def __init__(self):
        self.BMI=marry.getBMI()
        self.name=marry.getName()
        self.age=marry.getAge()
        self.height=marry.getHeight()
        self.weight=marry.getWeight()
        Person.sum_number+=1
    def introduce(self):
        print('my name is'+self.name+',gender is '+'age is '+str(self.age)+
              'my height and weight are '+str(self.height)+str(self.weight)+'my address :')
class BMI:
    def __init__(self,name,age,weight,height):
        self.__name=name
        self.__age=age
        self.__weight=weight
        self.__height=height
    def getBMI(self):
        bmi=self.__weight/(self.__height * self.__height)
        return round(bmi * 100)/100
    def getStatus(self):
        bmi=self.getBMI()
        if bmi<18.5:
            return '偏瘦'
        elif bmi<24:
            return '正常'
        elif bmi<30:
            return '偏胖'
        else:
            return '肥胖'
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height
marry=BMI("zhaosi",18,70,1.75)
print(marry.getName(),"BMI是",marry.getBMI(),marry.getStatus())
P=Person()
P.introduce()