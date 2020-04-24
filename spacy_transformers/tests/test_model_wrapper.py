import pytest
import spacy
from thinc.api import Model
from transformers import AutoModel
from ..model_wrapper import TransformerByName


MODEL_NAMES = ["distilbert-base-uncased"]
# "bert-base-uncased", "gpt2", "xlnet-base-cased"]


@pytest.fixture
def nlp():
    return spacy.blank("en")


@pytest.fixture
def docs(nlp):
    texts = ["the cat sat on the mat.", "hello world."]
    return [nlp(text) for text in texts]


@pytest.fixture(scope="session", params=MODEL_NAMES)
def name(request):
    return request.param


@pytest.fixture(scope="session")
def trf_model(name):
    return TransformerByName(name)


def test_model_init(name, trf_model):
    assert isinstance(trf_model, Model)


def test_model_predict(docs, trf_model):
    outputs = trf_model.predict(docs)