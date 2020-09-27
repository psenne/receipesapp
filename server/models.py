from server import db, ma
from datetime import datetime
from sqlalchemy.exc import IntegrityError


################## DATABASE #################


recipes_to_categories = db.Table('recipe_categories',
                                 db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
                                 db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
                                 )


class User(db.Model):
    # Exclude nested model of the same class to avoid max recursion error
    serialize_rules = ('-recipes.author',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=True)
    google_id = db.Column(db.String(255), unique=True, nullable=True)
    recipes = db.relationship('Recipe', backref='author', lazy='dynamic')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User ${self.name}>'


class Recipe(db.Model):
    # Exclude nested model of the same class to avoid max recursion error
    serialize_rules = ('-user.recipes',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    summary = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    directions = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    categories = db.relationship("Category", secondary=recipes_to_categories, back_populates="recipes", lazy=True)

    # def __init__(self, title, ingredients, directions, image, user_id):
    #     self.title = title
    #     self.ingredients = ingredients
    #     self.directions = directions
    #     self.image = image
    #     self.user_id = user_id

    def __repr__(self):
        return f'<Recipe ${self.title}>'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipes = db.relationship("Recipe", secondary=recipes_to_categories, back_populates="categories", lazy=True)

    def __repr__(self):
        return f'<Category ${self.name}>'


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        include_fk = True
    
    author = ma.HyperlinkRelated("getuser")
