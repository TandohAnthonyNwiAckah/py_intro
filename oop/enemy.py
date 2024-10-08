class Enemy:

    type_of_enemy:str
    health:int = 12
    attack_damage:int =8

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight !")

    def walk(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attack for {self.attack_damage} damage")