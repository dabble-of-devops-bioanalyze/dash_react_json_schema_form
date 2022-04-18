# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashReactJsonSchemaForm(Component):
    """A DashReactJsonSchemaForm component.
DashReactJsonSchemaForm is dash component to render react-json-schema-form forms.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Sets the class name of the element (the value of an element's html
    class attribute).

- extraErrors (dict; optional):
    Extra Errors.

- formData (dict; optional):
    The formData.

- label (string; required):
    A label that will be printed when this component is rendered.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- n_submit (number; default 0):
    Number of times the `Enter` key was pressed while the input had
    focus.

- n_submit_timestamp (number; default -1):
    Last time that `Enter` was pressed.

- prevent_default_on_submit (boolean; default True):
    The form calls preventDefault on submit events. If you want form
    data to be posted to the endpoint specified by `action` on submit
    events, set prevent_default_on_submit to False. Defaults to True.

- schema (dict; optional):
    The schema in the input.

- style (dict; optional):
    Add inline styles to the root element.

- uiSchema (dict; optional):
    The uiSchema in the input."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, label=Component.REQUIRED, schema=Component.UNDEFINED, uiSchema=Component.UNDEFINED, formData=Component.UNDEFINED, extraErrors=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, n_submit=Component.UNDEFINED, n_submit_timestamp=Component.UNDEFINED, prevent_default_on_submit=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'extraErrors', 'formData', 'label', 'loading_state', 'n_submit', 'n_submit_timestamp', 'prevent_default_on_submit', 'schema', 'style', 'uiSchema']
        self._type = 'DashReactJsonSchemaForm'
        self._namespace = 'dash_react_json_schema_form'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'extraErrors', 'formData', 'label', 'loading_state', 'n_submit', 'n_submit_timestamp', 'prevent_default_on_submit', 'schema', 'style', 'uiSchema']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashReactJsonSchemaForm, self).__init__(children=children, **args)
