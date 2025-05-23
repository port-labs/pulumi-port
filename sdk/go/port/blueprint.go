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

type Blueprint struct {
	pulumi.CustomResourceState

	// The calculation properties of the blueprint
	CalculationProperties BlueprintCalculationPropertiesMapOutput `pulumi:"calculationProperties"`
	// This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
	CreateCatalogPage pulumi.BoolOutput `pulumi:"createCatalogPage"`
	// The creation date of the blueprint
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The creator of the blueprint
	CreatedBy pulumi.StringOutput `pulumi:"createdBy"`
	// The description of the blueprint
	Description         pulumi.StringPtrOutput `pulumi:"description"`
	ForceDeleteEntities pulumi.BoolOutput      `pulumi:"forceDeleteEntities"`
	// The icon of the blueprint
	Icon pulumi.StringPtrOutput `pulumi:"icon"`
	// The identifier of the blueprint
	Identifier pulumi.StringOutput `pulumi:"identifier"`
	// The changelog destination of the blueprint
	KafkaChangelogDestination BlueprintKafkaChangelogDestinationPtrOutput `pulumi:"kafkaChangelogDestination"`
	// The mirror properties of the blueprint
	MirrorProperties BlueprintMirrorPropertiesMapOutput `pulumi:"mirrorProperties"`
	// Optional ownership field for Blueprint. 'type' can be Inherited or Direct. If 'Inherited', then 'path' is required and must be a valid relation identifiers path.
	Ownership BlueprintOwnershipPtrOutput `pulumi:"ownership"`
	// The properties of the blueprint
	Properties BlueprintPropertiesPtrOutput `pulumi:"properties"`
	// The relations of the blueprint
	Relations BlueprintRelationsMapOutput `pulumi:"relations"`
	// The team inheritance of the blueprint
	//
	// Deprecated: After the Users and Teams migration, `teamInheritance` will be ignored in favor of `ownership`
	TeamInheritance BlueprintTeamInheritancePtrOutput `pulumi:"teamInheritance"`
	// The display name of the blueprint
	Title pulumi.StringOutput `pulumi:"title"`
	// The last update date of the blueprint
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
	// The last updater of the blueprint
	UpdatedBy pulumi.StringOutput `pulumi:"updatedBy"`
	// The webhook changelog destination of the blueprint
	WebhookChangelogDestination BlueprintWebhookChangelogDestinationPtrOutput `pulumi:"webhookChangelogDestination"`
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
	if args.Title == nil {
		return nil, errors.New("invalid value for required argument 'Title'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
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
	// The calculation properties of the blueprint
	CalculationProperties map[string]BlueprintCalculationProperties `pulumi:"calculationProperties"`
	// This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
	CreateCatalogPage *bool `pulumi:"createCatalogPage"`
	// The creation date of the blueprint
	CreatedAt *string `pulumi:"createdAt"`
	// The creator of the blueprint
	CreatedBy *string `pulumi:"createdBy"`
	// The description of the blueprint
	Description         *string `pulumi:"description"`
	ForceDeleteEntities *bool   `pulumi:"forceDeleteEntities"`
	// The icon of the blueprint
	Icon *string `pulumi:"icon"`
	// The identifier of the blueprint
	Identifier *string `pulumi:"identifier"`
	// The changelog destination of the blueprint
	KafkaChangelogDestination *BlueprintKafkaChangelogDestination `pulumi:"kafkaChangelogDestination"`
	// The mirror properties of the blueprint
	MirrorProperties map[string]BlueprintMirrorProperties `pulumi:"mirrorProperties"`
	// Optional ownership field for Blueprint. 'type' can be Inherited or Direct. If 'Inherited', then 'path' is required and must be a valid relation identifiers path.
	Ownership *BlueprintOwnership `pulumi:"ownership"`
	// The properties of the blueprint
	Properties *BlueprintProperties `pulumi:"properties"`
	// The relations of the blueprint
	Relations map[string]BlueprintRelations `pulumi:"relations"`
	// The team inheritance of the blueprint
	//
	// Deprecated: After the Users and Teams migration, `teamInheritance` will be ignored in favor of `ownership`
	TeamInheritance *BlueprintTeamInheritance `pulumi:"teamInheritance"`
	// The display name of the blueprint
	Title *string `pulumi:"title"`
	// The last update date of the blueprint
	UpdatedAt *string `pulumi:"updatedAt"`
	// The last updater of the blueprint
	UpdatedBy *string `pulumi:"updatedBy"`
	// The webhook changelog destination of the blueprint
	WebhookChangelogDestination *BlueprintWebhookChangelogDestination `pulumi:"webhookChangelogDestination"`
}

type BlueprintState struct {
	// The calculation properties of the blueprint
	CalculationProperties BlueprintCalculationPropertiesMapInput
	// This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
	CreateCatalogPage pulumi.BoolPtrInput
	// The creation date of the blueprint
	CreatedAt pulumi.StringPtrInput
	// The creator of the blueprint
	CreatedBy pulumi.StringPtrInput
	// The description of the blueprint
	Description         pulumi.StringPtrInput
	ForceDeleteEntities pulumi.BoolPtrInput
	// The icon of the blueprint
	Icon pulumi.StringPtrInput
	// The identifier of the blueprint
	Identifier pulumi.StringPtrInput
	// The changelog destination of the blueprint
	KafkaChangelogDestination BlueprintKafkaChangelogDestinationPtrInput
	// The mirror properties of the blueprint
	MirrorProperties BlueprintMirrorPropertiesMapInput
	// Optional ownership field for Blueprint. 'type' can be Inherited or Direct. If 'Inherited', then 'path' is required and must be a valid relation identifiers path.
	Ownership BlueprintOwnershipPtrInput
	// The properties of the blueprint
	Properties BlueprintPropertiesPtrInput
	// The relations of the blueprint
	Relations BlueprintRelationsMapInput
	// The team inheritance of the blueprint
	//
	// Deprecated: After the Users and Teams migration, `teamInheritance` will be ignored in favor of `ownership`
	TeamInheritance BlueprintTeamInheritancePtrInput
	// The display name of the blueprint
	Title pulumi.StringPtrInput
	// The last update date of the blueprint
	UpdatedAt pulumi.StringPtrInput
	// The last updater of the blueprint
	UpdatedBy pulumi.StringPtrInput
	// The webhook changelog destination of the blueprint
	WebhookChangelogDestination BlueprintWebhookChangelogDestinationPtrInput
}

func (BlueprintState) ElementType() reflect.Type {
	return reflect.TypeOf((*blueprintState)(nil)).Elem()
}

type blueprintArgs struct {
	// The calculation properties of the blueprint
	CalculationProperties map[string]BlueprintCalculationProperties `pulumi:"calculationProperties"`
	// This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
	CreateCatalogPage *bool `pulumi:"createCatalogPage"`
	// The description of the blueprint
	Description         *string `pulumi:"description"`
	ForceDeleteEntities *bool   `pulumi:"forceDeleteEntities"`
	// The icon of the blueprint
	Icon *string `pulumi:"icon"`
	// The identifier of the blueprint
	Identifier string `pulumi:"identifier"`
	// The changelog destination of the blueprint
	KafkaChangelogDestination *BlueprintKafkaChangelogDestination `pulumi:"kafkaChangelogDestination"`
	// The mirror properties of the blueprint
	MirrorProperties map[string]BlueprintMirrorProperties `pulumi:"mirrorProperties"`
	// Optional ownership field for Blueprint. 'type' can be Inherited or Direct. If 'Inherited', then 'path' is required and must be a valid relation identifiers path.
	Ownership *BlueprintOwnership `pulumi:"ownership"`
	// The properties of the blueprint
	Properties *BlueprintProperties `pulumi:"properties"`
	// The relations of the blueprint
	Relations map[string]BlueprintRelations `pulumi:"relations"`
	// The team inheritance of the blueprint
	//
	// Deprecated: After the Users and Teams migration, `teamInheritance` will be ignored in favor of `ownership`
	TeamInheritance *BlueprintTeamInheritance `pulumi:"teamInheritance"`
	// The display name of the blueprint
	Title string `pulumi:"title"`
	// The webhook changelog destination of the blueprint
	WebhookChangelogDestination *BlueprintWebhookChangelogDestination `pulumi:"webhookChangelogDestination"`
}

// The set of arguments for constructing a Blueprint resource.
type BlueprintArgs struct {
	// The calculation properties of the blueprint
	CalculationProperties BlueprintCalculationPropertiesMapInput
	// This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
	CreateCatalogPage pulumi.BoolPtrInput
	// The description of the blueprint
	Description         pulumi.StringPtrInput
	ForceDeleteEntities pulumi.BoolPtrInput
	// The icon of the blueprint
	Icon pulumi.StringPtrInput
	// The identifier of the blueprint
	Identifier pulumi.StringInput
	// The changelog destination of the blueprint
	KafkaChangelogDestination BlueprintKafkaChangelogDestinationPtrInput
	// The mirror properties of the blueprint
	MirrorProperties BlueprintMirrorPropertiesMapInput
	// Optional ownership field for Blueprint. 'type' can be Inherited or Direct. If 'Inherited', then 'path' is required and must be a valid relation identifiers path.
	Ownership BlueprintOwnershipPtrInput
	// The properties of the blueprint
	Properties BlueprintPropertiesPtrInput
	// The relations of the blueprint
	Relations BlueprintRelationsMapInput
	// The team inheritance of the blueprint
	//
	// Deprecated: After the Users and Teams migration, `teamInheritance` will be ignored in favor of `ownership`
	TeamInheritance BlueprintTeamInheritancePtrInput
	// The display name of the blueprint
	Title pulumi.StringInput
	// The webhook changelog destination of the blueprint
	WebhookChangelogDestination BlueprintWebhookChangelogDestinationPtrInput
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

// The calculation properties of the blueprint
func (o BlueprintOutput) CalculationProperties() BlueprintCalculationPropertiesMapOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintCalculationPropertiesMapOutput { return v.CalculationProperties }).(BlueprintCalculationPropertiesMapOutput)
}

// This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
func (o BlueprintOutput) CreateCatalogPage() pulumi.BoolOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.BoolOutput { return v.CreateCatalogPage }).(pulumi.BoolOutput)
}

