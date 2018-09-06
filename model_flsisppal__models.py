# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from YBLEGACY.FLUtil import FLUtil


def _miextend(self, **kwargs):
    self._legacy_mtd = kwargs
    return self


class mtd_chatmessages(models.Model):
    id = models.AutoField(db_column="id", verbose_name=FLUtil.translate(u"Identificador", u"MetaData"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
    room = models.CharField(blank=True, null=True, max_length=20)
    sender = models.CharField(blank=True, null=True, max_length=20)
    receiver = models.CharField(blank=True, null=True, max_length=20)
    message = models.TextField(blank=True, null=True)
    fechahora = models.DateTimeField(null=True)

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Chat messages", u"MetaData")
        db_table = 'sis_chatmessages'


class mtd_chatstatus(models.Model):
    room = models.CharField(null=False, max_length=20, primary_key=True)
    ultcon = models.DateTimeField(null=True)

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Chat users", u"MetaData")
        db_table = 'sis_chatstatus'


models.Field._miextend = _miextend
