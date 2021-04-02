from model.data import Node, Edge

from typing import List, Dict, Tuple

SIZE: Tuple[int, int] = (500, 500)

NODES: Dict[str, Node] = {
    'N11': Node(50, 50), 'N12': Node(100, 50), 'N13': Node(150, 50), 'N14': Node(200, 50), 'N15': Node(250, 50), 'N16': Node(300, 50), 'N17': Node(350, 50), 'N18': Node(400, 50), 'N19': Node(450, 50),
    'N21': Node(50, 100), 'N22': Node(100, 100), 'N23': Node(150, 100), 'N24': Node(200, 100), 'N25': Node(250, 100), 'N26': Node(300, 100), 'N27': Node(350, 100), 'N28': Node(400, 100), 'N29': Node(450, 100),
    'N31': Node(50, 150), 'N32': Node(100, 150), 'N33': Node(150, 150), 'N34': Node(200, 150), 'N35': Node(250, 150), 'N36': Node(300, 150), 'N37': Node(350, 150), 'N38': Node(400, 150), 'N39': Node(450, 150),
    'N41': Node(50, 200), 'N42': Node(100, 200), 'N43': Node(150, 200), 'N44': Node(200, 200), 'N45': Node(250, 200), 'N46': Node(300, 200), 'N47': Node(350, 200), 'N48': Node(400, 200), 'N49': Node(450, 200),
    'N51': Node(50, 250), 'N52': Node(100, 250), 'N53': Node(150, 250), 'N54': Node(200, 250), 'N55': Node(250, 250), 'N56': Node(300, 250), 'N57': Node(350, 250), 'N58': Node(400, 250), 'N59': Node(450, 250),
    'N61': Node(50, 300), 'N62': Node(100, 300), 'N63': Node(150, 300), 'N64': Node(200, 300), 'N65': Node(250, 300), 'N66': Node(300, 300), 'N67': Node(350, 300), 'N68': Node(400, 300), 'N69': Node(450, 300),
    'N71': Node(50, 350), 'N72': Node(100, 350), 'N73': Node(150, 350), 'N74': Node(200, 350), 'N75': Node(250, 350), 'N76': Node(300, 350), 'N77': Node(350, 350), 'N78': Node(400, 350), 'N79': Node(450, 350),
    'N81': Node(50, 400), 'N82': Node(100, 400), 'N83': Node(150, 400), 'N84': Node(200, 400), 'N85': Node(250, 400), 'N86': Node(300, 400), 'N87': Node(350, 400), 'N88': Node(400, 400), 'N89': Node(450, 400),
    'N91': Node(50, 450), 'N92': Node(100, 450), 'N93': Node(150, 450), 'N94': Node(200, 450), 'N95': Node(250, 450), 'N96': Node(300, 450), 'N97': Node(350, 450), 'N98': Node(400, 450), 'N99': Node(450, 450),
}

