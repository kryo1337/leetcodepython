from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        rtr = ""
        for s in strs:
            rtr += f"{len(s)}#{s}"
        return rtr
    
    def decode(self, s: str) -> List[str]:
        rtr = []
        i = 0
        
        while i < len(s):
            delimiter_pos = s.find('#', i)
            length = int(s[i:delimiter_pos])
            
            start = delimiter_pos + 1
            end = start + length
            rtr.append(s[start:end])
            
            i = end
        
        return rtr

def test_basic():
    codec = Codec()
    strs = ["hello", "world"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs

def test_empty_strings():
    codec = Codec()
    strs = ["", "a", ""]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs

def test_special_characters():
    codec = Codec()
    strs = ["a#b", "c:d", "e/f"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs

def test_single_string():
    codec = Codec()
    strs = ["neetcode"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs

if __name__ == "__main__":
    test_basic()
    test_empty_strings()
    test_special_characters()
    test_single_string()
    print("All tests passed.")
