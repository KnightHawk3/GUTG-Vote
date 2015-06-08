from GUTG_Vote.extensions import db, login

@login.user_loader
def load_user(id):
    return User.objects(username=id).first()

class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return str(self.username)
 

class Game(db.Document):
    game_id = db.IntField(required=True)
    title = db.StringField(required=True)
    url = db.StringField(required=True)
    votes = db.IntField(required=True)
    cost = db.FloatField(required=True)
    voters = db.ListField()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return str(self.user_id)
