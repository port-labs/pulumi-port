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

__all__ = ['FolderArgs', 'Folder']

@pulumi.input_type
class FolderArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str],
                 after: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Folder resource.
        :param pulumi.Input[str] identifier: The identifier of the folder
        :param pulumi.Input[str] after: The identifier of the folder after which the folder should be placed
        :param pulumi.Input[str] parent: The identifier of the parent folder
        :param pulumi.Input[str] title: The title of the folder
        """
        pulumi.set(__self__, "identifier", identifier)
        if after is not None:
            pulumi.set(__self__, "after", after)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        The identifier of the folder
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def after(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the folder after which the folder should be placed
        """
        return pulumi.get(self, "after")

    @after.setter
    def after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "after", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the parent folder
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the folder
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class _FolderState:
    def __init__(__self__, *,
                 after: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Folder resources.
        :param pulumi.Input[str] after: The identifier of the folder after which the folder should be placed
        :param pulumi.Input[str] identifier: The identifier of the folder
        :param pulumi.Input[str] parent: The identifier of the parent folder
        :param pulumi.Input[str] title: The title of the folder
        """
        if after is not None:
            pulumi.set(__self__, "after", after)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def after(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the folder after which the folder should be placed
        """
        return pulumi.get(self, "after")

    @after.setter
    def after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "after", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the folder
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the parent folder
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the folder
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class Folder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 after: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A full list of the available folder types and their identifiers can be found [here](https://docs.getport.io/customize-pages-dashboards-and-plugins/folder/catalog-folder).

        > **WARNING**
        The folder resource is currently in beta and is subject to change in future versions.
        Use it by setting the Environment Variable `PORT_BETA_FEATURES_ENABLED=true`.
        If this Environment Variable isn't specified, you won't be able to use the resource.

        ## Example Usage

        ### Basic Folder

        ```python
        import pulumi
        import pulumi_port as port

        example_folder = port.index.Port_folder("exampleFolder",
            identifier=example_folder,
            title=Example Folder)
        ```

        ### Folder with Parent

        Create a folder inside another folder.

        ```python
        import pulumi
        import pulumi_port as port

        child_folder = port.index.Port_folder("childFolder",
            identifier=child_folder,
            parent=port_folder.example_folder.identifier,
            title=Child Folder)
        ```

        ### Folder with After

        Create a folder after another folder.

        ```python
        import pulumi
        import pulumi_port as port

        another_folder = port.index.Port_folder("anotherFolder",
            identifier=another_folder,
            after=port_folder.example_folder.identifier,
            title=Another Folder)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] after: The identifier of the folder after which the folder should be placed
        :param pulumi.Input[str] identifier: The identifier of the folder
        :param pulumi.Input[str] parent: The identifier of the parent folder
        :param pulumi.Input[str] title: The title of the folder
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FolderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A full list of the available folder types and their identifiers can be found [here](https://docs.getport.io/customize-pages-dashboards-and-plugins/folder/catalog-folder).

        > **WARNING**
        The folder resource is currently in beta and is subject to change in future versions.
        Use it by setting the Environment Variable `PORT_BETA_FEATURES_ENABLED=true`.
        If this Environment Variable isn't specified, you won't be able to use the resource.

        ## Example Usage

        ### Basic Folder

        ```python
        import pulumi
        import pulumi_port as port

        example_folder = port.index.Port_folder("exampleFolder",
            identifier=example_folder,
            title=Example Folder)
        ```

        ### Folder with Parent

        Create a folder inside another folder.

        ```python
        import pulumi
        import pulumi_port as port

        child_folder = port.index.Port_folder("childFolder",
            identifier=child_folder,
            parent=port_folder.example_folder.identifier,
            title=Child Folder)
        ```

        ### Folder with After

        Create a folder after another folder.

        ```python
        import pulumi
        import pulumi_port as port

        another_folder = port.index.Port_folder("anotherFolder",
            identifier=another_folder,
            after=port_folder.example_folder.identifier,
            title=Another Folder)
        ```

        :param str resource_name: The name of the resource.
        :param FolderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FolderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 after: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FolderArgs.__new__(FolderArgs)

            __props__.__dict__["after"] = after
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["parent"] = parent
            __props__.__dict__["title"] = title
        super(Folder, __self__).__init__(
            'port:index/folder:Folder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            after: Optional[pulumi.Input[str]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            parent: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None) -> 'Folder':
        """
        Get an existing Folder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] after: The identifier of the folder after which the folder should be placed
        :param pulumi.Input[str] identifier: The identifier of the folder
        :param pulumi.Input[str] parent: The identifier of the parent folder
        :param pulumi.Input[str] title: The title of the folder
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FolderState.__new__(_FolderState)

        __props__.__dict__["after"] = after
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["parent"] = parent
        __props__.__dict__["title"] = title
        return Folder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def after(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the folder after which the folder should be placed
        """
        return pulumi.get(self, "after")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        The identifier of the folder
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the parent folder
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        The title of the folder
        """
        return pulumi.get(self, "title")

