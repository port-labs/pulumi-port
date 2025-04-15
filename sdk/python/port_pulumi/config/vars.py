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
from .. import _utilities

import types

__config__ = pulumi.Config('port')


class _ExportableConfig(types.ModuleType):
    @property
    def base_url(self) -> Optional[str]:
        return __config__.get('baseUrl')

    @property
    def client_id(self) -> Optional[str]:
        """
        Client ID for Port-labs
        """
        return __config__.get('clientId')

    @property
    def json_escape_html(self) -> Optional[bool]:
        """
        When set to `false` disables the default HTML escaping of json.Marshal when reading data from Port. Defaults to `true`
        """
        return __config__.get_bool('jsonEscapeHtml')

    @property
    def secret(self) -> Optional[str]:
        """
        Client Secret for Port-labs
        """
        return __config__.get('secret')

    @property
    def token(self) -> Optional[str]:
        """
        Token for Port-labs
        """
        return __config__.get('token')

