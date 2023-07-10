def solution(l):
    def version_key(version):
        components = version.split('.')
        padded_components = [c.rjust(3, '0') for c in components]
        return tuple(map(int, padded_components))

    sorted_versions = sorted(l, key=version_key)
    return sorted_versions
