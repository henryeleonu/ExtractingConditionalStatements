import spacy
from spacy.matcher import Matcher
#from spacy.tokens import Span
#from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
#phrase_matcher = PhraseMatcher(nlp.vocab)
# Add match ID "ConditionalSentence" with no callback and one pattern
conditional_pattern = []
#
#if_condition_action_pattern.append({'LOWER': 'if'})

if_condition_action_pattern = [{'LOWER': 'if'}, 
            {'OP': '*'},
            {'DEP': 'nsubj'},
            {'OP': '*'},
            {'POS': 'VERB'},
            {'OP': '*'},
            {'TEXT': ',', 'OP': '?'},
            {'OP': '*'},
            {'DEP': 'nsubj'},
            {'OP': '*'},
            {'POS': 'VERB'}
            #{'OP': '*'},
            #{'TEXT': '.'}
        ]

action_if_conditon_pattern = [ 
            {"OP": "*"},
            {"DEP": "nsubj"},
            {"OP": "*"},
            {"POS": "VERB"},
            {"OP": "*"},
            {"TEXT": ",", "OP": "?"},
            {"LOWER": "if"}, 
            {"OP": "*"},
            {"DEP": "nsubj"},
            {"OP": "*"},
            {"POS": "VERB"}
            #{"OP": "*"},
            #{"TEXT": "."}
        ]

conditional_pattern.append(if_condition_action_pattern)
conditional_pattern.append(action_if_conditon_pattern)
#phrase_matcher.add("ICA",None, *if_condition_action_pattern)
#phrase_matcher.add("AIC",None, *action_if_conditon_pattern)
matcher.add("ICA", conditional_pattern)
#matcher.add("AIC", action_if_conditon_pattern)

doc = nlp("If it had rained, you would have gotten wet. You would have gotten wet if it had rained. What do you mean by that? I don’t care if it rains today.")
"""
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)
"""
for sent in doc.sents:
    matches = matcher(sent)
    #matches = phrase_matcher(sent)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = sent[start:end]  # The matched span
        #print(match_id, string_id, start, end, span.text)
        print(string_id, start, end, span.text)
