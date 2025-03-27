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

// Entity resource
type Entity struct {
	pulumi.CustomResourceState

	// The blueprint identifier the entity relates to
	Blueprint pulumi.StringOutput `pulumi:"blueprint"`
	// Whether to create missing related entities
	CreateMissingRelatedEntities pulumi.BoolOutput `pulumi:"createMissingRelatedEntities"`
	// The creation date of the entity
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The creator of the entity
	CreatedBy pulumi.StringOutput `pulumi:"createdBy"`
	// The icon of the entity
	Icon pulumi.StringPtrOutput `pulumi:"icon"`
	// The identifier of the entity
	Identifier pulumi.StringOutput `pulumi:"identifier"`
	// The properties of the entity
	Properties EntityPropertiesPtrOutput `pulumi:"properties"`
	// The relations of the entity
	Relations EntityRelationsPtrOutput `pulumi:"relations"`
	// The runID of the action run that created the entity
	RunId pulumi.StringPtrOutput `pulumi:"runId"`
	// The teams the entity belongs to
	Teams pulumi.StringArrayOutput `pulumi:"teams"`
	// The title of the entity
	Title pulumi.StringOutput `pulumi:"title"`
	// The last update date of the entity
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
	// The last updater of the entity
	UpdatedBy pulumi.StringOutput `pulumi:"updatedBy"`
}

