class Task:

    def __init__(self,name) -> None:

        self.name = name
        self.done = False

### Task name setter and getter ##################
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if name != "":
            self._name = name

#### Task Data setter and getter ################## 
            
    @property
    def data(self):

        return self._data
    @data.setter
    def data(self,data):
        if data != "":
            self._data = data


#### Task Status setter and getter ################## 
        
    @property
    def done(self):

        return self._done
    
    @done.setter
    def done(self,done):
        if done != "":
            self._done = done

    def dic(self):
        data = {    "name":self.name,
                    "data":self.data,
                    "done": self.done
                }
        return data