import piskvorky

def test_ok_vyhodnoceni():
    assert piskvorky.vyhodnot ("---xxxoxo--") == "x"
    assert piskvorky.vyhodnot ("oooxx--xx") == "o"
    assert piskvorky.vyhodnot ("oxoxoxoxox") == "!"
    assert piskvorky.vyhodnot ("----------") == "-"

def test_tah ():
    assert piskvorky.tah ("-----", 2, "x") == "--x--"
    assert piskvorky.tah ("-----", 0, "o") == "o----"
