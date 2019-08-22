#!/usr/bin/env python3.5

import sqlite3
import EbayItem

"""
Items  | name | image | price | currency |
------------------------------------------
item 1 |      |       |       |          |
-------|----------------------------------
item 2 |      |       |       |          |
------------------------------------------
"""

uk_item = EbayItem.EbayItem("https://www.ebay.co.uk/itm/Sony-A5100-Mirrorless-Camera-24MP-3-Inch-Screen-With-16-50Mm-Lens-White/352629671771?_trkparms=%26rpp_cid%3D5669a6a7e4b06cad1c1edf84%26rpp_icid%3D5912f793e4b00d651026f422")

print(uk_item.convert_to_dict())
