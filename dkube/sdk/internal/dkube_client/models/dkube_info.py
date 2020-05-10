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


class DkubeInfo(object):
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
        'version': 'str',
        'platform': 'str',
        'license': 'DkubeInfoLicense',
        'release': 'DkubeInfoRelease',
        'auth': 'AuthModel',
        'rdma': 'bool',
        'frameworks': 'list[str]',
        'tensorflow': 'DLSupportTensorflow'
    }

    attribute_map = {
        'version': 'version',
        'platform': 'platform',
        'license': 'license',
        'release': 'release',
        'auth': 'auth',
        'rdma': 'rdma',
        'frameworks': 'frameworks',
        'tensorflow': 'tensorflow'
    }

    def __init__(self, version=None, platform=None, license=None, release=None, auth=None, rdma=False, frameworks=None, tensorflow=None):  # noqa: E501
        """DkubeInfo - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._platform = None
        self._license = None
        self._release = None
        self._auth = None
        self._rdma = None
        self._frameworks = None
        self._tensorflow = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if platform is not None:
            self.platform = platform
        if license is not None:
            self.license = license
        if release is not None:
            self.release = release
        if auth is not None:
            self.auth = auth
        if rdma is not None:
            self.rdma = rdma
        if frameworks is not None:
            self.frameworks = frameworks
        if tensorflow is not None:
            self.tensorflow = tensorflow

    @property
    def version(self):
        """Gets the version of this DkubeInfo.  # noqa: E501


        :return: The version of this DkubeInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DkubeInfo.


        :param version: The version of this DkubeInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def platform(self):
        """Gets the platform of this DkubeInfo.  # noqa: E501


        :return: The platform of this DkubeInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DkubeInfo.


        :param platform: The platform of this DkubeInfo.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def license(self):
        """Gets the license of this DkubeInfo.  # noqa: E501


        :return: The license of this DkubeInfo.  # noqa: E501
        :rtype: DkubeInfoLicense
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this DkubeInfo.


        :param license: The license of this DkubeInfo.  # noqa: E501
        :type: DkubeInfoLicense
        """

        self._license = license

    @property
    def release(self):
        """Gets the release of this DkubeInfo.  # noqa: E501


        :return: The release of this DkubeInfo.  # noqa: E501
        :rtype: DkubeInfoRelease
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this DkubeInfo.


        :param release: The release of this DkubeInfo.  # noqa: E501
        :type: DkubeInfoRelease
        """

        self._release = release

    @property
    def auth(self):
        """Gets the auth of this DkubeInfo.  # noqa: E501


        :return: The auth of this DkubeInfo.  # noqa: E501
        :rtype: AuthModel
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this DkubeInfo.


        :param auth: The auth of this DkubeInfo.  # noqa: E501
        :type: AuthModel
        """

        self._auth = auth

    @property
    def rdma(self):
        """Gets the rdma of this DkubeInfo.  # noqa: E501


        :return: The rdma of this DkubeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._rdma

    @rdma.setter
    def rdma(self, rdma):
        """Sets the rdma of this DkubeInfo.


        :param rdma: The rdma of this DkubeInfo.  # noqa: E501
        :type: bool
        """

        self._rdma = rdma

    @property
    def frameworks(self):
        """Gets the frameworks of this DkubeInfo.  # noqa: E501


        :return: The frameworks of this DkubeInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._frameworks

    @frameworks.setter
    def frameworks(self, frameworks):
        """Sets the frameworks of this DkubeInfo.


        :param frameworks: The frameworks of this DkubeInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["tensorflow"]  # noqa: E501
        if not set(frameworks).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `frameworks` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(frameworks) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._frameworks = frameworks

    @property
    def tensorflow(self):
        """Gets the tensorflow of this DkubeInfo.  # noqa: E501


        :return: The tensorflow of this DkubeInfo.  # noqa: E501
        :rtype: DLSupportTensorflow
        """
        return self._tensorflow

    @tensorflow.setter
    def tensorflow(self, tensorflow):
        """Sets the tensorflow of this DkubeInfo.


        :param tensorflow: The tensorflow of this DkubeInfo.  # noqa: E501
        :type: DLSupportTensorflow
        """

        self._tensorflow = tensorflow

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
        if issubclass(DkubeInfo, dict):
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
        if not isinstance(other, DkubeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
