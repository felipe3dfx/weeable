from django.conf import settings

def logo_company(request):
	return {'LOGO_COMPANY' : settings.LOGO_COMPANY}
