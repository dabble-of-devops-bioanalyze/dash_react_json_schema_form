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

- schema (dict; optional):
    The schema in the input.

- style (dict; optional):
    Add inline styles to the root element.

- uiSchema (dict; optional):
    The uiSchema in the input."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, schema=Component.UNDEFINED, uiSchema=Component.UNDEFINED, formData=Component.UNDEFINED, extraErrors=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'extraErrors', 'formData', 'label', 'schema', 'style', 'uiSchema']
        self._type = 'DashReactJsonSchemaForm'
        self._namespace = 'dash_react_json_schema_form'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'extraErrors', 'formData', 'label', 'schema', 'style', 'uiSchema']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashReactJsonSchemaForm, self).__init__(**args)
