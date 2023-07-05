// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package port

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Blueprint struct {
	pulumi.CustomResourceState

	// A set of properties that are calculated upon entity's regular properties.
	CalculationProperties BlueprintCalculationPropertyArrayOutput `pulumi:"calculationProperties"`
	// Blueprints changelog destination, Supports WEBHOOK and KAFKA
	ChangelogDestination BlueprintChangelogDestinationPtrOutput `pulumi:"changelogDestination"`
	CreatedAt            pulumi.StringOutput                    `pulumi:"createdAt"`
	CreatedBy            pulumi.StringOutput                    `pulumi:"createdBy"`
	// The data source for entities of this blueprint
	//
	// Deprecated: Data source is ignored
	DataSource pulumi.StringPtrOutput `pulumi:"dataSource"`
	// The description of the blueprint
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The icon of the blueprint
	Icon pulumi.StringPtrOutput `pulumi:"icon"`
	// The identifier of the blueprint
	Identifier pulumi.StringOutput `pulumi:"identifier"`
	// When two Blueprints are connected via a Relation, a new set of properties becomes available to Entities in the source
	// Blueprint.
	MirrorProperties BlueprintMirrorPropertyArrayOutput `pulumi:"mirrorProperties"`
	// The metadata of the entity
	Properties BlueprintPropertyArrayOutput `pulumi:"properties"`
	// The blueprints that are connected to this blueprint
	Relations BlueprintRelationArrayOutput `pulumi:"relations"`
	// The display name of the blueprint
	Title     pulumi.StringOutput `pulumi:"title"`
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
	UpdatedBy pulumi.StringOutput `pulumi:"updatedBy"`
}

