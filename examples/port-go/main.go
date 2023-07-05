package main

import (
	"github.com/port-labs/pulumi-port/go/port"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		entity, err := port.NewEntity(ctx, "entity", &port.EntityArgs{
			Title:     pulumi.String("monolith"),
			Blueprint: pulumi.String("microservice"),
			Properties: port.EntityPropertyArray{
				&port.EntityPropertyArgs{
					Name:  pulumi.String("language"),
					Value: pulumi.String("GO"),
				},
			},
		})
		ctx.Export("entity", entity.Title)
		if err != nil {
			return err
		}
		return nil
	})
}
