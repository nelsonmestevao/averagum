#!/usr/bin/env python
# -*- coding: utf-8 -*-
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(secret="fnADc8Fd6WACFHM0aQ1r5PykHfNUKJ_q4vT0Z_D4")

databases = client.query(q.paginate(q.databases()))

print(databases)

