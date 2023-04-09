from flask import Blueprint, render_template

tutors = Blueprint("tutors", __name__, url_prefix="/tutors")

class Tutor:
    def __init__(self, name, img_url, subjects, rating):
        self.name = name
        self.img_url = img_url
        self.subjects = subjects
        self.rating = rating

tutors_list = [
    Tutor("Emma Thompson", "tutor_1.png", ["math", "history"], 4.5),
    Tutor("Sophia Rodriguez", "tutor_2.png", ["astronomy", "physics"], 4.9),
    Tutor("Matthew Brown", "tutor_3.png", ["history", "social studies", "civics"], 4.7),
    Tutor("Alexander Kim", "tutor_4.png", ["math", "algebra", "calculus"], 4.8),
    Tutor("Christopher Chen", "tutor_5.png", ["civics", "history", "government"], 4.5)
]

@tutors.route("/")
def tutors_page():
    subjects = ["Astronomy", "Physics", "Civics", "History", "Algebra", "Calculus"]
    return render_template("tutors.html", tutors_list=tutors_list, subjects=subjects)