from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import Template, Context, loader, RequestContext
from app.weather import WeatherParser

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        desired = request.GET.get('desired','Cracow')
        template = Template("""
            <html>
                <head>
                    <title>Weather in the city</title>
                </head>
                <body>
                    <form>{% csrf_token %}
                        Desired city: <input type="text" name="desired"><br>
                        <input type="submit" value="Submit">
                    </form>
                    <h5>
                    Weather for {{ request.0.query }}
                    </h5>
                    <br>
                    Observation time: {{ current_condition.0.observation_time}}
                    <br>
                    Temperature: {{ current_condition.0.temp_C }}
                    <br>
                    Humidity: {{current_condition.0.humidity}}
                    <br>
                    Pressure: {{current_condition.0.pressure}}
                    <br>
                    Windspeed in Kmph: {{current_condition.0.windspeedKmph}}
                </body>
            </html>
        """)
        context = Context(WeatherParser.download(desired))
        return HttpResponse(template.render(context))