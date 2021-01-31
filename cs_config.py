from os import path


DATA_PATH = path.join('..', 'data', 'input', 'raw_data_dump.json')

VALUES = ('high value', 'certain value', 'potential value', 'no value')

SS_1 = {'navigation equipment', 'leadership role in an organization'}
SD_1 = {'aural transfer', 'semiconductor chip product',
        'distributive share of the income'}
LS_1 = {'preexisting work'}
LD_1 = {'audiovisual work'}

SS_2 = {'nonindustrial use', 'significant property damage'}
SD_2 = {'nonmonetary benefits', 'basic allowance for subsistence',
        'stored electronically'}
LS_2 = {'independent economic value'}
LD_2 = {'technological measure'}

SS_3 = {'unduly disrupt the operations', 'substantial portion of the public'}
SD_3 = {'small manufacturer', 'accommodation trade', 'standard coin'}
LS_3 = {'residential dwelling'}
LD_3 = {'common business purpose'}

SS_4 = {'hazardous liquid', 'fully amortize'}
SD_4 = {'security vulnerability', 'familiar symbol', 'mechanical recordation'}
LS_4 = {'electronic signature'}
LD_4 = {'fermented liquor'}

SS_5 = {'hybrid instrument', 'unreasonably low prices'}
SD_5 = {'gas pipeline facility', 'preemployment testing',
        'final average compensation'}
LS_5 = {'identifying particular'}
LD_5 = {'useful improvement'}

SS_6 = {'dischargeable consumer debt', 'cybercrime'}
SD_6 = {'digital musical recording', 'viticultural',
        'dependent on hours worked'}
LS_6 = {'essential step'}
LD_6 = {'switchblade knife'}

SS = SS_1.union(SS_2).union(SS_3).union(SS_4).union(SS_5).union(SS_6)
SD = SD_1.union(SD_2).union(SD_3).union(SD_4).union(SD_5).union(SD_6)
LS = LS_1.union(LS_2).union(LS_3).union(LS_4).union(LS_5).union(LS_6)
LD = LD_1.union(LD_2).union(LD_3).union(LD_4).union(LD_5).union(LD_6)
S = SS.union(SD)
L = LS.union(LD)

FOLD_1 = SS_1.union(SD_1).union(LS_1).union(LD_1)
FOLD_2 = SS_2.union(SD_2).union(LS_2).union(LD_2)
FOLD_3 = SS_3.union(SD_3).union(LS_3).union(LD_3)
FOLD_4 = SS_4.union(SD_4).union(LS_4).union(LD_4)
FOLD_5 = SS_5.union(SD_5).union(LS_5).union(LD_5)
FOLD_6 = SS_6.union(SD_6).union(LS_6).union(LD_6)

FOLDS = (FOLD_1, FOLD_2, FOLD_3, FOLD_4, FOLD_5, FOLD_6)

SCALE_FEATURES = [
    'Word Count', 'Exp Word Count', 'Exp Word Ratio', 'Quote Count',
    'Min Quote Len', 'Max Quote Len', 'Quote Ratio',
    '-2s:Word Count', '-2s:Exp Word Count', '-2s:Exp Word Ratio',
    '-2s:Quote Count', '-2s:Min Quote Len', '-2s:Max Quote Len',
    '-2s:Quote Ratio', '-1s:Word Count', '-1s:Exp Word Count',
    '-1s:Exp Word Ratio', '-1s:Quote Count', '-1s:Min Quote Len',
    '-1s:Max Quote Len', '-1s:Quote Ratio', '+1s:Word Count',
    '+1s:Exp Word Count', '+1s:Exp Word Ratio', '+1s:Quote Count',
    '+1s:Min Quote Len', '+1s:Max Quote Len', '+1s:Quote Ratio',
    '+2s:Word Count', '+2s:Exp Word Count', '+2s:Exp Word Ratio',
    '+2s:Quote Count', '+2s:Min Quote Len', '+2s:Max Quote Len',
    '+2s:Quote Ratio', 'p:Word Count', 'p:Exp Word Count',
    'p:Exp Word Ratio', 'p:Quote Count', 'p:Min Quote Len',
    'p:Max Quote Len', 'p:Quote Ratio', 'o:Word Count',
    'c:Word Count', 'prv:Word Count', 'BM25', 'TF',
    'Max Qry/Qte Ratio', 'Dist to Root', 'Subtree Size',
    'Ancestors Size', 'Exp in Path', 'Min Dist to Exp', '-2s:BM25',
    '-2s:TF', '-2s:Max Qry/Qte Ratio', '-2s:Dist to Root',
    '-2s:Subtree Size', '-2s:Ancestors Size', '-2s:Exp in Path',
    '-2s:Min Dist to Exp', '-1s:BM25', '-1s:TF',
    '-1s:Max Qry/Qte Ratio', '-1s:Dist to Root', '-1s:Subtree Size',
    '-1s:Ancestors Size', '-1s:Exp in Path', '-1s:Min Dist to Exp',
    '+1s:BM25', '+1s:TF', '+1s:Max Qry/Qte Ratio', '+1s:Dist to Root',
    '+1s:Subtree Size', '+1s:Ancestors Size', '+1s:Exp in Path',
    '+1s:Min Dist to Exp', '+2s:BM25', '+2s:TF',
    '+2s:Max Qry/Qte Ratio', '+2s:Dist to Root', '+2s:Subtree Size',
    '+2s:Ancestors Size', '+2s:Exp in Path', '+2s:Min Dist to Exp',
    'par:BM25', 'par:TF', 'opn:BM25', 'opn:TF', 'cas:BM25', 'cas:TF',
    'New Words', 'New Words Ratio', '-2s:New Words',
    '-2s:New Words Ratio', '-1s:New Words', '-1s:New Words Ratio',
    '+1s:New Words', '+1s:New Words Ratio', '+2s:New Words',
    '+2s:New Words Ratio', 'par:New Words', 'par:New Words Ratio',
    'par:LDA', 'par:DESMIO', 'opn:LDA', 'opn:DESMIO', 'cas:fastSIF',
    'cas:LDA', 'cas:DESMIO'
]
QRY_WIDE_FEATURES = [
    'Qry Word Count', 'prv:Word Count', 'prv:Exp Word Count',
    'prv:Exp Word Ratio', 'prv:Quote Count', 'prv:Min Quote Len',
    'prv:Max Quote Len', 'prv:Quote Ratio', 'Number of Cases',
    'Number of Opinions', 'Number of Paragraphs',
    'Number of Sentences', 'Sentence/Case Ratio'
]
TOIS = FOLD_1.union(FOLD_2).union(FOLD_3).union(FOLD_4).union(FOLD_5)\
        .union(FOLD_6)

