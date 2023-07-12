"""A Python Pulumi program"""

import pulumi
from port_pulumi import Entity,EntityPropertiesArgs

entity = Entity("port_pulumi", title="monolith", blueprint="microservice",
                properties=EntityPropertiesArgs(string_props={"language": "python"}),
                )
