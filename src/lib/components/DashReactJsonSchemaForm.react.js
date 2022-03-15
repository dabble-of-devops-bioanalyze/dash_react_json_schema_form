import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Form from "@rjsf/bootstrap-4";


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
        this.props.setProps({formData : formData});
        event.preventDefault();
    }

    render() {
        const { id, label, setProps, formData, schema, uiSchema, extraErrors } = this.props;
        const log = (type) => console.log.bind(console, type)
        const onSubmit = ({formData}) => console.log("yay I'm valid!");

        return (
            <Form id={id} extraErrors={extraErrors} formData={this.props.formData} uiSchema={uiSchema} schema={schema}
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
                // onChange={log("changed")}
                // onSubmit={onSubmit}
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
                onError={log("errors")} />
        )
        // return (
        //     <div id={id}>
        //         ExampleComponent: {label}&nbsp;
        //         <input
        //             value={value}
        //             onChange={
        //                 /*
        //                  * Send the new value to the parent component.
        //                  * setProps is a prop that is automatically supplied
        //                  * by dash's front-end ("dash-renderer").
        //                  * In a Dash app, this will update the component's
        //                  * props and send the data back to the Python Dash
        //                  * app server if a callback uses the modified prop as
        //                  * Input or State.
        //                  */
        //                 e => setProps({ value: e.target.value })
        //             }
        //         />
        //     </div>
        // );
    }
}

DashReactJsonSchemaForm.defaultProps = {};

DashReactJsonSchemaForm.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

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
    setProps: PropTypes.func
};
