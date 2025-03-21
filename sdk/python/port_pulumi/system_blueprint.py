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

__all__ = ['SystemBlueprintArgs', 'SystemBlueprint']

@pulumi.input_type
class SystemBlueprintArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str],
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]]] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]]] = None,
                 properties: Optional[pulumi.Input['SystemBlueprintPropertiesArgs']] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]]] = None):
        """
        The set of arguments for constructing a SystemBlueprint resource.
        :param pulumi.Input[str] identifier: Identifier of the system blueprint.
        :param pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input['SystemBlueprintPropertiesArgs'] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]] relations: The relations of the blueprint
        """
        pulumi.set(__self__, "identifier", identifier)
        if calculation_properties is not None:
            pulumi.set(__self__, "calculation_properties", calculation_properties)
        if mirror_properties is not None:
            pulumi.set(__self__, "mirror_properties", mirror_properties)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if relations is not None:
            pulumi.set(__self__, "relations", relations)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        Identifier of the system blueprint.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="calculationProperties")
    def calculation_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]]]:
        """
        The calculation properties of the blueprint
        """
        return pulumi.get(self, "calculation_properties")

    @calculation_properties.setter
    def calculation_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]]]):
        pulumi.set(self, "calculation_properties", value)

    @property
    @pulumi.getter(name="mirrorProperties")
    def mirror_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]]]:
        """
        The mirror properties of the blueprint
        """
        return pulumi.get(self, "mirror_properties")

    @mirror_properties.setter
    def mirror_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]]]):
        pulumi.set(self, "mirror_properties", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['SystemBlueprintPropertiesArgs']]:
        """
        The properties of the blueprint
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['SystemBlueprintPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def relations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]]]:
        """
        The relations of the blueprint
        """
        return pulumi.get(self, "relations")

    @relations.setter
    def relations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]]]):
        pulumi.set(self, "relations", value)


@pulumi.input_type
class _SystemBlueprintState:
    def __init__(__self__, *,
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]]] = None,
                 properties: Optional[pulumi.Input['SystemBlueprintPropertiesArgs']] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]]] = None):
        """
        Input properties used for looking up and filtering SystemBlueprint resources.
        :param pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[str] identifier: Identifier of the system blueprint.
        :param pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input['SystemBlueprintPropertiesArgs'] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]] relations: The relations of the blueprint
        """
        if calculation_properties is not None:
            pulumi.set(__self__, "calculation_properties", calculation_properties)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if mirror_properties is not None:
            pulumi.set(__self__, "mirror_properties", mirror_properties)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if relations is not None:
            pulumi.set(__self__, "relations", relations)

    @property
    @pulumi.getter(name="calculationProperties")
    def calculation_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]]]:
        """
        The calculation properties of the blueprint
        """
        return pulumi.get(self, "calculation_properties")

    @calculation_properties.setter
    def calculation_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintCalculationPropertiesArgs']]]]):
        pulumi.set(self, "calculation_properties", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the system blueprint.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="mirrorProperties")
    def mirror_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]]]:
        """
        The mirror properties of the blueprint
        """
        return pulumi.get(self, "mirror_properties")

    @mirror_properties.setter
    def mirror_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintMirrorPropertiesArgs']]]]):
        pulumi.set(self, "mirror_properties", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['SystemBlueprintPropertiesArgs']]:
        """
        The properties of the blueprint
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['SystemBlueprintPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def relations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]]]:
        """
        The relations of the blueprint
        """
        return pulumi.get(self, "relations")

    @relations.setter
    def relations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SystemBlueprintRelationsArgs']]]]):
        pulumi.set(self, "relations", value)


class SystemBlueprint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintCalculationPropertiesArgs', 'SystemBlueprintCalculationPropertiesArgsDict']]]]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintMirrorPropertiesArgs', 'SystemBlueprintMirrorPropertiesArgsDict']]]]] = None,
                 properties: Optional[pulumi.Input[Union['SystemBlueprintPropertiesArgs', 'SystemBlueprintPropertiesArgsDict']]] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintRelationsArgs', 'SystemBlueprintRelationsArgsDict']]]]] = None,
                 __props__=None):
        """
        Port System Blueprint Resource. This resource is used to extend system blueprints with additional properties and relations.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintCalculationPropertiesArgs', 'SystemBlueprintCalculationPropertiesArgsDict']]]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[str] identifier: Identifier of the system blueprint.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintMirrorPropertiesArgs', 'SystemBlueprintMirrorPropertiesArgsDict']]]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input[Union['SystemBlueprintPropertiesArgs', 'SystemBlueprintPropertiesArgsDict']] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintRelationsArgs', 'SystemBlueprintRelationsArgsDict']]]] relations: The relations of the blueprint
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SystemBlueprintArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Port System Blueprint Resource. This resource is used to extend system blueprints with additional properties and relations.

        :param str resource_name: The name of the resource.
        :param SystemBlueprintArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SystemBlueprintArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintCalculationPropertiesArgs', 'SystemBlueprintCalculationPropertiesArgsDict']]]]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintMirrorPropertiesArgs', 'SystemBlueprintMirrorPropertiesArgsDict']]]]] = None,
                 properties: Optional[pulumi.Input[Union['SystemBlueprintPropertiesArgs', 'SystemBlueprintPropertiesArgsDict']]] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintRelationsArgs', 'SystemBlueprintRelationsArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SystemBlueprintArgs.__new__(SystemBlueprintArgs)

            __props__.__dict__["calculation_properties"] = calculation_properties
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["mirror_properties"] = mirror_properties
            __props__.__dict__["properties"] = properties
            __props__.__dict__["relations"] = relations
        super(SystemBlueprint, __self__).__init__(
            'port:index/systemBlueprint:SystemBlueprint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintCalculationPropertiesArgs', 'SystemBlueprintCalculationPropertiesArgsDict']]]]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintMirrorPropertiesArgs', 'SystemBlueprintMirrorPropertiesArgsDict']]]]] = None,
            properties: Optional[pulumi.Input[Union['SystemBlueprintPropertiesArgs', 'SystemBlueprintPropertiesArgsDict']]] = None,
            relations: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintRelationsArgs', 'SystemBlueprintRelationsArgsDict']]]]] = None) -> 'SystemBlueprint':
        """
        Get an existing SystemBlueprint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintCalculationPropertiesArgs', 'SystemBlueprintCalculationPropertiesArgsDict']]]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[str] identifier: Identifier of the system blueprint.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintMirrorPropertiesArgs', 'SystemBlueprintMirrorPropertiesArgsDict']]]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input[Union['SystemBlueprintPropertiesArgs', 'SystemBlueprintPropertiesArgsDict']] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['SystemBlueprintRelationsArgs', 'SystemBlueprintRelationsArgsDict']]]] relations: The relations of the blueprint
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SystemBlueprintState.__new__(_SystemBlueprintState)

        __props__.__dict__["calculation_properties"] = calculation_properties
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["mirror_properties"] = mirror_properties
        __props__.__dict__["properties"] = properties
        __props__.__dict__["relations"] = relations
        return SystemBlueprint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="calculationProperties")
    def calculation_properties(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.SystemBlueprintCalculationProperties']]]:
        """
        The calculation properties of the blueprint
        """
        return pulumi.get(self, "calculation_properties")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        Identifier of the system blueprint.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter(name="mirrorProperties")
    def mirror_properties(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.SystemBlueprintMirrorProperties']]]:
        """
        The mirror properties of the blueprint
        """
        return pulumi.get(self, "mirror_properties")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional['outputs.SystemBlueprintProperties']]:
        """
        The properties of the blueprint
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def relations(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.SystemBlueprintRelations']]]:
        """
        The relations of the blueprint
        """
        return pulumi.get(self, "relations")

