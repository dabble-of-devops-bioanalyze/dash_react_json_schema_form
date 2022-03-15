# AUTO GENERATED FILE - DO NOT EDIT

export dashreactjsonschemaform

"""
    dashreactjsonschemaform(;kwargs...)

A DashReactJsonSchemaForm component.
DashReactJsonSchemaForm is dash component to render react-json-schema-form forms.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Sets the class name of the element (the value of an element's html
class attribute).
- `extraErrors` (Dict; optional): Extra Errors.
- `formData` (Dict; optional): The formData.
- `label` (String; required): A label that will be printed when this component is rendered.
- `schema` (Dict; optional): The schema in the input.
- `style` (Dict; optional): Add inline styles to the root element.
- `uiSchema` (Dict; optional): The uiSchema in the input.
"""
function dashreactjsonschemaform(; kwargs...)
        available_props = Symbol[:id, :className, :extraErrors, :formData, :label, :schema, :style, :uiSchema]
        wild_props = Symbol[]
        return Component("dashreactjsonschemaform", "DashReactJsonSchemaForm", "dash_react_json_schema_form", available_props, wild_props; kwargs...)
end

