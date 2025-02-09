# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ScorecardArgs', 'Scorecard']

@pulumi.input_type
class ScorecardArgs:
    def __init__(__self__, *,
                 blueprint: pulumi.Input[str],
                 identifier: pulumi.Input[str],
                 rules: pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]],
                 title: pulumi.Input[str],
                 filter: Optional[pulumi.Input['ScorecardFilterArgs']] = None,
                 levels: Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]]] = None):
        """
        The set of arguments for constructing a Scorecard resource.
        :param pulumi.Input[str] blueprint: The blueprint of the scorecard
        :param pulumi.Input[str] identifier: The identifier of the scorecard
        :param pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]] rules: The rules of the scorecard
        :param pulumi.Input[str] title: The title of the scorecard
        :param pulumi.Input['ScorecardFilterArgs'] filter: The filter to apply on the entities before calculating the scorecard
        :param pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]] levels: The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
        """
        pulumi.set(__self__, "blueprint", blueprint)
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "rules", rules)
        pulumi.set(__self__, "title", title)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if levels is not None:
            pulumi.set(__self__, "levels", levels)

    @property
    @pulumi.getter
    def blueprint(self) -> pulumi.Input[str]:
        """
        The blueprint of the scorecard
        """
        return pulumi.get(self, "blueprint")

    @blueprint.setter
    def blueprint(self, value: pulumi.Input[str]):
        pulumi.set(self, "blueprint", value)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        The identifier of the scorecard
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]]:
        """
        The rules of the scorecard
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the scorecard
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['ScorecardFilterArgs']]:
        """
        The filter to apply on the entities before calculating the scorecard
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['ScorecardFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def levels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]]]:
        """
        The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
        """
        return pulumi.get(self, "levels")

    @levels.setter
    def levels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]]]):
        pulumi.set(self, "levels", value)


