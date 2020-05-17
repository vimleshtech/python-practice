#Handling Text
'''
text=­'Some words'
assign string
list(­text)
Split text into character tokens
set(t­ext)
Unique tokens
len(t­ext)
Number of characters
'''

#Sentence Parsing
'''
g=nlt­k.d­ata.lo­ad(­'gr­amm­ar.c­fg')
Load a grammar from a file
g=nlt­k.C­FG.f­ro­mst­rin­g("""...""")
Manually define grammar
parse­r=n­ltk.Ch­art­Par­ser(g)
Create a parser out of the grammar
trees­=pa­rse­r.p­ars­e_a­ll(­text)
for tree in trees: ... print tree
from nltk.c­orpus import treebank
treeb­ank.pa­rse­d_s­ent­s('­wsj­_00­01.m­rg')
'''

#Accessing corpora and lexical resources
'''
from nltk.c­orpus import brown
import Corpus­Reader object
brown.wo­rds­(te­xt_id)
Returns pretok­enised document as list of words
brown.fi­lei­ds()
Lists docs in Brown corpus
brown.ca­teg­ori­es()
Lists categories in Brown corpus
'''
#Tokenization
'''
text.s­pl­it(­" ")
Split by space
nltk.w­or­d_t­oke­niz­er(­text)
nltk in-built word tokenizer
nltk.s­en­t_t­oke­niz­e(doc)
nltk in-built sentence tokenizer
'''
#Lemmatization & Stemming
'''
input­="List listed lists listing listin­gs"
Different suffixes
words­=in­put.lo­wer­().s­plit(' ')
Normalize (lower­case) words
porte­r=n­ltk.Po­rte­rSt­emmer
Initialise Stemmer
[port­er.s­tem(t) for t in words]
Create list of stems
WNL=n­ltk.Wo­rdN­etL­emm­ati­zer()
Initialise WordNet lemmatizer
[WNL.l­em­mat­ize(t) for t in words]
Use the lemmatizer
'''
#Part of Speech (POS) Tagging
'''
nltk.h­el­p.u­pen­n_t­ags­et(­'MD')
Lookup definition for a POS tag
nltk.p­os­_ta­g(w­ords)
nltk in-built POS tagger
 	
<use an altern­ative tagger to illustrate ambigu­ity>
'''

#Text Classi­fic­ation
'''
from sklear­n.f­eat­ure­_ex­tra­cti­on.text import CountV­ect­orizer, TfidfV­ect­orizer
vect=­Cou­ntV­ect­ori­zer­().f­it­(X_­train)
Fit bag of words model to data
vect.g­et­_fe­atu­re_­nam­es()
Get features
vect.t­ra­nsf­orm­(X_­train)
Convert to doc-term matrix
'''

#Entity Recogn­ition (Chunk­ing­/Ch­inking)
'''
g="NP: {<D­T>?­<JJ­>*<­NN>­}"
Regex chunk grammar
cp=nl­tk.R­eg­exp­Par­ser(g)
Parse grammar
ch=cp.pa­rse­(po­s_s­ent)
Parse tagged sent. using grammar
print­(ch)
Show chunks
ch.dr­aw()
Show chunks in IOB tree
cp.ev­alu­ate­(te­st_­sents)
Evaluate against test doc
sents­=nl­tk.c­or­pus.tr­eeb­ank.ta­gge­d_s­ents()
print­(nl­tk.n­e_­chu­nk(­sent))
Print chunk tree
'''


#RegEx with Pandas & Named Groups
'''
df=pd.Da­taF­ram­e(t­ime­_sents, column­s=[­'te­xt'])
df['t­ext­'].s­tr.sp­lit­().s­tr.len()
df['t­ext­'].s­tr.co­nta­ins­('w­ord')
df['t­ext­'].s­tr.co­unt­(r'­\d')
df['t­ext­'].s­tr.fi­nda­ll(­r'\d')
df['t­ext­'].s­tr.re­pla­ce(­r'­\w+d­ay\b', '???')
df['t­ext­'].s­tr.re­pla­ce(­r'(­\w)', lambda x: x.grou­ps(­)[0­][:3])
df['t­ext­'].s­tr.ex­tra­ct(­r'(­\d?­\d)­:(­\d\d)')
df['t­ext­'].s­tr.ex­tra­cta­ll(­r'(­(\d­?\d­):(­\d\d) ?([ap]­m))')
df['t­ext­'].s­tr.ex­tra­cta­ll(­r'(­?P<­dig­its­>\d)')
'''


