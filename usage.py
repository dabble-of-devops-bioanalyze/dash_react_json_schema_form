import dash_react_json_schema_form
import dash
from dash import Dash, dash_table
from dash.dependencies import Input, Output
from dash import html
import dash_bootstrap_components as dbc
from pprint import pprint
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.DataFrame(
    {
        ("Score", "Max"): {
            "Arthur Dent": 6.0,
            "Ford Prefect": 4.0,
            "Zaphod Beeblebrox": 1.0,
            "Trillian Astra": 3.0,
        },
        ("Score", "Average"): {
            "Arthur Dent": 2.0,
            "Ford Prefect": 2.0,
            "Zaphod Beeblebrox": 0.7,
            "Trillian Astra": 1.9,
        },
    }
)
df.index.set_names("Name", inplace=True)
table = dbc.Table.from_dataframe(
    df, striped=True, bordered=True, hover=True, index=True
)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
data_table = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
                                  id="my-data-table",
                                  row_selectable='single')

form = html.Div(
    [
        dash_react_json_schema_form.DashReactJsonSchemaForm(
            id="form",
            children=[data_table, html.Br()],
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
    app.run_server(debug=True, host="0.0.0.0")
