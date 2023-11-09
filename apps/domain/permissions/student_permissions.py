def has_student_permissions(user, student):
    return user.id == student.owner.id
