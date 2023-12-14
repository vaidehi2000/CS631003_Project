from django.db import models

class Species(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    species_name = models.CharField(max_length=10)
    food_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.species_name}"

class Building(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    building_name = models.CharField(max_length=20, unique=True)
    building_type = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.building_name
    
class Enclosure(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, db_column='Building_ID')
    square_feet = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.building_id.building_name}"
    
class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    animal_status = models.CharField(max_length=7)
    birth_year = models.CharField(max_length=15)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.CASCADE)
    enclosure = models.ForeignKey(Enclosure, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.animal_status} - {self.birth_year} - {self.species}"
    
class HourlyRate(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} - ${self.rate}/hour"
    
class Employee(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    start_date = models.DateField()
    job_type = models.CharField(max_length=20)
    first_name = models.CharField(max_length=9)
    minit = models.CharField(max_length=1, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    street = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    address_state = models.CharField(max_length=9)
    zip = models.IntegerField()
    supervisor_id = models.CharField(max_length=15)
    hourly_rate_id = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_type}"

class Supervisor(models.Model):
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    
class Veterinarian(models.Model):
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Veterinarian - {self.emp_id.first_name} {self.emp_id.last_name}"
    
class AnimalCareSpecialist(models.Model):
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Animal Care Specialist - {self.emp_id.first_name} {self.emp_id.last_name}"
    
class Maintenance(models.Model):
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Maintenance - {self.emp_id.first_name} {self.emp_id.last_name}"
    
class RevenueTypes(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    revenue_type = models.CharField(max_length=20)
    revenue_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.revenue_type} - {self.revenue_name}"
    
# class AnimalShow(models.Model):
#     revenue_type_id = models.CharField(max_length=15, primary_key=True)
#     senior_price = models.CharField(max_length=5)
#     adult_price = models.CharField(max_length=15)
#     child_price = models.CharField(max_length=9)
#     num_per_day = models.CharField(max_length=20)

#     # Foreign Key relationship with REVENUE_TYPES
#     revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.revenue_type} - {self.num_per_day}"
    
class AnimalShow(models.Model):
    revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE, related_name='animal_shows')
    senior_price = models.CharField(max_length=5)
    adult_price = models.CharField(max_length=15)
    child_price = models.CharField(max_length=9)
    num_per_day = models.CharField(max_length=20)

    def __str__(self):
        return f"Animal Show for Revenue Type {self.revenue_type}"
    
# class Concession(models.Model):
#     revenue_type_id = models.CharField(max_length=15, primary_key=True)
#     product = models.CharField(max_length=19)

#     # Foreign Key relationship with REVENUE_TYPES
#     revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.revenue_type} - {self.product}"
    
# class ZooAdmission(models.Model):
#     revenue_type_id = models.CharField(max_length=15, primary_key=True)
#     senior_price = models.DecimalField(max_digits=10, decimal_places=2)
#     adult_price = models.DecimalField(max_digits=15, decimal_places=2)
#     child_price = models.CharField(max_length=9)

#     # Foreign Key relationship with REVENUE_TYPES
#     revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.revenue_type} - Senior: {self.senior_price}, Adult: {self.adult_price}, Child: {self.child_price}"

class ZooAdmission(models.Model):
    revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE, related_name='zoo_admissions')
    senior_price = models.CharField(max_length=10)
    adult_price = models.CharField(max_length=15)
    child_price = models.CharField(max_length=9)

    def __str__(self):
        return f"Zoo Admission for Revenue Type {self.revenue_type}"

class Concession(models.Model):
    revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE, related_name='concession_entries')
    product = models.CharField(max_length=19)

    def __str__(self):
        return f"Concession for Revenue Type {self.revenue_type}"

class ParticipatesIn(models.Model):
    species = models.ForeignKey('Species', on_delete=models.CASCADE, related_name='participation_species')
    revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE, related_name='participation_entries')
    num_per_day = models.CharField(max_length=15)

    def __str__(self):
        return f"Participates In for Species {self.species} and Revenue Type {self.revenue_type}"

class VeterinarianCaresFor(models.Model):
    species = models.ForeignKey('Species', on_delete=models.CASCADE, related_name='veterinarian_care_species')
    emp_id = models.CharField(max_length=15)

    def __str__(self):
        return f"Veterinarian Cares For for Species {self.species} and Employee ID {self.emp_id}"
    
# class VeterinarianCaresFor(models.Model):
#     species_id = models.CharField(max_length=15)
#     emp_id = models.CharField(max_length=15)

#     # Primary Key
#     class Meta:
#         unique_together = ('species_id', 'emp_id')

#     # Foreign Key relationships
#     species = models.ForeignKey('Species', on_delete=models.CASCADE)
#     employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"Veterinarian {self.employee} cares for Species {self.species}"

# class ParticipatesIn(models.Model):
#     species_id = models.CharField(max_length=15)
#     revenue_type_id = models.CharField(max_length=15)
#     num_per_day = models.CharField(max_length=15)

#     # Primary Key
#     class Meta:
#         unique_together = ('species_id', 'revenue_type_id')

#     # Foreign Key relationships
#     species = models.ForeignKey('Species', on_delete=models.CASCADE, related_name='participations')
#     revenue_type = models.ForeignKey('RevenueTypes', on_delete=models.CASCADE, related_name='participations')

#     def __str__(self):
#         return f"Species {self.species} participates in Revenue Type {self.revenue_type}"


class Attraction(models.Model):
    name = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    shows_per_day = models.IntegerField()
    ticket_price = models.FloatField()
    # Add other fields as needed