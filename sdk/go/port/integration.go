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

// **NOTE:** This resource manages existing integration and integration mappings, not for creating new integrations.
//
// Docs about integrations can be found [here](https://docs.getport.io/integrations-index/).
//
// Docs about how to import existing integrations and manage their mappings can be found here.
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
// _, err := port.NewPort_integration(ctx, "myCustomIntegration", &port.Port_integrationArgs{
// InstallationId: "my-custom-integration-id",
// Title: "My Custom Integration",
// Version: "1.33.7",
// Config: %!v(PANIC=Format method: fatal: An assertion has failed: unlowered function toJSON),
// })
// if err != nil {
// return err
// }
// return nil
// })
// }
// ```
type Integration struct {
	pulumi.CustomResourceState

	// Integration Config Raw JSON string (use `jsonencode`)
	Config              pulumi.StringPtrOutput `pulumi:"config"`
	InstallationAppType pulumi.StringPtrOutput `pulumi:"installationAppType"`
	InstallationId      pulumi.StringOutput    `pulumi:"installationId"`
	// The changelog destination of the blueprint (just an empty `{}`)
	KafkaChangelogDestination IntegrationKafkaChangelogDestinationPtrOutput `pulumi:"kafkaChangelogDestination"`
	Title                     pulumi.StringPtrOutput                        `pulumi:"title"`
	Version                   pulumi.StringPtrOutput                        `pulumi:"version"`
	// The webhook changelog destination of the integration
	WebhookChangelogDestination IntegrationWebhookChangelogDestinationPtrOutput `pulumi:"webhookChangelogDestination"`
}

// NewIntegration registers a new resource with the given unique name, arguments, and options.
func NewIntegration(ctx *pulumi.Context,
	name string, args *IntegrationArgs, opts ...pulumi.ResourceOption) (*Integration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstallationId == nil {
		return nil, errors.New("invalid value for required argument 'InstallationId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Integration
	err := ctx.RegisterResource("port:index/integration:Integration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIntegration gets an existing Integration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIntegration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IntegrationState, opts ...pulumi.ResourceOption) (*Integration, error) {
	var resource Integration
	err := ctx.ReadResource("port:index/integration:Integration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Integration resources.
type integrationState struct {
	// Integration Config Raw JSON string (use `jsonencode`)
	Config              *string `pulumi:"config"`
	InstallationAppType *string `pulumi:"installationAppType"`
	InstallationId      *string `pulumi:"installationId"`
	// The changelog destination of the blueprint (just an empty `{}`)
	KafkaChangelogDestination *IntegrationKafkaChangelogDestination `pulumi:"kafkaChangelogDestination"`
	Title                     *string                               `pulumi:"title"`
	Version                   *string                               `pulumi:"version"`
	// The webhook changelog destination of the integration
	WebhookChangelogDestination *IntegrationWebhookChangelogDestination `pulumi:"webhookChangelogDestination"`
}

type IntegrationState struct {
	// Integration Config Raw JSON string (use `jsonencode`)
	Config              pulumi.StringPtrInput
	InstallationAppType pulumi.StringPtrInput
	InstallationId      pulumi.StringPtrInput
	// The changelog destination of the blueprint (just an empty `{}`)
	KafkaChangelogDestination IntegrationKafkaChangelogDestinationPtrInput
	Title                     pulumi.StringPtrInput
	Version                   pulumi.StringPtrInput
	// The webhook changelog destination of the integration
	WebhookChangelogDestination IntegrationWebhookChangelogDestinationPtrInput
}

func (IntegrationState) ElementType() reflect.Type {
	return reflect.TypeOf((*integrationState)(nil)).Elem()
}

type integrationArgs struct {
	// Integration Config Raw JSON string (use `jsonencode`)
	Config              *string `pulumi:"config"`
	InstallationAppType *string `pulumi:"installationAppType"`
	InstallationId      string  `pulumi:"installationId"`
	// The changelog destination of the blueprint (just an empty `{}`)
	KafkaChangelogDestination *IntegrationKafkaChangelogDestination `pulumi:"kafkaChangelogDestination"`
	Title                     *string                               `pulumi:"title"`
	Version                   *string                               `pulumi:"version"`
	// The webhook changelog destination of the integration
	WebhookChangelogDestination *IntegrationWebhookChangelogDestination `pulumi:"webhookChangelogDestination"`
}

// The set of arguments for constructing a Integration resource.
type IntegrationArgs struct {
	// Integration Config Raw JSON string (use `jsonencode`)
	Config              pulumi.StringPtrInput
	InstallationAppType pulumi.StringPtrInput
	InstallationId      pulumi.StringInput
	// The changelog destination of the blueprint (just an empty `{}`)
	KafkaChangelogDestination IntegrationKafkaChangelogDestinationPtrInput
	Title                     pulumi.StringPtrInput
	Version                   pulumi.StringPtrInput
	// The webhook changelog destination of the integration
	WebhookChangelogDestination IntegrationWebhookChangelogDestinationPtrInput
}

func (IntegrationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*integrationArgs)(nil)).Elem()
}

type IntegrationInput interface {
	pulumi.Input

	ToIntegrationOutput() IntegrationOutput
	ToIntegrationOutputWithContext(ctx context.Context) IntegrationOutput
}

func (*Integration) ElementType() reflect.Type {
	return reflect.TypeOf((**Integration)(nil)).Elem()
}

func (i *Integration) ToIntegrationOutput() IntegrationOutput {
	return i.ToIntegrationOutputWithContext(context.Background())
}

func (i *Integration) ToIntegrationOutputWithContext(ctx context.Context) IntegrationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationOutput)
}

// IntegrationArrayInput is an input type that accepts IntegrationArray and IntegrationArrayOutput values.
// You can construct a concrete instance of `IntegrationArrayInput` via:
//
//	IntegrationArray{ IntegrationArgs{...} }
type IntegrationArrayInput interface {
	pulumi.Input

	ToIntegrationArrayOutput() IntegrationArrayOutput
	ToIntegrationArrayOutputWithContext(context.Context) IntegrationArrayOutput
}

type IntegrationArray []IntegrationInput

func (IntegrationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Integration)(nil)).Elem()
}

