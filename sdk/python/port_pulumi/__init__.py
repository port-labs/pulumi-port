# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .action import *
from .action_permissions import *
from .aggregation_properties import *
from .blueprint import *
from .blueprint_permissions import *
from .entity import *
from .get_search import *
from .integration import *
from .page import *
from .page_permissions import *
from .provider import *
from .scorecard import *
from .system_blueprint import *
from .team import *
from .webhook import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import port_pulumi.config as __config
    config = __config
else:
    config = _utilities.lazy_import('port_pulumi.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "port",
  "mod": "index/action",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/action:Action": "Action"
  }
 },
 {
  "pkg": "port",
  "mod": "index/actionPermissions",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/actionPermissions:ActionPermissions": "ActionPermissions"
  }
 },
 {
  "pkg": "port",
  "mod": "index/aggregationProperties",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/aggregationProperties:AggregationProperties": "AggregationProperties"
  }
 },
 {
  "pkg": "port",
  "mod": "index/blueprint",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/blueprint:Blueprint": "Blueprint"
  }
 },
 {
  "pkg": "port",
  "mod": "index/blueprintPermissions",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/blueprintPermissions:BlueprintPermissions": "BlueprintPermissions"
  }
 },
 {
  "pkg": "port",
  "mod": "index/entity",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/entity:Entity": "Entity"
  }
 },
 {
  "pkg": "port",
  "mod": "index/integration",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/integration:Integration": "Integration"
  }
 },
 {
  "pkg": "port",
  "mod": "index/page",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/page:Page": "Page"
  }
 },
 {
  "pkg": "port",
  "mod": "index/pagePermissions",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/pagePermissions:PagePermissions": "PagePermissions"
  }
 },
 {
  "pkg": "port",
  "mod": "index/scorecard",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/scorecard:Scorecard": "Scorecard"
  }
 },
 {
  "pkg": "port",
  "mod": "index/systemBlueprint",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/systemBlueprint:SystemBlueprint": "SystemBlueprint"
  }
 },
 {
  "pkg": "port",
  "mod": "index/team",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/team:Team": "Team"
  }
 },
 {
  "pkg": "port",
  "mod": "index/webhook",
  "fqn": "port_pulumi",
  "classes": {
   "port:index/webhook:Webhook": "Webhook"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "port",
  "token": "pulumi:providers:port",
  "fqn": "port_pulumi",
  "class": "Provider"
 }
]
"""
)
