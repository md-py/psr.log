# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2021-07-27

- Interface `psr.log.LoggerAwareInterface` removed
- enum class `psr.log.LogLevel` removed in favor of constants usage,
  use `LEVEL_EMERGENCY`, `LEVEL_ALERT`, `LEVEL_CRITICAL`, `LEVEL_ERROR`,
  `LEVEL_WARNING`, `LEVEL_NOTICE`, `LEVEL_INFO`, `LEVEL_DEBUG` 
  constants instead.

## [1.0.0] - 2020-09-26

- Initial commit

[2.0.0]: https://github.com/md-py/psr.log/releases/tag/2.0.0
[1.0.0]: https://github.com/md-py/psr.log/releases/tag/1.0.0
