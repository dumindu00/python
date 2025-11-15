name = "Dumindu"
count = 1

def another():
    color = "red"
    global count
    count += 1
    print(count)
    def say_my_name(name):
        
        print(name)
        print(color)
    
    say_my_name("Smith")
    
    
    
another()
