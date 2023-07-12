# Port Resource Provider

![Port](./img/port.svg)

The Port Resource Provider lets you manage [Port](https://www.getport.io) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @port-labs/port
```

or `yarn`:

```bash
yarn add @port-labs/port
```

### Python

To use from Python, install using `pip`:

```bash
pip install port_pulumi
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/port-labs/pulumi-port/sdk
```

## Configuration

The following configuration points are available for the `port` provider:

- `port:clientId` - This is the Port client ID.
- `port:secret` - This is the Port secret.
- `port:baseUrl` (optional) - This is the Port base URL.
- `port:token` - (optional) This is the Port token.

