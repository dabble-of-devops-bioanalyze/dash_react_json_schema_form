import dash_react_json_schema_form
import dash
from dash.dependencies import Input, Output
from dash import html
import dash_bootstrap_components as dbc
from pprint import pprint

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

form = html.Div(
    [
        dash_react_json_schema_form.DashReactJsonSchemaForm(
            id="form",
            schema={
                "title": "Todo",
                "type": "object",
                "required": ["title"],
                "properties": {
                    "title": {
                        "type": "string",
                        "title": "Field Title",
                        "default": "A new task",
                    },
                    "firstName": {"type": "string"},
                    "done": {"type": "boolean", "title": "Done?", "default": False},
                },
            },
            uiSchema={
            },
            formData={},
            extraErrors={
                # "title": {
                #     "__errors": ["some error that got added as a prop"],
                # },
            },
            label="my-label",
        ),
        html.Div(id="output"),
    ]
)

app.layout = dbc.Container(
    [
        dbc.Alert("Hello Bootstrap!", color="success"),
        form,
    ],
    fluid=True,
)


@app.callback(Output("output", "children"), [Input("form", "formData")])
def display_output(value):
    print('Getting form data')
    pprint(value)
    return "You have entered {}".format(value)


if __name__ == "__main__":
    app.run_server(debug=True)
