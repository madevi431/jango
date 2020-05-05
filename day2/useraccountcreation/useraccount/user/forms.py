from django.forms import ModelForm
from user.models import candidate
class candidateform(ModelForm):
	class Meta:
		model=candidate
		#fields='__all__'#generates one list for all the fields in the model
		fields=['first_name','last_name','user_name','email','age','contact']

