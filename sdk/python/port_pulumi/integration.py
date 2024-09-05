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

__all__ = ['IntegrationArgs', 'Integration']

@pulumi.input_type
class IntegrationArgs:
    def __init__(__self__, *,
                 installation_id: pulumi.Input[str],
                 config: Optional[pulumi.Input[str]] = None,
                 installation_app_type: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input['IntegrationKafkaChangelogDestinationArgs']] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 webhook_changelog_destination: Optional[pulumi.Input['IntegrationWebhookChangelogDestinationArgs']] = None):
        """
        The set of arguments for constructing a Integration resource.
        :param pulumi.Input[str] config: Integration Config Raw JSON string (use `jsonencode`)
        :param pulumi.Input['IntegrationKafkaChangelogDestinationArgs'] kafka_changelog_destination: The changelog destination of the blueprint (just an empty `{}`)
        :param pulumi.Input['IntegrationWebhookChangelogDestinationArgs'] webhook_changelog_destination: The webhook changelog destination of the integration
        """
        pulumi.set(__self__, "installation_id", installation_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if installation_app_type is not None:
            pulumi.set(__self__, "installation_app_type", installation_app_type)
        if kafka_changelog_destination is not None:
            pulumi.set(__self__, "kafka_changelog_destination", kafka_changelog_destination)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if webhook_changelog_destination is not None:
            pulumi.set(__self__, "webhook_changelog_destination", webhook_changelog_destination)

    @property
    @pulumi.getter(name="installationId")
    def installation_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "installation_id")

    @installation_id.setter
    def installation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "installation_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        Integration Config Raw JSON string (use `jsonencode`)
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="installationAppType")
    def installation_app_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "installation_app_type")

    @installation_app_type.setter
    def installation_app_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "installation_app_type", value)

    @property
    @pulumi.getter(name="kafkaChangelogDestination")
    def kafka_changelog_destination(self) -> Optional[pulumi.Input['IntegrationKafkaChangelogDestinationArgs']]:
        """
        The changelog destination of the blueprint (just an empty `{}`)
        """
        return pulumi.get(self, "kafka_changelog_destination")

    @kafka_changelog_destination.setter
    def kafka_changelog_destination(self, value: Optional[pulumi.Input['IntegrationKafkaChangelogDestinationArgs']]):
        pulumi.set(self, "kafka_changelog_destination", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="webhookChangelogDestination")
    def webhook_changelog_destination(self) -> Optional[pulumi.Input['IntegrationWebhookChangelogDestinationArgs']]:
        """
        The webhook changelog destination of the integration
        """
        return pulumi.get(self, "webhook_changelog_destination")

    @webhook_changelog_destination.setter
    def webhook_changelog_destination(self, value: Optional[pulumi.Input['IntegrationWebhookChangelogDestinationArgs']]):
        pulumi.set(self, "webhook_changelog_destination", value)


