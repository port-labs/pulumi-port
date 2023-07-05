// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface ActionInvocationMethod {
    agent?: pulumi.Input<boolean>;
    azureOrg?: pulumi.Input<string>;
    omitPayload?: pulumi.Input<boolean>;
    omitUserInputs?: pulumi.Input<boolean>;
    org?: pulumi.Input<string>;
    repo?: pulumi.Input<string>;
    reportWorkflowStatus?: pulumi.Input<boolean>;
    type: pulumi.Input<string>;
    url?: pulumi.Input<string>;
    webhook?: pulumi.Input<string>;
    workflow?: pulumi.Input<string>;
}

export interface ActionUserProperty {
    blueprint?: pulumi.Input<string>;
    default?: pulumi.Input<string>;
    defaultItems?: pulumi.Input<pulumi.Input<string>[]>;
    description?: pulumi.Input<string>;
    enums?: pulumi.Input<pulumi.Input<string>[]>;
    format?: pulumi.Input<string>;
    identifier: pulumi.Input<string>;
    pattern?: pulumi.Input<string>;
    required?: pulumi.Input<boolean>;
    title: pulumi.Input<string>;
    type: pulumi.Input<string>;
}

export interface BlueprintCalculationProperty {
    calculation: pulumi.Input<string>;
    colorized?: pulumi.Input<boolean>;
    colors?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    description?: pulumi.Input<string>;
    format?: pulumi.Input<string>;
    icon?: pulumi.Input<string>;
    identifier: pulumi.Input<string>;
    title?: pulumi.Input<string>;
    type: pulumi.Input<string>;
}

export interface BlueprintChangelogDestination {
    agent?: pulumi.Input<boolean>;
    type: pulumi.Input<string>;
    url?: pulumi.Input<string>;
}

export interface BlueprintMirrorProperty {
    identifier: pulumi.Input<string>;
    path: pulumi.Input<string>;
    title?: pulumi.Input<string>;
}

export interface BlueprintProperty {
    /**
     * @deprecated Use default_value instead
     */
    default?: pulumi.Input<string>;
    defaultItems?: pulumi.Input<pulumi.Input<string>[]>;
    defaultValue?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    description?: pulumi.Input<string>;
    enumColors?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    enums?: pulumi.Input<pulumi.Input<string>[]>;
    format?: pulumi.Input<string>;
    icon?: pulumi.Input<string>;
    identifier: pulumi.Input<string>;
    items?: pulumi.Input<{[key: string]: any}>;
    maxItems?: pulumi.Input<number>;
    maxLength?: pulumi.Input<number>;
    minItems?: pulumi.Input<number>;
    minLength?: pulumi.Input<number>;
    required?: pulumi.Input<boolean>;
    spec?: pulumi.Input<string>;
    specAuthentication?: pulumi.Input<inputs.BlueprintPropertySpecAuthentication>;
    title: pulumi.Input<string>;
    type: pulumi.Input<string>;
}

export interface BlueprintPropertySpecAuthentication {
    authorizationUrl: pulumi.Input<string>;
    clientId: pulumi.Input<string>;
    tokenUrl: pulumi.Input<string>;
}

export interface BlueprintRelation {
    identifier: pulumi.Input<string>;
    many?: pulumi.Input<boolean>;
    required?: pulumi.Input<boolean>;
    target: pulumi.Input<string>;
    title?: pulumi.Input<string>;
}

export interface EntityProperty {
    items?: pulumi.Input<pulumi.Input<string>[]>;
    name: pulumi.Input<string>;
    /**
     * @deprecated property type is not required anymore
     */
    type?: pulumi.Input<string>;
    value?: pulumi.Input<string>;
}

export interface EntityRelation {
    identifier?: pulumi.Input<string>;
    identifiers?: pulumi.Input<pulumi.Input<string>[]>;
    name: pulumi.Input<string>;
}
