"""A Python Pulumi program"""
import json
import pulumi
from port_pulumi import Entity, EntityPropertiesArgs, Page, PagePermissions

# Creating an entity
entity = Entity(
    "port_pulumi",
    title="monolith",
    blueprint="microservice",
    properties=EntityPropertiesArgs(string_props={"language": "python"}),
)

# Creating a page
catalog_page = Page(
    "my-catalog-page-resource",
    identifier="my_catalog_page",
    title="Our Services",
    blueprint="service",
    icon="Microservice",
    type="blueprint-entities",
    widgets=[
        json.dumps(
            {
                "displayMode": "widget",
                "title": "Services",
                "type": "table-entities-explorer",
                "dataset": {
                    "combinator": "and",
                    "rules": [
                        {"operator": "=", "value": "service", "property": "$blueprint"}
                    ],
                },
                "id": "servicesTable-en",
                "excludedFields": ["properties.readme", "properties.slack"],
            }
        )
    ],
)

# Page Permissions: Allow read access to all admins and a specific user and team
microservices_permissions = PagePermissions(
    "catalog_page_permissions",
    page_identifier="my_catalog_page",
    read={
        "roles": [
            "Admin",
        ],
        "users": ["one_of_your_users@gmail.com"],
        "teams": ["Your Team"],
    },
)
