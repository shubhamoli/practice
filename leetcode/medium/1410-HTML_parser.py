"""
    Leetcode #1410
"""


class Solution:
    def entityParser(self, text: str) -> str:
        entities = {'&quot;': '"', '&apos;': "'", '&amp;': '&', '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        parsed = []
        i = 0
        while i < len(text):
            window = text[i:i + 7]
            for key in entities:
                if window.startswith(key):
                    parsed.append(entities[key])
                    i += len(key)
                    break
            else:
                parsed.append(text[i])
                i += 1

        return ''.join(parsed)


if __name__ == "__main__":

    solution = Solution()

    assert solution.entityParser("&amp; is an HTML entity but &ambassador; is not.") == "& is an HTML entity but &ambassador; is not."