@pulumi.input_type
class _ScorecardState:
    def __init__(__self__, *,
                 blueprint: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input['ScorecardFilterArgs']] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 levels: Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Scorecard resources.
        :param pulumi.Input[str] blueprint: The blueprint of the scorecard
        :param pulumi.Input[str] created_at: The creation date of the scorecard
        :param pulumi.Input[str] created_by: The creator of the scorecard
        :param pulumi.Input['ScorecardFilterArgs'] filter: The filter to apply on the entities before calculating the scorecard
        :param pulumi.Input[str] identifier: The identifier of the scorecard
        :param pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]] levels: The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
        :param pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]] rules: The rules of the scorecard
        :param pulumi.Input[str] title: The title of the scorecard
        :param pulumi.Input[str] updated_at: The last update date of the scorecard
        :param pulumi.Input[str] updated_by: The last updater of the scorecard
        """
        if blueprint is not None:
            pulumi.set(__self__, "blueprint", blueprint)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if levels is not None:
            pulumi.set(__self__, "levels", levels)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if updated_by is not None:
            pulumi.set(__self__, "updated_by", updated_by)

    @property
    @pulumi.getter
    def blueprint(self) -> Optional[pulumi.Input[str]]:
        """
        The blueprint of the scorecard
        """
        return pulumi.get(self, "blueprint")

    @blueprint.setter
    def blueprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "blueprint", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The creation date of the scorecard
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The creator of the scorecard
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['ScorecardFilterArgs']]:
        """
        The filter to apply on the entities before calculating the scorecard
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['ScorecardFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the scorecard
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def levels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]]]:
        """
        The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
        """
        return pulumi.get(self, "levels")

    @levels.setter
    def levels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardLevelArgs']]]]):
        pulumi.set(self, "levels", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]]]:
        """
        The rules of the scorecard
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScorecardRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the scorecard
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The last update date of the scorecard
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[pulumi.Input[str]]:
        """
        The last updater of the scorecard
        """
        return pulumi.get(self, "updated_by")

    @updated_by.setter
    def updated_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_by", value)


class Scorecard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blueprint: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[Union['ScorecardFilterArgs', 'ScorecardFilterArgsDict']]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 levels: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScorecardLevelArgs', 'ScorecardLevelArgsDict']]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScorecardRuleArgs', 'ScorecardRuleArgsDict']]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to manage a scorecard.

        See the [Port documentation](https://docs.getport.io/promote-scorecards/) for more information about scorecards.

        ## Example Usage

        This will create a blueprint with a Scorecard measuring the readiness of a microservice.

        ```python
        import pulumi
        import json
        import pulumi_port as port

        microservice = port.index.Port_blueprint("microservice",
            title=microservice,
            icon=Terraform,
            identifier=microservice,
            properties={
                stringProps: {
                    author: {
                        title: Author,
                    },
                    url: {
                        title: URL,
                    },
                },
                booleanProps: {
                    required: {
                        type: boolean,
                    },
                },
                numberProps: {
                    sum: {
                        type: number,
                    },
                },
            })
        readiness = port.index.Port_scorecard("readiness",
            identifier=Readiness,
            title=Readiness,
            blueprint=microservice.identifier,
            rules=[
                {
                    identifier: hasOwner,
                    title: Has Owner,
                    level: Gold,
                    query: {
                        combinator: and,
                        conditions: [
                            json.dumps({
                                property: $team,
                                operator: isNotEmpty,
                            }),
                            json.dumps({
                                property: author,
                                operator: =,
                                value: myValue,
                            }),
                        ],
                    },
                },
                {
                    identifier: hasUrl,
                    title: Has URL,
                    level: Silver,
                    query: {
                        combinator: and,
                        conditions: [json.dumps({
                            property: url,
                            operator: isNotEmpty,
                        })],
                    },
                },
                {
                    identifier: checkSumIfRequired,
                    title: Check Sum If Required,
                    level: Bronze,
                    query: {
                        combinator: or,
                        conditions: [
                            json.dumps({
                                property: required,
                                operator: =,
                                value: False,
                            }),
                            json.dumps({
                                property: sum,
                                operator: >,
                                value: 2,
                            }),
                        ],
                    },
                },
            ],
            opts = pulumi.ResourceOptions(depends_on=[microservice]))
        ```

        ### With Levels And Filter

        This will override the default levels (Basic, Bronze, Silver, Gold) with the provided levels: Not Ready, Partially Ready, Ready.

        ```python
        import pulumi
        import json
        import pulumi_port as port

        microservice = port.index.Port_blueprint("microservice",
            title=microservice,
            icon=Terraform,
            identifier=microservice,
            properties={
                stringProps: {
                    author: {
                        title: Author,
                    },
                    url: {
                        title: URL,
                    },
                },
                booleanProps: {
                    required: {
                        type: boolean,
                    },
                },
                numberProps: {
                    sum: {
                        type: number,
                    },
                },
            })
        readiness = port.index.Port_scorecard("readiness",
            identifier=Readiness,
            title=Readiness,
            blueprint=microservice.identifier,
            filter={
                combinator: and,
                conditions: [json.dumps({
                    property: sum,
                    operator: >,
                    value: 0,
                })],
            },
            levels=[
                {
                    color: red,
                    title: No Ready,
                },
                {
                    color: yellow,
                    title: Partially Ready,
                },
                {
                    color: green,
                    title: Ready,
                },
            ],
            rules=[
                {
                    identifier: hasOwner,
                    title: Has Owner,
                    level: Ready,
                    query: {
                        combinator: and,
                        conditions: [
                            json.dumps({
                                property: $team,
                                operator: isNotEmpty,
                            }),
                            json.dumps({
                                property: author,
                                operator: =,
                                value: myValue,
                            }),
                        ],
                    },
                },
                {
                    identifier: hasUrl,
                    title: Has URL,
                    level: Partially Ready,
                    query: {
                        combinator: and,
                        conditions: [json.dumps({
                            property: url,
                            operator: isNotEmpty,
                        })],
                    },
                },
                {
                    identifier: checkSumIfRequired,
                    title: Check Sum If Required,
                    level: Partially Ready,
                    query: {
                        combinator: or,
                        conditions: [
                            json.dumps({
                                property: required,
                                operator: =,
                                value: False,
                            }),
                            json.dumps({
                                property: sum,
                                operator: >,
                                value: 2,
                            }),
                        ],
                    },
                },
            ],
            opts = pulumi.ResourceOptions(depends_on=[microservice]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] blueprint: The blueprint of the scorecard
        :param pulumi.Input[Union['ScorecardFilterArgs', 'ScorecardFilterArgsDict']] filter: The filter to apply on the entities before calculating the scorecard
        :param pulumi.Input[str] identifier: The identifier of the scorecard
        :param pulumi.Input[Sequence[pulumi.Input[Union['ScorecardLevelArgs', 'ScorecardLevelArgsDict']]]] levels: The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
        :param pulumi.Input[Sequence[pulumi.Input[Union['ScorecardRuleArgs', 'ScorecardRuleArgsDict']]]] rules: The rules of the scorecard
        :param pulumi.Input[str] title: The title of the scorecard
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScorecardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to manage a scorecard.

        See the [Port documentation](https://docs.getport.io/promote-scorecards/) for more information about scorecards.

        ## Example Usage

        This will create a blueprint with a Scorecard measuring the readiness of a microservice.

        ```python
        import pulumi
        import json
        import pulumi_port as port

        microservice = port.index.Port_blueprint("microservice",
            title=microservice,
            icon=Terraform,
            identifier=microservice,
            properties={
                stringProps: {
                    author: {
                        title: Author,
                    },
                    url: {
                        title: URL,
                    },
                },
                booleanProps: {
                    required: {
                        type: boolean,
                    },
                },
                numberProps: {
                    sum: {
                        type: number,
                    },
                },
            })
        readiness = port.index.Port_scorecard("readiness",
            identifier=Readiness,
            title=Readiness,
            blueprint=microservice.identifier,
            rules=[
                {
                    identifier: hasOwner,
                    title: Has Owner,
                    level: Gold,
                    query: {
                        combinator: and,
                        conditions: [
                            json.dumps({
                                property: $team,
                                operator: isNotEmpty,
                            }),
                            json.dumps({
                                property: author,
                                operator: =,
                                value: myValue,
                            }),
                        ],
                    },
                },
                {
                    identifier: hasUrl,
                    title: Has URL,
                    level: Silver,
                    query: {
                        combinator: and,
                        conditions: [json.dumps({
                            property: url,
                            operator: isNotEmpty,
                        })],
                    },
                },
                {
                    identifier: checkSumIfRequired,
                    title: Check Sum If Required,
                    level: Bronze,
                    query: {
                        combinator: or,
                        conditions: [
                            json.dumps({
                                property: required,
                                operator: =,
                                value: False,
                            }),
                            json.dumps({
                                property: sum,
                                operator: >,
                                value: 2,
                            }),
                        ],
                    },
                },
            ],
            opts = pulumi.ResourceOptions(depends_on=[microservice]))
        ```

        ### With Levels And Filter

        This will override the default levels (Basic, Bronze, Silver, Gold) with the provided levels: Not Ready, Partially Ready, Ready.

        ```python
        import pulumi
        import json
        import pulumi_port as port

        microservice = port.index.Port_blueprint("microservice",
            title=microservice,
            icon=Terraform,
            identifier=microservice,
            properties={
                stringProps: {
                    author: {
                        title: Author,
                    },
                    url: {
                        title: URL,
                    },
                },
                booleanProps: {
                    required: {
                        type: boolean,
                    },
                },
                numberProps: {
                    sum: {
                        type: number,
                    },
                },
            })
        readiness = port.index.Port_scorecard("readiness",
            identifier=Readiness,
            title=Readiness,
            blueprint=microservice.identifier,
            filter={
                combinator: and,
                conditions: [json.dumps({
                    property: sum,
                    operator: >,
                    value: 0,
                })],
            },
            levels=[
                {
                    color: red,
                    title: No Ready,
                },
                {
                    color: yellow,
                    title: Partially Ready,
                },
                {
                    color: green,
                    title: Ready,
                },
            ],
            rules=[
                {
                    identifier: hasOwner,
                    title: Has Owner,
                    level: Ready,
                    query: {
                        combinator: and,
                        conditions: [
                            json.dumps({
                                property: $team,
                                operator: isNotEmpty,
                            }),
                            json.dumps({
                                property: author,
                                operator: =,
                                value: myValue,
                            }),
                        ],
                    },
                },
                {
                    identifier: hasUrl,
                    title: Has URL,
                    level: Partially Ready,
                    query: {
                        combinator: and,
                        conditions: [json.dumps({
                            property: url,
                            operator: isNotEmpty,
                        })],
                    },
                },
                {
                    identifier: checkSumIfRequired,
                    title: Check Sum If Required,
                    level: Partially Ready,
                    query: {
                        combinator: or,
                        conditions: [
                            json.dumps({
                                property: required,
                                operator: =,
                                value: False,
                            }),
                            json.dumps({
                                property: sum,
                                operator: >,
                                value: 2,
                            }),
                        ],
                    },
                },
            ],
            opts = pulumi.ResourceOptions(depends_on=[microservice]))
        ```

        :param str resource_name: The name of the resource.
        :param ScorecardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScorecardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blueprint: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[Union['ScorecardFilterArgs', 'ScorecardFilterArgsDict']]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 levels: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScorecardLevelArgs', 'ScorecardLevelArgsDict']]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScorecardRuleArgs', 'ScorecardRuleArgsDict']]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScorecardArgs.__new__(ScorecardArgs)

            if blueprint is None and not opts.urn:
                raise TypeError("Missing required property 'blueprint'")
            __props__.__dict__["blueprint"] = blueprint
            __props__.__dict__["filter"] = filter
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["levels"] = levels
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["created_at"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["updated_at"] = None
            __props__.__dict__["updated_by"] = None
        super(Scorecard, __self__).__init__(
            'port:index/scorecard:Scorecard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            blueprint: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            filter: Optional[pulumi.Input[Union['ScorecardFilterArgs', 'ScorecardFilterArgsDict']]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            levels: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScorecardLevelArgs', 'ScorecardLevelArgsDict']]]]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScorecardRuleArgs', 'ScorecardRuleArgsDict']]]]] = None,
            title: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            updated_by: Optional[pulumi.Input[str]] = None) -> 'Scorecard':
        """
        Get an existing Scorecard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] blueprint: The blueprint of the scorecard
        :param pulumi.Input[str] created_at: The creation date of the scorecard
        :param pulumi.Input[str] created_by: The creator of the scorecard
        :param pulumi.Input[Union['ScorecardFilterArgs', 'ScorecardFilterArgsDict']] filter: The filter to apply on the entities before calculating the scorecard
        :param pulumi.Input[str] identifier: The identifier of the scorecard
        :param pulumi.Input[Sequence[pulumi.Input[Union['ScorecardLevelArgs', 'ScorecardLevelArgsDict']]]] levels: The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
        :param pulumi.Input[Sequence[pulumi.Input[Union['ScorecardRuleArgs', 'ScorecardRuleArgsDict']]]] rules: The rules of the scorecard
        :param pulumi.Input[str] title: The title of the scorecard
        :param pulumi.Input[str] updated_at: The last update date of the scorecard
        :param pulumi.Input[str] updated_by: The last updater of the scorecard
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScorecardState.__new__(_ScorecardState)

        __props__.__dict__["blueprint"] = blueprint
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["filter"] = filter
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["levels"] = levels
        __props__.__dict__["rules"] = rules
        __props__.__dict__["title"] = title
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["updated_by"] = updated_by
        return Scorecard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def blueprint(self) -> pulumi.Output[str]:
        """
        The blueprint of the scorecard
        """
        return pulumi.get(self, "blueprint")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The creation date of the scorecard
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        The creator of the scorecard
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional['outputs.ScorecardFilter']]:
        """
        The filter to apply on the entities before calculating the scorecard
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        The identifier of the scorecard
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def levels(self) -> pulumi.Output[Optional[Sequence['outputs.ScorecardLevel']]]:
        """
        The levels of the scorecard. This overrides the default levels (Basic, Bronze, Silver, Gold) if provided
        """
        return pulumi.get(self, "levels")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.ScorecardRule']]:
        """
        The rules of the scorecard
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the scorecard
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The last update date of the scorecard
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[str]:
        """
        The last updater of the scorecard
        """
        return pulumi.get(self, "updated_by")

