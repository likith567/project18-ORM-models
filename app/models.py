from django.db import models

# Create your models here.


    

class course(models.Model):
    cid=models.IntegerField(primary_key=True)
    coursename=models.CharField(max_length=100)
    trainer=models.CharField(max_length=50)

    def __str__(self):
        return self.coursename

class student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50)
    email=models.CharField(max_length=100,unique=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

class bonus(models.Model):
    Ename=models.CharField(max_length=10)
    Job=models.CharField(max_length=9)
    Sal=models.IntegerField()
    Comm=models.IntegerField()

    def __str__(self):
        return self.Ename

class Salgrade(models.Model):
    grade=models.IntegerField()
    losal=models.IntegerField()
    hisal=models.IntegerField()

class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=14)
    loc=models.CharField(max_length=13)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=10)
    job=models.CharField(max_length=10)
    mgr=models.IntegerField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.IntegerField()

def __str__(self):
    return self.ename