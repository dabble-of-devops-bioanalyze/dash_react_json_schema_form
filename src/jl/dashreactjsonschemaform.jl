# AUTO GENERATED FILE - DO NOT EDIT

export dashreactjsonschemaform

"""
    dashreactjsonschemaform(;kwargs...)
    dashreactjsonschemaform(children::Any;kwargs...)
    dashreactjsonschemaform(children_maker::Function;kwargs...)


A DashReactJsonSchemaForm component.
DashReactJsonSchemaForm is dash component to render react-json-schema-form forms.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Sets the class name of the element (the value of an element's html
class attribute).
- `extraErrors` (Dict; optional): Extra Errors.
- `formData` (Dict; optional): The formData.
- `label` (String; required): A label that will be printed when this component is rendered.
- `loading_state` (optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `n_submit` (Real; optional): Number of times the `Enter` key was pressed while the input had focus.
- `n_submit_timestamp` (Real; optional): Last time that `Enter` was pressed.
- `prevent_default_on_submit` (Bool; optional): The form calls preventDefault on submit events. If you want form data to
be posted to the endpoint specified by `action` on submit events, set
prevent_default_on_submit to False. Defaults to True.
- `schema` (Dict; optional): The schema in the input.
- `style` (Dict; optional): Add inline styles to the root element.
- `uiSchema` (Dict; optional): The uiSchema in the input.
"""
function dashreactjsonschemaform(; kwargs...)
        available_props = Symbol[:children, :id, :className, :extraErrors, :formData, :label, :loading_state, :n_submit, :n_submit_timestamp, :prevent_default_on_submit, :schema, :style, :uiSchema]
        wild_props = Symbol[]
        return Component("dashreactjsonschemaform", "DashReactJsonSchemaForm", "dash_react_json_schema_form", available_props, wild_props; kwargs...)
end

dashreactjsonschemaform(children::Any; kwargs...) = dashreactjsonschemaform(;kwargs..., children = children)
dashreactjsonschemaform(children_maker::Function; kwargs...) = dashreactjsonschemaform(children_maker(); kwargs...)

