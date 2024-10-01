import * as port from "@port-labs/port";

export const blueprint = new port.Blueprint("microservice", {
    identifier: "microservice",
    title: "Microservice",
    properties: {
        stringProps: {
            "language": {
                default: "Go",
            }
        }
    }
});

export const entity = new port.Entity("monolith", {
    identifier: "monolith",
    title: "monolith",
    blueprint: blueprint.identifier,
    properties: {
        stringProps: {
            "language": "Node",
        }
    }
});

