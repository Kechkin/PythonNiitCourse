class Bird: 
    def says(self) :
        raise NotImplemented

class Duck(Bird):
    def says(self):
        return "say duck"

class Other(Bird):
    def says(self):
        return "say other"
        



birds = []    

def add_birds(birds, nell):
    if isinstance(nell, Bird):
        birds.append(nell)
    else:
        print("Error{}" nell)
        
        
        
add_birds(birds, Duck())
add_birds(birds, Other())
add_birds(birds, "abc")

for i in birds:
    print(i.says())