"""
Helper for Python import strings with not set master module name.
"""
from typing import TypeVar

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString

_R = TypeVar("_R", bound="InternalImportRecord")


class InternalImportRecord(ImportRecord):
    """
    Helper for Python import strings with not set master module name.

    Arguments:
        service_module_name -- Service module name.
        name -- Import name.
        alias -- Import local name.
    """

    def __init__(self, service_module_name: ServiceModuleName, name: str = "", alias: str = ""):
        self._local_source = ImportString(service_module_name.name)
        source = ImportString.parent() + self._local_source
        super().__init__(source, name=name, alias=alias)
