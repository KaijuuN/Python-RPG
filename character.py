### Das Schwarze Auge in Python
### using german words


from dataclasses import dataclass

@dataclass
class Character:
    
    name: str = ""
    rasse: str = ""
    kultur:str = ""
    profession: str = ""
    
    xp: int = 0

    mut: int = 0
    klugheit: int = 0
    intuition: int = 0
    charisma: int = 0
    fingerfertigkeit: int = 0
    gewandtheit: int = 0
    konstitution: int = 0
    körperkraft: int = 0
    geschwindigkeit: int = 0

    lebenspunkte: int = 0
    ausdauer: int = 0
    astralenergie: int = 0
    karmaenergie: int = 0
    magieresistenz: int = 0
    ini_basiswert: int = 0
    at_basiswert: int = 0
    pa_basiswert: int = 0
    fk_basiswert: int = 0


    # How to access --> equiptment_slots["Head"] = "Helmet" // equiptment_slots['Hand_L']['Indexfinger'] = "Ring"
    #  to be expanded that equiptment gives stat bonuses
    equiptment_slots = {
        "Head": None,
        "Chest": None,
        "Arm_L": None,
        "Hand_L": {
            "Thumb": None,
            "Indexfinger": None,
            "Middlefinger": None,
            "Ringfinger": None,
            "Pinkyfinger": None,
        },
        "Hand_R": {
            "Thumb": None,
            "Indexfinger": None,
            "Middlefinger": None,
            "Ringfinger": None,
            "Pinkyfinger": None,
        },
        "Arm_R": None,
        "Hips": None,
        "Leg_L": None,
        "Leg_R":None
    }   

    def get_attr(self,attribute):
        return attribute
    
    def set_attr(self,attribute: str, amount: int):
        current_value = getattr(self,attribute)
        setattr(self, attribute, current_value + amount)
    
    def set_lebenspunkte(self,konstitution,körperkraft):
        value = round(((konstitution*2) + körperkraft)/2)
        setattr(self,"lebenspunkte", value) 
    
    def set_ausdauer(self, mut, konstitution, gewandtheit):
        value = (mut + konstitution + gewandtheit) / 2
        setattr(self, "ausdauer", value)

    def set_astralenergie(self, mut, intuition, charisma):
        value = (mut + intuition + charisma) / 2
        setattr(self, "astralenergie", value)

    def set_magieresistenz(self, mut, klugheit, konstitution):
        value = (mut + klugheit + konstitution) / 5
        setattr(self, "magieresistenz", value)

    def set_ini_basiswert(self, mut, intuition, gewandtheit):
        value = (mut * 2 + intuition + gewandtheit) / 5
        setattr(self, "ini_basiswert", value)

    def set_at_basiswert(self, mut, gewandtheit, körperkraft):
        value = (mut + gewandtheit + körperkraft) / 5
        setattr(self, "at_basiswert", value)

    def set_pa_basiswert(self, intuition, gewandtheit, körperkraft):
        value = (intuition + gewandtheit + körperkraft) / 5
        setattr(self, "pa_basiswert", value)

    def set_fk_basiswert(self, intuition, fingerfertigkeit, körperkraft):
        value = (intuition + fingerfertigkeit + körperkraft) / 5
        setattr(self, "fk_basiswert", value)
    

# Testing
x = Character(name="x")
print(x)

x.set_attr("konstitution",8)
x.set_attr("körperkraft",9)
x.set_lebenspunkte(x.konstitution,x.körperkraft) # 8*2 = 16+9 = 25/2 = 12.5 round = 12 / round uses Bankers Round?
print(x)

# x.equiptment_slots["Head"] = "Helmet"
# print(x.equiptment_slots["Head"])