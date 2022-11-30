from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_date = models.DateField()

    class Meta:
        abstract = True


class ClassRoom(models.Model):
    name = models.CharField(max_length=2)
    start_time = models.TimeField()

    def __str__(self) -> str:
        return self.name+" - "+ str(self.start_time)

    class Meta:
        db_table = "classrooms"



class Student(Person):
    classroom_id = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    grade_lab = models.FloatField(default=0.0)
    grade_exam = models.FloatField(default=0.0)
    grade_final = models.FloatField(default=0.0)

    class Meta:
        db_table = "students"


class StudentProxy(Student):
    class Meta:
        ordering = ["-id"]
        proxy = True

    def average(self):
        return self.grade_exam*0.1+self.grade_lab*0.6+self.grade_final*0.3


class Teacher(Person):
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = "teachers"


class TeacherProxy(Teacher):
    class Meta:
        proxy = True

    def get_bonnus(self):
        return self.salary + self.rating*100