// NewBlueprint registers a new resource with the given unique name, arguments, and options.
func NewBlueprint(ctx *pulumi.Context,
	name string, args *BlueprintArgs, opts ...pulumi.ResourceOption) (*Blueprint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Identifier == nil {
		return nil, errors.New("invalid value for required argument 'Identifier'")
	}
	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	if args.Title == nil {
		return nil, errors.New("invalid value for required argument 'Title'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource Blueprint
	err := ctx.RegisterResource("port:index/blueprint:Blueprint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBlueprint gets an existing Blueprint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBlueprint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BlueprintState, opts ...pulumi.ResourceOption) (*Blueprint, error) {
	var resource Blueprint
	err := ctx.ReadResource("port:index/blueprint:Blueprint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Blueprint resources.
type blueprintState struct {
	// A set of properties that are calculated upon entity's regular properties.
	CalculationProperties []BlueprintCalculationProperty `pulumi:"calculationProperties"`
	// Blueprints changelog destination, Supports WEBHOOK and KAFKA
	ChangelogDestination *BlueprintChangelogDestination `pulumi:"changelogDestination"`
	CreatedAt            *string                        `pulumi:"createdAt"`
	CreatedBy            *string                        `pulumi:"createdBy"`
	// The data source for entities of this blueprint
	//
	// Deprecated: Data source is ignored
	DataSource *string `pulumi:"dataSource"`
	// The description of the blueprint
	Description *string `pulumi:"description"`
	// The icon of the blueprint
	Icon *string `pulumi:"icon"`
	// The identifier of the blueprint
	Identifier *string `pulumi:"identifier"`
	// When two Blueprints are connected via a Relation, a new set of properties becomes available to Entities in the source
	// Blueprint.
	MirrorProperties []BlueprintMirrorProperty `pulumi:"mirrorProperties"`
	// The metadata of the entity
	Properties []BlueprintProperty `pulumi:"properties"`
	// The blueprints that are connected to this blueprint
	Relations []BlueprintRelation `pulumi:"relations"`
	// The display name of the blueprint
	Title     *string `pulumi:"title"`
	UpdatedAt *string `pulumi:"updatedAt"`
	UpdatedBy *string `pulumi:"updatedBy"`
}

type BlueprintState struct {
	// A set of properties that are calculated upon entity's regular properties.
	CalculationProperties BlueprintCalculationPropertyArrayInput
	// Blueprints changelog destination, Supports WEBHOOK and KAFKA
	ChangelogDestination BlueprintChangelogDestinationPtrInput
	CreatedAt            pulumi.StringPtrInput
	CreatedBy            pulumi.StringPtrInput
	// The data source for entities of this blueprint
	//
	// Deprecated: Data source is ignored
	DataSource pulumi.StringPtrInput
	// The description of the blueprint
	Description pulumi.StringPtrInput
	// The icon of the blueprint
	Icon pulumi.StringPtrInput
	// The identifier of the blueprint
	Identifier pulumi.StringPtrInput
	// When two Blueprints are connected via a Relation, a new set of properties becomes available to Entities in the source
	// Blueprint.
	MirrorProperties BlueprintMirrorPropertyArrayInput
	// The metadata of the entity
	Properties BlueprintPropertyArrayInput
	// The blueprints that are connected to this blueprint
	Relations BlueprintRelationArrayInput
	// The display name of the blueprint
	Title     pulumi.StringPtrInput
	UpdatedAt pulumi.StringPtrInput
	UpdatedBy pulumi.StringPtrInput
}

func (BlueprintState) ElementType() reflect.Type {
	return reflect.TypeOf((*blueprintState)(nil)).Elem()
}

type blueprintArgs struct {
	// A set of properties that are calculated upon entity's regular properties.
	CalculationProperties []BlueprintCalculationProperty `pulumi:"calculationProperties"`
	// Blueprints changelog destination, Supports WEBHOOK and KAFKA
	ChangelogDestination *BlueprintChangelogDestination `pulumi:"changelogDestination"`
	// The data source for entities of this blueprint
	//
	// Deprecated: Data source is ignored
	DataSource *string `pulumi:"dataSource"`
	// The description of the blueprint
	Description *string `pulumi:"description"`
	// The icon of the blueprint
	Icon *string `pulumi:"icon"`
	// The identifier of the blueprint
	Identifier string `pulumi:"identifier"`
	// When two Blueprints are connected via a Relation, a new set of properties becomes available to Entities in the source
	// Blueprint.
	MirrorProperties []BlueprintMirrorProperty `pulumi:"mirrorProperties"`
	// The metadata of the entity
	Properties []BlueprintProperty `pulumi:"properties"`
	// The blueprints that are connected to this blueprint
	Relations []BlueprintRelation `pulumi:"relations"`
	// The display name of the blueprint
	Title string `pulumi:"title"`
}

// The set of arguments for constructing a Blueprint resource.
type BlueprintArgs struct {
	// A set of properties that are calculated upon entity's regular properties.
	CalculationProperties BlueprintCalculationPropertyArrayInput
	// Blueprints changelog destination, Supports WEBHOOK and KAFKA
	ChangelogDestination BlueprintChangelogDestinationPtrInput
	// The data source for entities of this blueprint
	//
	// Deprecated: Data source is ignored
	DataSource pulumi.StringPtrInput
	// The description of the blueprint
	Description pulumi.StringPtrInput
	// The icon of the blueprint
	Icon pulumi.StringPtrInput
	// The identifier of the blueprint
	Identifier pulumi.StringInput
	// When two Blueprints are connected via a Relation, a new set of properties becomes available to Entities in the source
	// Blueprint.
	MirrorProperties BlueprintMirrorPropertyArrayInput
	// The metadata of the entity
	Properties BlueprintPropertyArrayInput
	// The blueprints that are connected to this blueprint
	Relations BlueprintRelationArrayInput
	// The display name of the blueprint
	Title pulumi.StringInput
}

func (BlueprintArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*blueprintArgs)(nil)).Elem()
}

type BlueprintInput interface {
	pulumi.Input

	ToBlueprintOutput() BlueprintOutput
	ToBlueprintOutputWithContext(ctx context.Context) BlueprintOutput
}

func (*Blueprint) ElementType() reflect.Type {
	return reflect.TypeOf((**Blueprint)(nil)).Elem()
}

func (i *Blueprint) ToBlueprintOutput() BlueprintOutput {
	return i.ToBlueprintOutputWithContext(context.Background())
}

func (i *Blueprint) ToBlueprintOutputWithContext(ctx context.Context) BlueprintOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BlueprintOutput)
}

// BlueprintArrayInput is an input type that accepts BlueprintArray and BlueprintArrayOutput values.
// You can construct a concrete instance of `BlueprintArrayInput` via:
//
//	BlueprintArray{ BlueprintArgs{...} }
type BlueprintArrayInput interface {
	pulumi.Input

	ToBlueprintArrayOutput() BlueprintArrayOutput
	ToBlueprintArrayOutputWithContext(context.Context) BlueprintArrayOutput
}

type BlueprintArray []BlueprintInput

func (BlueprintArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Blueprint)(nil)).Elem()
}

func (i BlueprintArray) ToBlueprintArrayOutput() BlueprintArrayOutput {
	return i.ToBlueprintArrayOutputWithContext(context.Background())
}

func (i BlueprintArray) ToBlueprintArrayOutputWithContext(ctx context.Context) BlueprintArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BlueprintArrayOutput)
}

// BlueprintMapInput is an input type that accepts BlueprintMap and BlueprintMapOutput values.
// You can construct a concrete instance of `BlueprintMapInput` via:
//
//	BlueprintMap{ "key": BlueprintArgs{...} }
type BlueprintMapInput interface {
	pulumi.Input

	ToBlueprintMapOutput() BlueprintMapOutput
	ToBlueprintMapOutputWithContext(context.Context) BlueprintMapOutput
}

