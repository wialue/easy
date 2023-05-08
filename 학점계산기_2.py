import random
def score (sco) :
    match sco:
        case 'A+' :
            sco = 4.5
        case 'A' :
            sco = 4
        case 'B+' :
            sco = 3.5
        case 'B' :
            sco = 3
        case 'C+' :
            sco = 2.5
        case 'C' :
            sco = 2
        case 'D+' :
            sco = 1.5
        case 'D' :
            sco = 1
        case 'F' :
            sco = 0
    return sco
sum_unit = 0
sum_unit_F = 0
sum_multiple = 0
sum_multiple_F = 0
sum_storage = []
diction_name={}
diction_name_sum = []
#3번째

storage_unit = []
storage_grade = []

#3번째 추가사항
class sugang :
    def __init__(self):
        self.name= []
        self.id = []
        self.unit = []
        self.grade = []
    def unitadd(self, x):
        self.unit.append(x)

    def gradeadd(self, x):
        self.grade.append(x)
    
    def callunit(self, index) :
        return self.unit[index]
    
    def callgrade(self, index) :
        return self.grade[index]

while True :
    print("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 조회\n4. 계산\n5. 종료")
    a = input()
    number = int(a)
    match number :
        case 1 :            
            #입력값
            name = input("과목명을 입력하세요:\n")
            unit = input("학점을 입력하세요:\n")
            number_unit = int(unit)
            grade = input("평점을 입력하세요\n")
            name_code = random.randint(10000, 99999)
            
            #리스트
            diction_name_sum.append(name)
            diction_name[name_code] = name
            storage = [name_code, unit, grade]
            
            tuple(storage)
            sum_storage.append(storage)

            #3번째 추가사항
            i = 0
            i+=1
            
            storage = sugang()
            storage.name = name
            
            
            storage_unit.append (str(number_unit))
            storage_grade.append (grade)
        


            #계산
            number_score = score(grade)
            
            if (number_score != 0) :
                sum_unit += number_unit
                sum_multiple += number_unit*number_score
                mean_sum = sum_multiple/sum_unit
            sum_unit_F += number_unit
            sum_multiple_F += number_unit*number_score
            mean_sum_F = sum_multiple_F/sum_unit_F

            
            
            print("입력되었습니다.")
        case 2 :
            for name_code, unit, grade in sum_storage :
                print(str("[") + diction_name[name_code] + str("] ") + unit + str("학점 : ") + grade)
        case 4 :
            print("제출용 : " + str(sum_unit) + "학점 (GPA:" + str(mean_sum) + ")")
            print("열람용 : " + str(sum_unit_F) + "학점 (GPA:" + str(mean_sum_F) + ")")
        #추가
        case 3 :
            print("과목명을 입력하세요:")
            name_num = input()
            if name_num in diction_name_sum :
                b = diction_name_sum.index(name_num)
                b = int(b)
                print(str("[") + name_num + str("] ") + str(storage_unit[b]) + str("학점 : ") + str(storage_grade[b]))

            else :
                print("해당하는 과목이 없습니다.")
        case 5 :
            break           