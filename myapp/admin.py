from django.contrib import admin
from .models import Species, Building, Enclosure, Animal, HourlyRate, Employee, Supervisor, Veterinarian, AnimalCareSpecialist, Maintenance, RevenueTypes, AnimalShow, Concession, ZooAdmission, VeterinarianCaresFor, ParticipatesIn, Attraction

admin.site.register(Species)
admin.site.register(Building)
admin.site.register(Enclosure)
admin.site.register(Animal)
admin.site.register(HourlyRate)
admin.site.register(Employee)
admin.site.register(Supervisor)
admin.site.register(Veterinarian)
admin.site.register(AnimalCareSpecialist)
admin.site.register(RevenueTypes)
admin.site.register(AnimalShow)
admin.site.register(Concession)
admin.site.register(ZooAdmission)
admin.site.register(VeterinarianCaresFor)
admin.site.register(ParticipatesIn)
admin.site.register(Attraction)
