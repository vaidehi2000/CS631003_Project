from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Animal, Building, Enclosure, Species
import ast
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType

@csrf_exempt
def view_table(request, table_name):
    try:
        if isinstance(table_name, str):
            try:
                table_name_dict = ast.literal_eval(table_name)
                actual_table_name = table_name_dict.get('name', 'Unknown')
            except (ValueError, SyntaxError):
                actual_table_name = 'Unknown'
        else:
            actual_table_name = table_name

        # Define a mapping of table names to model classes
        table_model_mapping = {
            'buildings': Building,
            'enclosures': Enclosure,
            'species': Species,
            'animals': Animal,
            # Add more mappings as needed
        }

        # Get the model class for the specified table name
        model_class = table_model_mapping.get(actual_table_name.lower())

        if model_class:
            # Retrieve all rows from the model
            rows = list(model_class.objects.values())
            data = {
                'table_name': actual_table_name,
                'rows': rows,
            }
            return render(request, 'view_table.html', data)
        else:
            # Handle the case where the table name doesn't match any model
            return render(request, 'error_page.html', {'message': f"Table '{table_name}' not found"})
    except ContentType.DoesNotExist:
        # Handle the case where the content type for the specified table name doesn't exist
        return render(request, 'error_page.html', {'message': f"Table '{table_name}' not found"})


def home(request):
    return render(request, 'home.html')


# @csrf_exempt
# def get_buildings(request):
#     buildings = Building.objects.all()
#     data = [{'id': building.id, 'name': building.building_name, 'type': building.building_type} for building in buildings]
#     return JsonResponse(data, safe=False)

# def asset_management(request):
#     animals = Animal.objects.all()
#     buildings = Building.objects.all()
#     attractions = Attraction.objects.all()
#     employees = Employee.objects.all()
#     employee_types = EmployeeType.objects.all()

#     context = {
#         'animals': animals,
#         'buildings': buildings,
#         'attractions': attractions,
#         'employees': employees,
#         'employee_types': employee_types,
#     }

#     return render(request, 'asset_management.html', context)
# views.py

def asset_management(request):
    # Sample list of tables, replace this with your actual logic to fetch tables
    tables = [
        {'name': 'Animals'},
        {'name': 'Buildings'},
        # Add more tables as needed
    ]

    return render(request, 'asset_management.html', {'tables': tables})


def daily_zoo_activity(request):
    # Add logic to fetch and pass data related to daily zoo activities
    return render(request, 'daily_zoo_activity.html')

def management_reporting(request):
    # Add logic to fetch and pass data related to management reporting
    return render(request, 'management_reporting.html')

# def view_table(request, table_name):
#     try:
#         if isinstance(table_name, str):
#             try:
#                 table_name_dict = ast.literal_eval(table_name)
#                 actual_table_name = table_name_dict.get('name', 'Unknown')
#             except (ValueError, SyntaxError):
#                 actual_table_name = 'Unknown'
#         else:
#             actual_table_name = table_name
#         # Get the content type for the specified table name
#         content_type = ContentType.objects.get(model=actual_table_name.lower())
    
#         # Get the model class for the content type
#         model_class = content_type.model_class()
#         # Retrieve all rows from the model
#         rows = list(model_class.objects.values())
#         data = {
#             'table_name': actual_table_name,
#             'rows': rows,
#         }
#         return render(request, 'view_table.html', data)
#     except ContentType.DoesNotExist:
#         # Handle the case where the table name doesn't match any model
#         return render(request, 'error_page.html', {'message': f"Table '{table_name}' not found"})
    

#     # print(actual_table_name)

#     # model = actual_table_name.objects.all()

#     # # Convert the queryset to a list of dictionaries
#     # rows = list(model.values())

#     # # Your logic to fetch data for the specified table_name
#     # # For simplicity, let's assume you have a dictionary with some data.
#     # data = {
#     #     'table_name': actual_table_name,
#     #     'rows': rows  # Replace this with actual data for the table
#     # }

#     # data['table_name'] = actual_table_name
#     # return render(request, 'view_table.html', data)

def insert_table(request, table_name):
    # Your logic for inserting data into the specified table_name
    return render(request, 'myapp/insert_table.html', {'table_name': table_name})

def update_table(request, table_name):
    # Your logic for updating data in the specified table_name and row_id
    return render(request, 'myapp/update_table.html', {'table_name': table_name})