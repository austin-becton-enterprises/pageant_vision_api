from hax_telegraph.model.database_object.wrapper import DatabaseObjectWrapper

def get_dummy_media_list() -> DatabaseObjectWrapper:
    """Creates a dummy DatabaseObjectWrapper for testing purposes."""
    nested_object_dict = {
        "metaTags": {
            "displayTitle": "Nested Video",
            "subtitle": "A nested video example",
            "date": "July 1, 2025",
            "thumbnailURL": "dummy_thumbnail"
        },
        "value": "nested_video_id"
    }

    children = [
        {
            "metaTags": {
                "displayTitle": "Miss Michigan",
                "subtitle": "Live from Port Huron, Michigan",
                "date": "August 9, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4",
            "children": [nested_object_dict, nested_object_dict]
        },
        {
            "metaTags": {
                "displayTitle": "Miss USA",
                "subtitle": "Live from Las Vegas, Nevada",
                "date": "September 12, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        },
        {
            "metaTags": {
                "displayTitle": "Miss Universe",
                "subtitle": "Live from Miami, Florida",
                "date": "October 3, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        },
        {
            "metaTags": {
                "displayTitle": "Miss Teen",
                "subtitle": "Live from Dallas, Texas",
                "date": "July 21, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        },
        {
            "metaTags": {
                "displayTitle": "Miss World",
                "subtitle": "Live from London, England",
                "date": "November 15, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        }
    ]

    return DatabaseObjectWrapper(jsonDict={"children": children})
