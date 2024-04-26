class NameData:
    def __init__(self, gender):
        self.title = "" 
        self.fname = ""
        self.lname = fake.last_name() + " " + fake.last_name()
        self.mname = ""
        
        if gender == "Male":
            self.fname = randomizer.randomize('male_names_processed.csv')
            self.mname = randomizer.randomize('male_names_processed.csv')
            self.title = random.choice(["Mr.", "Dr."])
        elif gender == "Female":
            self.fname = randomizer.randomize('female_names_processed.csv')
            self.mname = randomizer.randomize('female_names_processed.csv')
            self.title = random.choice(["Mrs.", "Ms.", "Dr."])
        
        self.preferred_name = random.choice([self.fname, self.mname])