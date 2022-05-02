import domain.filters as filters_package

from inspect import getmembers, isclass, isabstract
from typing import Dict, Type, Tuple

from domain.filters import Filter


class FilterClasses:
    """Return a dictionary of all filter classes in the domain.filters module."""

    def get_filters(self) -> Dict[str, Tuple[Type[Filter], int, str]]:
        """Get all available filters."""

        filters = {}

        filters_classes = getmembers(
            filters_package,
            lambda m: isclass(m) and not isabstract(m)
        )

        for name, _type in filters_classes:
            if isclass(_type) and issubclass(_type, filters_package.Filter):
                filters[name.lower()] = (_type, _type.ARGUMENTS, _type.HELP)

        return filters
