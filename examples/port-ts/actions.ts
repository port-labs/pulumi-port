import {
    Action
} from '@port-labs/port';


const doSomethingAction = new Action("doSomethingAction", {
    title: "Do Something",
    identifier: "do-something",
    icon: "Terraform",
    description: "This action does something",
    selfServiceTrigger: {
        operation: "DAY-2",
        blueprintIdentifier: "service",
        userProperties: {
            stringProps: {
                myStringIdentifier: {
                    title: "My String Identifier",
                    required: true,
                    format: "entity",
                    blueprint: "githubPullRequest",
                    dataset: {
                        combinator: "and",
                        rules: [{
                            property: "$title",
                            operator: "contains",
                            value: {
                                jqQuery: "\"Bump\"", // filter PRs with title containing "Bump" i.e dependabot PRs
                            },
                        }],
                    },
                },
            },
            numberProps: {
                myNumberIdentifier: {
                    title: "My Number Identifier",
                    required: true,
                    maximum: 100,
                    minimum: 0,
                },
            },
            booleanProps: {
                myBooleanIdentifier: {
                    title: "My Boolean Identifier",
                    required: true,
                },
            },
            objectProps: {
                myObjectIdentifier: {
                    title: "My Object Identifier",
                    required: true,
                },
            },
            arrayProps: {
                myArrayIdentifier: {
                    title: "My Array Identifier",
                    required: true,
                    stringItems: {
                        format: "entity",
                        blueprint: "githubPullRequest",
                        dataset: JSON.stringify({
                            combinator: "and",
                            rules: [{
                                property: "$title",
                                operator: "contains",
                                value: "Bump", // filter PRs with title containing "Bump" i.e dependabot PRs
                            }],
                        }),
                    },
                },
            },
        },
    },
    webhookMethod: {
        url: "https://myserver.app/hook",
        body: JSON.stringify({
            myStringIdentifier: "{{.inputs.myStringIdentifier}}",
            myNumberIdentifier: "{{.inputs.myNumberIdentifier}}",
            myBooleanIdentifier: "{{.inputs.myBooleanIdentifier}}",
            myObjectIdentifier: "{{.inputs.myObjectIdentifier}}",
            myArrayIdentifier: "{{.inputs.myArrayIdentifier}}",
            runId: "{{.run.id}}",
            fullEntity: "{{.entity}}",
            partialEntity: {
                id: "{{.entity.identifier}}",
                type: "{{.entity.title}}",
                url: "{{.entity.properties.url}}",
                defaultBranch: "{{.entity.properties.defaultBranch}}",
                createdAt: "{{.entity.createdAt}}",
            },
            triggeredBy: "{{.trigger.by.user.email}}",
            triggeredAt: "{{.trigger.at}}",
            triggeredFrom: "{{.trigger.origin}}",
            actionType: "{{.trigger.operation}}",
            action: "{{.action}}",
        }),
        headers: {
            runId: "{{.run.id}}",
        },
        method: "POST",
        agent: "false",
        synchronized: "false",
    },
});

export const actions = {
    doSomethingAction,
};
