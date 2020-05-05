from django.forms import ModelForm
from mayapp2.models import Student
class StudentForm(ModelForm):
	class Meta:
		model=Student
		fields='__all__'#generates one list for all the fields in the model
		#fields=['stuid','stuName'] for specific fields
		

