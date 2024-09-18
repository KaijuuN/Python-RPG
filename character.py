### Das Schwarze Auge in Python
### using german words

from dataclasses import dataclass
import spezies_db

@dataclass
class Character:
    # Persönliche Daten
    name: str = ""
    spezies: str = ""
    kultur:str = ""
    profession: str = ""
    xp: int = 0
    # Eigenschaften
    mut: int = 0
    klugheit: int = 0
    intuition: int = 0
    charisma: int = 0
    fingerfertigkeit: int = 0
    gewandtheit: int = 0
    konstitution: int = 0
    körperkraft: int = 0

    lebenspunkte: int = 0
    lp_grundwert: int = 0
    astralenergie: int = 0
    karmaenergie: int = 0
    seelenkraft: int = 0
    seelenkraft_grundwert: int = 0
    zähigkeit: int = 0
    zähigkeit_grundwert: int = 0
    ausweichen: int = 0
    geschwindigkeit: int = 0
    geschwindigkeit_grundwert: int = 0
    
    ausdauer: int = 0
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
    
    def set_lebenspunkte(self,konstitution,le_gw):
        value = le_gw+(2*konstitution)
        setattr(self,"lebenspunkte", value) 
    
    def set_ausdauer(self, mut, konstitution, gewandtheit):
        value = (mut + konstitution + gewandtheit) / 2
        setattr(self, "ausdauer", value)

    def set_astralenergie(self, mut, intuition, charisma):
        value = (mut + intuition + charisma) / 2
        setattr(self, "astralenergie", value)

    def set_seelenkraft(self,grundwert, mut, klugheit, intuition):
        value = round(grundwert+((mut + klugheit + intuition) / 6))
        setattr(self, "seelenkraft", value)
    
    def set_zähigkeit(self,grundwert, konstitution,körperkraft):
        value = round(grundwert+(((konstitution*2)+körperkraft) / 6))
        setattr(self, "zähigkeit", value)


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

    def set_spezies(self, spezies_name):
        spezies_data = spezies_db.spezies[spezies_name]
        self.spezies = spezies_data["name"]
        self.lebensenergie_grundwert = spezies_data["LP-Grundwert"]
        self.seelenkraft_grundwert = spezies_data["Seelenkraft-Grundwert"]
        self.zähigkeit_grundwert = spezies_data["Zähigkeit-Grundwert"]
        for attr, value in spezies_data["Eigenschaftsänderung"].items():
            setattr(self, attr, getattr(self, attr) + value)

    def set_all_attr():
        pass



    def __str__(self):
        return (f"Character Name: {self.name}\n"
                f"Spezies: {self.spezies}\n"
                f"Kultur: {self.kultur}, Profession: {self.profession}, XP: {self.xp}\n"
                f"Mut: {self.mut}, Klugheit: {self.klugheit}, Intuition: {self.intuition}, Charisma: {self.charisma}\n"
                f"Fingerfertigkeit: {self.fingerfertigkeit}, Gewandtheit: {self.gewandtheit}, Konstitution: {self.konstitution}, Körperkraft: {self.körperkraft}\n"
                f"Geschwindigkeit: {self.geschwindigkeit}, LP: {self.lebenspunkte}, Seelenkraft: {self.seelenkraft}, Zähigkeit: {self.zähigkeit}\n"
                f"Magieresistenz: {self.magieresistenz}, Astralenergie: {self.astralenergie}, Karmaenergie: {self.karmaenergie}\n"
                f"Ini-Basiswert: {self.ini_basiswert}, AT-Basiswert: {self.at_basiswert}, PA-Basiswert: {self.pa_basiswert}, FK-Basiswert: {self.fk_basiswert}")


# region Testing
x = Character(name="x")
x.set_spezies("ACHAZ")
x.set_attr("mut",9)
x.set_attr("klugheit",13)
x.set_attr("intuition",10)
x.set_attr("charisma",7)
x.set_attr("fingerfertigkeit",10)
x.set_attr("gewandtheit",12)
x.set_attr("konstitution",8)
x.set_attr("körperkraft",13)

x.set_attr("geschwindigkeit", x.geschwindigkeit_grundwert)

x.set_lebenspunkte(x.konstitution,x.lp_grundwert) 
x.set_seelenkraft(x.seelenkraft_grundwert,x.mut,x.klugheit,x.intuition)
x.set_zähigkeit(x.zähigkeit_grundwert,x.konstitution,x.körperkraft)
print(x)
# endregion