// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package port

import (
	"context"
	"reflect"

	"github.com/port-labs/pulumi-port/sdk/v2/go/port/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the port-labs package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	BaseUrl pulumi.StringPtrOutput `pulumi:"baseUrl"`
	// Client ID for Port-labs
	ClientId pulumi.StringPtrOutput `pulumi:"clientId"`
	// Client Secret for Port-labs
	Secret pulumi.StringPtrOutput `pulumi:"secret"`
	// Token for Port-labs
	Token pulumi.StringPtrOutput `pulumi:"token"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}

	if args.Secret != nil {
		args.Secret = pulumi.ToSecret(args.Secret).(pulumi.StringPtrInput)
	}
	if args.Token != nil {
		args.Token = pulumi.ToSecret(args.Token).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"secret",
		"token",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:port", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	BaseUrl *string `pulumi:"baseUrl"`
	// Protects you from accidentally changing the property type of blueprints which will delete the property before recreating
	// it with the new type. Defaults to `true`
	BlueprintPropertyTypeChangeProtection *bool `pulumi:"blueprintPropertyTypeChangeProtection"`
	// Client ID for Port-labs
	ClientId *string `pulumi:"clientId"`
	// When set to `false` disables the default HTML escaping of json.Marshal when reading data from Port. Defaults to `true`
	JsonEscapeHtml *bool `pulumi:"jsonEscapeHtml"`
	// Client Secret for Port-labs
	Secret *string `pulumi:"secret"`
	// Token for Port-labs
	Token *string `pulumi:"token"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	BaseUrl pulumi.StringPtrInput
	// Protects you from accidentally changing the property type of blueprints which will delete the property before recreating
	// it with the new type. Defaults to `true`
	BlueprintPropertyTypeChangeProtection pulumi.BoolPtrInput
	// Client ID for Port-labs
	ClientId pulumi.StringPtrInput
	// When set to `false` disables the default HTML escaping of json.Marshal when reading data from Port. Defaults to `true`
	JsonEscapeHtml pulumi.BoolPtrInput
	// Client Secret for Port-labs
	Secret pulumi.StringPtrInput
	// Token for Port-labs
	Token pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

func (o ProviderOutput) BaseUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.BaseUrl }).(pulumi.StringPtrOutput)
}

// Client ID for Port-labs
func (o ProviderOutput) ClientId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ClientId }).(pulumi.StringPtrOutput)
}

// Client Secret for Port-labs
func (o ProviderOutput) Secret() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Secret }).(pulumi.StringPtrOutput)
}

// Token for Port-labs
func (o ProviderOutput) Token() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Token }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
