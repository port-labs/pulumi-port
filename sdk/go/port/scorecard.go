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

// This resource allows you to manage a scorecard.
//
// See the [Port documentation](https://docs.getport.io/promote-scorecards/) for more information about scorecards.
//
// ## Example Usage
//
// This will create a blueprint with a Scorecard measuring the readiness of a microservice.
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
// microservice, err := port.NewPort_blueprint(ctx, "microservice", &port.Port_blueprintArgs{
// Title: "microservice",
// Icon: "Terraform",
// Identifier: "microservice",
// Properties: map[string]interface{}{
// "stringProps": map[string]interface{}{
// "author": map[string]interface{}{
// "title": "Author",
// },
// "url": map[string]interface{}{
// "title": "URL",
// },
// },
// "booleanProps": map[string]interface{}{
// "required": map[string]interface{}{
// "type": "boolean",
// },
// },
// "numberProps": map[string]interface{}{
// "sum": map[string]interface{}{
// "type": "number",
// },
// },
// },
// })
// if err != nil {
// return err
// }
// _, err = port.NewPort_scorecard(ctx, "readiness", &port.Port_scorecardArgs{
// Identifier: "Readiness",
// Title: "Readiness",
// Blueprint: microservice.Identifier,
// Rules: []interface{}{
// map[string]interface{}{
// "identifier": "hasOwner",
// "title": "Has Owner",
// "level": "Gold",
// "query": map[string]interface{}{
// "combinator": "and",
// "conditions": []string{
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// },
// map[string]interface{}{
// "identifier": "hasUrl",
// "title": "Has URL",
// "level": "Silver",
// "query": map[string]interface{}{
// "combinator": "and",
// "conditions": []string{
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// },
// map[string]interface{}{
// "identifier": "checkSumIfRequired",
// "title": "Check Sum If Required",
// "level": "Bronze",
// "query": map[string]interface{}{
// "combinator": "or",
// "conditions": []string{
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// },
// },
// }, pulumi.DependsOn([]pulumi.Resource{
// microservice,
// }))
// if err != nil {
// return err
// }
// return nil
// })
// }
// ```
//
// ### With Levels And Filter
//
// This will override the default levels (Basic, Bronze, Silver, Gold) with the provided levels: Not Ready, Partially Ready, Ready.
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
// microservice, err := port.NewPort_blueprint(ctx, "microservice", &port.Port_blueprintArgs{
// Title: "microservice",
// Icon: "Terraform",
// Identifier: "microservice",
// Properties: map[string]interface{}{
// "stringProps": map[string]interface{}{
// "author": map[string]interface{}{
// "title": "Author",
// },
// "url": map[string]interface{}{
// "title": "URL",
// },
// },
// "booleanProps": map[string]interface{}{
// "required": map[string]interface{}{
// "type": "boolean",
// },
// },
// "numberProps": map[string]interface{}{
// "sum": map[string]interface{}{
// "type": "number",
// },
// },
// },
// })
// if err != nil {
// return err
// }
// _, err = port.NewPort_scorecard(ctx, "readiness", &port.Port_scorecardArgs{
// Identifier: "Readiness",
// Title: "Readiness",
// Blueprint: microservice.Identifier,
// Filter: map[string]interface{}{
// "combinator": "and",
// "conditions": []string{
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// Levels: []map[string]interface{}{
// map[string]interface{}{
// "color": "red",
// "title": "No Ready",
// },
// map[string]interface{}{
// "color": "yellow",
// "title": "Partially Ready",
// },
// map[string]interface{}{
// "color": "green",
// "title": "Ready",
// },
// },
// Rules: []interface{}{
// map[string]interface{}{
// "identifier": "hasOwner",
// "title": "Has Owner",
// "level": "Ready",
// "query": map[string]interface{}{
// "combinator": "and",
// "conditions": []string{
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// },
// map[string]interface{}{
// "identifier": "hasUrl",
// "title": "Has URL",
// "level": "Partially Ready",
// "query": map[string]interface{}{
// "combinator": "and",
// "conditions": []string{
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// },
// map[string]interface{}{
// "identifier": "checkSumIfRequired",
// "title": "Check Sum If Required",
// "level": "Partially Ready",
// "query": map[string]interface{}{
// "combinator": "or",
// "conditions": []string{
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// },
// },
// },
// },
// }, pulumi.DependsOn([]pulumi.Resource{
// microservice,
// }))
// if err != nil {
// return err
// }
// return nil
// })
// }
// ```
type Scorecard struct {
	pulumi.CustomResourceState

	// The blueprint of the scorecard
	Blueprint pulumi.StringOutput `pulumi:"blueprint"`
	// The creation date of the scorecard
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The creator of the scorecard
	CreatedBy pulumi.StringOutput `pulumi:"createdBy"`
	// The filter to apply on the entities before calculating the scorecard
	Filter ScorecardFilterPtrOutput `pulumi:"filter"`
	// The identifier of the scorecard
	Identifier pulumi.StringOutput `pulumi:"identifier"`
	// The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
	Levels ScorecardLevelArrayOutput `pulumi:"levels"`
	// The rules of the scorecard
	Rules ScorecardRuleArrayOutput `pulumi:"rules"`
	// The title of the scorecard
	Title pulumi.StringOutput `pulumi:"title"`
	// The last update date of the scorecard
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
	// The last updater of the scorecard
	UpdatedBy pulumi.StringOutput `pulumi:"updatedBy"`
}

