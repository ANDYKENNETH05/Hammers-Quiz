from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    # Relationship to questions
    questions = db.relationship('Question', backref='quiz', lazy=True, cascade="all, delete-orphan")


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)

    # Relationship to answers
    answers = db.relationship('Answer', backref='question', lazy=True, cascade="all, delete-orphan")


class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)


class User(db.model, UserMixin):
    id = db.Column(db.Interger, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Ccolumn(db.String(150))
    first_name = db.Column(db.String(150))