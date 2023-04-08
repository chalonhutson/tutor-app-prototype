from flask import Blueprint, render_template

tutors = Blueprint("tutors", __name__, url_prefix="/tutors")

class Tutor:
    def __init__(self, name, img_url, subjects):
        self.name = name
        self.img_url = img_url
        self.subjects = subjects

tutors_list = [
    Tutor("Emma Thompson", "tutor_1.png", ["math", "history"]),
    Tutor("Sophia Rodriguez", "tutor_2.png", ["astronomy", "physics"]),
    Tutor("Matthew Brown", "tutor_3.png", ["history", "social studies", "civics"]),
    Tutor("Alexander Kim", "tutor_4.png", ["math", "algebra", "calculus"]),
    Tutor("Christopher Chen", "tutor_5.png", ["civics", "history", "government"])
]

@tutors.route("/")
def tutors_page():
    # tutors_list = tutors_list
    return render_template("tutors.html", tutors_list=tutors_list)