type BlueprintMap map[string]BlueprintInput

func (BlueprintMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Blueprint)(nil)).Elem()
}

func (i BlueprintMap) ToBlueprintMapOutput() BlueprintMapOutput {
	return i.ToBlueprintMapOutputWithContext(context.Background())
}

func (i BlueprintMap) ToBlueprintMapOutputWithContext(ctx context.Context) BlueprintMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BlueprintMapOutput)
}

type BlueprintOutput struct{ *pulumi.OutputState }

func (BlueprintOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Blueprint)(nil)).Elem()
}

func (o BlueprintOutput) ToBlueprintOutput() BlueprintOutput {
	return o
}

func (o BlueprintOutput) ToBlueprintOutputWithContext(ctx context.Context) BlueprintOutput {
	return o
}

// A set of properties that are calculated upon entity's regular properties.
func (o BlueprintOutput) CalculationProperties() BlueprintCalculationPropertyArrayOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintCalculationPropertyArrayOutput { return v.CalculationProperties }).(BlueprintCalculationPropertyArrayOutput)
}

// Blueprints changelog destination, Supports WEBHOOK and KAFKA
func (o BlueprintOutput) ChangelogDestination() BlueprintChangelogDestinationPtrOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintChangelogDestinationPtrOutput { return v.ChangelogDestination }).(BlueprintChangelogDestinationPtrOutput)
}

func (o BlueprintOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

func (o BlueprintOutput) CreatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.CreatedBy }).(pulumi.StringOutput)
}

// The data source for entities of this blueprint
//
// Deprecated: Data source is ignored
func (o BlueprintOutput) DataSource() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringPtrOutput { return v.DataSource }).(pulumi.StringPtrOutput)
}

// The description of the blueprint
func (o BlueprintOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The icon of the blueprint
func (o BlueprintOutput) Icon() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringPtrOutput { return v.Icon }).(pulumi.StringPtrOutput)
}

// The identifier of the blueprint
func (o BlueprintOutput) Identifier() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.Identifier }).(pulumi.StringOutput)
}

// When two Blueprints are connected via a Relation, a new set of properties becomes available to Entities in the source
// Blueprint.
func (o BlueprintOutput) MirrorProperties() BlueprintMirrorPropertyArrayOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintMirrorPropertyArrayOutput { return v.MirrorProperties }).(BlueprintMirrorPropertyArrayOutput)
}

// The metadata of the entity
func (o BlueprintOutput) Properties() BlueprintPropertyArrayOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintPropertyArrayOutput { return v.Properties }).(BlueprintPropertyArrayOutput)
}

// The blueprints that are connected to this blueprint
func (o BlueprintOutput) Relations() BlueprintRelationArrayOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintRelationArrayOutput { return v.Relations }).(BlueprintRelationArrayOutput)
}

// The display name of the blueprint
func (o BlueprintOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.Title }).(pulumi.StringOutput)
}

func (o BlueprintOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

func (o BlueprintOutput) UpdatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.UpdatedBy }).(pulumi.StringOutput)
}

type BlueprintArrayOutput struct{ *pulumi.OutputState }

func (BlueprintArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Blueprint)(nil)).Elem()
}

func (o BlueprintArrayOutput) ToBlueprintArrayOutput() BlueprintArrayOutput {
	return o
}

func (o BlueprintArrayOutput) ToBlueprintArrayOutputWithContext(ctx context.Context) BlueprintArrayOutput {
	return o
}

func (o BlueprintArrayOutput) Index(i pulumi.IntInput) BlueprintOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Blueprint {
		return vs[0].([]*Blueprint)[vs[1].(int)]
	}).(BlueprintOutput)
}

type BlueprintMapOutput struct{ *pulumi.OutputState }

func (BlueprintMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Blueprint)(nil)).Elem()
}

func (o BlueprintMapOutput) ToBlueprintMapOutput() BlueprintMapOutput {
	return o
}

func (o BlueprintMapOutput) ToBlueprintMapOutputWithContext(ctx context.Context) BlueprintMapOutput {
	return o
}

func (o BlueprintMapOutput) MapIndex(k pulumi.StringInput) BlueprintOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Blueprint {
		return vs[0].(map[string]*Blueprint)[vs[1].(string)]
	}).(BlueprintOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BlueprintInput)(nil)).Elem(), &Blueprint{})
	pulumi.RegisterInputType(reflect.TypeOf((*BlueprintArrayInput)(nil)).Elem(), BlueprintArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*BlueprintMapInput)(nil)).Elem(), BlueprintMap{})
	pulumi.RegisterOutputType(BlueprintOutput{})
	pulumi.RegisterOutputType(BlueprintArrayOutput{})
	pulumi.RegisterOutputType(BlueprintMapOutput{})
}
