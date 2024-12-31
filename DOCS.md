# `ct`

**Usage**:

```console
$ ct [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--version`
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `cs`: Endpoint Check: Check Sites
* `test`: Test cmd
* `aws`: AWS cmd: default: li
* `gcp`: GCP cmd: default: li
* `kube-events`: Show K8s events with failed status
* `kube-pods`: Show K8s pods with failed status

## `ct cs`

Endpoint Check: Check Sites

**Usage**:

```console
$ ct cs [OPTIONS]
```

**Options**:

* `-v, --verbose`
* `--help`: Show this message and exit.

## `ct test`

Test cmd

**Usage**:

```console
$ ct test [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `ct aws`

AWS cmd: default: li

**Usage**:

```console
$ ct aws [OPTIONS]
```

**Options**:

* `-c, --cmd TEXT`: commands: li, ldb, udns  [default: li]
* `-v, --verbose`
* `--help`: Show this message and exit.

## `ct gcp`

GCP cmd: default: li

**Usage**:

```console
$ ct gcp [OPTIONS]
```

**Options**:

* `-c, --cmd TEXT`: commands: li  [default: li]
* `-v, --verbose`
* `--help`: Show this message and exit.

## `ct kube-events`

Show K8s events with failed status

**Usage**:

```console
$ ct kube-events [OPTIONS]
```

**Options**:

* `-v, --verbose`
* `--help`: Show this message and exit.

## `ct kube-pods`

Show K8s pods with failed status

**Usage**:

```console
$ ct kube-pods [OPTIONS]
```

**Options**:

* `-v, --verbose`
* `--help`: Show this message and exit.
