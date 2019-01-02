from . import IRISClassifier

def test_IRISClassifier():
    assert IRISClassifier.apply("Jane") == "hello Jane"