@pulumi.input_type
class _IntegrationState:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input[str]] = None,
                 installation_app_type: Optional[pulumi.Input[str]] = None,
                 installation_id: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input['IntegrationKafkaChangelogDestinationArgs']] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 webhook_changelog_destination: Optional[pulumi.Input['IntegrationWebhookChangelogDestinationArgs']] = None):
        """
        Input properties used for looking up and filtering Integration resources.
        :param pulumi.Input[str] config: Integration Config Raw JSON string (use `jsonencode`)
        :param pulumi.Input['IntegrationKafkaChangelogDestinationArgs'] kafka_changelog_destination: The changelog destination of the blueprint (just an empty `{}`)
        :param pulumi.Input['IntegrationWebhookChangelogDestinationArgs'] webhook_changelog_destination: The webhook changelog destination of the integration
        """
        if config is not None:
            pulumi.set(__self__, "config", config)
        if installation_app_type is not None:
            pulumi.set(__self__, "installation_app_type", installation_app_type)
        if installation_id is not None:
            pulumi.set(__self__, "installation_id", installation_id)
        if kafka_changelog_destination is not None:
            pulumi.set(__self__, "kafka_changelog_destination", kafka_changelog_destination)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if webhook_changelog_destination is not None:
            pulumi.set(__self__, "webhook_changelog_destination", webhook_changelog_destination)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        Integration Config Raw JSON string (use `jsonencode`)
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="installationAppType")
    def installation_app_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "installation_app_type")

    @installation_app_type.setter
    def installation_app_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "installation_app_type", value)

    @property
    @pulumi.getter(name="installationId")
    def installation_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "installation_id")

    @installation_id.setter
    def installation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "installation_id", value)

    @property
    @pulumi.getter(name="kafkaChangelogDestination")
    def kafka_changelog_destination(self) -> Optional[pulumi.Input['IntegrationKafkaChangelogDestinationArgs']]:
        """
        The changelog destination of the blueprint (just an empty `{}`)
        """
        return pulumi.get(self, "kafka_changelog_destination")

    @kafka_changelog_destination.setter
    def kafka_changelog_destination(self, value: Optional[pulumi.Input['IntegrationKafkaChangelogDestinationArgs']]):
        pulumi.set(self, "kafka_changelog_destination", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="webhookChangelogDestination")
    def webhook_changelog_destination(self) -> Optional[pulumi.Input['IntegrationWebhookChangelogDestinationArgs']]:
        """
        The webhook changelog destination of the integration
        """
        return pulumi.get(self, "webhook_changelog_destination")

    @webhook_changelog_destination.setter
    def webhook_changelog_destination(self, value: Optional[pulumi.Input['IntegrationWebhookChangelogDestinationArgs']]):
        pulumi.set(self, "webhook_changelog_destination", value)


