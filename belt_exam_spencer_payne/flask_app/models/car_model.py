from flask_app.config.mysqlconnection import connectToMySQL
import pprint
from flask import flash


db = "car_dealz_schema_final"

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def car_save(cls, data):
        query = """ INSERT INTO cars(price, model, make, year, description, user_id)
        VALUES(%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(user_id)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_car_by_user(cls):
        query = """SELECT * FROM cars
        LEFT JOIN users ON cars.user_id = users.id;
        """
        results=connectToMySQL(db).query_db(query)
        return results
    
    @classmethod
    def update_car(cls, data):
        query = """UPDATE cars
        SET price = %(price)s, model =%(model)s, make=%(make)s, year=%(year)s, description=%(description)s
        WHERE id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_car_by_id(cls, data):
        query="""SELECT * FROM cars
        WHERE id = %(id)s;
        """
        results=connectToMySQL(db).query_db(query, data)
        return results[0]

    @classmethod
    def delete(cls, data):
        query="""DELETE FROM cars
        WHERE id=%(id)s;
        """
        results=connectToMySQL(db).query_db(query,data)
        pprint.pprint(results)
        return results



    @staticmethod
    def validation(data):
        is_valid = True
        if not data['model']:
            flash("Invalid")
            is_valid=False
        if not data['price']:
            flash("Price field must not be left blank")
            is_valid=False
        if not data['model']:
            flash("Model field cannot be left blank", "car_error")
            is_valid = False
        if not data['make']:
            flash("Make field cannot be left blank", "car_error")
            is_valid = False
        if not data['year']:
            flash("Please include a year.", "car_error")
            is_valid = False
        if not data['description']:
            flash("Please provide a description.")
            is_valid=False
        return is_valid
        