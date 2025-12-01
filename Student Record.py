import json

class student:
    def __init__(self,filename = "student.json"):
        self.filename = filename
       
        self.data={}
        self.load()


    def addstudent(self,name,marks):
        self.data[name] = marks
        self.save()
        
    def updatestudent(self,name,marks):
        if name in self.data:
            
            self.data[name] = marks
            save()
        else:
            print("Student not found")

    def deletestudent(self,name):
        if name in self.data:
            
            del self.data[name]
            self.save()
        else:
            print("Student not found")


    def save(self):
        with open(self.filename,"w")as f:
           json.dump(self.data,f)

    def view(self):
        for name,marks in self.data.items():
           print(name," : " ,marks)
      
       
   
       


    def load(self):
        try:
           with open(self.filename,"r")as f:
               self.data = json.load(f)

        except(FileNotFoundError,json.JSONDecodeError):
               self.data = {}
        
        
    
db = student()
db.addstudent("Muruga" ,90)
db.updatestudent("Madhu",95)
db.deletestudent("Madhu")
db.view()

