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
    kultur_index:int = 0
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
    
    def set_eigenschaften(self,attribute: str, amount: int):
        current_value = getattr(self,attribute)
        setattr(self, attribute, current_value + amount)

    def set_attribute(self, attribute_name, basiswert, *multipliers, divisor=1):
        value = basiswert + sum(multipliers) / divisor
        setattr(self, attribute_name, round(value))

    def set_lebenspunkte(self):
        self.set_attribute("lebenspunkte", self.lp_grundwert, 2 * self.konstitution)

    def set_seelenkraft(self):
        self.set_attribute("seelenkraft", self.seelenkraft_grundwert, self.mut, self.klugheit, self.intuition, divisor=6)

    def set_zähigkeit(self):
        self.set_attribute("zähigkeit", self.zähigkeit_grundwert, 2 * self.konstitution, self.körperkraft, divisor=6)
    
    def set_ausdauer(self):
        self.set_attribute("ausdauer", self.mut, self.konstitution,self.gewandtheit, divisor=2)

    def set_astralenergie(self):
        self.set_attribute("astralenergie", self.mut,self.intuition,self.charisma, divisor=2)

    def set_magieresistenz(self):
        self.set_attribute("magieresistenz", self.mut,self.klugheit,self.konstitution, divisor=5)

    def set_geschwindigkeit(self):
        self.set_attribute("geschwindigkeit", self.geschwindigkeit_grundwert)


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

    def set_spezies_data(self, spezies_name:str,spezies_kultur_idx:int):
        spezies_data = spezies_db.spezies[spezies_name]
        self.spezies = spezies_data["name"]
        self.kultur = spezies_data["Übliche Kulturen"][spezies_kultur_idx]
        self.lebensenergie_grundwert = spezies_data["LP-Grundwert"]
        self.seelenkraft_grundwert = spezies_data["Seelenkraft-Grundwert"]
        self.zähigkeit_grundwert = spezies_data["Zähigkeit-Grundwert"]
        self.geschwindigkeit_grundwert = spezies_data["Geschwindigkeit-Grundwert"]
        for attr, value in spezies_data["Eigenschaftsänderung"].items():
            setattr(self, attr, getattr(self, attr) + value)

    def set_kultur(self, kultur_name):
        # Ähnlich wie set_spezies_data, wird Kultur-Modifikationen auf die Attribute angewendet.
        kultur_data = spezies_db.kulturen[kultur_name]
        self.kultur = kultur_data["name"]
        
        # for attr, value in kultur_data["Eigenschaftsänderung"].items():
        #     setattr(self, attr, getattr(self, attr) + value)

    def set_all(self):
        """Automatisch alle relevanten Funktionen für die Charaktererstellung aufrufen"""
        self.set_eigenschaften("geschwindigkeit", self.geschwindigkeit_grundwert)
        self.set_lebenspunkte()
        self.set_seelenkraft()
        self.set_zähigkeit()
        self.set_magieresistenz()
        self.set_astralenergie()
        # self.set_karmaenergie() # TODO or maybe not XD
        self.set_ini_basiswert(self.mut, self.intuition, self.gewandtheit)
        self.set_at_basiswert(self.mut, self.gewandtheit, self.körperkraft)
        self.set_pa_basiswert(self.intuition, self.gewandtheit, self.körperkraft)
        self.set_fk_basiswert(self.intuition, self.fingerfertigkeit, self.körperkraft)



    def __str__(self):
        return (f"Character Name: {self.name}\n"
                f"Spezies: {self.spezies}\n"
                f"Kultur: {self.kultur}, Profession: {self.profession}, XP: {self.xp}\n"
                f"Mut: {self.mut}, Klugheit: {self.klugheit}, Intuition: {self.intuition}, Charisma: {self.charisma}\n"
                f"Fingerfertigkeit: {self.fingerfertigkeit}, Gewandtheit: {self.gewandtheit}, Konstitution: {self.konstitution}, Körperkraft: {self.körperkraft}\n"
                f"Geschwindigkeit: {self.geschwindigkeit}, Lebenspunkte: {self.lebenspunkte}, Seelenkraft: {self.seelenkraft}, Zähigkeit: {self.zähigkeit}\n"
                f"Magieresistenz: {self.magieresistenz}, Astralenergie: {self.astralenergie}, Karmaenergie: {self.karmaenergie}\n"
                f"Ini-Basiswert: {self.ini_basiswert}, AT-Basiswert: {self.at_basiswert}, PA-Basiswert: {self.pa_basiswert}, FK-Basiswert: {self.fk_basiswert}")

# region Testing
x = Character(name="x")
x.set_spezies_data("ACHAZ",2) # Spezies: dict -> str "ACHAZ" / "Übliche Kulturen": list -> index 2 = "Stammesachaz"
x.set_eigenschaften("mut",9)
x.set_eigenschaften("klugheit",13)
x.set_eigenschaften("intuition",10)
x.set_eigenschaften("charisma",7)
x.set_eigenschaften("fingerfertigkeit",10)
x.set_eigenschaften("gewandtheit",12)
x.set_eigenschaften("konstitution",8)
x.set_eigenschaften("körperkraft",13)

x.set_all()


print(x)
# endregion