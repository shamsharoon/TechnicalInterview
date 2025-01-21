
# Shams Haroon
# Jan 21 2025
# Shopify - Technical Interview

# Secret Santa Algorithm for gift exchange
# ! Reqs:
# 10 People
# A gifter cannot get their own gifts
# 
# Stretch Goal: 

# # Mateus
# Henry
# John
# Nicole
# Kush
# Raman
# Tim
# Zakaria
# Aryan
# Hoang


secretSantaList = {
    "Mateus" : ["Candle", ""],
    "Henry" : ["Coffee Mug", ""],
    "John" : ["Portrait", ""],
    "Nicole" : ["Cactus", ""],
    "Kush": ["Keyboard", ""],
    "Raman": ["Timer", ""],
    "Tim": ["Waterbottle", ""],
    "Zakaria" :["Unicorn", ""],
    "Aryan" :["Phone", ""],
    "Hoang": ["Cool Pen!" ""]
}

class giftExchanger:
    # constructor
    def __init__(self, name, giftName):
        self.name = name
        self.giftName = giftName
    
    def getName(self):
        return self.name
    
    def getGiftName(self):
        return self.giftName
    
    
    # giftExchange

def giftExchange(person1, person2):
    if person1.name == person2.name:
        print("Cannot gift to oneself!")
    
    else:
        secretSantaList[person1.name][1] = secretSantaList[person2.name][0]
        # secretSantaList.get(person1.name)
    
    print(f"{person1.name} Recieved {person2.giftName}!")

person1 = giftExchanger("Mateus", "Candle")
person2 = giftExchanger("Henry", "Coffee Mug")

giftExchange(person1, person2)
print(secretSantaList)
        
