from typing import Any, Dict, List, Optional, Union, Literal

from pydantic import BaseModel, Field

from stac_pydantic.catalog import Catalog
from stac_pydantic.shared import Asset, NumType, Provider


class SpatialExtent(BaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md#spatial-extent-object
    """

    bbox: List[List[NumType]]


class TimeInterval(BaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md#temporal-extent-object
    """

    interval: List[List[Union[str, None]]]


class Extent(BaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md#extent-object
    """

    spatial: SpatialExtent
    temporal: TimeInterval


class Range(BaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md#stats-object
    """

    minimum: Union[NumType, str]
    maximum: Union[NumType, str]


class Collection(Catalog):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/collection-spec/collection-spec.md
    """

    assets: Optional[Dict[str, Asset]] = None
    license: str = Field(..., alias="license", min_length=1)
    extent: Extent
    title: Optional[str] = None
    keywords: Optional[List[str]] = None
    providers: Optional[List[Provider]] = None
    summaries: Optional[Dict[str, Union[Range, List[Any], Dict[str, Any]]]] = None
    type: Literal["Collection"] = "Collection"
