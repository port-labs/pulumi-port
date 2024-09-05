// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package port

import (
	"context"
	"reflect"

	"errors"
	"github.com/port-labs/pulumi-port/sdk/v2/go/port/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource allows you to manage aggregation properties of a blueprint.
//
// See the [Port documentation](https://docs.getport.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/aggregation-property/) for more information about aggregation properties.
//
// Supported Methods:
//
// - countEntities - Count the entities of the target blueprint
// - averageEntities - Average the entities of the target blueprint by time periods
// - averageByProperty - Calculate the average by property value of the target entities
// - aggregateByProperty - Calculate the aggregate by property value of the target entities, such as sum, min, max, median
//
// ## Example Usage
//
// Create a parent blueprint with a child blueprint and an aggregation property to count the parent kids:
//
// ```go
// package main
//
// import (
//
//	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			parentBlueprint, err := port.NewPort_blueprint(ctx, "parentBlueprint", &port.Port_blueprintArgs{
//				Title:       "Parent Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "parent",
//				Description: "",
//				Properties: map[string]interface{}{
//					"numberProps": map[string]interface{}{
//						"age": map[string]interface{}{
//							"title": "Age",
//						},
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			childBlueprint, err := port.NewPort_blueprint(ctx, "childBlueprint", &port.Port_blueprintArgs{
//				Title:       "Child Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "child",
//				Description: "",
//				Properties: map[string]interface{}{
//					"numberProps": map[string]interface{}{
//						"age": map[string]interface{}{
//							"title": "Age",
//						},
//					},
//				},
//				Relations: map[string]interface{}{
//					"parent": map[string]interface{}{
//						"title":  "Parent",
//						"target": parentBlueprint.Identifier,
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = port.NewPort_aggregation_properties(ctx, "parentAggregationProperties", &port.Port_aggregation_propertiesArgs{
//				BlueprintIdentifier: parentBlueprint.Identifier,
//				Properties: map[string]interface{}{
//					"count_kids": map[string]interface{}{
//						"targetBlueprintIdentifier": childBlueprint.Identifier,
//						"title":                     "Count Kids",
//						"icon":                      "Terraform",
//						"description":               "Count Kids",
//						"method": map[string]interface{}{
//							"countEntities": true,
//						},
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// Create a parent blueprint with a child blueprint and an aggregation property to calculate the average avg of the parent kids age:
//
// ```go
// package main
//
// import (
//
//	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			parentBlueprint, err := port.NewPort_blueprint(ctx, "parentBlueprint", &port.Port_blueprintArgs{
//				Title:       "Parent Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "parent",
//				Description: "",
//				Properties: map[string]interface{}{
//					"numberProps": map[string]interface{}{
//						"age": map[string]interface{}{
//							"title": "Age",
//						},
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			childBlueprint, err := port.NewPort_blueprint(ctx, "childBlueprint", &port.Port_blueprintArgs{
//				Title:       "Child Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "child",
//				Description: "",
//				Properties: map[string]interface{}{
//					"numberProps": map[string]interface{}{
//						"age": map[string]interface{}{
//							"title": "Age",
//						},
//					},
//				},
//				Relations: map[string]interface{}{
//					"parent": map[string]interface{}{
//						"title":  "Parent",
//						"target": parentBlueprint.Identifier,
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = port.NewPort_aggregation_properties(ctx, "parentAggregationProperties", &port.Port_aggregation_propertiesArgs{
//				BlueprintIdentifier: parentBlueprint.Identifier,
//				Properties: map[string]interface{}{
//					"averageKidsAge": map[string]interface{}{
//						"targetBlueprintIdentifier": childBlueprint.Identifier,
//						"title":                     "Average Kids Age",
//						"icon":                      "Terraform",
//						"description":               "Average Kids Age",
//						"method": map[string]interface{}{
//							"averageByProperty": map[string]interface{}{
//								"averageOf":     "total",
//								"measureTimeBy": "$createdAt",
//								"property":      "age",
//							},
//						},
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// Create a repository blueprint and a pull request blueprint and an aggregation property to calculate the average of pull requests created per day:
//
// ```go
// package main
//
// import (
//
//	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			repositoryBlueprint, err := port.NewPort_blueprint(ctx, "repositoryBlueprint", &port.Port_blueprintArgs{
//				Title:       "Repository Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "repository",
//				Description: "",
//			})
//			if err != nil {
//				return err
//			}
//			pullRequestBlueprint, err := port.NewPort_blueprint(ctx, "pullRequestBlueprint", &port.Port_blueprintArgs{
//				Title:       "Pull Request Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "pull_request",
//				Description: "",
//				Properties: map[string]interface{}{
//					"stringProps": map[string]interface{}{
//						"status": map[string]interface{}{
//							"title": "Status",
//						},
//					},
//				},
//				Relations: map[string]interface{}{
//					"repository": map[string]interface{}{
//						"title":  "Repository",
//						"target": repositoryBlueprint.Identifier,
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = port.NewPort_aggregation_properties(ctx, "repositoryAggregationProperties", &port.Port_aggregation_propertiesArgs{
//				BlueprintIdentifier: repositoryBlueprint.Identifier,
//				Properties: map[string]interface{}{
//					"pull_requests_per_day": map[string]interface{}{
//						"targetBlueprintIdentifier": pullRequestBlueprint.Identifier,
//						"title":                     "Pull Requests Per Day",
//						"icon":                      "Terraform",
//						"description":               "Pull Requests Per Day",
//						"method": map[string]interface{}{
//							"averageEntities": map[string]interface{}{
//								"averageOf":     "day",
//								"measureTimeBy": "$createdAt",
//							},
//						},
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// Create a repository blueprint and a pull request blueprint and an aggregation property to calculate the average of fix pull request per month:
//
// To do that we will add a query to the aggregation property to filter only pull requests with fixed title:
//
// ```go
// package main
//
// import (
//
//	"encoding/json"
//
//	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
// func main() {
// pulumi.Run(func(ctx *pulumi.Context) error {
// repositoryBlueprint, err := port.NewPort_blueprint(ctx, "repositoryBlueprint", &port.Port_blueprintArgs{
// Title: "Repository Blueprint",
// Icon: "Terraform",
// Identifier: "repository",
// Description: "",
// })
// if err != nil {
// return err
// }
// pullRequestBlueprint, err := port.NewPort_blueprint(ctx, "pullRequestBlueprint", &port.Port_blueprintArgs{
// Title: "Pull Request Blueprint",
// Icon: "Terraform",
// Identifier: "pull_request",
// Description: "",
// Properties: map[string]interface{}{
// "stringProps": map[string]interface{}{
// "status": map[string]interface{}{
// "title": "Status",
// },
// },
// },
// Relations: map[string]interface{}{
// "repository": map[string]interface{}{
// "title": "Repository",
// "target": repositoryBlueprint.Identifier,
// },
// },
// })
// if err != nil {
// return err
// }
// _, err = port.NewPort_aggregation_properties(ctx, "repositoryAggregationProperties", &port.Port_aggregation_propertiesArgs{
// BlueprintIdentifier: repositoryBlueprint.Identifier,
// Properties: map[string]interface{}{
// "fix_pull_requests_count": map[string]interface{}{
// "targetBlueprintIdentifier": pullRequestBlueprint.Identifier,
// "title": "Pull Requests Per Day",
// "icon": "Terraform",
// "description": "Pull Requests Per Day",
// "method": map[string]interface{}{
// "averageEntities": map[string]interface{}{
// "averageOf": "month",
// "measureTimeBy": "$createdAt",
// },
// },
// "query": %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// })
// if err != nil {
// return err
// }
// return nil
// })
// }
// ```
//
// Create multiple aggregation properties in one resource:
//
// ```go
// package main
//
// import (
//
//	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			repositoryBlueprint, err := port.NewPort_blueprint(ctx, "repositoryBlueprint", &port.Port_blueprintArgs{
//				Title:       "Repository Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "repository",
//				Description: "",
//			})
//			if err != nil {
//				return err
//			}
//			pullRequestBlueprint, err := port.NewPort_blueprint(ctx, "pullRequestBlueprint", &port.Port_blueprintArgs{
//				Title:       "Pull Request Blueprint",
//				Icon:        "Terraform",
//				Identifier:  "pull_request",
//				Description: "",
//				Properties: map[string]interface{}{
//					"stringProps": map[string]interface{}{
//						"status": map[string]interface{}{
//							"title": "Status",
//						},
//					},
//				},
//				Relations: map[string]interface{}{
//					"repository": map[string]interface{}{
//						"title":  "Repository",
//						"target": repositoryBlueprint.Identifier,
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = port.NewPort_aggregation_properties(ctx, "repositoryAggregationProperties", &port.Port_aggregation_propertiesArgs{
//				BlueprintIdentifier: repositoryBlueprint.Identifier,
//				Properties: map[string]interface{}{
//					"pull_requests_per_day": map[string]interface{}{
//						"targetBlueprintIdentifier": pullRequestBlueprint.Identifier,
//						"title":                     "Pull Requests Per Day",
//						"icon":                      "Terraform",
//						"description":               "Pull Requests Per Day",
//						"method": map[string]interface{}{
//							"averageEntities": map[string]interface{}{
//								"averageOf":     "day",
//								"measureTimeBy": "$createdAt",
//							},
//						},
//					},
//					"overall_pull_requests_count": map[string]interface{}{
//						"targetBlueprintIdentifier": pullRequestBlueprint.Identifier,
//						"title":                     "Overall Pull Requests Count",
//						"icon":                      "Terraform",
//						"description":               "Overall Pull Requests Count",
//						"method": map[string]interface{}{
//							"countEntities": true,
//						},
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type AggregationProperties struct {
	pulumi.CustomResourceState

	// The identifier of the blueprint the aggregation property will be added to
	BlueprintIdentifier pulumi.StringOutput `pulumi:"blueprintIdentifier"`
	// The aggregation property of the blueprint
	Properties AggregationPropertiesPropertiesMapOutput `pulumi:"properties"`
}

// NewAggregationProperties registers a new resource with the given unique name, arguments, and options.
func NewAggregationProperties(ctx *pulumi.Context,
	name string, args *AggregationPropertiesArgs, opts ...pulumi.ResourceOption) (*AggregationProperties, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BlueprintIdentifier == nil {
		return nil, errors.New("invalid value for required argument 'BlueprintIdentifier'")
	}
	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AggregationProperties
	err := ctx.RegisterResource("port:index/aggregationProperties:AggregationProperties", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAggregationProperties gets an existing AggregationProperties resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAggregationProperties(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AggregationPropertiesState, opts ...pulumi.ResourceOption) (*AggregationProperties, error) {
	var resource AggregationProperties
	err := ctx.ReadResource("port:index/aggregationProperties:AggregationProperties", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AggregationProperties resources.
type aggregationPropertiesState struct {
	// The identifier of the blueprint the aggregation property will be added to
	BlueprintIdentifier *string `pulumi:"blueprintIdentifier"`
	// The aggregation property of the blueprint
	Properties map[string]AggregationPropertiesProperties `pulumi:"properties"`
}

type AggregationPropertiesState struct {
	// The identifier of the blueprint the aggregation property will be added to
	BlueprintIdentifier pulumi.StringPtrInput
	// The aggregation property of the blueprint
	Properties AggregationPropertiesPropertiesMapInput
}

func (AggregationPropertiesState) ElementType() reflect.Type {
	return reflect.TypeOf((*aggregationPropertiesState)(nil)).Elem()
}

type aggregationPropertiesArgs struct {
	// The identifier of the blueprint the aggregation property will be added to
	BlueprintIdentifier string `pulumi:"blueprintIdentifier"`
	// The aggregation property of the blueprint
	Properties map[string]AggregationPropertiesProperties `pulumi:"properties"`
}

// The set of arguments for constructing a AggregationProperties resource.
type AggregationPropertiesArgs struct {
	// The identifier of the blueprint the aggregation property will be added to
	BlueprintIdentifier pulumi.StringInput
	// The aggregation property of the blueprint
	Properties AggregationPropertiesPropertiesMapInput
}

func (AggregationPropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*aggregationPropertiesArgs)(nil)).Elem()
}

type AggregationPropertiesInput interface {
	pulumi.Input

	ToAggregationPropertiesOutput() AggregationPropertiesOutput
	ToAggregationPropertiesOutputWithContext(ctx context.Context) AggregationPropertiesOutput
}

func (*AggregationProperties) ElementType() reflect.Type {
	return reflect.TypeOf((**AggregationProperties)(nil)).Elem()
}

func (i *AggregationProperties) ToAggregationPropertiesOutput() AggregationPropertiesOutput {
	return i.ToAggregationPropertiesOutputWithContext(context.Background())
}

func (i *AggregationProperties) ToAggregationPropertiesOutputWithContext(ctx context.Context) AggregationPropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AggregationPropertiesOutput)
}

// AggregationPropertiesArrayInput is an input type that accepts AggregationPropertiesArray and AggregationPropertiesArrayOutput values.
// You can construct a concrete instance of `AggregationPropertiesArrayInput` via:
//
//	AggregationPropertiesArray{ AggregationPropertiesArgs{...} }
type AggregationPropertiesArrayInput interface {
	pulumi.Input

	ToAggregationPropertiesArrayOutput() AggregationPropertiesArrayOutput
	ToAggregationPropertiesArrayOutputWithContext(context.Context) AggregationPropertiesArrayOutput
}

type AggregationPropertiesArray []AggregationPropertiesInput

func (AggregationPropertiesArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AggregationProperties)(nil)).Elem()
}

func (i AggregationPropertiesArray) ToAggregationPropertiesArrayOutput() AggregationPropertiesArrayOutput {
	return i.ToAggregationPropertiesArrayOutputWithContext(context.Background())
}

func (i AggregationPropertiesArray) ToAggregationPropertiesArrayOutputWithContext(ctx context.Context) AggregationPropertiesArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AggregationPropertiesArrayOutput)
}

// AggregationPropertiesMapInput is an input type that accepts AggregationPropertiesMap and AggregationPropertiesMapOutput values.
// You can construct a concrete instance of `AggregationPropertiesMapInput` via:
//
//	AggregationPropertiesMap{ "key": AggregationPropertiesArgs{...} }
type AggregationPropertiesMapInput interface {
	pulumi.Input

	ToAggregationPropertiesMapOutput() AggregationPropertiesMapOutput
	ToAggregationPropertiesMapOutputWithContext(context.Context) AggregationPropertiesMapOutput
}

type AggregationPropertiesMap map[string]AggregationPropertiesInput

func (AggregationPropertiesMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AggregationProperties)(nil)).Elem()
}

func (i AggregationPropertiesMap) ToAggregationPropertiesMapOutput() AggregationPropertiesMapOutput {
	return i.ToAggregationPropertiesMapOutputWithContext(context.Background())
}

func (i AggregationPropertiesMap) ToAggregationPropertiesMapOutputWithContext(ctx context.Context) AggregationPropertiesMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AggregationPropertiesMapOutput)
}

type AggregationPropertiesOutput struct{ *pulumi.OutputState }

func (AggregationPropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AggregationProperties)(nil)).Elem()
}

func (o AggregationPropertiesOutput) ToAggregationPropertiesOutput() AggregationPropertiesOutput {
	return o
}

func (o AggregationPropertiesOutput) ToAggregationPropertiesOutputWithContext(ctx context.Context) AggregationPropertiesOutput {
	return o
}

// The identifier of the blueprint the aggregation property will be added to
func (o AggregationPropertiesOutput) BlueprintIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *AggregationProperties) pulumi.StringOutput { return v.BlueprintIdentifier }).(pulumi.StringOutput)
}

