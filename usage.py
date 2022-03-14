import dash_react_json_schema_form
import dash
from dash.dependencies import Input, Output
from dash import html
import dash_bootstrap_components as dbc

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
                        "title": "Title",
                        "default": "A new task",
                    },
                    "done": {"type": "boolean", "title": "Done?", "default": False},
                },
            },
            uiSchema={},
            formData={},
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
    return "You have entered {}".format(value)


if __name__ == "__main__":
    app.run_server(debug=True)
