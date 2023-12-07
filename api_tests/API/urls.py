from api_tests.helpers.project_helpers import get_base_url
from api_tests.helpers.url_helpers import url_join
from api_tests.helpers.project_exceptions import UnknownAPIVersionException


class GoRestURLs:

    USERS = 'users'
    POSTS = 'posts'
    COMMENTS = 'comments'
    TODOS = 'todos'

    def _get_version(self, version):
        """Returns version component of url by number"""
        versions = {0: 'public-api',
                    1: 'public/v1',
                    2: 'public/v2',
                    }
        try:
            return versions[version]
        except KeyError:
            raise UnknownAPIVersionException(f'Unknown API version: {version}. Should be one of {set(versions.keys())}')

    def users_url(self, version, user=''):
        return url_join(get_base_url(), self._get_version(version), GoRestURLs.USERS, user)

    def posts_url(self, version, user=''):
        return url_join(get_base_url(), self._get_version(version), user, GoRestURLs.POSTS)

    def comments_url(self, version, user=''):
        return url_join(get_base_url(), self._get_version(version), user, GoRestURLs.COMMENTS)

    def todos_url(self, version, user=''):
        return url_join(get_base_url(), self._get_version(version), user, GoRestURLs.TODOS)


if __name__ == '__main__':
    gorest_urls = GoRestURLs()
    print(gorest_urls._get_version(0))
    #print(gorest_urls._get_version(10))
    print(gorest_urls.users_url(0))
    print(gorest_urls.users_url(2, '12345'))
    print(gorest_urls.posts_url(1))
    print(gorest_urls.posts_url(2, '54321'))
