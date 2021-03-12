import unittest

import social


class TestDouban(unittest.TestCase):

    def test_generate_douban(self):
        DOUBAN_NAME = "znyalor"
        DOUBAN_LIMIT = 5

        old_readme = social.DOUBAN_START_COMMENT + "old_content" + social.DOUBAN_END_COMMENT
        new_readme = old_readme

        print("DOUBAN_NAME:" + DOUBAN_NAME)
        print("DOUBAN_LIMIT:" + str(DOUBAN_LIMIT))
        new_readme = social.generate_douban(DOUBAN_NAME, DOUBAN_LIMIT, new_readme)
        print("new_readme:")
        print(new_readme)
        self.assertNotEqual(old_readme, new_readme)


if __name__ == '__main__':
    unittest.main()
