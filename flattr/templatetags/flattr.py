#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
templatetags/flattr.py 

See also:
[[http://developers.flattr.net/button/]]

"""

from django import template

register = template.Library()

class FlattrScriptNode(template.Node):
    """
    FlattrScriptNode renders the actual javascript
    """
    script = """<script type="text/javascript">
    /* <![CDATA[ */
    (function() {
    var s = document.createElement('script');
    var t = document.getElementsByTagName('script')[0];

    s.type = 'text/javascript';
    s.async = true;
    s.src = '//api.flattr.com/js/0.6/load.js?mode=auto';

    t.parentNode.insertBefore(s, t);
    })();
    /* ]]> */
    </script>
    """

    def render(self, context=None):
        return self.script

@register.tag
def flattr_script(parser, token):
    return FlattrScriptNode()


# vim: ts=4 et sw=4 sts=4


