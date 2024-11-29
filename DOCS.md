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
* `rust-version`: Rust Version
* `rust-print`: Rust Print
* `rust-rand`: Rust Rand

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

## `ct rust-version`

Rust Version

**Usage**:

```console
$ ct rust-version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `ct rust-print`

Rust Print

**Usage**:

```console
$ ct rust-print [OPTIONS]
```

**Options**:

* `-c, --cmd TEXT`: rust_print  [default: test]
* `-v, --verbose`
* `--help`: Show this message and exit.

## `ct rust-rand`

Rust Rand

**Usage**:

```console
$ ct rust-rand [OPTIONS]
```

**Options**:

* `-c, --cmd TEXT`: rust_rand  [required]
* `-v, --verbose`
* `--help`: Show this message and exit.
