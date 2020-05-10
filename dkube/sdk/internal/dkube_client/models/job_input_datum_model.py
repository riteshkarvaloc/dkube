# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobInputDatumModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'version': 'str',
        'mountpath': 'str'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'mountpath': 'mountpath'
    }

    def __init__(self, name=None, version=None, mountpath=None):  # noqa: E501
        """JobInputDatumModel - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._version = None
        self._mountpath = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if mountpath is not None:
            self.mountpath = mountpath

    @property
    def name(self):
        """Gets the name of this JobInputDatumModel.  # noqa: E501


        :return: The name of this JobInputDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobInputDatumModel.


        :param name: The name of this JobInputDatumModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this JobInputDatumModel.  # noqa: E501


        :return: The version of this JobInputDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this JobInputDatumModel.


        :param version: The version of this JobInputDatumModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def mountpath(self):
        """Gets the mountpath of this JobInputDatumModel.  # noqa: E501


        :return: The mountpath of this JobInputDatumModel.  # noqa: E501
        :rtype: str
        """
        return self._mountpath

    @mountpath.setter
    def mountpath(self, mountpath):
        """Sets the mountpath of this JobInputDatumModel.


        :param mountpath: The mountpath of this JobInputDatumModel.  # noqa: E501
        :type: str
        """

        self._mountpath = mountpath

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(JobInputDatumModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobInputDatumModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
