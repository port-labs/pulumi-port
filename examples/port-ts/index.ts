import * as port from "@port-labs/port";

export const blueprint = new port.Blueprint("microservice", {
    identifier: "microservice",
    title: "Microservice",
    properties: [
        {
            identifier: "language",
            title: "Language",
            type: "string",
            required: false,
        }
    ]
});

export const entity = new port.Entity("monolith", {
    identifier: "monolith",
    title: "monolith",
    blueprint: blueprint.identifier,
    properties: [
        {
            name: "language",
            value: "Node",
        }
    ]
});

