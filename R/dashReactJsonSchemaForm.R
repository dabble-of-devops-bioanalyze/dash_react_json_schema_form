# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashReactJsonSchemaForm <- function(id=NULL, className=NULL, extraErrors=NULL, formData=NULL, label=NULL, schema=NULL, style=NULL, uiSchema=NULL) {
    
    props <- list(id=id, className=className, extraErrors=extraErrors, formData=formData, label=label, schema=schema, style=style, uiSchema=uiSchema)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashReactJsonSchemaForm',
        namespace = 'dash_react_json_schema_form',
        propNames = c('id', 'className', 'extraErrors', 'formData', 'label', 'schema', 'style', 'uiSchema'),
        package = 'dashReactJsonSchemaForm'
        )

    structure(component, class = c('dash_component', 'list'))
}