// The creation date of the blueprint
func (o BlueprintOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The creator of the blueprint
func (o BlueprintOutput) CreatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.CreatedBy }).(pulumi.StringOutput)
}

// The description of the blueprint
func (o BlueprintOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o BlueprintOutput) ForceDeleteEntities() pulumi.BoolOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.BoolOutput { return v.ForceDeleteEntities }).(pulumi.BoolOutput)
}

// The icon of the blueprint
func (o BlueprintOutput) Icon() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringPtrOutput { return v.Icon }).(pulumi.StringPtrOutput)
}

// The identifier of the blueprint
func (o BlueprintOutput) Identifier() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.Identifier }).(pulumi.StringOutput)
}

// The changelog destination of the blueprint
func (o BlueprintOutput) KafkaChangelogDestination() BlueprintKafkaChangelogDestinationPtrOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintKafkaChangelogDestinationPtrOutput { return v.KafkaChangelogDestination }).(BlueprintKafkaChangelogDestinationPtrOutput)
}

// The mirror properties of the blueprint
func (o BlueprintOutput) MirrorProperties() BlueprintMirrorPropertiesMapOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintMirrorPropertiesMapOutput { return v.MirrorProperties }).(BlueprintMirrorPropertiesMapOutput)
}

// Optional ownership field for Blueprint. 'type' can be Inherited or Direct. If 'Inherited', then 'path' is required and must be a valid relation identifiers path.
func (o BlueprintOutput) Ownership() BlueprintOwnershipPtrOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintOwnershipPtrOutput { return v.Ownership }).(BlueprintOwnershipPtrOutput)
}

