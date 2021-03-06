
module DashReactJsonSchemaForm
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.1.12"

include("jl/dashreactjsonschemaform.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_react_json_schema_form",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_react_json_schema_form.min.js",
    external_url = "https://unpkg.com/dash_react_json_schema_form@0.1.12/dash_react_json_schema_form/dash_react_json_schema_form.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_react_json_schema_form.min.js.map",
    external_url = "https://unpkg.com/dash_react_json_schema_form@0.1.12/dash_react_json_schema_form/dash_react_json_schema_form.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
