class ClassRoom(object):
    students = []

    def __init__(self, count):
        self.count = count
        
        self.students = []

    def insertScore(self, data):
        data = data.split(" ")

        student = {}
        student["name"] = data[0]
        student["kor"] = int(data[1])
        student["eng"] = int(data[2])
        student["math"] = int(data[3])
        self.students.append(student)
    def bubbleSort(self, students, last=None):
        if last==None:
            self.bubbleSort(students, len(students))
        else:

            if (last > 0):

                for i in range(1, last):
                    if students[i]["kor"]>students[i-1]["kor"]:
                        self.swap(students, i, i-1)

                    elif students[i]["kor"]==students[i-1]["kor"]:
                        if students[i]["eng"] < students[i-1]["eng"]:
                            self.swap(students, i, i-1)

                        elif students[i]["eng"] == students[i-1]["eng"]:
                            if students[i]["math"] > students[i-1]["math"]:
                                self.swap(students, i, i-1)

                            elif students[i]["math"] == students[i-1]["math"]:
                                if students[i]['name'] < students[i-1]["name"]:
                                    self.swap(students, i, i-1)
                    else :
                        pass
                self.bubbleSort(students, last-1)

    def swap(self, students, start, end):
        temp = students[start]
        students[start] = students[end]
        students[end] = temp  

    def sortStudent(self, students):
        students.sort(key = lambda x: (100-x["kor"], x["eng"], 100-x["math"], x["name"]))
        

if __name__ == "__main__":
    classRoom = ClassRoom(int(input()))
    for i in range(classRoom.count):
        classRoom.insertScore(input())
    
    classRoom.sortStudent(classRoom.students)

    for i in classRoom.students:
        print(i["name"])
