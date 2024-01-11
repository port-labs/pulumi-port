// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package port

import (
	_ "embed"
	"fmt"
	"path/filepath"
	"unicode"

	"github.com/port-labs/pulumi-port/provider/pkg/version"
	port "github.com/port-labs/terraform-provider-port-labs/provider"
	portVersion "github.com/port-labs/terraform-provider-port-labs/version"
	pf "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tfbridgetokens "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "port"
	// modules:
	mainMod = "index" // the vultr module
)

//go:embed cmd/pulumi-resource-port/bridge-metadata.json
var metadata []byte

// portMember manufactures a type token for the random package and the given module and type.
func portMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// portType manufactures a type token for the random package and the given module and type.
func portType(mod string, typ string) tokens.Type {
	return tokens.Type(portMember(mod, typ))
}

// fly package and names the file by simply lower casing the resource's first character.
func portResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return portType(mod+"/"+fn, res)
}

// portDataSource manufactures a standard resource token given a module and resource name.  It automatically uses the
// fly package and names the file by simply lower casing the resource's first character.
func portDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return portMember(mod+"/"+fn, res)
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	portVersion.ProviderVersion = "pulumi-provider-port-labs/" + version.Version
	info := tfbridge.ProviderInfo{
		P:                 pf.ShimProvider(port.New()),
		Name:              "port",
		DisplayName:       "Port",
		Publisher:         "port-labs",
		LogoURL:           "",
		PluginDownloadURL: "github://api.github.com/port-labs/pulumi-port",
		Version:           version.Version,
		MetadataInfo:      tfbridge.NewProviderMetadata(metadata),
		Description:       "A Pulumi package for creating and managing Port resources.",
		Keywords:          []string{"pulumi", "port", "category/utility"},
		License:           "Apache-2.0",
		Homepage:          "https://www.pulumi.com",
		Repository:        "https://github.com/port-labs/pulumi-port",
		GitHubOrg:         "port-labs",
		Config:            map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			// "aws_iam_role": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "IamRole")}
			//
			// "aws_acm_certificate": {
			// 	Tok: tfbridge.MakeResource(mainPkg, mainMod, "Certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: tfbridge.MakeType(mainPkg, "Tags")},
			// 	},
			// },
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			// "aws_ami": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getAmi")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@port-labs/port",
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "port_pulumi",
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/port-labs/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "port_labs",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}
	info.MustComputeTokens(tfbridgetokens.SingleModule("port_", mainMod,
		tfbridgetokens.MakeStandard(mainPkg)))

	return info
}
