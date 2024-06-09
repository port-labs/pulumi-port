// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The search data source allows you to search for entities in Port.
 *
 * See the [Port documentation](https://docs.getport.io/search-and-query/) for more information about the search capabilities in Port.
 *
 * ## Example Usage
 */
export function getSearch(args: GetSearchArgs, opts?: pulumi.InvokeOptions): Promise<GetSearchResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("port:index/getSearch:getSearch", {
        "attachTitleToRelation": args.attachTitleToRelation,
        "excludeCalculatedProperties": args.excludeCalculatedProperties,
        "excludes": args.excludes,
        "includes": args.includes,
        "query": args.query,
    }, opts);
}

/**
 * A collection of arguments for invoking getSearch.
 */
export interface GetSearchArgs {
    /**
     * Attach title to relation
     */
    attachTitleToRelation?: boolean;
    /**
     * Exclude calculated properties
     */
    excludeCalculatedProperties?: boolean;
    /**
     * Properties to exclude from the results
     */
    excludes?: string[];
    /**
     * Properties to include in the results
     */
    includes?: string[];
    /**
     * The search query
     */
    query: string;
}

/**
 * A collection of values returned by getSearch.
 */
export interface GetSearchResult {
    /**
     * Attach title to relation
     */
    readonly attachTitleToRelation?: boolean;
    /**
     * A list of entities matching the search query
     */
    readonly entities: outputs.GetSearchEntity[];
    /**
     * Exclude calculated properties
     */
    readonly excludeCalculatedProperties?: boolean;
    /**
     * Properties to exclude from the results
     */
    readonly excludes?: string[];
    /**
     * The ID of this resource.
     */
    readonly id: string;
    /**
     * Properties to include in the results
     */
    readonly includes?: string[];
    /**
     * The matching blueprints for the search query
     */
    readonly matchingBlueprints: string[];
    /**
     * The search query
     */
    readonly query: string;
}
/**
 * The search data source allows you to search for entities in Port.
 *
 * See the [Port documentation](https://docs.getport.io/search-and-query/) for more information about the search capabilities in Port.
 *
 * ## Example Usage
 */
export function getSearchOutput(args: GetSearchOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSearchResult> {
    return pulumi.output(args).apply((a: any) => getSearch(a, opts))
}

/**
 * A collection of arguments for invoking getSearch.
 */
export interface GetSearchOutputArgs {
    /**
     * Attach title to relation
     */
    attachTitleToRelation?: pulumi.Input<boolean>;
    /**
     * Exclude calculated properties
     */
    excludeCalculatedProperties?: pulumi.Input<boolean>;
    /**
     * Properties to exclude from the results
     */
    excludes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Properties to include in the results
     */
    includes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The search query
     */
    query: pulumi.Input<string>;
}
