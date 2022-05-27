# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class Feline(msrest.serialization.Model):
    """Feline.

    :ivar meows:
    :vartype meows: bool
    :ivar hisses:
    :vartype hisses: bool
    """

    _attribute_map = {
        "meows": {"key": "meows", "type": "bool"},
        "hisses": {"key": "hisses", "type": "bool"},
    }

    def __init__(self, **kwargs):
        """
        :keyword meows:
        :paramtype meows: bool
        :keyword hisses:
        :paramtype hisses: bool
        """
        super(Feline, self).__init__(**kwargs)
        self.meows = kwargs.get("meows", None)
        self.hisses = kwargs.get("hisses", None)


class Pet(msrest.serialization.Model):
    """Pet.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword name: Required.
        :paramtype name: str
        """
        super(Pet, self).__init__(**kwargs)
        self.name = kwargs["name"]


class Cat(Pet, Feline):
    """Cat.

    All required parameters must be populated in order to send to Azure.

    :ivar meows:
    :vartype meows: bool
    :ivar hisses:
    :vartype hisses: bool
    :ivar name: Required.
    :vartype name: str
    :ivar likes_milk:
    :vartype likes_milk: bool
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "meows": {"key": "meows", "type": "bool"},
        "hisses": {"key": "hisses", "type": "bool"},
        "name": {"key": "name", "type": "str"},
        "likes_milk": {"key": "likesMilk", "type": "bool"},
    }

    def __init__(self, **kwargs):
        """
        :keyword meows:
        :paramtype meows: bool
        :keyword hisses:
        :paramtype hisses: bool
        :keyword name: Required.
        :paramtype name: str
        :keyword likes_milk:
        :paramtype likes_milk: bool
        """
        super(Cat, self).__init__(**kwargs)
        self.meows = kwargs.get("meows", None)
        self.hisses = kwargs.get("hisses", None)
        self.likes_milk = kwargs.get("likes_milk", None)
        self.name = kwargs["name"]


class Error(msrest.serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get("status", None)
        self.message = kwargs.get("message", None)


class Horse(Pet):
    """Horse.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar is_a_show_horse:
    :vartype is_a_show_horse: bool
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "is_a_show_horse": {"key": "isAShowHorse", "type": "bool"},
    }

    def __init__(self, **kwargs):
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword is_a_show_horse:
        :paramtype is_a_show_horse: bool
        """
        super(Horse, self).__init__(**kwargs)
        self.is_a_show_horse = kwargs.get("is_a_show_horse", None)


class Kitten(Cat):
    """Kitten.

    All required parameters must be populated in order to send to Azure.

    :ivar meows:
    :vartype meows: bool
    :ivar hisses:
    :vartype hisses: bool
    :ivar name: Required.
    :vartype name: str
    :ivar likes_milk:
    :vartype likes_milk: bool
    :ivar eats_mice_yet:
    :vartype eats_mice_yet: bool
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "meows": {"key": "meows", "type": "bool"},
        "hisses": {"key": "hisses", "type": "bool"},
        "name": {"key": "name", "type": "str"},
        "likes_milk": {"key": "likesMilk", "type": "bool"},
        "eats_mice_yet": {"key": "eatsMiceYet", "type": "bool"},
    }

    def __init__(self, **kwargs):
        """
        :keyword meows:
        :paramtype meows: bool
        :keyword hisses:
        :paramtype hisses: bool
        :keyword name: Required.
        :paramtype name: str
        :keyword likes_milk:
        :paramtype likes_milk: bool
        :keyword eats_mice_yet:
        :paramtype eats_mice_yet: bool
        """
        super(Kitten, self).__init__(**kwargs)
        self.eats_mice_yet = kwargs.get("eats_mice_yet", None)
