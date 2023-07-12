"use strict";
const pulumi = require("@pulumi/pulumi");
const port = require("@port-labs/port");

const entity = new port.Entity("entity", {
    identifier: "monolith",
    title: "monolith",
    blueprint: "microservice",
    properties: {
        stringProps: {
            "language": "typescript",
        }
    }
});

exports.title = entity.title;
