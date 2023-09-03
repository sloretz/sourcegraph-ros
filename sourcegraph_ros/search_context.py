import json

class SearchContext:

    def __init__(self):
        self._repositories = {}

    def add_repository(self, url, revision=None):
        url = self._cleanup_url(url)
        if url not in self._repositories:
            self._repositories[url] = []
        if not revision:
            revision = "HEAD"
        if revision not in self._repositories[url]:
            self._repositories[url].append(revision)

    def json(self):
        output = []
        for repo, revisions in self._repositories.items():
            output.append({
                "repository": repo,
                "revisions": [r for r in revisions],   
            })
        return json.dumps(output)
    
    def _cleanup_url(self, url):
        if url.lower().startswith("https://"):
            url = url[len("https://"):]
        if url.lower().endswith(".git"):
            url = url[:-len(".git")]
        return url
    
    @classmethod
    def from_rosdistro(cls, distro):
        s = cls()
        repo_names = distro.repository_names
        for name in repo_names:
            r = distro.get_repository(name)
            # Prefer source URL
            if r.source_url and r.source_version:
                s.add_repository(r.source_url, r.source_version)
            elif r.release_url:
                packages = r.release_package_names
                for p in packages:
                    tag = r.get_release_tag_for_package(p)
                    s.add_repository(r.release_url, tag)
        return s