# Releasing a new version of the Pulumi Port Provider after Terraform Provider Update

## Context

The Pulumi Port Provider is a wrapper around the Terraform Provider. The Terraform Provider is updated regularly, and the Pulumi Port Provider needs to be updated to match the Terraform Provider version. This document outlines the steps to update the Pulumi Port Provider to the latest version of the Terraform Provider.

## Preparation Steps:

### Setup Environment

- Clone the pulumi-port repository.
- Start the project in a devcontainer (local, DevPod, or GH workspaces).
- Open Terminal in remote VS Code. ( F1 -> Dev Container: Open Folder in Container -> pulumi-port )
- Export GitHub token: export GITHUB_TOKEN=xxx. (This is needed for the upgrade process to create a PR in the repository.)
- Upgrade Provider
    - If you added new resources, you will need to update the resource definitions in the provider module.
        - Open resources.go in the provider module.
        - Add new resources to the Resources field.
    - Run `upgrade-provider port-labs/pulumi-port` (this will update everything and create a PR in the repository).


### Steps for Handling Errors:

#### Check Go Mod Versions

Ensure that github.com/pulumi/pulumi/pkg/v3 and github.com/pulumi/pulumi/sdk/v3 in go.mod are the same versions.
Update the version in go.mod so they both are the same to avoid errors.
Run Upgrade Again

After adjustments, rerun the upgrade process.
Monitor the process; tfgen might take a few minutes to complete.
Verify PR Creation

Once successful, a PR should be created upgrading the Pulumi provider to the new version.