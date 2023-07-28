# imports
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from werkzeug.exceptions import HTTPException
import json

# initialisation
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api_database.sqlite3"
db = SQLAlchemy(app)
api = Api(app)
app.app_context().push()

# models
class Enrollment(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"),nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    courses = db.relationship("Course", backref="students", secondary = "enrollment")

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)    
    course_code = db.Column(db.String, nullable=False, unique=True)
    course_description = db.Column(db.String)

#common errors
class NotFoundError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('', status_code)

class InternalServerError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('', status_code)

class ExistsError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('', status_code)

class NotExistsError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('', status_code)

class BuisnessValidationError(HTTPException):
    def __init__(self, status_code, error_code, error_message):
        message={"error_code": error_code, "error_message": error_message}
        self.response = make_response(json.dumps(message), status_code)

#courseAPI
output_course = {
    "course_id": fields.Integer,
    "course_name": fields.String,
    "course_code": fields.String,
    "course_description": fields.String
}

course_parser = reqparse.RequestParser()
course_parser.add_argument("course_name")
course_parser.add_argument("course_code")
course_parser.add_argument("course_description")

class courseAPI(Resource):
    @marshal_with(output_course)
    def get(self, course_id):
            try:
                course_obj = Course.query.get(int(course_id))
                if course_obj:
                    return  course_obj
                else:
                    raise NotFoundError(status_code=404)
            except NotFoundError as nfe:
                raise nfe
            except Exception as e:
                raise InternalServerError(status_code=500)

    @marshal_with(output_course)          
    def put(self, course_id):
        try:
            args = course_parser.parse_args()
            course_name = args.get("course_name",None)
            course_code = args.get("course_code",None)
            course_description = args.get("course_description",None)
            if course_name is None:
                raise BuisnessValidationError(status_code=400, error_code="COURSE001", error_message="Course Name is required")
            if course_code is None:
                raise BuisnessValidationError(status_code=400, error_code="COURSE002", error_message="Course Code is required")
            course_obj = Course.query.filter_by(course_id=course_id).first()
            if course_obj:
                course_obj.course_name=course_name
                course_obj.course_code=course_code
                course_obj.course_description=course_description
                db.session.commit()
                updated_course = Course.query.filter_by(course_id=course_id).first()
                return updated_course, 200              
            else:
                raise NotExistsError(status_code=404)

        except BuisnessValidationError as bve:
            raise bve
        except NotExistsError as nee:
            raise nee
        except Exception as e:
            raise InternalServerError(status_code=500)

    def delete(self, course_id):
        try:
            course_obj = Course.query.get(int(course_id))
            if course_obj:
                enroll_obj=Enrollment.query.filter_by(course_id=course_obj.course_id).first()
                while enroll_obj:
                    db.session.delete(enroll_obj)
                    db.session.commit()
                    enroll_obj=Enrollment.query.filter_by(course_id=course_obj.course_id).first()
                db.session.delete(course_obj)
                db.session.commit()
                return "", 200
            else:
                raise NotFoundError(status_code=404)
        except NotFoundError as nfe:
            raise nfe
        except Exception as e:
            raise InternalServerError(status_code=500)

    @marshal_with(output_course)
    def post(self):
        try:
            args = course_parser.parse_args()
            course_name = args.get("course_name",None)
            course_code = args.get("course_code",None)
            course_description = args.get("course_description",None)
            if course_name is None:
                raise BuisnessValidationError(status_code=400, error_code="COURSE001", error_message="Course Name is required")
            if course_code is None:
                raise BuisnessValidationError(status_code=400, error_code="COURSE002", error_message="Course Code is required")
            course_obj = Course.query.filter_by(course_code=course_code).first()
            if course_obj:
                raise ExistsError(status_code=409)
            else:
                new_course = Course(course_name=course_name, course_code=course_code, course_description=course_description)
                db.session.add(new_course)
                db.session.commit()
                new_course = Course.query.filter_by(course_code=course_code).first()
                return new_course, 201
        except BuisnessValidationError as bve:
            raise bve
        except ExistsError as ee:
            raise ee
        except Exception as e:
            raise InternalServerError(status_code=500)

api.add_resource(courseAPI, "/api/course", "/api/course/<int:course_id>")

#studentAPI
output_student = {
    "student_id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "roll_number": fields.String
}

student_parser = reqparse.RequestParser()
student_parser.add_argument("first_name")
student_parser.add_argument("last_name")
student_parser.add_argument("roll_number")

