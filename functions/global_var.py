class Person():
    _id_counter = 0
    
    def __init__(self, name=None, main_category=None, side_categories=None):
        Person._id_counter += 1
        
        self.id = Person._id_counter
        self.name = name
        self.main_category = main_category
        self.side_categories = side_categories



class Team():
    _id_counter = 0

    def __init__(self):
        Team._id_counter += 1

        self.id = Team._id_counter
        self.members = list()


    def add_member(self,member):
        self.members.append(member)


    def remove_member(self, member):
        self.members.remove(member)


    def is_in_team(self, member):
        try:
            return bool(self.members.index(member))
        except:
            return False
        # return bool(self.members.index(member))