// NewScorecard registers a new resource with the given unique name, arguments, and options.
func NewScorecard(ctx *pulumi.Context,
	name string, args *ScorecardArgs, opts ...pulumi.ResourceOption) (*Scorecard, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Blueprint == nil {
		return nil, errors.New("invalid value for required argument 'Blueprint'")
	}
	if args.Identifier == nil {
		return nil, errors.New("invalid value for required argument 'Identifier'")
	}
	if args.Rules == nil {
		return nil, errors.New("invalid value for required argument 'Rules'")
	}
	if args.Title == nil {
		return nil, errors.New("invalid value for required argument 'Title'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Scorecard
	err := ctx.RegisterResource("port:index/scorecard:Scorecard", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetScorecard gets an existing Scorecard resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetScorecard(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ScorecardState, opts ...pulumi.ResourceOption) (*Scorecard, error) {
	var resource Scorecard
	err := ctx.ReadResource("port:index/scorecard:Scorecard", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Scorecard resources.
type scorecardState struct {
	// The blueprint of the scorecard
	Blueprint *string `pulumi:"blueprint"`
	// The creation date of the scorecard
	CreatedAt *string `pulumi:"createdAt"`
	// The creator of the scorecard
	CreatedBy *string `pulumi:"createdBy"`
	// The filter to apply on the entities before calculating the scorecard
	Filter *ScorecardFilter `pulumi:"filter"`
	// The identifier of the scorecard
	Identifier *string `pulumi:"identifier"`
	// The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
	Levels []ScorecardLevel `pulumi:"levels"`
	// The rules of the scorecard
	Rules []ScorecardRule `pulumi:"rules"`
	// The title of the scorecard
	Title *string `pulumi:"title"`
	// The last update date of the scorecard
	UpdatedAt *string `pulumi:"updatedAt"`
	// The last updater of the scorecard
	UpdatedBy *string `pulumi:"updatedBy"`
}

type ScorecardState struct {
	// The blueprint of the scorecard
	Blueprint pulumi.StringPtrInput
	// The creation date of the scorecard
	CreatedAt pulumi.StringPtrInput
	// The creator of the scorecard
	CreatedBy pulumi.StringPtrInput
	// The filter to apply on the entities before calculating the scorecard
	Filter ScorecardFilterPtrInput
	// The identifier of the scorecard
	Identifier pulumi.StringPtrInput
	// The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
	Levels ScorecardLevelArrayInput
	// The rules of the scorecard
	Rules ScorecardRuleArrayInput
	// The title of the scorecard
	Title pulumi.StringPtrInput
	// The last update date of the scorecard
	UpdatedAt pulumi.StringPtrInput
	// The last updater of the scorecard
	UpdatedBy pulumi.StringPtrInput
}

func (ScorecardState) ElementType() reflect.Type {
	return reflect.TypeOf((*scorecardState)(nil)).Elem()
}

type scorecardArgs struct {
	// The blueprint of the scorecard
	Blueprint string `pulumi:"blueprint"`
	// The filter to apply on the entities before calculating the scorecard
	Filter *ScorecardFilter `pulumi:"filter"`
	// The identifier of the scorecard
	Identifier string `pulumi:"identifier"`
	// The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
	Levels []ScorecardLevel `pulumi:"levels"`
	// The rules of the scorecard
	Rules []ScorecardRule `pulumi:"rules"`
	// The title of the scorecard
	Title string `pulumi:"title"`
}

// The set of arguments for constructing a Scorecard resource.
type ScorecardArgs struct {
	// The blueprint of the scorecard
	Blueprint pulumi.StringInput
	// The filter to apply on the entities before calculating the scorecard
	Filter ScorecardFilterPtrInput
	// The identifier of the scorecard
	Identifier pulumi.StringInput
	// The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
	Levels ScorecardLevelArrayInput
	// The rules of the scorecard
	Rules ScorecardRuleArrayInput
	// The title of the scorecard
	Title pulumi.StringInput
}

func (ScorecardArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*scorecardArgs)(nil)).Elem()
}

type ScorecardInput interface {
	pulumi.Input

	ToScorecardOutput() ScorecardOutput
	ToScorecardOutputWithContext(ctx context.Context) ScorecardOutput
}

func (*Scorecard) ElementType() reflect.Type {
	return reflect.TypeOf((**Scorecard)(nil)).Elem()
}

func (i *Scorecard) ToScorecardOutput() ScorecardOutput {
	return i.ToScorecardOutputWithContext(context.Background())
}

func (i *Scorecard) ToScorecardOutputWithContext(ctx context.Context) ScorecardOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScorecardOutput)
}

// ScorecardArrayInput is an input type that accepts ScorecardArray and ScorecardArrayOutput values.
// You can construct a concrete instance of `ScorecardArrayInput` via:
//
//	ScorecardArray{ ScorecardArgs{...} }
type ScorecardArrayInput interface {
	pulumi.Input

	ToScorecardArrayOutput() ScorecardArrayOutput
	ToScorecardArrayOutputWithContext(context.Context) ScorecardArrayOutput
}

type ScorecardArray []ScorecardInput

func (ScorecardArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Scorecard)(nil)).Elem()
}