EDGES: List[Edge] = [
    Edge(NODES['N11'], NODES['N12']), Edge(NODES['N12'], NODES['N13']), Edge(NODES['N13'], NODES['N14']), Edge(NODES['N14'], NODES['N15']), Edge(NODES['N15'], NODES['N16']), Edge(NODES['N16'], NODES['N17']), Edge(NODES['N17'], NODES['N18']), Edge(NODES['N18'], NODES['N19']),
    Edge(NODES['N21'], NODES['N22']), Edge(NODES['N22'], NODES['N23']), Edge(NODES['N23'], NODES['N24']), Edge(NODES['N24'], NODES['N25']), Edge(NODES['N25'], NODES['N26']), Edge(NODES['N26'], NODES['N27']), Edge(NODES['N27'], NODES['N28']), Edge(NODES['N28'], NODES['N29']),
    Edge(NODES['N31'], NODES['N32']), Edge(NODES['N32'], NODES['N33']), Edge(NODES['N33'], NODES['N34']), Edge(NODES['N34'], NODES['N35']), Edge(NODES['N35'], NODES['N36']), Edge(NODES['N36'], NODES['N37']), Edge(NODES['N37'], NODES['N38']), Edge(NODES['N38'], NODES['N39']),
    Edge(NODES['N41'], NODES['N42']), Edge(NODES['N42'], NODES['N43']), Edge(NODES['N43'], NODES['N44']), Edge(NODES['N44'], NODES['N45']), Edge(NODES['N45'], NODES['N46']), Edge(NODES['N46'], NODES['N47']), Edge(NODES['N47'], NODES['N48']), Edge(NODES['N48'], NODES['N49']),
    Edge(NODES['N51'], NODES['N52']), Edge(NODES['N52'], NODES['N53']), Edge(NODES['N53'], NODES['N54']), Edge(NODES['N54'], NODES['N55']), Edge(NODES['N55'], NODES['N56']), Edge(NODES['N56'], NODES['N57']), Edge(NODES['N57'], NODES['N58']), Edge(NODES['N58'], NODES['N59']),
    Edge(NODES['N61'], NODES['N62']), Edge(NODES['N62'], NODES['N63']), Edge(NODES['N63'], NODES['N64']), Edge(NODES['N64'], NODES['N65']), Edge(NODES['N65'], NODES['N66']), Edge(NODES['N66'], NODES['N67']), Edge(NODES['N67'], NODES['N68']), Edge(NODES['N68'], NODES['N69']),
    Edge(NODES['N71'], NODES['N72']), Edge(NODES['N72'], NODES['N73']), Edge(NODES['N73'], NODES['N74']), Edge(NODES['N74'], NODES['N75']), Edge(NODES['N75'], NODES['N76']), Edge(NODES['N76'], NODES['N77']), Edge(NODES['N77'], NODES['N78']), Edge(NODES['N78'], NODES['N79']),
    Edge(NODES['N81'], NODES['N82']), Edge(NODES['N82'], NODES['N83']), Edge(NODES['N83'], NODES['N84']), Edge(NODES['N84'], NODES['N85']), Edge(NODES['N85'], NODES['N86']), Edge(NODES['N86'], NODES['N87']), Edge(NODES['N87'], NODES['N88']), Edge(NODES['N88'], NODES['N89']),
    Edge(NODES['N91'], NODES['N92']), Edge(NODES['N92'], NODES['N93']), Edge(NODES['N93'], NODES['N94']), Edge(NODES['N94'], NODES['N95']), Edge(NODES['N95'], NODES['N96']), Edge(NODES['N96'], NODES['N97']), Edge(NODES['N97'], NODES['N98']), Edge(NODES['N98'], NODES['N99']),
    Edge(NODES['N11'], NODES['N21']), Edge(NODES['N12'], NODES['N22']), Edge(NODES['N13'], NODES['N23']), Edge(NODES['N14'], NODES['N24']), Edge(NODES['N15'], NODES['N25']), Edge(NODES['N16'], NODES['N26']), Edge(NODES['N17'], NODES['N27']), Edge(NODES['N18'], NODES['N28']), Edge(NODES['N19'], NODES['N29']),
    Edge(NODES['N21'], NODES['N31']), Edge(NODES['N22'], NODES['N32']), Edge(NODES['N23'], NODES['N33']), Edge(NODES['N24'], NODES['N34']), Edge(NODES['N25'], NODES['N35']), Edge(NODES['N26'], NODES['N36']), Edge(NODES['N27'], NODES['N37']), Edge(NODES['N28'], NODES['N38']), Edge(NODES['N29'], NODES['N39']),
    Edge(NODES['N31'], NODES['N41']), Edge(NODES['N32'], NODES['N42']), Edge(NODES['N33'], NODES['N43']), Edge(NODES['N34'], NODES['N44']), Edge(NODES['N35'], NODES['N45']), Edge(NODES['N36'], NODES['N46']), Edge(NODES['N37'], NODES['N47']), Edge(NODES['N38'], NODES['N48']), Edge(NODES['N39'], NODES['N49']),
    Edge(NODES['N41'], NODES['N51']), Edge(NODES['N42'], NODES['N52']), Edge(NODES['N43'], NODES['N53']), Edge(NODES['N44'], NODES['N54']), Edge(NODES['N45'], NODES['N55']), Edge(NODES['N46'], NODES['N56']), Edge(NODES['N47'], NODES['N57']), Edge(NODES['N48'], NODES['N58']), Edge(NODES['N49'], NODES['N59']),
    Edge(NODES['N51'], NODES['N61']), Edge(NODES['N52'], NODES['N62']), Edge(NODES['N53'], NODES['N63']), Edge(NODES['N54'], NODES['N64']), Edge(NODES['N55'], NODES['N65']), Edge(NODES['N56'], NODES['N66']), Edge(NODES['N57'], NODES['N67']), Edge(NODES['N58'], NODES['N68']), Edge(NODES['N59'], NODES['N69']),
    Edge(NODES['N61'], NODES['N71']), Edge(NODES['N62'], NODES['N72']), Edge(NODES['N63'], NODES['N73']), Edge(NODES['N64'], NODES['N74']), Edge(NODES['N65'], NODES['N75']), Edge(NODES['N66'], NODES['N76']), Edge(NODES['N67'], NODES['N77']), Edge(NODES['N68'], NODES['N78']), Edge(NODES['N69'], NODES['N79']),
    Edge(NODES['N71'], NODES['N81']), Edge(NODES['N72'], NODES['N82']), Edge(NODES['N73'], NODES['N83']), Edge(NODES['N74'], NODES['N84']), Edge(NODES['N75'], NODES['N85']), Edge(NODES['N76'], NODES['N86']), Edge(NODES['N77'], NODES['N87']), Edge(NODES['N78'], NODES['N88']), Edge(NODES['N79'], NODES['N89']),
    Edge(NODES['N81'], NODES['N91']), Edge(NODES['N82'], NODES['N92']), Edge(NODES['N83'], NODES['N93']), Edge(NODES['N84'], NODES['N94']), Edge(NODES['N85'], NODES['N95']), Edge(NODES['N86'], NODES['N96']), Edge(NODES['N87'], NODES['N97']), Edge(NODES['N88'], NODES['N98']), Edge(NODES['N89'], NODES['N99']),
]

START_NODE = NODES['N11']
GOAL_NODE = NODES['N99']