// NewEntity registers a new resource with the given unique name, arguments, and options.
func NewEntity(ctx *pulumi.Context,
	name string, args *EntityArgs, opts ...pulumi.ResourceOption) (*Entity, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Blueprint == nil {
		return nil, errors.New("invalid value for required argument 'Blueprint'")
	}
	if args.Title == nil {
		return nil, errors.New("invalid value for required argument 'Title'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Entity
	err := ctx.RegisterResource("port:index/entity:Entity", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEntity gets an existing Entity resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEntity(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EntityState, opts ...pulumi.ResourceOption) (*Entity, error) {
	var resource Entity
	err := ctx.ReadResource("port:index/entity:Entity", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Entity resources.
type entityState struct {
	// The blueprint identifier the entity relates to
	Blueprint *string `pulumi:"blueprint"`
	// Whether to create missing related entities
	CreateMissingRelatedEntities *bool `pulumi:"createMissingRelatedEntities"`
	// The creation date of the entity
	CreatedAt *string `pulumi:"createdAt"`
	// The creator of the entity
	CreatedBy *string `pulumi:"createdBy"`
	// The icon of the entity
	Icon *string `pulumi:"icon"`
	// The identifier of the entity
	Identifier *string `pulumi:"identifier"`
	// The properties of the entity
	Properties *EntityProperties `pulumi:"properties"`
	// The relations of the entity
	Relations *EntityRelations `pulumi:"relations"`
	// The runID of the action run that created the entity
	RunId *string `pulumi:"runId"`
	// The teams the entity belongs to
	Teams []string `pulumi:"teams"`
	// The title of the entity
	Title *string `pulumi:"title"`
	// The last update date of the entity
	UpdatedAt *string `pulumi:"updatedAt"`
	// The last updater of the entity
	UpdatedBy *string `pulumi:"updatedBy"`
}

type EntityState struct {
	// The blueprint identifier the entity relates to
	Blueprint pulumi.StringPtrInput
	// Whether to create missing related entities
	CreateMissingRelatedEntities pulumi.BoolPtrInput
	// The creation date of the entity
	CreatedAt pulumi.StringPtrInput
	// The creator of the entity
	CreatedBy pulumi.StringPtrInput
	// The icon of the entity
	Icon pulumi.StringPtrInput
	// The identifier of the entity
	Identifier pulumi.StringPtrInput
	// The properties of the entity
	Properties EntityPropertiesPtrInput
	// The relations of the entity
	Relations EntityRelationsPtrInput
	// The runID of the action run that created the entity
	RunId pulumi.StringPtrInput
	// The teams the entity belongs to
	Teams pulumi.StringArrayInput
	// The title of the entity
	Title pulumi.StringPtrInput
	// The last update date of the entity
	UpdatedAt pulumi.StringPtrInput
	// The last updater of the entity
	UpdatedBy pulumi.StringPtrInput
}

func (EntityState) ElementType() reflect.Type {
	return reflect.TypeOf((*entityState)(nil)).Elem()
}

type entityArgs struct {
	// The blueprint identifier the entity relates to
	Blueprint string `pulumi:"blueprint"`
	// Whether to create missing related entities
	CreateMissingRelatedEntities *bool `pulumi:"createMissingRelatedEntities"`
	// The icon of the entity
	Icon *string `pulumi:"icon"`
	// The identifier of the entity
	Identifier *string `pulumi:"identifier"`
	// The properties of the entity
	Properties *EntityProperties `pulumi:"properties"`
	// The relations of the entity
	Relations *EntityRelations `pulumi:"relations"`
	// The runID of the action run that created the entity
	RunId *string `pulumi:"runId"`
	// The teams the entity belongs to
	Teams []string `pulumi:"teams"`
	// The title of the entity
	Title string `pulumi:"title"`
}

// The set of arguments for constructing a Entity resource.
type EntityArgs struct {
	// The blueprint identifier the entity relates to
	Blueprint pulumi.StringInput
	// Whether to create missing related entities
	CreateMissingRelatedEntities pulumi.BoolPtrInput
	// The icon of the entity
	Icon pulumi.StringPtrInput
	// The identifier of the entity
	Identifier pulumi.StringPtrInput
	// The properties of the entity
	Properties EntityPropertiesPtrInput
	// The relations of the entity
	Relations EntityRelationsPtrInput
	// The runID of the action run that created the entity
	RunId pulumi.StringPtrInput
	// The teams the entity belongs to
	Teams pulumi.StringArrayInput
	// The title of the entity
	Title pulumi.StringInput
}

func (EntityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*entityArgs)(nil)).Elem()
}

type EntityInput interface {
	pulumi.Input

	ToEntityOutput() EntityOutput
	ToEntityOutputWithContext(ctx context.Context) EntityOutput
}

func (*Entity) ElementType() reflect.Type {
	return reflect.TypeOf((**Entity)(nil)).Elem()
}

func (i *Entity) ToEntityOutput() EntityOutput {
	return i.ToEntityOutputWithContext(context.Background())
}

func (i *Entity) ToEntityOutputWithContext(ctx context.Context) EntityOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EntityOutput)
}

// EntityArrayInput is an input type that accepts EntityArray and EntityArrayOutput values.
// You can construct a concrete instance of `EntityArrayInput` via:
//
//	EntityArray{ EntityArgs{...} }
type EntityArrayInput interface {
	pulumi.Input

	ToEntityArrayOutput() EntityArrayOutput
	ToEntityArrayOutputWithContext(context.Context) EntityArrayOutput
}

type EntityArray []EntityInput

func (EntityArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Entity)(nil)).Elem()
}

func (i EntityArray) ToEntityArrayOutput() EntityArrayOutput {
	return i.ToEntityArrayOutputWithContext(context.Background())
}

func (i EntityArray) ToEntityArrayOutputWithContext(ctx context.Context) EntityArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EntityArrayOutput)
}

// EntityMapInput is an input type that accepts EntityMap and EntityMapOutput values.
// You can construct a concrete instance of `EntityMapInput` via:
//
//	EntityMap{ "key": EntityArgs{...} }
type EntityMapInput interface {
	pulumi.Input

	ToEntityMapOutput() EntityMapOutput
	ToEntityMapOutputWithContext(context.Context) EntityMapOutput
}

type EntityMap map[string]EntityInput

func (EntityMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Entity)(nil)).Elem()
}

func (i EntityMap) ToEntityMapOutput() EntityMapOutput {
	return i.ToEntityMapOutputWithContext(context.Background())
}