func (i ScorecardArray) ToScorecardArrayOutput() ScorecardArrayOutput {
	return i.ToScorecardArrayOutputWithContext(context.Background())
}

func (i ScorecardArray) ToScorecardArrayOutputWithContext(ctx context.Context) ScorecardArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScorecardArrayOutput)
}

// ScorecardMapInput is an input type that accepts ScorecardMap and ScorecardMapOutput values.
// You can construct a concrete instance of `ScorecardMapInput` via:
//
//	ScorecardMap{ "key": ScorecardArgs{...} }
type ScorecardMapInput interface {
	pulumi.Input

	ToScorecardMapOutput() ScorecardMapOutput
	ToScorecardMapOutputWithContext(context.Context) ScorecardMapOutput
}

type ScorecardMap map[string]ScorecardInput

func (ScorecardMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Scorecard)(nil)).Elem()
}

func (i ScorecardMap) ToScorecardMapOutput() ScorecardMapOutput {
	return i.ToScorecardMapOutputWithContext(context.Background())
}

func (i ScorecardMap) ToScorecardMapOutputWithContext(ctx context.Context) ScorecardMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScorecardMapOutput)
}

type ScorecardOutput struct{ *pulumi.OutputState }

func (ScorecardOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Scorecard)(nil)).Elem()
}

