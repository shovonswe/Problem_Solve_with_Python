class MyHashSet:

    def __init__(self):
        self.ans = []
        
    def add(self, key: int) -> None:
        if key not in self.ans:  
            self.ans.append(key)

    def remove(self, key: int) -> None:
        if key in self.ans:       
            self.ans.remove(key)
       
    def contains(self, key: int) -> bool:
        return key in self.ans




if __name__ == "__main__":
    
    MyHashSet = MyHashSet ()
    MyHashSet.add(1)
    MyHashSet.add(2);      
    print(MyHashSet.contains(1)) 
    print(MyHashSet.contains(3)) 
    MyHashSet.add(2);     
    print(MyHashSet.contains(2)) 
    MyHashSet.remove(2) 
    print(MyHashSet.contains(2))
        
    