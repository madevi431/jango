from django.forms import ModelForm
from myapp.models import userregister
class userregisterform(ModelForm):
	class Meta:
		model=userregister
		fields='__all__'