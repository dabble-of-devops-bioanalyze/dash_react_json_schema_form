import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Form from "@rjsf/bootstrap-4";
import RBButton from 'react-bootstrap/Button';
// import Form from "react-jsonschema-form";
// import fields from "react-jsonschema-form-extras";

/**
 * DashReactJsonSchemaForm is dash component to render react-json-schema-form forms.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class DashReactJsonSchemaForm extends Component {
    constructor(props) {
        super(props);
        this.onSubmit = this.onSubmit.bind(this);
    }

    onSubmit({formData}, event) {
        console.log('In on submit')
        console.log(formData);
        console.log(this.props)
        this.props.setProps({formData: formData});
        event.preventDefault();
    }


    render() {
        const {
            id,
            children,
            label,
            setProps,
            formData,
            schema,
            uiSchema,
            extraErrors,
            loading_state,
            n_submit,
            prevent_default_on_submit,
        } = this.props;
        const log = (type) => console.log.bind(console, type)
        console.log('Rendering')
        console.log(children)
        const widgets = {
            ChildrenWidget: function (props) {
                return (
                    <Form.Group>
                        {props.children}
                    </Form.Group>
                );
            }
        };

        return (
            <Form
                id={id}
                extraErrors={extraErrors}
                formData={formData}
                uiSchema={uiSchema}
                schema={schema}
                widgets={widgets}
                onChange={
                    /*
                     * Send the new value to the parent component.
                     * setProps is a prop that is automatically supplied
                     * by dash's front-end ("dash-renderer").
                     * In a Dash app, this will update the component's
                     * props and send the data back to the Python Dash
                     * app server if a callback uses the modified prop as
                     * Input or State.
                     */
                    // e => setProps({ formData: {} })
                    // e => setProps({ formData: e.target.formData })
                    log("changed")
                }
                onSubmit={
                    /*
                     * Send the new value to the parent component.
                     * setProps is a prop that is automatically supplied
                     * by dash's front-end ("dash-renderer").
                     * In a Dash app, this will update the component's
                     * props and send the data back to the Python Dash
                     * app server if a callback uses the modified prop as
                     * Input or State.
                     */
                    this.onSubmit
                }
                onError={log("errors")}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                }
            >
                {children}
                <RBButton type="submit">Submit</RBButton>
            </Form>
        )
    }
}

DashReactJsonSchemaForm.defaultProps = {
    prevent_default_on_submit: true,
    n_submit: 0,
    n_submit_timestamp: -1
};

DashReactJsonSchemaForm.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The children of this component
     */
    children: PropTypes.node,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string.isRequired,

    /**
     * The schema in the input.
     */
    schema: PropTypes.object,

    /**
     * The uiSchema in the input.
     */
    uiSchema: PropTypes.object,

    /**
     * The formData.
     */
    formData: PropTypes.object,

    /**
     * Extra Errors.
     */
    extraErrors: PropTypes.object,

    /**
     * Sets the class name of the element (the value of an element's html
     * class attribute).
     */
    className: PropTypes.string,

    /**
     * Add inline styles to the root element.
     */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /**
     * Number of times the `Enter` key was pressed while the input had focus.
     */
    n_submit: PropTypes.number,

    /**
     * Last time that `Enter` was pressed.
     */
    n_submit_timestamp: PropTypes.number,

    /**
     * The form calls preventDefault on submit events. If you want form data to
     * be posted to the endpoint specified by `action` on submit events, set
     * prevent_default_on_submit to False. Defaults to True.
     */
    prevent_default_on_submit: PropTypes.bool,
    /**
     * Object that holds the loading state object coming from dash-renderer
     */
    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    })
};
