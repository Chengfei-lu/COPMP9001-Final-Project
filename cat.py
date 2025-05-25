import random
class Cat:
    def __init__(self,name,age=1):
        self.name=name
        self.health=100
        self.energy=100
        self.mood=100
        self.hunger=0
        self.age=age
        self.skills=[]
    def status(self):
        print(f'\n--- {self.name}\'s Current Status ---')
        print(f'Health:{self.health}')
        print(f'Energy:{self.energy}')
        print(f'Mood:{self.mood}')
        print(f'Hunger:{self.hunger}')
        print(f'Age:{self.age}')
        print(f'Skills:{self.skills}')
        print('-----------------------------------')
    def eat(self,food):
        if food not in ['fish','chicken','chocolate']:
            raise ValueError('The food is not suitable for cat!')
        print(f'{self.name} has eaten {food}')
        
        if food =='fish':
            self.health += 5
            self.energy+=10
            if self.mood>=10:
                self.mood -= 10
            self.hunger = max(0, self.hunger - 30)
        elif food =='chocolate':
            self.health+=5
            self.energy+=10
            self.mood+=10
            self.hunger = max(0, self.hunger - 30)
        elif food =='chicken':
            self.health+=5
            self.energy+=10
            self.mood+=5
            self.hunger = max(0, self.hunger - 30)

    def sleep(self,hours:int):
        while True:
            try:
                if not isinstance(hours, int):
                    raise ValueError("Sleep time must be an integer")
                if hours < 0:
                    raise IndexError('Sleep time must be positive')
                print(f'{self.name} is sleeping for {hours} hours')
                self.energy = min(100, self.energy + hours * 10)
                self.health = min(100, self.health + hours * 5)
                break
            except ValueError as ve:
                print('NO',ve)
                hours = int(input('Please enter an integer sleep time: '))
            except IndexError as ie:
                print('No',ie)
                hours = int(input('Please enter an integer sleep time: '))

    def play(self,command):
        try:
            parts=command.split()
            if len(parts)<2:
                raise ValueError('Use correct format:play_toy')
            action,toy=parts[0],parts[1]
            if action!='play':
                raise ValueError('First part must be play!')
            toy_effects = {
            "yarn": 10,
            "mouse": 15,
            "feather": 20,
            "laser": 25
            }
            if self.energy < 15:
                raise IndexError(f'{self.name} is too tired to play')
            mood_boost = toy_effects.get(toy, 5)
            self.mood= min(100,self.mood+mood_boost)
            self.energy -= 15
            print(f'{self.name} is happily playe with{toy}')
            if toy not in self.skills:
                self.skills.append(toy)
                print(f'{self.name} has mastered the skills of {toy}')
        except ValueError as ve:
            print('NO',ve)
        except IndexError as ie:
            print('No',ie)
        
    def birthday(self):
        print(f'Happy birthday! {self.name}. Now you are {self.age+1} years old!')
        self.age+=1
        self.mood +=random.randint(1,5)
        self.health +=random.randint(1,5)
        self.energy = min(100, self.energy + 5)
        print(f"{self.name}'s mood and health improved slightly to celebrate!")
    
    def happiness_index(self,age=None):
        if age==None:
            age= self.age
        if age<=0:
            return 0
        annual_happiness = self.mood * random.uniform(0.8, 1.2) / age
        print(f"Year {age}: {annual_happiness:.2f} happiness")
        return annual_happiness +self.happiness_index(age-1)
