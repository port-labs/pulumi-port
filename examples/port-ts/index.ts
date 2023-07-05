import * as pulumi from "@pulumi/pulumi";
import * as port from "@port-labs/pulumi";

export const blueprint = new port.Blueprint("microservice", {
    identifier: "microservice",
    title: "Microservice",
    properties: [
        {
            identifier: "language",
            title: "Language",
            type: "string",
            required: true,
        }
    ]
});

export const entity = new port.Entity("monolith", {
    identifier: "monolith",
    title: "monolith",
    blueprint: "microservice",
    properties: [
        {
            name: "language",
            value: "Node",
        }
    ]
});

