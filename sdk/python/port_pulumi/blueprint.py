# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['BlueprintArgs', 'Blueprint']

@pulumi.input_type
class BlueprintArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str],
                 title: pulumi.Input[str],
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]]] = None,
                 create_catalog_page: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 force_delete_entities: Optional[pulumi.Input[bool]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input['BlueprintKafkaChangelogDestinationArgs']] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]]] = None,
                 properties: Optional[pulumi.Input['BlueprintPropertiesArgs']] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]]] = None,
                 team_inheritance: Optional[pulumi.Input['BlueprintTeamInheritanceArgs']] = None,
                 webhook_changelog_destination: Optional[pulumi.Input['BlueprintWebhookChangelogDestinationArgs']] = None):
        """
        The set of arguments for constructing a Blueprint resource.
        :param pulumi.Input[str] identifier: The identifier of the blueprint
        :param pulumi.Input[str] title: The display name of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[bool] create_catalog_page: This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
        :param pulumi.Input[str] description: The description of the blueprint
        :param pulumi.Input[str] icon: The icon of the blueprint
        :param pulumi.Input['BlueprintKafkaChangelogDestinationArgs'] kafka_changelog_destination: The changelog destination of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input['BlueprintPropertiesArgs'] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]] relations: The relations of the blueprint
        :param pulumi.Input['BlueprintTeamInheritanceArgs'] team_inheritance: The team inheritance of the blueprint
        :param pulumi.Input['BlueprintWebhookChangelogDestinationArgs'] webhook_changelog_destination: The webhook changelog destination of the blueprint
        """
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "title", title)
        if calculation_properties is not None:
            pulumi.set(__self__, "calculation_properties", calculation_properties)
        if create_catalog_page is not None:
            pulumi.set(__self__, "create_catalog_page", create_catalog_page)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if force_delete_entities is not None:
            pulumi.set(__self__, "force_delete_entities", force_delete_entities)
        if icon is not None:
            pulumi.set(__self__, "icon", icon)
        if kafka_changelog_destination is not None:
            pulumi.set(__self__, "kafka_changelog_destination", kafka_changelog_destination)
        if mirror_properties is not None:
            pulumi.set(__self__, "mirror_properties", mirror_properties)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if relations is not None:
            pulumi.set(__self__, "relations", relations)
        if team_inheritance is not None:
            pulumi.set(__self__, "team_inheritance", team_inheritance)
        if webhook_changelog_destination is not None:
            pulumi.set(__self__, "webhook_changelog_destination", webhook_changelog_destination)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        The identifier of the blueprint
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The display name of the blueprint
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="calculationProperties")
    def calculation_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]]]:
        """
        The calculation properties of the blueprint
        """
        return pulumi.get(self, "calculation_properties")

    @calculation_properties.setter
    def calculation_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]]]):
        pulumi.set(self, "calculation_properties", value)

    @property
    @pulumi.getter(name="createCatalogPage")
    def create_catalog_page(self) -> Optional[pulumi.Input[bool]]:
        """
        This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
        """
        return pulumi.get(self, "create_catalog_page")

    @create_catalog_page.setter
    def create_catalog_page(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_catalog_page", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the blueprint
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="forceDeleteEntities")
    def force_delete_entities(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force_delete_entities")

    @force_delete_entities.setter
    def force_delete_entities(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_delete_entities", value)

    @property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[str]]:
        """
        The icon of the blueprint
        """
        return pulumi.get(self, "icon")

    @icon.setter
    def icon(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon", value)

    @property
    @pulumi.getter(name="kafkaChangelogDestination")
    def kafka_changelog_destination(self) -> Optional[pulumi.Input['BlueprintKafkaChangelogDestinationArgs']]:
        """
        The changelog destination of the blueprint
        """
        return pulumi.get(self, "kafka_changelog_destination")

    @kafka_changelog_destination.setter
    def kafka_changelog_destination(self, value: Optional[pulumi.Input['BlueprintKafkaChangelogDestinationArgs']]):
        pulumi.set(self, "kafka_changelog_destination", value)

    @property
    @pulumi.getter(name="mirrorProperties")
    def mirror_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]]]:
        """
        The mirror properties of the blueprint
        """
        return pulumi.get(self, "mirror_properties")

    @mirror_properties.setter
    def mirror_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]]]):
        pulumi.set(self, "mirror_properties", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['BlueprintPropertiesArgs']]:
        """
        The properties of the blueprint
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['BlueprintPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def relations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]]]:
        """
        The relations of the blueprint
        """
        return pulumi.get(self, "relations")

    @relations.setter
    def relations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]]]):
        pulumi.set(self, "relations", value)

    @property
    @pulumi.getter(name="teamInheritance")
    def team_inheritance(self) -> Optional[pulumi.Input['BlueprintTeamInheritanceArgs']]:
        """
        The team inheritance of the blueprint
        """
        return pulumi.get(self, "team_inheritance")

    @team_inheritance.setter
    def team_inheritance(self, value: Optional[pulumi.Input['BlueprintTeamInheritanceArgs']]):
        pulumi.set(self, "team_inheritance", value)

    @property
    @pulumi.getter(name="webhookChangelogDestination")
    def webhook_changelog_destination(self) -> Optional[pulumi.Input['BlueprintWebhookChangelogDestinationArgs']]:
        """
        The webhook changelog destination of the blueprint
        """
        return pulumi.get(self, "webhook_changelog_destination")

    @webhook_changelog_destination.setter
    def webhook_changelog_destination(self, value: Optional[pulumi.Input['BlueprintWebhookChangelogDestinationArgs']]):
        pulumi.set(self, "webhook_changelog_destination", value)


@pulumi.input_type
class _BlueprintState:
    def __init__(__self__, *,
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]]] = None,
                 create_catalog_page: Optional[pulumi.Input[bool]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 force_delete_entities: Optional[pulumi.Input[bool]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input['BlueprintKafkaChangelogDestinationArgs']] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]]] = None,
                 properties: Optional[pulumi.Input['BlueprintPropertiesArgs']] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]]] = None,
                 team_inheritance: Optional[pulumi.Input['BlueprintTeamInheritanceArgs']] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input[str]] = None,
                 webhook_changelog_destination: Optional[pulumi.Input['BlueprintWebhookChangelogDestinationArgs']] = None):
        """
        Input properties used for looking up and filtering Blueprint resources.
        :param pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[bool] create_catalog_page: This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
        :param pulumi.Input[str] created_at: The creation date of the blueprint
        :param pulumi.Input[str] created_by: The creator of the blueprint
        :param pulumi.Input[str] description: The description of the blueprint
        :param pulumi.Input[str] icon: The icon of the blueprint
        :param pulumi.Input[str] identifier: The identifier of the blueprint
        :param pulumi.Input['BlueprintKafkaChangelogDestinationArgs'] kafka_changelog_destination: The changelog destination of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input['BlueprintPropertiesArgs'] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]] relations: The relations of the blueprint
        :param pulumi.Input['BlueprintTeamInheritanceArgs'] team_inheritance: The team inheritance of the blueprint
        :param pulumi.Input[str] title: The display name of the blueprint
        :param pulumi.Input[str] updated_at: The last update date of the blueprint
        :param pulumi.Input[str] updated_by: The last updater of the blueprint
        :param pulumi.Input['BlueprintWebhookChangelogDestinationArgs'] webhook_changelog_destination: The webhook changelog destination of the blueprint
        """
        if calculation_properties is not None:
            pulumi.set(__self__, "calculation_properties", calculation_properties)
        if create_catalog_page is not None:
            pulumi.set(__self__, "create_catalog_page", create_catalog_page)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if force_delete_entities is not None:
            pulumi.set(__self__, "force_delete_entities", force_delete_entities)
        if icon is not None:
            pulumi.set(__self__, "icon", icon)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if kafka_changelog_destination is not None:
            pulumi.set(__self__, "kafka_changelog_destination", kafka_changelog_destination)
        if mirror_properties is not None:
            pulumi.set(__self__, "mirror_properties", mirror_properties)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if relations is not None:
            pulumi.set(__self__, "relations", relations)
        if team_inheritance is not None:
            pulumi.set(__self__, "team_inheritance", team_inheritance)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if updated_by is not None:
            pulumi.set(__self__, "updated_by", updated_by)
        if webhook_changelog_destination is not None:
            pulumi.set(__self__, "webhook_changelog_destination", webhook_changelog_destination)

    @property
    @pulumi.getter(name="calculationProperties")
    def calculation_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]]]:
        """
        The calculation properties of the blueprint
        """
        return pulumi.get(self, "calculation_properties")

    @calculation_properties.setter
    def calculation_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintCalculationPropertiesArgs']]]]):
        pulumi.set(self, "calculation_properties", value)

    @property
    @pulumi.getter(name="createCatalogPage")
    def create_catalog_page(self) -> Optional[pulumi.Input[bool]]:
        """
        This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
        """
        return pulumi.get(self, "create_catalog_page")

    @create_catalog_page.setter
    def create_catalog_page(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_catalog_page", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The creation date of the blueprint
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The creator of the blueprint
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the blueprint
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="forceDeleteEntities")
    def force_delete_entities(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "force_delete_entities")

    @force_delete_entities.setter
    def force_delete_entities(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_delete_entities", value)

    @property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[str]]:
        """
        The icon of the blueprint
        """
        return pulumi.get(self, "icon")

    @icon.setter
    def icon(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the blueprint
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="kafkaChangelogDestination")
    def kafka_changelog_destination(self) -> Optional[pulumi.Input['BlueprintKafkaChangelogDestinationArgs']]:
        """
        The changelog destination of the blueprint
        """
        return pulumi.get(self, "kafka_changelog_destination")

    @kafka_changelog_destination.setter
    def kafka_changelog_destination(self, value: Optional[pulumi.Input['BlueprintKafkaChangelogDestinationArgs']]):
        pulumi.set(self, "kafka_changelog_destination", value)

    @property
    @pulumi.getter(name="mirrorProperties")
    def mirror_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]]]:
        """
        The mirror properties of the blueprint
        """
        return pulumi.get(self, "mirror_properties")

    @mirror_properties.setter
    def mirror_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintMirrorPropertiesArgs']]]]):
        pulumi.set(self, "mirror_properties", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['BlueprintPropertiesArgs']]:
        """
        The properties of the blueprint
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['BlueprintPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def relations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]]]:
        """
        The relations of the blueprint
        """
        return pulumi.get(self, "relations")

    @relations.setter
    def relations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['BlueprintRelationsArgs']]]]):
        pulumi.set(self, "relations", value)

    @property
    @pulumi.getter(name="teamInheritance")
    def team_inheritance(self) -> Optional[pulumi.Input['BlueprintTeamInheritanceArgs']]:
        """
        The team inheritance of the blueprint
        """
        return pulumi.get(self, "team_inheritance")

    @team_inheritance.setter
    def team_inheritance(self, value: Optional[pulumi.Input['BlueprintTeamInheritanceArgs']]):
        pulumi.set(self, "team_inheritance", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the blueprint
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The last update date of the blueprint
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[pulumi.Input[str]]:
        """
        The last updater of the blueprint
        """
        return pulumi.get(self, "updated_by")

    @updated_by.setter
    def updated_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_by", value)

    @property
    @pulumi.getter(name="webhookChangelogDestination")
    def webhook_changelog_destination(self) -> Optional[pulumi.Input['BlueprintWebhookChangelogDestinationArgs']]:
        """
        The webhook changelog destination of the blueprint
        """
        return pulumi.get(self, "webhook_changelog_destination")

    @webhook_changelog_destination.setter
    def webhook_changelog_destination(self, value: Optional[pulumi.Input['BlueprintWebhookChangelogDestinationArgs']]):
        pulumi.set(self, "webhook_changelog_destination", value)


class Blueprint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintCalculationPropertiesArgs']]]]] = None,
                 create_catalog_page: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 force_delete_entities: Optional[pulumi.Input[bool]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input[pulumi.InputType['BlueprintKafkaChangelogDestinationArgs']]] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintMirrorPropertiesArgs']]]]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['BlueprintPropertiesArgs']]] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintRelationsArgs']]]]] = None,
                 team_inheritance: Optional[pulumi.Input[pulumi.InputType['BlueprintTeamInheritanceArgs']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 webhook_changelog_destination: Optional[pulumi.Input[pulumi.InputType['BlueprintWebhookChangelogDestinationArgs']]] = None,
                 __props__=None):
        """
        Create a Blueprint resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintCalculationPropertiesArgs']]]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[bool] create_catalog_page: This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
        :param pulumi.Input[str] description: The description of the blueprint
        :param pulumi.Input[str] icon: The icon of the blueprint
        :param pulumi.Input[str] identifier: The identifier of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintKafkaChangelogDestinationArgs']] kafka_changelog_destination: The changelog destination of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintMirrorPropertiesArgs']]]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintPropertiesArgs']] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintRelationsArgs']]]] relations: The relations of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintTeamInheritanceArgs']] team_inheritance: The team inheritance of the blueprint
        :param pulumi.Input[str] title: The display name of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintWebhookChangelogDestinationArgs']] webhook_changelog_destination: The webhook changelog destination of the blueprint
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BlueprintArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Blueprint resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BlueprintArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BlueprintArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintCalculationPropertiesArgs']]]]] = None,
                 create_catalog_page: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 force_delete_entities: Optional[pulumi.Input[bool]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input[pulumi.InputType['BlueprintKafkaChangelogDestinationArgs']]] = None,
                 mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintMirrorPropertiesArgs']]]]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['BlueprintPropertiesArgs']]] = None,
                 relations: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintRelationsArgs']]]]] = None,
                 team_inheritance: Optional[pulumi.Input[pulumi.InputType['BlueprintTeamInheritanceArgs']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 webhook_changelog_destination: Optional[pulumi.Input[pulumi.InputType['BlueprintWebhookChangelogDestinationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BlueprintArgs.__new__(BlueprintArgs)

            __props__.__dict__["calculation_properties"] = calculation_properties
            __props__.__dict__["create_catalog_page"] = create_catalog_page
            __props__.__dict__["description"] = description
            __props__.__dict__["force_delete_entities"] = force_delete_entities
            __props__.__dict__["icon"] = icon
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["kafka_changelog_destination"] = kafka_changelog_destination
            __props__.__dict__["mirror_properties"] = mirror_properties
            __props__.__dict__["properties"] = properties
            __props__.__dict__["relations"] = relations
            __props__.__dict__["team_inheritance"] = team_inheritance
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["webhook_changelog_destination"] = webhook_changelog_destination
            __props__.__dict__["created_at"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["updated_at"] = None
            __props__.__dict__["updated_by"] = None
        super(Blueprint, __self__).__init__(
            'port:index/blueprint:Blueprint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            calculation_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintCalculationPropertiesArgs']]]]] = None,
            create_catalog_page: Optional[pulumi.Input[bool]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            force_delete_entities: Optional[pulumi.Input[bool]] = None,
            icon: Optional[pulumi.Input[str]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            kafka_changelog_destination: Optional[pulumi.Input[pulumi.InputType['BlueprintKafkaChangelogDestinationArgs']]] = None,
            mirror_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintMirrorPropertiesArgs']]]]] = None,
            properties: Optional[pulumi.Input[pulumi.InputType['BlueprintPropertiesArgs']]] = None,
            relations: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintRelationsArgs']]]]] = None,
            team_inheritance: Optional[pulumi.Input[pulumi.InputType['BlueprintTeamInheritanceArgs']]] = None,
            title: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            updated_by: Optional[pulumi.Input[str]] = None,
            webhook_changelog_destination: Optional[pulumi.Input[pulumi.InputType['BlueprintWebhookChangelogDestinationArgs']]] = None) -> 'Blueprint':
        """
        Get an existing Blueprint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintCalculationPropertiesArgs']]]] calculation_properties: The calculation properties of the blueprint
        :param pulumi.Input[bool] create_catalog_page: This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
        :param pulumi.Input[str] created_at: The creation date of the blueprint
        :param pulumi.Input[str] created_by: The creator of the blueprint
        :param pulumi.Input[str] description: The description of the blueprint
        :param pulumi.Input[str] icon: The icon of the blueprint
        :param pulumi.Input[str] identifier: The identifier of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintKafkaChangelogDestinationArgs']] kafka_changelog_destination: The changelog destination of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintMirrorPropertiesArgs']]]] mirror_properties: The mirror properties of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintPropertiesArgs']] properties: The properties of the blueprint
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['BlueprintRelationsArgs']]]] relations: The relations of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintTeamInheritanceArgs']] team_inheritance: The team inheritance of the blueprint
        :param pulumi.Input[str] title: The display name of the blueprint
        :param pulumi.Input[str] updated_at: The last update date of the blueprint
        :param pulumi.Input[str] updated_by: The last updater of the blueprint
        :param pulumi.Input[pulumi.InputType['BlueprintWebhookChangelogDestinationArgs']] webhook_changelog_destination: The webhook changelog destination of the blueprint
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BlueprintState.__new__(_BlueprintState)

        __props__.__dict__["calculation_properties"] = calculation_properties
        __props__.__dict__["create_catalog_page"] = create_catalog_page
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["description"] = description
        __props__.__dict__["force_delete_entities"] = force_delete_entities
        __props__.__dict__["icon"] = icon
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["kafka_changelog_destination"] = kafka_changelog_destination
        __props__.__dict__["mirror_properties"] = mirror_properties
        __props__.__dict__["properties"] = properties
        __props__.__dict__["relations"] = relations
        __props__.__dict__["team_inheritance"] = team_inheritance
        __props__.__dict__["title"] = title
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["updated_by"] = updated_by
        __props__.__dict__["webhook_changelog_destination"] = webhook_changelog_destination
        return Blueprint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="calculationProperties")
    def calculation_properties(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.BlueprintCalculationProperties']]]:
        """
        The calculation properties of the blueprint
        """
        return pulumi.get(self, "calculation_properties")

    @property
    @pulumi.getter(name="createCatalogPage")
    def create_catalog_page(self) -> pulumi.Output[bool]:
        """
        This flag is only relevant for blueprint creation, by default if not set, a catalog page will be created for the blueprint
        """
        return pulumi.get(self, "create_catalog_page")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The creation date of the blueprint
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        The creator of the blueprint
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the blueprint
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="forceDeleteEntities")
    def force_delete_entities(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "force_delete_entities")

    @property
    @pulumi.getter
    def icon(self) -> pulumi.Output[Optional[str]]:
        """
        The icon of the blueprint
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        The identifier of the blueprint
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter(name="kafkaChangelogDestination")
    def kafka_changelog_destination(self) -> pulumi.Output[Optional['outputs.BlueprintKafkaChangelogDestination']]:
        """
        The changelog destination of the blueprint
        """
        return pulumi.get(self, "kafka_changelog_destination")

    @property
    @pulumi.getter(name="mirrorProperties")
    def mirror_properties(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.BlueprintMirrorProperties']]]:
        """
        The mirror properties of the blueprint
        """
        return pulumi.get(self, "mirror_properties")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional['outputs.BlueprintProperties']]:
        """
        The properties of the blueprint
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def relations(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.BlueprintRelations']]]:
        """
        The relations of the blueprint
        """
        return pulumi.get(self, "relations")

    @property
    @pulumi.getter(name="teamInheritance")
    def team_inheritance(self) -> pulumi.Output[Optional['outputs.BlueprintTeamInheritance']]:
        """
        The team inheritance of the blueprint
        """
        return pulumi.get(self, "team_inheritance")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The display name of the blueprint
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The last update date of the blueprint
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[str]:
        """
        The last updater of the blueprint
        """
        return pulumi.get(self, "updated_by")

    @property
    @pulumi.getter(name="webhookChangelogDestination")
    def webhook_changelog_destination(self) -> pulumi.Output[Optional['outputs.BlueprintWebhookChangelogDestination']]:
        """
        The webhook changelog destination of the blueprint
        """
        return pulumi.get(self, "webhook_changelog_destination")