func (i IntegrationArray) ToIntegrationArrayOutput() IntegrationArrayOutput {
	return i.ToIntegrationArrayOutputWithContext(context.Background())
}

func (i IntegrationArray) ToIntegrationArrayOutputWithContext(ctx context.Context) IntegrationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationArrayOutput)
}

// IntegrationMapInput is an input type that accepts IntegrationMap and IntegrationMapOutput values.
// You can construct a concrete instance of `IntegrationMapInput` via:
//
//	IntegrationMap{ "key": IntegrationArgs{...} }
type IntegrationMapInput interface {
	pulumi.Input

	ToIntegrationMapOutput() IntegrationMapOutput
	ToIntegrationMapOutputWithContext(context.Context) IntegrationMapOutput
}

type IntegrationMap map[string]IntegrationInput

func (IntegrationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Integration)(nil)).Elem()
}

func (i IntegrationMap) ToIntegrationMapOutput() IntegrationMapOutput {
	return i.ToIntegrationMapOutputWithContext(context.Background())
}

func (i IntegrationMap) ToIntegrationMapOutputWithContext(ctx context.Context) IntegrationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationMapOutput)
}

type IntegrationOutput struct{ *pulumi.OutputState }

func (IntegrationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Integration)(nil)).Elem()
}

func (o IntegrationOutput) ToIntegrationOutput() IntegrationOutput {
	return o
}

func (o IntegrationOutput) ToIntegrationOutputWithContext(ctx context.Context) IntegrationOutput {
	return o
}

// Integration Config Raw JSON string (use `jsonencode`)
func (o IntegrationOutput) Config() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Integration) pulumi.StringPtrOutput { return v.Config }).(pulumi.StringPtrOutput)
}

func (o IntegrationOutput) InstallationAppType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Integration) pulumi.StringPtrOutput { return v.InstallationAppType }).(pulumi.StringPtrOutput)
}

func (o IntegrationOutput) InstallationId() pulumi.StringOutput {
	return o.ApplyT(func(v *Integration) pulumi.StringOutput { return v.InstallationId }).(pulumi.StringOutput)
}

// The changelog destination of the blueprint (just an empty `{}`)
func (o IntegrationOutput) KafkaChangelogDestination() IntegrationKafkaChangelogDestinationPtrOutput {
	return o.ApplyT(func(v *Integration) IntegrationKafkaChangelogDestinationPtrOutput { return v.KafkaChangelogDestination }).(IntegrationKafkaChangelogDestinationPtrOutput)
}

func (o IntegrationOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Integration) pulumi.StringPtrOutput { return v.Title }).(pulumi.StringPtrOutput)
}

func (o IntegrationOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Integration) pulumi.StringPtrOutput { return v.Version }).(pulumi.StringPtrOutput)
}

// The webhook changelog destination of the integration
func (o IntegrationOutput) WebhookChangelogDestination() IntegrationWebhookChangelogDestinationPtrOutput {
	return o.ApplyT(func(v *Integration) IntegrationWebhookChangelogDestinationPtrOutput {
		return v.WebhookChangelogDestination
	}).(IntegrationWebhookChangelogDestinationPtrOutput)
}

type IntegrationArrayOutput struct{ *pulumi.OutputState }

func (IntegrationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Integration)(nil)).Elem()
}

func (o IntegrationArrayOutput) ToIntegrationArrayOutput() IntegrationArrayOutput {
	return o
}

func (o IntegrationArrayOutput) ToIntegrationArrayOutputWithContext(ctx context.Context) IntegrationArrayOutput {
	return o
}

func (o IntegrationArrayOutput) Index(i pulumi.IntInput) IntegrationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Integration {
		return vs[0].([]*Integration)[vs[1].(int)]
	}).(IntegrationOutput)
}

type IntegrationMapOutput struct{ *pulumi.OutputState }

func (IntegrationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Integration)(nil)).Elem()
}

func (o IntegrationMapOutput) ToIntegrationMapOutput() IntegrationMapOutput {
	return o
}

func (o IntegrationMapOutput) ToIntegrationMapOutputWithContext(ctx context.Context) IntegrationMapOutput {
	return o
}

func (o IntegrationMapOutput) MapIndex(k pulumi.StringInput) IntegrationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Integration {
		return vs[0].(map[string]*Integration)[vs[1].(string)]
	}).(IntegrationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IntegrationInput)(nil)).Elem(), &Integration{})
	pulumi.RegisterInputType(reflect.TypeOf((*IntegrationArrayInput)(nil)).Elem(), IntegrationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IntegrationMapInput)(nil)).Elem(), IntegrationMap{})
	pulumi.RegisterOutputType(IntegrationOutput{})
	pulumi.RegisterOutputType(IntegrationArrayOutput{})
	pulumi.RegisterOutputType(IntegrationMapOutput{})
}