// The aggregation property of the blueprint
func (o AggregationPropertiesOutput) Properties() AggregationPropertiesPropertiesMapOutput {
	return o.ApplyT(func(v *AggregationProperties) AggregationPropertiesPropertiesMapOutput { return v.Properties }).(AggregationPropertiesPropertiesMapOutput)
}

type AggregationPropertiesArrayOutput struct{ *pulumi.OutputState }

func (AggregationPropertiesArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AggregationProperties)(nil)).Elem()
}

func (o AggregationPropertiesArrayOutput) ToAggregationPropertiesArrayOutput() AggregationPropertiesArrayOutput {
	return o
}

func (o AggregationPropertiesArrayOutput) ToAggregationPropertiesArrayOutputWithContext(ctx context.Context) AggregationPropertiesArrayOutput {
	return o
}

func (o AggregationPropertiesArrayOutput) Index(i pulumi.IntInput) AggregationPropertiesOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AggregationProperties {
		return vs[0].([]*AggregationProperties)[vs[1].(int)]
	}).(AggregationPropertiesOutput)
}

type AggregationPropertiesMapOutput struct{ *pulumi.OutputState }

func (AggregationPropertiesMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AggregationProperties)(nil)).Elem()
}

func (o AggregationPropertiesMapOutput) ToAggregationPropertiesMapOutput() AggregationPropertiesMapOutput {
	return o
}

func (o AggregationPropertiesMapOutput) ToAggregationPropertiesMapOutputWithContext(ctx context.Context) AggregationPropertiesMapOutput {
	return o
}

func (o AggregationPropertiesMapOutput) MapIndex(k pulumi.StringInput) AggregationPropertiesOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AggregationProperties {
		return vs[0].(map[string]*AggregationProperties)[vs[1].(string)]
	}).(AggregationPropertiesOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AggregationPropertiesInput)(nil)).Elem(), &AggregationProperties{})
	pulumi.RegisterInputType(reflect.TypeOf((*AggregationPropertiesArrayInput)(nil)).Elem(), AggregationPropertiesArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AggregationPropertiesMapInput)(nil)).Elem(), AggregationPropertiesMap{})
	pulumi.RegisterOutputType(AggregationPropertiesOutput{})
	pulumi.RegisterOutputType(AggregationPropertiesArrayOutput{})
	pulumi.RegisterOutputType(AggregationPropertiesMapOutput{})
}
