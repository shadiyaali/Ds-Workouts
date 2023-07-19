class Hashtable:
    def __init__(self):
        self.table = {}

    def insert(self,key,value):
        if key in self.table:
           self.table[key].append(value)

        else:
            self.table[key]  = [value]  

    def delete(self,key):
        if key in self.table:
            del self.table[key]

    def get(self,key):
        if key in self.table :
            return self.table[key]

hh = Hashtable()
hh.insert("1","apple")
hh.insert("2" , "banana")
hh.insert("2","mango")

 
print(hh.get("2"))
