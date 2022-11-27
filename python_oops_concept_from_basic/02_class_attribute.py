class student():
    name="Rame kumar"
    age=24
#getattr method 1

print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','male'))

#dot . method 2

print(student.name)
print(student.age)


#setattr

setattr(student,'name','vijay')

print(student.name)

setattr(student,'gender','male')
print(student.gender)

student.city='salem'
print(student.city)


print(student.__dict__)


#delete attribute

del student.gender
print(student.__dict__)