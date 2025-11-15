from random import choice

name = "dumindu"
city = "future"
favorite = "Technology"
book= "sherlock holmes"

def facts():
    secret = [
        "DV likes super cars.And he has tons of them.",
        "city called future and it has everything. future city has the most cutting edge Technology.",
        "and he loves technology.",
        "but he also likes book"
    ]
    
    index = choice("0123")
    
    print(secret[int(index)])
    
    
# if __name__ == "__main__":
facts()