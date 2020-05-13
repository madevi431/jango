from django.forms import ModelForm
from imageupload.models import upload
class uploadform(ModelForm):
	class Meta:
		model=upload
		fields='__all__'