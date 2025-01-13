import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("*Weather Temperature Converter*", style={'textAlign': 'center','color':'blue'}),

    # Input for city name
    dcc.Input(id="city-name", type="text", placeholder="Enter city name", style={'margin': '10px'}),

    # Dropdown for conversion type
    dcc.Dropdown(
        id="conversion-type",
        options=[
            {'label': 'Celsius to Fahrenheit', 'value': 'C_to_F'},
            {'label': 'Fahrenheit to Celsius', 'value': 'F_to_C'}
        ],
        value='C_to_F',
        style={'width': '50%', 'margin': '10px'}
    ),

    # Button to trigger conversion
    html.Button('Get Weather', id='get-weather-button', n_clicks=0, style={'margin': '10px'}),

    # Output for converted temperature
    html.Div(id="output-temperature", style={'margin': '20px'})
])


# Callback to fetch weather and convert the temperature
@app.callback(
    Output('output-temperature', 'children'),
    [Input('city-name', 'value'),
     Input('conversion-type', 'value'),
     Input('get-weather-button', 'n_clicks')]
)
def fetch_weather_and_convert(city, conversion_type, n_clicks):
    if n_clicks == 0 or city is None:
        return ''

    # Fetch weather data from the API (OpenWeatherMap)
    api_key = '1c022e92f8630f77939e2c594d132af1'  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
    else:
        return "City not found or API error."

    # Convert the temperature based on selected conversion type
    if conversion_type == 'C_to_F':
        converted_temp = (temperature * 9 / 5) + 32  # Celsius to Fahrenheit
        return f"The current temperature in {city} is {temperature}°C or {converted_temp:.2f}°F"

    elif conversion_type == 'F_to_C':
        converted_temp = (temperature - 32) * 5 / 9  # Fahrenheit to Celsius
        return f"The current temperature in {city} is {temperature}°F or {converted_temp:.2f}°C"


# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
