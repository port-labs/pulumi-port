package main

import (
	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		bp, err := port.NewBlueprint(ctx, "microservice", &port.BlueprintArgs{
			Title:      pulumi.String("Microservice"),
			Identifier: pulumi.String("microservice"),
		})

		entity, err := port.NewEntity(ctx, "entity", &port.EntityArgs{
			Title:     pulumi.String("monolith"),
			Blueprint: bp.Identifier,
			Properties: port.EntityPropertiesArgs{
				StringProps: pulumi.StringMap{
					"language": pulumi.String("Go"),
				},
			},
		})
		ctx.Export("entity", entity.Title)
		if err != nil {
			return err
		}

		_, err = port.NewAction(ctx, "action", &port.ActionArgs{
			Identifier: pulumi.String("my-action"),
			Title:      pulumi.String("My Action"),
			SelfServiceTrigger: port.ActionSelfServiceTriggerArgs{
				Operation:           pulumi.String("CREATE"),
				BlueprintIdentifier: bp.Identifier,
				UserProperties: port.ActionSelfServiceTriggerUserPropertiesArgs{
					StringProps: port.ActionSelfServiceTriggerUserPropertiesStringPropsMap{
						"name": port.ActionSelfServiceTriggerUserPropertiesStringPropsArgs{
							Title:       pulumi.String("Name"),
							Description: pulumi.String("The name of the service"),
							Required:    pulumi.Bool(true),
							MinLength:   pulumi.Int(5),
							MaxLength:   pulumi.Int(100),
							Icon:        pulumi.String("BlankPage"),
						},
					},
				},
			},
			WebhookMethod: port.ActionWebhookMethodArgs{
				Url:    pulumi.String("https://webhook.site/bd277853-07e9-425a-820d-e0ae8d200a1d"),
				Method: pulumi.String("POST"),
				Body:   pulumi.JSONMarshal(map[string]interface{}{"name": "test"}),
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