func (o ScorecardOutput) ToScorecardOutput() ScorecardOutput {
	return o
}

func (o ScorecardOutput) ToScorecardOutputWithContext(ctx context.Context) ScorecardOutput {
	return o
}

// The blueprint of the scorecard
func (o ScorecardOutput) Blueprint() pulumi.StringOutput {
	return o.ApplyT(func(v *Scorecard) pulumi.StringOutput { return v.Blueprint }).(pulumi.StringOutput)
}

// The creation date of the scorecard
func (o ScorecardOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Scorecard) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The creator of the scorecard
func (o ScorecardOutput) CreatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Scorecard) pulumi.StringOutput { return v.CreatedBy }).(pulumi.StringOutput)
}

// The filter to apply on the entities before calculating the scorecard
func (o ScorecardOutput) Filter() ScorecardFilterPtrOutput {
	return o.ApplyT(func(v *Scorecard) ScorecardFilterPtrOutput { return v.Filter }).(ScorecardFilterPtrOutput)
}

// The identifier of the scorecard
func (o ScorecardOutput) Identifier() pulumi.StringOutput {
	return o.ApplyT(func(v *Scorecard) pulumi.StringOutput { return v.Identifier }).(pulumi.StringOutput)
}

// The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
func (o ScorecardOutput) Levels() ScorecardLevelArrayOutput {
	return o.ApplyT(func(v *Scorecard) ScorecardLevelArrayOutput { return v.Levels }).(ScorecardLevelArrayOutput)
}

// The rules of the scorecard
func (o ScorecardOutput) Rules() ScorecardRuleArrayOutput {
	return o.ApplyT(func(v *Scorecard) ScorecardRuleArrayOutput { return v.Rules }).(ScorecardRuleArrayOutput)
}

// The title of the scorecard
func (o ScorecardOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v *Scorecard) pulumi.StringOutput { return v.Title }).(pulumi.StringOutput)
}

// The last update date of the scorecard
func (o ScorecardOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Scorecard) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

// The last updater of the scorecard
func (o ScorecardOutput) UpdatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Scorecard) pulumi.StringOutput { return v.UpdatedBy }).(pulumi.StringOutput)
}

type ScorecardArrayOutput struct{ *pulumi.OutputState }

func (ScorecardArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Scorecard)(nil)).Elem()
}

func (o ScorecardArrayOutput) ToScorecardArrayOutput() ScorecardArrayOutput {
	return o
}

func (o ScorecardArrayOutput) ToScorecardArrayOutputWithContext(ctx context.Context) ScorecardArrayOutput {
	return o
}

func (o ScorecardArrayOutput) Index(i pulumi.IntInput) ScorecardOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Scorecard {
		return vs[0].([]*Scorecard)[vs[1].(int)]
	}).(ScorecardOutput)
}

type ScorecardMapOutput struct{ *pulumi.OutputState }

func (ScorecardMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Scorecard)(nil)).Elem()
}

func (o ScorecardMapOutput) ToScorecardMapOutput() ScorecardMapOutput {
	return o
}

func (o ScorecardMapOutput) ToScorecardMapOutputWithContext(ctx context.Context) ScorecardMapOutput {
	return o
}

func (o ScorecardMapOutput) MapIndex(k pulumi.StringInput) ScorecardOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Scorecard {
		return vs[0].(map[string]*Scorecard)[vs[1].(string)]
	}).(ScorecardOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ScorecardInput)(nil)).Elem(), &Scorecard{})
	pulumi.RegisterInputType(reflect.TypeOf((*ScorecardArrayInput)(nil)).Elem(), ScorecardArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ScorecardMapInput)(nil)).Elem(), ScorecardMap{})
	pulumi.RegisterOutputType(ScorecardOutput{})
	pulumi.RegisterOutputType(ScorecardArrayOutput{})
	pulumi.RegisterOutputType(ScorecardMapOutput{})
}
