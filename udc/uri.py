# Parse a UDC "app+protocol://" URI

from urllib.parse import parse_qs, urlparse

SEP = "+"
K_TOOL = "_tool"
K_PROT = "_protocol"
K_QRY = "_query"


class UdcUri:
    def __init__(self, uri_string: str):
        self.uri = urlparse(uri_string)
        self.attrs = self.parse_fragments(self.uri.fragment)
        self.parse_scheme(self.uri.scheme)
        self.attrs[K_QRY] = self.uri.query

    def __str__(self):
        return self.__repr__()

    def get(self, key):
        return self.attrs.get(key)

    def parse_fragments(self, fragment: str):
        list_dict = parse_qs(fragment)
        scalars = {k: v[0] for k, v in list_dict.items()}
        return scalars

    def parse_scheme(self, scheme: str):
        schemes = scheme.split(SEP)
        if len(schemes) != 2:
            raise ValueError(
                f"Error: URI scheme `{self.uri.scheme}` does not contain '{SEP}'"
            )
        self.attrs[K_TOOL] = schemes[0]
        self.attrs[K_PROT] = schemes[1]

    def tool(self):
        return self.attrs[K_TOOL]

    def endpoint(self):
        return f"{self.attrs[K_PROT]}://{self.uri.hostname}"
