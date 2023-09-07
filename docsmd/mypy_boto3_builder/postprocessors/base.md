# Base

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Postprocessors](./index.md#postprocessors) /
Base

> Auto-generated documentation for [mypy_boto3_builder.postprocessors.base](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py) module.

## BasePostprocessor

[Show source in base.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L19)

Base postprocessor for classes and methods.

#### Arguments

- `session` - Boto3 session
- `package` - Service package
- `service_names` - Available service names

#### Signature

```python
class BasePostprocessor(ABC):
    def __init__(
        self,
        session: Session,
        package: ServicePackage,
        service_names: Sequence[ServiceName],
    ) -> None:
        ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)

### BasePostprocessor().extend_literals

[Show source in base.py:181](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L181)

Add extra literals.

- `<Class>ServiceName`
- `ServiceName`
- `ResourceServiceName`
- `PaginatorName`
- `WaiterName`
- `RegionName`

#### Signature

```python
def extend_literals(self) -> None:
    ...
```

### BasePostprocessor().generate_docstrings

[Show source in base.py:41](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L41)

Generate all docstrings.

#### Signature

```python
def generate_docstrings(self) -> None:
    ...
```

### BasePostprocessor().process_package

[Show source in base.py:52](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L52)

Postprocess built package.

#### Signature

```python
@abstractmethod
def process_package(self) -> None:
    ...
```

### BasePostprocessor().replace_self_ref_typed_dicts

[Show source in base.py:262](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L262)

Remove self-references from TypedDicts.

#### Signature

```python
def replace_self_ref_typed_dicts(self) -> None:
    ...
```