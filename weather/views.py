from django.shortcuts import render
import json
import urllib.request



# Create your views here.
def index(request):
	if request.method == 'POST':
		city = request.POST['city']
		res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=d105e968ff6e87c8b9d22d3f4145c1bd').read()
		json_data = json.loads(res)
		data = {
			"country_code": str(json_data['sys']['country']),
			"coordinate": str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
			"temp": str(json_data['main']['temp']) + 'k',
			'pressure': str(json_data['main']['pressure']),
			'humidity': str(json_data['main']['humidity']),
			
		}
	else:
		city = ''
		data = {}
	return render(request, 'index.html', {'city': city, 'data': data})



