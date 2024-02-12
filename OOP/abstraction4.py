from abc import ABC,abstractmethod

class DbConnect(ABC):
    def __init__ (self,user,password,port,databaseattributes):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def close(self):
        pass

class MyDb(DbConnect):
     def __init__ (self,user,password,port,databaseattributes):
        self.user=user
        self.password=password
        self.port=port
        self.databaseattributes=databaseattributes

     
     def connect(self):
        print("Db connects")

     def execute_query(self):
        print("Query executes")

     def close(self):
        print("Db closes")


obj=MyDb("anu","a212",1234,"aghf")
obj.connect()
