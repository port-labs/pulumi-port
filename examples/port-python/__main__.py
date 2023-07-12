"""A Python Pulumi program"""

import pulumi
from port_pulumi import Entity

entity = Entity("port_pulumi", title="monolith", blueprint="microservice",
                properties={string_props={"language": "node"}})
