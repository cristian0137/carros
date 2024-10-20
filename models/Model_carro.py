from config.database import db

class Carro(db.Model):

    __tablename__ = 'Carros'

    id = db.Column(db.Integer, primary_key= True) 
    modelo = db.Column(db.String(100))
    color = db.Column(db.String(100))
    puertas = db.Column(db.Integer)

    def to_dict (self):
        return{
            'id':self.id,
            'modelo':self.modelo,
            'color': self.color,
            'puertas':self.puertas
        }

