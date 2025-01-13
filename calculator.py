import dash
from dash import dcc, html
from dash.dependencies import Input, Output


# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("*** Simple Calculator ***", style={'color': '#FF5733'}),
    dcc.Input(id='input1', type='number',placeholder="Enter the First Number"),
    dcc.Dropdown(
        id='operation-dropdown',
        options=[
            {'label': 'Add', 'value': '+'},
            {'label': 'Subtract', 'value': '-'},
            {'label': 'Multiply', 'value': '*'},
            {'label': 'Divide', 'value': '/'}
        ],
        value='+'
    ),
    dcc.Input(id='input2', type='number',placeholder="Enter the Second Number"),
    html.Button('Calculate', id='calculate-button'),
    html.Div(id='result')
])

@app.callback(
    Output('result', 'children'),
    [Input('input1', 'value'),
     Input('input2', 'value'),
     Input('operation-dropdown', 'value'),
     Input('calculate-button', 'n_clicks')]
)
def update_output(input1, input2, operation,n_clicks):
    if n_clicks is None:  # If the button hasn't been clicked
        return "Please press the button to calculate."

    try:
        if input1 is None or input2 is None:
            return "Please enter both numbers."

        input1, input2 = float(input1), float(input2)
        if operation == '+':
            return f"Result: {input1 + input2}"
        elif operation == '-':
            return f"Result: {input1 - input2}"
        elif operation == '*':
            return f"Result: {input1 * input2}"
        elif operation == '/':
            if input2==0:
                return "Error:Division by Zero"
            return f"Result: {input1 / input2}"
    except ValueError:
        return "Please enter valid numbers."

if __name__ == "__main__":
    app.run_server(debug=True)