class studentAPI(Resource):
    @marshal_with(output_student)
    def get(self, student_id):
            try:
                student_obj = Student.query.get(int(student_id))
                if student_obj:
                    return student_obj
                else:
                    raise NotFoundError(status_code=404)
            except NotFoundError as nfe:
                raise nfe
            except Exception as e:
                raise InternalServerError(status_code=500)

    @marshal_with(output_student)       
    def put(self, student_id):
        try:
            args = student_parser.parse_args()
            first_name = args.get("first_name",None)
            last_name = args.get("last_name",None)
            roll_number = args.get("roll_number",None)
            if roll_number is None:
                raise BuisnessValidationError(status_code=400, error_code="STUDENT001", error_message="Roll Number required")
            if first_name is None:
                raise BuisnessValidationError(status_code=400, error_code="STUDENT002", error_message="First Name is required")
            student_obj = Student.query.filter_by(student_id=student_id).first()
            if student_obj:
                student_obj.first_name=first_name
                student_obj.last_name=last_name
                student_obj.roll_number=roll_number
                db.session.commit()
                updated_student = Student.query.filter_by(student_id=student_id).first()
                return updated_student, 200              
            else:
                raise NotExistsError(status_code=404)

        except BuisnessValidationError as bve:
            raise bve
        except NotExistsError as nee:
            raise nee
        except Exception as e:
            raise InternalServerError(status_code=500)

    def delete(self, student_id):
        try:
            student_obj = Student.query.get(int(student_id))
            if student_obj:
                enroll_obj=Enrollment.query.filter_by(student_id=student_obj.student_id).first()
                while enroll_obj:
                    db.session.delete(enroll_obj)
                    db.session.commit()
                    enroll_obj=Enrollment.query.filter_by(student_id=student_obj.student_id).first()
                db.session.delete(student_obj)
                db.session.commit()
                return "", 200
            else:
                raise NotFoundError(status_code=404)
        except NotFoundError as nfe:
            raise nfe
        except Exception as e:
            raise InternalServerError(status_code=500)

    @marshal_with(output_student)
    def post(self):
        try:
            args = student_parser.parse_args()
            first_name = args.get("first_name",None)
            last_name = args.get("last_name",None)
            roll_number = args.get("roll_number",None)
            if roll_number is None:
                raise BuisnessValidationError(status_code=400, error_code="STUDENT001", error_message="Roll Number required")
            if first_name is None:
                raise BuisnessValidationError(status_code=400, error_code="STUDENT002", error_message="First Name is required")
            student_obj = Student.query.filter_by(roll_number=roll_number).first()
            if student_obj:
                raise ExistsError(status_code=409)
            else:
                new_student = Student(first_name=first_name, last_name=last_name, roll_number=roll_number)
                db.session.add(new_student)
                db.session.commit()
                new_student = Student.query.filter_by(roll_number=roll_number).first()
                return new_student, 201
        except BuisnessValidationError as bve:
            raise bve
        except ExistsError as ee:
            raise ee
        except Exception as e:
            raise InternalServerError(status_code=500)

api.add_resource(studentAPI, "/api/student", "/api/student/<int:student_id>")
#enrollmentAPI
output_enrollment = {
    "enrollment_id": fields.Integer,
    "student_id": fields.Integer,
    "course_id": fields.Integer
}

enrollment_parser = reqparse.RequestParser()
enrollment_parser.add_argument("course_id")

class enrollmentAPI(Resource):
    @marshal_with(output_enrollment)
    def get(self, student_id):
        try:
            student = Student.query.filter_by(student_id=student_id).first()
            if student:
                enrollment_objs = Enrollment.query.filter_by(student_id=student_id).all()
                if enrollment_objs:
                    return enrollment_objs
                else:
                    raise NotFoundError(status_code=404)
            else:
                raise BuisnessValidationError(status_code=400, error_code="ENROLLMENT002", error_message="Student does not exist.")
        except NotFoundError as nfe:
            raise nfe
        except BuisnessValidationError as bve:
            raise bve
        except Exception as e:
            raise InternalServerError(status_code=500)

    def delete(self, student_id, course_id):
        try:
            student = Student.query.filter_by(student_id=student_id).first()
            course = Course.query.filter_by(course_id=course_id).first()
            if student is None:
                raise BuisnessValidationError(status_code=400, error_code="ENROLLMENT002", error_message="Student does not exist.")
            if course is None:
                raise BuisnessValidationError(status_code=400, error_code="ENROLLMENT001",error_message="Course does not exist")
            enroll_obj =  Enrollment.query.filter_by(course_id=course_id, student_id=student_id).first()
            if enroll_obj is None:
                raise NotFoundError(status_code=404)
            else:
                db.session.delete(enroll_obj)
                db.session.commit()
                return "", 200
        except NotFoundError as nfe:
            raise nfe
        except BuisnessValidationError as bve:
            raise bve
        except Exception as e:
            raise InternalServerError(status_code=500)

    @marshal_with(output_enrollment)
    def post(self, student_id):
        try:
            args = enrollment_parser.parse_args()
            course_id = args.get("course_id",None)
            student = Student.query.filter_by(student_id=student_id).first()
            if student:
                course = Course.query.filter_by(course_id=course_id).first()
                if course:
                    student.courses.append(course)
                    db.session.commit()
                    enrollment_objs = Enrollment.query.filter_by(student_id=student_id).all()
                    return enrollment_objs, 201
                else:
                    raise BuisnessValidationError(status_code=400, error_code="ENROLLMENT001",error_message="Course does not exist")
            else:
                raise NotFoundError(status_code=404)
        except NotFoundError as nfe:
            raise nfe
        except BuisnessValidationError as bve:
            raise bve
        except Exception as e:
            raise InternalServerError(status_code=500)
api.add_resource(enrollmentAPI, "/api/student/<int:student_id>/course", "/api/student/<int:student_id>/course/<int:course_id>")

#run call
if __name__ == "__main__":
    app.run()
