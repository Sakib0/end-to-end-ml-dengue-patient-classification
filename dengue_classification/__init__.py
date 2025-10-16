"""Compatibility package for dengue classification (underscore name)

This package mirrors the existing `dengue-classification` package folder but uses
an import-friendly name (`dengue_classification`). It's a lightweight shim to
avoid breaking imports while preserving original code layout.
"""

__path__ = __import__('pkgutil').extend_path(__path__, __name__)