func (i EntityMap) ToEntityMapOutputWithContext(ctx context.Context) EntityMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EntityMapOutput)
}

type EntityOutput struct{ *pulumi.OutputState }

func (EntityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Entity)(nil)).Elem()
}

func (o EntityOutput) ToEntityOutput() EntityOutput {
	return o
}

func (o EntityOutput) ToEntityOutputWithContext(ctx context.Context) EntityOutput {
	return o
}

// The blueprint identifier the entity relates to
func (o EntityOutput) Blueprint() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Blueprint }).(pulumi.StringOutput)
}

// Whether to create missing related entities
func (o EntityOutput) CreateMissingRelatedEntities() pulumi.BoolOutput {
	return o.ApplyT(func(v *Entity) pulumi.BoolOutput { return v.CreateMissingRelatedEntities }).(pulumi.BoolOutput)
}

// The creation date of the entity
func (o EntityOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The creator of the entity
func (o EntityOutput) CreatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.CreatedBy }).(pulumi.StringOutput)
}

// The icon of the entity
func (o EntityOutput) Icon() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringPtrOutput { return v.Icon }).(pulumi.StringPtrOutput)
}

// The identifier of the entity
func (o EntityOutput) Identifier() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Identifier }).(pulumi.StringOutput)
}

// The properties of the entity
func (o EntityOutput) Properties() EntityPropertiesPtrOutput {
	return o.ApplyT(func(v *Entity) EntityPropertiesPtrOutput { return v.Properties }).(EntityPropertiesPtrOutput)
}

// The relations of the entity
func (o EntityOutput) Relations() EntityRelationsPtrOutput {
	return o.ApplyT(func(v *Entity) EntityRelationsPtrOutput { return v.Relations }).(EntityRelationsPtrOutput)
}

// The runID of the action run that created the entity
func (o EntityOutput) RunId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringPtrOutput { return v.RunId }).(pulumi.StringPtrOutput)
}

// The teams the entity belongs to
func (o EntityOutput) Teams() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringArrayOutput { return v.Teams }).(pulumi.StringArrayOutput)
}

// The title of the entity
func (o EntityOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Title }).(pulumi.StringOutput)
}

// The last update date of the entity
func (o EntityOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

// The last updater of the entity
func (o EntityOutput) UpdatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.UpdatedBy }).(pulumi.StringOutput)
}

type EntityArrayOutput struct{ *pulumi.OutputState }

func (EntityArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Entity)(nil)).Elem()
}

func (o EntityArrayOutput) ToEntityArrayOutput() EntityArrayOutput {
	return o
}

func (o EntityArrayOutput) ToEntityArrayOutputWithContext(ctx context.Context) EntityArrayOutput {
	return o
}

func (o EntityArrayOutput) Index(i pulumi.IntInput) EntityOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Entity {
		return vs[0].([]*Entity)[vs[1].(int)]
	}).(EntityOutput)
}

type EntityMapOutput struct{ *pulumi.OutputState }

func (EntityMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Entity)(nil)).Elem()
}

func (o EntityMapOutput) ToEntityMapOutput() EntityMapOutput {
	return o
}

func (o EntityMapOutput) ToEntityMapOutputWithContext(ctx context.Context) EntityMapOutput {
	return o
}

func (o EntityMapOutput) MapIndex(k pulumi.StringInput) EntityOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Entity {
		return vs[0].(map[string]*Entity)[vs[1].(string)]
	}).(EntityOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EntityInput)(nil)).Elem(), &Entity{})
	pulumi.RegisterInputType(reflect.TypeOf((*EntityArrayInput)(nil)).Elem(), EntityArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EntityMapInput)(nil)).Elem(), EntityMap{})
	pulumi.RegisterOutputType(EntityOutput{})
	pulumi.RegisterOutputType(EntityArrayOutput{})
	pulumi.RegisterOutputType(EntityMapOutput{})
}
