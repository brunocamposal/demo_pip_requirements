from src.soma import soma
def test_deve_retornar_a_soma_entre_dois_numeros():
    result = soma(1, 2)
    expected = 3

    assert result == expected
