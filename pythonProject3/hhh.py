class Person:
    sum_number=0
    @classmethod
    def sum_num(cls):
        return  cls.sum_number
    def __init__(self,name,gender,age,height,weight,address):
        self.name=name
        self.gender=gender
        self.age=age
        self.height=height
        self.weight=weight
        self.address=address
        Person.sum_number+=1
    def introduce(self):
        print('my name is'+self.name+',gender is '+self.gender+'age is '+self.age+
              'my height and weight are '+self.height+self.weight+'my address :'+self.address)
class Students(Person):
    sum_number=0
    advice=[]
    @classmethod
    def sum_num(cls):
        return Students.sum_number

    def __init__(self,name,gender,age,height,weight,address,college):
        super().__init__(name,gender,age,height,weight,address)
        self.college=college
        Students.sum_number+=1
    def introduce(self):
        print('{}'.format(self.name))
    def rececive_advice(self,advice):
        self.advice.append(advice)
class Teacher(Person):
    sum_number = 0
    @classmethod
    def sum_num(cls):
        return  Teacher.sum_number
    def __init__(self,name,gender,age,height,weight,address,job_id,school,department):
        super().__init__(name,gender,age,height,weight,address)
        self.job_id=job_id
        self.school=school
        self.department=department
        Teacher.sum_number+=1
    def information(self,stu): #教师发消息让学生做自我介绍
        stu.introduce()
    def information_0(self,stu):#教师提意见，学生收到反馈
        stu.recevice_advice()
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
class ClassAdvisor:
    studentslist=[]
    def __init__(self,*list):
        for i in list:
            self.studentslist.append(i)
    def introduce(self):
        for i in self.studentslist:
            i.introduce()
Teacher('Wang')
