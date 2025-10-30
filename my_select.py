from sqlalchemy import func, desc
from database import session
from create_db import Student, Group, Teacher, Subject, Grade


def select_1():
    result = (
        session.query(Student.fullname, func.round(func.avg(Grade.grade)).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


def select_2(subject_name):
    result = (
        session.query(Student.fullname, func.round(func.avg(Grade.grade)).label("avg_grade"))
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    )
    return result


def select_3(subject_name):
    result = (
        session.query(Group.name, func.round(func.avg(Grade.grade)).label("avg_grade"))
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .all()
    )
    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.grade))).scalar()
    return result


def select_5(group_name, subject_name):
    result = (
        session.query(func.round(func.avg(Grade.grade)))
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .scalar()
    )
    return result


def select_6(teacher_name, subject_name):
    result = (
        session.query(func.round(func.avg(Grade.grade)))
        .select_from(Grade)
        .join(Subject)
        .join(Teacher)
        .filter(Teacher.fullname == teacher_name, Subject.name == subject_name)
        .scalar()
    )
    return result


def select_7(student_name, teacher_name):
    result = (
        session.query(Subject.name)
        .select_from(Subject)
        .join(Teacher)
        .join(Grade)
        .join(Student)
        .filter(Student.fullname == student_name, Teacher.fullname == teacher_name)
        .distinct()
        .all()
    )
    return result

def select_8(teacher_name):
    result = (
        session.query(Subject.name)
        .select_from(Subject)
        .join(Teacher)
        .filter(Teacher.fullname == teacher_name)
        .all()
    )
    return result


def select_9(group_name):
    result = (
        session.query(Student.fullname)
        .select_from(Student)
        .join(Group)
        .filter(Group.name == group_name)
        .all()
    )
    return result


def select_10(group_name, subject_name):
    result = (
        session.query(Student.fullname, Grade.grade)
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )
    return result


if __name__ == "__main__":
    print("1.", select_1())
    print("2.", select_2("Math"))
    print("3.", select_3("Math"))
    print("4.", select_4())
    print("5.", select_5("Group A", "Math"))
    print("6.", select_6("Jose Garcia", "Math"))
    print("7.", select_7("Tiffany Jones", "Jose Garcia"))
    print("8.", select_8("Jose Garcia"))
    print("9.", select_9("Group A"))
    print("10.", select_10("Group A", "Math"))
