# Function

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Function

> Auto-generated documentation for [mypy_boto3_builder.structures.function](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py) module.

## Function

[Show source in function.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L16)

Module-level function.

#### Signature

```python
class Function:
    def __init__(
        self,
        name: str,
        arguments: Iterable[Argument],
        return_type: FakeAnnotation,
        docstring: str = "",
        decorators: Iterable[FakeAnnotation] = (),
        body_lines: Iterable[str] = (),
        type_ignore: bool = False,
        is_async: bool = False,
    ):
        ...
```

#### See also

- [Argument](./argument.md#argument)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().body

[Show source in function.py:83](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L83)

Function body as a string.

#### Signature

```python
@property
def body(self) -> str:
    ...
```

### Function().copy

[Show source in function.py:136](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L136)

Deep copy function.

#### Signature

```python
def copy(self: _R) -> _R:
    ...
```

### Function().create_request_type_annotation

[Show source in function.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L62)

Create and set `request_type_annotation` TypedDict based on function arguments.

#### Signature

```python
def create_request_type_annotation(self, name: str) -> None:
    ...
```

### Function().get_required_import_records

[Show source in function.py:100](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L100)

Extract required import records.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Function().is_kw_only

[Show source in function.py:117](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L117)

Whether method arguments can be passed only as kwargs.

#### Signature

```python
def is_kw_only(self) -> bool:
    ...
```

### Function().iterate_types

[Show source in function.py:90](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L90)

Iterate over required type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Function().remove_argument

[Show source in function.py:151](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L151)

Remove argument by name.

#### Signature

```python
def remove_argument(self: _R, *names: str) -> _R:
    ...
```

### Function().returns_none

[Show source in function.py:110](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L110)

Whether return type is None.

#### Signature

```python
@property
def returns_none(self) -> bool:
    ...
```

### Function().short_docstring

[Show source in function.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L49)

Docstring without documentation links.

#### Signature

```python
@property
def short_docstring(self) -> str:
    ...
```

### Function().type_hint_annotations

[Show source in function.py:123](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/function.py#L123)

Type annotations list from arguments and return type with internal types.

#### Signature

```python
@property
def type_hint_annotations(self) -> list[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
