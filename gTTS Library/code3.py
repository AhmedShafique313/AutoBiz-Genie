from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols

gtts.tokenizer.symbols.SUB_PAIRS.append(
    ('sub.', 'submarine')
)
test_text = "Have you seen the Queen's new sub.?"
print(pre_processors.word_sub(test_text))