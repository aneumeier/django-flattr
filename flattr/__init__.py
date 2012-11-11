#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
__init__.py 

"""

version_info = (0, 0, 14)
__version__ = ".".join(map(str, version_info))

FLATTR_API_ENDPOINT = "https://api.flattr.com/rest/v2"
FLATTR_OAUTH2_AUTHORIZE = "https://flattr.com/oauth/authorize"
FLATTR_OAUTH2_TOKEN = "https://flattr.com/oauth/token"

import oauth2

class FlattrError(Exception):
    """
    Base class for Flattr errors
    """
    @property
    def message(self):
        """
        Returns the first argument used to construct this error.
        """
        return self.args[0]

class Ouath2API(object):
    token = None
    def __init__(self, token):
        self.token = token

    def get(self):
        pass

class Flattr(object):
    """
    The flattr object.
    See:: http://developers.flattr.net/api/resources/flattrs/

    Field       Type      Permission  Description
    type        string                Object type, set to flattr.
    thing       hash                  Contains a thing object.
    owner       hash                  Contains either a user object or a mini user object (default).
    created_at  string                Format is unixtime.
    """
    def __init__(self):
        return

class Thing(object):
    """
    The Thing object.
    See:: http://developers.flattr.net/api/resources/things/

    Field               Type      Permission      Description
    type                string                    Object type, set to thing.
    resource            string                    URL to the API resource
    link                string                    URL to user on Flattr.com website
    id                  int                       ID of the thing
    url                 string                    URL the thing is pointing to
    flattrs             int                       Number of flattrs
    flattrs_user_count  int                       Number of user who have flattred
    title               string                    Title of the thing
    description         string                    Description of the thing
    tags                array                     Array with tags as strings
    language            string                    Langauge
    category            string                    Category
    created_at          int                       Format is unixtime
    owner               hash                      Contains either a user object or a mini user object (default).
    hidden              bool                      Hidden or not in listings. Example, API search and Catalog.
    image               string                    URL to thing image
    flattred            bool      authenticated   Has the authenticated user flattred the thing
    last_flattr_at      int       owner           Last time flattred. Format is unixtime. Only available if the authenticated user owns the thing.
    updated_at          int       owner           Last time updated. Format is unixtime. Only available if the authenticated user owns the thing.
    """

    def __init__(self, *args, **kwargs):
        

# vim: ts=4 et sw=4 sts=4

