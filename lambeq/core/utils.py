from __future__ import annotations

import importlib
from typing import List, Union

SentenceType = Union[str, List[str]]
SentenceBatchType = Union[List[str], List[List[str]]]


def tokenised_sentence_type_check(sentence: SentenceType) -> bool:
    return isinstance(sentence, list) and all(
            isinstance(token, str) for token in sentence)


def untokenised_batch_type_check(sentence: SentenceBatchType) -> bool:
    return isinstance(sentence, list) and all(
            isinstance(token, str) for token in sentence)


def tokenised_batch_type_check(batch: SentenceBatchType) -> bool:
    return isinstance(batch, list) and all(
            tokenised_sentence_type_check(s) for s in batch)


def is_torch_available() -> bool:
    return importlib.util.find_spec('torch') is not None


def is_transformers_available() -> bool:
    return importlib.util.find_spec('transformers') is not None