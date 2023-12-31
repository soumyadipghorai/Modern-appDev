from .database import db
from flask_security import UserMixin, RoleMixin

roles_user = db.Table(
        'roles_user', 
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')), 
        db.Column('role_id', db.Integer, db.ForeignKey('role.id')), 
    )

class User(db.Model, UserMixin) : 
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_name = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary = roles_user, backref = db.backref('user', lazy = 'dynamic'))

class Role(db.Model, RoleMixin): 
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))

class Article(db.Model) : 
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    authors = db.relationship('User', secondary = 'article_authors')

class ArticleAuthors(db.Model) : 
    __tablename__ = 'article_authors'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True, nullable = False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'), primary_key = True, nullable = False)
 
class ArticleSearch(db.Model): 
    __tablename__ = 'article_search'
    rowid = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)