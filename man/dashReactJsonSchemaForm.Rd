% Auto-generated: do not edit by hand
\name{dashReactJsonSchemaForm}

\alias{dashReactJsonSchemaForm}

\title{DashReactJsonSchemaForm component}

\description{
DashReactJsonSchemaForm is dash component to render react-json-schema-form forms. It takes a property, `label`, and displays it. It renders an input with the property `value` which is editable by the user.
}

\usage{
dashReactJsonSchemaForm(children=NULL, id=NULL, className=NULL, extraErrors=NULL,
formData=NULL, label=NULL, loading_state=NULL,
n_submit=NULL, n_submit_timestamp=NULL,
prevent_default_on_submit=NULL, schema=NULL, style=NULL,
uiSchema=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The children of this component}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. Sets the class name of the element (the value of an element's html
class attribute).}

\item{extraErrors}{Named list. Extra Errors.}

\item{formData}{Named list. The formData.}

\item{label}{Character. A label that will be printed when this component is rendered.}

\item{loading_state}{Lists containing elements 'is_loading', 'prop_name', 'component_name'.
those elements have the following types:
  - is_loading (logical; optional): determines if the component is loading or not
  - prop_name (character; optional): holds which property is loading
  - component_name (character; optional): holds the name of the component that is loading. Object that holds the loading state object coming from dash-renderer}

\item{n_submit}{Numeric. Number of times the `Enter` key was pressed while the input had focus.}

\item{n_submit_timestamp}{Numeric. Last time that `Enter` was pressed.}

\item{prevent_default_on_submit}{Logical. The form calls preventDefault on submit events. If you want form data to
be posted to the endpoint specified by `action` on submit events, set
prevent_default_on_submit to False. Defaults to True.}

\item{schema}{Named list. The schema in the input.}

\item{style}{Named list. Add inline styles to the root element.}

\item{uiSchema}{Named list. The uiSchema in the input.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

