"use strict";
const pulumi = require("@pulumi/pulumi");
const port = require("@port-labs/pulumi");

const entity = new port.Entity("entity", {
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

exports.title = entity.title;