// The properties of the blueprint
func (o BlueprintOutput) Properties() BlueprintPropertiesPtrOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintPropertiesPtrOutput { return v.Properties }).(BlueprintPropertiesPtrOutput)
}

// The relations of the blueprint
func (o BlueprintOutput) Relations() BlueprintRelationsMapOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintRelationsMapOutput { return v.Relations }).(BlueprintRelationsMapOutput)
}

// The team inheritance of the blueprint
//
// Deprecated: After the Users and Teams migration, `teamInheritance` will be ignored in favor of `ownership`
func (o BlueprintOutput) TeamInheritance() BlueprintTeamInheritancePtrOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintTeamInheritancePtrOutput { return v.TeamInheritance }).(BlueprintTeamInheritancePtrOutput)
}

// The display name of the blueprint
func (o BlueprintOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.Title }).(pulumi.StringOutput)
}

// The last update date of the blueprint
func (o BlueprintOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

// The last updater of the blueprint
func (o BlueprintOutput) UpdatedBy() pulumi.StringOutput {
	return o.ApplyT(func(v *Blueprint) pulumi.StringOutput { return v.UpdatedBy }).(pulumi.StringOutput)
}

// The webhook changelog destination of the blueprint
func (o BlueprintOutput) WebhookChangelogDestination() BlueprintWebhookChangelogDestinationPtrOutput {
	return o.ApplyT(func(v *Blueprint) BlueprintWebhookChangelogDestinationPtrOutput { return v.WebhookChangelogDestination }).(BlueprintWebhookChangelogDestinationPtrOutput)
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
