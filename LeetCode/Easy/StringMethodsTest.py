import StringMethods

class StringMethodsTest:
    def longestCommonPrefixTest(self):
        obj = StringMethods.StringMethods()
        args = [
            ["flower", "flow", "flight"], # Shortest = 4 , Strs = 3
            ["dog","racecar","car"],
            [""],
            ["", ""],
            ["ab", "a"],
            ["flower","flower","flower","flower"] # Shortest = 6 , Strs = 4
        ]
        for i in args:
            print(f"Testing {i}:", obj.longestCommonPrefix_14(i))