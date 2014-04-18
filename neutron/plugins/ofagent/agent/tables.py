# Copyright (C) 2014 VA Linux Systems Japan K.K.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: YAMAMOTO Takashi, VA Linux Systems Japan K.K.

from neutron.plugins.common import constants as p_const


def _seq():
    i = 0
    while True:
        yield i
        i += 1

_table_id_gen = _seq()


def _table_id():
    return _table_id_gen.next()

TUNNEL_TYPES = [
    p_const.TYPE_GRE,
    p_const.TYPE_VXLAN,
]

TUNNEL_TYPE_IDX = dict((t, TUNNEL_TYPES.index(t)) for t in TUNNEL_TYPES)

CHECK_IN_PORT = _table_id()
TUNNEL_IN = {}
for t in TUNNEL_TYPES:
    TUNNEL_IN[t] = _table_id()
PHYS_IN = _table_id()
LOCAL_IN = _table_id()
ARP_PASSTHROUGH = _table_id()
ARP_RESPONDER = _table_id()
TUNNEL_OUT = _table_id()
LOCAL_OUT = _table_id()
PHYS_OUT = _table_id()
TUNNEL_FLOOD = {}
for t in TUNNEL_TYPES:
    TUNNEL_FLOOD[t] = _table_id()
PHYS_FLOOD = _table_id()
LOCAL_FLOOD = _table_id()