class Integration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 installation_app_type: Optional[pulumi.Input[str]] = None,
                 installation_id: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input[pulumi.InputType['IntegrationKafkaChangelogDestinationArgs']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 webhook_changelog_destination: Optional[pulumi.Input[pulumi.InputType['IntegrationWebhookChangelogDestinationArgs']]] = None,
                 __props__=None):
        """
        **NOTE:** This resource manages existing integration and integration mappings, not for creating new integrations.

        Docs about integrations can be found [here](https://docs.getport.io/integrations-index/).

        Docs about how to import existing integrations and manage their mappings can be found here.

        ```python
        import pulumi
        import json
        import pulumi_port as port

        my_custom_integration = port.index.Port_integration("myCustomIntegration",
            installation_id=my-custom-integration-id,
            title=My Custom Integration,
            version=1.33.7,
            config=json.dumps({
                createMissingRelatedEntitiesboolean: True,
                deleteDependentEntities: True,
                resources: [{
                    kind: my-custom-kind,
                    selector: {
                        query: .title,
                    },
                    port: {
                        entity: {
                            mappings: [{
                                identifier: 'my-identifier',
                                title: .title,
                                blueprint: 'my-blueprint',
                                properties: {
                                    my_property: 123,
                                },
                                relations: {},
                            }],
                        },
                    },
                }],
            }))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config: Integration Config Raw JSON string (use `jsonencode`)
        :param pulumi.Input[pulumi.InputType['IntegrationKafkaChangelogDestinationArgs']] kafka_changelog_destination: The changelog destination of the blueprint (just an empty `{}`)
        :param pulumi.Input[pulumi.InputType['IntegrationWebhookChangelogDestinationArgs']] webhook_changelog_destination: The webhook changelog destination of the integration
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        **NOTE:** This resource manages existing integration and integration mappings, not for creating new integrations.

        Docs about integrations can be found [here](https://docs.getport.io/integrations-index/).

        Docs about how to import existing integrations and manage their mappings can be found here.

        ```python
        import pulumi
        import json
        import pulumi_port as port

        my_custom_integration = port.index.Port_integration("myCustomIntegration",
            installation_id=my-custom-integration-id,
            title=My Custom Integration,
            version=1.33.7,
            config=json.dumps({
                createMissingRelatedEntitiesboolean: True,
                deleteDependentEntities: True,
                resources: [{
                    kind: my-custom-kind,
                    selector: {
                        query: .title,
                    },
                    port: {
                        entity: {
                            mappings: [{
                                identifier: 'my-identifier',
                                title: .title,
                                blueprint: 'my-blueprint',
                                properties: {
                                    my_property: 123,
                                },
                                relations: {},
                            }],
                        },
                    },
                }],
            }))
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 installation_app_type: Optional[pulumi.Input[str]] = None,
                 installation_id: Optional[pulumi.Input[str]] = None,
                 kafka_changelog_destination: Optional[pulumi.Input[pulumi.InputType['IntegrationKafkaChangelogDestinationArgs']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 webhook_changelog_destination: Optional[pulumi.Input[pulumi.InputType['IntegrationWebhookChangelogDestinationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationArgs.__new__(IntegrationArgs)

            __props__.__dict__["config"] = config
            __props__.__dict__["installation_app_type"] = installation_app_type
            if installation_id is None and not opts.urn:
                raise TypeError("Missing required property 'installation_id'")
            __props__.__dict__["installation_id"] = installation_id
            __props__.__dict__["kafka_changelog_destination"] = kafka_changelog_destination
            __props__.__dict__["title"] = title
            __props__.__dict__["version"] = version
            __props__.__dict__["webhook_changelog_destination"] = webhook_changelog_destination
        super(Integration, __self__).__init__(
            'port:index/integration:Integration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[str]] = None,
            installation_app_type: Optional[pulumi.Input[str]] = None,
            installation_id: Optional[pulumi.Input[str]] = None,
            kafka_changelog_destination: Optional[pulumi.Input[pulumi.InputType['IntegrationKafkaChangelogDestinationArgs']]] = None,
            title: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None,
            webhook_changelog_destination: Optional[pulumi.Input[pulumi.InputType['IntegrationWebhookChangelogDestinationArgs']]] = None) -> 'Integration':
        """
        Get an existing Integration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config: Integration Config Raw JSON string (use `jsonencode`)
        :param pulumi.Input[pulumi.InputType['IntegrationKafkaChangelogDestinationArgs']] kafka_changelog_destination: The changelog destination of the blueprint (just an empty `{}`)
        :param pulumi.Input[pulumi.InputType['IntegrationWebhookChangelogDestinationArgs']] webhook_changelog_destination: The webhook changelog destination of the integration
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationState.__new__(_IntegrationState)

        __props__.__dict__["config"] = config
        __props__.__dict__["installation_app_type"] = installation_app_type
        __props__.__dict__["installation_id"] = installation_id
        __props__.__dict__["kafka_changelog_destination"] = kafka_changelog_destination
        __props__.__dict__["title"] = title
        __props__.__dict__["version"] = version
        __props__.__dict__["webhook_changelog_destination"] = webhook_changelog_destination
        return Integration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[str]]:
        """
        Integration Config Raw JSON string (use `jsonencode`)
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="installationAppType")
    def installation_app_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "installation_app_type")

    @property
    @pulumi.getter(name="installationId")
    def installation_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "installation_id")

    @property
    @pulumi.getter(name="kafkaChangelogDestination")
    def kafka_changelog_destination(self) -> pulumi.Output[Optional['outputs.IntegrationKafkaChangelogDestination']]:
        """
        The changelog destination of the blueprint (just an empty `{}`)
        """
        return pulumi.get(self, "kafka_changelog_destination")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="webhookChangelogDestination")
    def webhook_changelog_destination(self) -> pulumi.Output[Optional['outputs.IntegrationWebhookChangelogDestination']]:
        """
        The webhook changelog destination of the integration
        """
        return pulumi.get(self, "webhook_changelog_destination")

