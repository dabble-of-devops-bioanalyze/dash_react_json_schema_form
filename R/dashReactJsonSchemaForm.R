# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashReactJsonSchemaForm <- function(children=NULL, id=NULL, className=NULL, extraErrors=NULL, formData=NULL, label=NULL, loading_state=NULL, n_submit=NULL, n_submit_timestamp=NULL, prevent_default_on_submit=NULL, schema=NULL, style=NULL, uiSchema=NULL) {
    
    props <- list(children=children, id=id, className=className, extraErrors=extraErrors, formData=formData, label=label, loading_state=loading_state, n_submit=n_submit, n_submit_timestamp=n_submit_timestamp, prevent_default_on_submit=prevent_default_on_submit, schema=schema, style=style, uiSchema=uiSchema)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashReactJsonSchemaForm',
        namespace = 'dash_react_json_schema_form',
        propNames = c('children', 'id', 'className', 'extraErrors', 'formData', 'label', 'loading_state', 'n_submit', 'n_submit_timestamp', 'prevent_default_on_submit', 'schema', 'style', 'uiSchema'),
        package = 'dashReactJsonSchemaForm'
        )

    structure(component, class = c('dash_component', 'list'))
}
