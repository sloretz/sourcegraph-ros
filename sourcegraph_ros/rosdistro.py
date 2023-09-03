from urllib.parse import urlparse, urlunparse

import requests
import yaml


class Index:

    def __init__(self, url, content):
        self._url = url
        self._content = yaml.safe_load(content)

        if 'type' not in self._content or self._content["type"] != "index":
            raise ValueError("Content does not appear to be a valid index.")

    def get_distro(self, name):
        """Get a ROS distro from this index, if there is one with that name."""
        if name not in self.distro_names:
            return None
        url_suffix = self._content['distributions'][name]['distribution'][0]
        return ROSDistro.from_url(name, self._base_url + '/' + url_suffix)

    @property
    def distro_names(self):
        """Get all distros in the index."""
        if 'distributions' in self._content:
            return [d for d in self._content['distributions'].keys()]
        return []

    @property
    def version(self):
        """Return version number, else None if it can't be determined."""
        if "version" in self._content:
            return self._content["version"]

    @classmethod
    def from_url(cls, url):
        resp = requests.get(url)
        if resp.status_code != 200:
            raise RuntimeError("Failed to download URL")
        return cls(url, resp.content)
    
    @property
    def _base_url(self):
        u = urlparse(self._url)
        base_path = "/".join(u.path.split("/")[:-1])
        return urlunparse(u._replace(path=base_path))


class ROSDistro:
    """Gets info about a ROS distribution from github.com/ros/rosdistro."""

    def __init__(self, name, content):
        self._name = name
        self._content = yaml.safe_load(content)

        if 'type' not in self._content or self._content["type"] != "distribution":
            raise ValueError("Content does not appear to be a valid distribution.")

    @property
    def name(self):
        return self._name
    
    @classmethod
    def from_url(cls, name, url):
        resp = requests.get(url)
        if resp.status_code != 200:
            raise RuntimeError("Failed to download URL")
        return cls(name, resp.content)
    
    @property
    def version(self):
        """Return version number, else None if it can't be determined."""
        if "version" in self._content:
            return self._content["version"]

    @property
    def repository_names(self):
        """Get all repository names in the distro."""
        if 'repositories' in self._content:
            return [r for r in self._content['repositories'].keys()]
        return []
    
    def get_repository(self, name):
        """Get a repository from this distribution, if there is one with that name."""
        if name not in self.repository_names:
            return None
        return Repository(name, self._content['repositories'][name])


class Repository:

    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def name(self):
        return self._name
    
    @property
    def source_type(self):
        """If the repository has a source entry, this returns the VCS type."""
        if "source" in self._content:
            return self._content["source"]["type"]
        
    @property
    def source_url(self):
        """If the repository has a source entry, this returns the url."""
        if "source" in self._content:
            return self._content["source"]["url"]
        
    @property
    def source_version(self):
        """
        If the repository has a source entry, this returns the
        version, usually meaning the branch name to check out.
        """
        if "source" in self._content:
            return self._content["source"]["version"]

    @property
    def release_package_names(self):
        """
        Return list of names of packages in release entry, if there is
        one.
        """
        if "release" in self._content:
            if "packages" in self._content["release"]:
                return [p for p in self._content["release"]["packages"]]
            else:
                return [self._name]
        return []
    
    @property
    def release_url(self):
        """Return url of the release repository, if there is one."""
        if "release" in self._content:
            return self._content["release"]["url"]
        
    @property
    def release_version(self):
        """Return version of released packages, if there is a release."""
        if "release" in self._content:
            return self._content["release"]["version"]
        
    @property
    def release_tags(self):
        """
        Return unexpanded tag used to get source code of a released package,
        if there is a release.
        """
        if "release" in self._content:
            return self._content["release"]["tags"]["release"]
        
    def get_release_tag_for_package(self, package_name):
        if package_name in self.release_package_names:
            return self.release_tags.format(
                package=package_name,
                version=self.release_version
            )