<img src="https://techally-content.s3-us-west-1.amazonaws.com/public-content/lacework_logo_full.png" width="600">

# Lacework CLI

The Lacework Command Line Interface is a tool that helps you manage the
Lacework cloud security platform. You can use it to manage compliance
reports, external integrations, vulnerability scans, and other operations.

## Installation

### Bash:

```
curl https://raw.githubusercontent.com/lacework/go-sdk/main/cli/install.sh | bash
```

### Powershell:

```
Set-ExecutionPolicy Bypass -Scope Process -Force;
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/lacework/go-sdk/main/cli/install.ps1'))
```

### Homebrew:

```
brew install lacework/tap/lacework-cli
```

## Quick Configuration

The `lacework configure` command is the fastest way to set up your Lacework
CLI installation. The command prompts you for three things:

- `account`: Account subdomain of URL (i.e. `<ACCOUNT>.lacework.net`)
- `api_key`: API Access Key
- `api_secret`: API Access Secret

> To create a set of API keys, log in to your Lacework account via WebUI and
> navigate to Settings > API Keys and click + Create New. Enter a name for
> the key and an optional description, then click Save. To get the secret key,
> download the generated API key file.

_**NOTE:** Use the argument `--json_file` to preload the downloaded API key file._

The following example shows sample values. Replace them with your own.

```bash
$ lacework configure
Account: example
Access Key ID: EXAMPLE_1234567890ABCDE1EXAMPLE1EXAMPLE123456789EXAMPLE
Secret Access Key: **********************************

You are all set!
```

The result of this command is the generation of a file named `.lacework.toml`
inside your home directory (`$HOME/.lacework.toml`) with a single profile
named `default`.

### Multiple Profiles

You can add additional profiles that you can refer to with a name by specifying
the `--profile` option. The following example creates a profile named `prod`.

```bash
$ lacework configure --profile prod
Account: prod.example
Access Key ID: PROD_1234567890ABCDE1EXAMPLE1EXAMPLE123456789EXAMPLE
Secret Access Key: **********************************

You are all set!
```

Then, when you run a command, you can specify a `--profile prod` and use the
credentials and settings stored under that name.

```bash
lacework integration list --profile prod
```

If there is no `--profile` option, the CLI will default to the `default` profile.

## Queries

### Synopsis

Run and manage Lacework Query Language (LQL) queries.

To provide customizable specification of datasets, Lacework provides the Lacework
Query Language (LQL). LQL is a human-readable text syntax for specifying selection,
filtering, and manipulation of data.

Currently, Lacework has introduced LQL for configuration of AWS CloudTrail policies
and queries. This means you can use LQL to customize AWS CloudTrail policies only.
For all other policies, use the previous existing methods.

Lacework ships a set of default LQL queries that are available in your account.

For more information about LQL, visit:

https://docs.lacework.com/lql-overview

To view all LQL queries in your Lacework account.

    lacework query list

To view all LQL data sources.

    lacework query list-sources

To view the fields of a specific data source.

    lacework query show-source <datasource>

To show a query.

    lacework query show <query_id>

To execute a query.

    lacework query run <query_id>

To execute an ad-hoc query.

    lacework query run --start "2022-01-28T05:00:00.000Z"

## Policies

### Synopsis

Manage policies in your Lacework account.

A policy is a mechanism used to add annotated metadata to a Lacework query for improving
the context of alerts, reports, and information displayed in the Lacework Console.

A policy also facilitates the scheduled execution of a Lacework query

A query is a mechanism used to interactively request information from a specific
curated dataset. A query has a defined structure for authoring detections.

Lacework ships a set of default LQL policies that are available in your account.

Limitations:

- The maximum number of records that each policy will return is 1000
- The maximum number of API calls is 120 per hour for ad-hoc LQL query executions

To view all the policies in your Lacework account.

    lacework policy ls

To view more details about a single policy.

    lacework policy show <policy_id>

To view the LQL query associated with the policy, use the query id shown.

    lacework query show <query_id>
