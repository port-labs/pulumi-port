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

__all__ = ['ActionPermissionsArgs', 'ActionPermissions']

@pulumi.input_type
class ActionPermissionsArgs:
    def __init__(__self__, *,
                 action_identifier: pulumi.Input[str],
                 permissions: pulumi.Input['ActionPermissionsPermissionsArgs'],
                 blueprint_identifier: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ActionPermissions resource.
        :param pulumi.Input[str] action_identifier: The ID of the action
        :param pulumi.Input['ActionPermissionsPermissionsArgs'] permissions: The permissions for the action
        :param pulumi.Input[str] blueprint_identifier: The ID of the blueprint
        """
        pulumi.set(__self__, "action_identifier", action_identifier)
        pulumi.set(__self__, "permissions", permissions)
        if blueprint_identifier is not None:
            warnings.warn("""Action is not attached to blueprint anymore. This value is ignored""", DeprecationWarning)
            pulumi.log.warn("""blueprint_identifier is deprecated: Action is not attached to blueprint anymore. This value is ignored""")
        if blueprint_identifier is not None:
            pulumi.set(__self__, "blueprint_identifier", blueprint_identifier)

    @property
    @pulumi.getter(name="actionIdentifier")
    def action_identifier(self) -> pulumi.Input[str]:
        """
        The ID of the action
        """
        return pulumi.get(self, "action_identifier")

    @action_identifier.setter
    def action_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_identifier", value)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input['ActionPermissionsPermissionsArgs']:
        """
        The permissions for the action
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input['ActionPermissionsPermissionsArgs']):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="blueprintIdentifier")
    @_utilities.deprecated("""Action is not attached to blueprint anymore. This value is ignored""")
    def blueprint_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the blueprint
        """
        return pulumi.get(self, "blueprint_identifier")

    @blueprint_identifier.setter
    def blueprint_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "blueprint_identifier", value)


@pulumi.input_type
class _ActionPermissionsState:
    def __init__(__self__, *,
                 action_identifier: Optional[pulumi.Input[str]] = None,
                 blueprint_identifier: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input['ActionPermissionsPermissionsArgs']] = None):
        """
        Input properties used for looking up and filtering ActionPermissions resources.
        :param pulumi.Input[str] action_identifier: The ID of the action
        :param pulumi.Input[str] blueprint_identifier: The ID of the blueprint
        :param pulumi.Input['ActionPermissionsPermissionsArgs'] permissions: The permissions for the action
        """
        if action_identifier is not None:
            pulumi.set(__self__, "action_identifier", action_identifier)
        if blueprint_identifier is not None:
            warnings.warn("""Action is not attached to blueprint anymore. This value is ignored""", DeprecationWarning)
            pulumi.log.warn("""blueprint_identifier is deprecated: Action is not attached to blueprint anymore. This value is ignored""")
        if blueprint_identifier is not None:
            pulumi.set(__self__, "blueprint_identifier", blueprint_identifier)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="actionIdentifier")
    def action_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the action
        """
        return pulumi.get(self, "action_identifier")

    @action_identifier.setter
    def action_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_identifier", value)

    @property
    @pulumi.getter(name="blueprintIdentifier")
    @_utilities.deprecated("""Action is not attached to blueprint anymore. This value is ignored""")
    def blueprint_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the blueprint
        """
        return pulumi.get(self, "blueprint_identifier")

    @blueprint_identifier.setter
    def blueprint_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "blueprint_identifier", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input['ActionPermissionsPermissionsArgs']]:
        """
        The permissions for the action
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input['ActionPermissionsPermissionsArgs']]):
        pulumi.set(self, "permissions", value)


class ActionPermissions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_identifier: Optional[pulumi.Input[str]] = None,
                 blueprint_identifier: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Union['ActionPermissionsPermissionsArgs', 'ActionPermissionsPermissionsArgsDict']]] = None,
                 __props__=None):
        """
        Create a ActionPermissions resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_identifier: The ID of the action
        :param pulumi.Input[str] blueprint_identifier: The ID of the blueprint
        :param pulumi.Input[Union['ActionPermissionsPermissionsArgs', 'ActionPermissionsPermissionsArgsDict']] permissions: The permissions for the action
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ActionPermissionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ActionPermissions resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ActionPermissionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ActionPermissionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_identifier: Optional[pulumi.Input[str]] = None,
                 blueprint_identifier: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Union['ActionPermissionsPermissionsArgs', 'ActionPermissionsPermissionsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ActionPermissionsArgs.__new__(ActionPermissionsArgs)

            if action_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'action_identifier'")
            __props__.__dict__["action_identifier"] = action_identifier
            __props__.__dict__["blueprint_identifier"] = blueprint_identifier
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__.__dict__["permissions"] = permissions
        super(ActionPermissions, __self__).__init__(
            'port:index/actionPermissions:ActionPermissions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action_identifier: Optional[pulumi.Input[str]] = None,
            blueprint_identifier: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Union['ActionPermissionsPermissionsArgs', 'ActionPermissionsPermissionsArgsDict']]] = None) -> 'ActionPermissions':
        """
        Get an existing ActionPermissions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_identifier: The ID of the action
        :param pulumi.Input[str] blueprint_identifier: The ID of the blueprint
        :param pulumi.Input[Union['ActionPermissionsPermissionsArgs', 'ActionPermissionsPermissionsArgsDict']] permissions: The permissions for the action
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ActionPermissionsState.__new__(_ActionPermissionsState)

        __props__.__dict__["action_identifier"] = action_identifier
        __props__.__dict__["blueprint_identifier"] = blueprint_identifier
        __props__.__dict__["permissions"] = permissions
        return ActionPermissions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionIdentifier")
    def action_identifier(self) -> pulumi.Output[str]:
        """
        The ID of the action
        """
        return pulumi.get(self, "action_identifier")

    @property
    @pulumi.getter(name="blueprintIdentifier")
    @_utilities.deprecated("""Action is not attached to blueprint anymore. This value is ignored""")
    def blueprint_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the blueprint
        """
        return pulumi.get(self, "blueprint_identifier")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output['outputs.ActionPermissionsPermissions']:
        """
        The permissions for the action
        """
        return pulumi.get(self, "permissions")

