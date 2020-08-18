import json

foods = dict()

foods["apple"] = {
    "name": "Apfel",
    "img": "assets/img/apple.jpg",
    "infoURL": "https://de.wikipedia.org/wiki/Kulturapfel",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [1.0, 1.0, 1.0,  1.0, 0.5, 0.5,   0.5, 1.0, 1.0,  1.0, 1.0, 1.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['apricot'] = {
    "name": "Aprikose",
    "img": "assets/img/apricot.jpg",
    "infoURL": "https://de.wikipedia.org/wiki/Aprikose",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.5, 0.5, 0.5,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 1.0, 1.0,   1.0, 1.0, 1.0,  0.0, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['pear'] = {
    "name": "Birne",
    "img": "assets/img/pear.jpg",
    "infoURL": "https://de.wikipedia.org/wiki/Birnen",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.5, 0.5, 0.0,  0.0, 0.0, 0.0,   0.0, 1.0, 1.0,  1.0, 1.0, 0.5],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['blueberry'] = {
    'name': 'Heidelbeere',
    'img': 'assets/img/blueberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Heidelbeere",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   1.0, 1.0, 1.0,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['blackberry'] = {
    'name': 'Brombeere',
    'img': 'assets/img/blackberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Brombeeren",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   1.0, 1.0, 1.0,  0.5, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   0.5, 0.5, 0.5,  0.5, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 0.5, 0.5]
}

foods['strawberry'] = {
    'name': 'Erdbeere',
    'img': 'assets/img/strawberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Erdbeeren",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.5, 1.0, 1.0,   1.0, 0.5, 0.5,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['raspberry'] = {
    'name': 'Himbeere',
    'img': 'assets/img/raspberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Himbeere",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.5, 1.0,   1.0, 0.5, 0.5,  0.5, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['elderberry'] = {
    'name': 'Holunderbeere',
    'img': 'assets/img/elderberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Schwarzer_Holunder",
    'isCommon': 0,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 1.0,  1.0, 0.0, 0.0]
}

foods['gooseberry'] = {
    'name': 'Stachelbeere',
    'img': 'assets/img/gooseberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Stachelbeere",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   1.0, 1.0, 0.5,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   1.0, 1.0, 0.5,  0.0, 0.0, 0.0]

}

foods['banana'] = {
    'name': 'Banane',
    'img': 'assets/img/banana.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Bananen",
    'isCommon': 1,
    'type': 'fruit',
    'seaTransport'            : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0]
}

foods['rhubarb'] = {
    'name': 'Rhabarber',
    'img': 'assets/img/rhubarb.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Gemeiner_Rhabarber",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  1.0, 1.0, 0.5,   0.5, 0.0, 0.0,  0.0, 0.0, 0.0],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['paprika'] = {
    'name': 'Paprika',
    'img': 'assets/img/paprika.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Paprika",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   1.0, 1.0, 1.0,  0.5, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['pineapple'] = {
    'name': 'Ananas',
    'img': 'assets/img/pineapple.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Ananas",
    'isCommon': 1,
    'type': 'fruit',
    'seaTransport'            : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0]
}

foods['avocado'] = {
    'name': 'Avocado',
    'img': 'assets/img/avocado.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Avocado",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['date'] = {
    'name': 'Dattel (frisch)',
    'img': 'assets/img/jujube-date.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Echte_Dattelpalme",
    'isCommon': 0,
    'type': 'fruit',
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['fig'] = {
    'name': 'Feige',
    'img': 'assets/img/fig.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Echte_Feige",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.0, 0.0, 0.0,  0.0, 0.5, 0.5]
}

foods['pomegranate'] = {
    'name': 'Granatapfel',
    'img': 'assets/img/pomegranate.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Granatapfel",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.5, 1.0,  1.0, 1.0, 0.5],
    'flightTransport'         : [0.0, 0.0, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.0,  0.0, 0.0, 0.0]
}

foods['grapefuit'] = {
    'name': 'Grapefruit',
    'img': 'assets/img/grapefruit.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Grapefruit",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [1.0, 1.0, 1.0,  0.5, 0.5, 0.5,   0.0, 0.0, 0.5,  1.0, 1.0, 1.0],
    'seaTransport'            : [0.0, 0.0, 0.0,  0.5, 1.0, 1.0,   1.0, 1.0, 1.0,  0.5, 0.0, 0.0]
}

foods['currant'] = {
    'name': 'Johannisbeere',
    'img': 'assets/img/currant.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Johannisbeeren",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 1.0,   1.0, 1.0, 0.0,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.5, 0.5,  0.0, 0.0, 0.0]
}

foods['persimmon'] = {
    'name': 'Kaki',
    'img': 'assets/img/persimmon.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kaki",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.5, 0.5, 0.5,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  1.0, 1.0, 1.0],
    'seaTransport'            : [0.0, 0.0, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.0,  0.0, 0.0, 0.0]
}

foods['pricklypear'] = {
    'name': 'Kaktusfeige',
    'img': 'assets/img/prickly-pear.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Opuntia_ficus-indica",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['physalis'] = {
    'name': 'Physalis',
    'img': 'assets/img/physalis.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kapstachelbeere",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.5, 0.5,  0.5, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['starfuit'] = {
    'name': 'Sternfrucht',
    'img': 'assets/img/star-fruit.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Sternfrucht",
    'isCommon': 1,
    'type': 'fruit',
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['kiwi'] = {
    'name': 'Kiwi',
    'img': 'assets/img/kiwi.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kiwifrucht",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [1.0, 1.0, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.5, 1.0, 1.0],
    'seaTransport'            : [0.0, 0.0, 0.0,  0.0, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['coco'] = {
    'name': 'Kokosnuss',
    'img': 'assets/img/coco.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kokospalme#Kokosnuss",
    'isCommon': 1,
    'type': 'fruit',
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['lychee'] = {
    'name': 'Litschi',
    'img': 'assets/img/lychee.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Litschibaum",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   0.5, 0.5, 0.5,  0.0, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.0,   0.0, 0.0, 0.0,  0.0, 0.5, 0.5]
}

foods['mango'] = {
    'name': 'Mango',
    'img': 'assets/img/mango.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Mango",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.5, 0.5,  0.5, 0.5, 0.0],
    'flightTransport'         : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0]
}

foods['watermelon'] = {
    'name': 'Wassermelone',
    'img': 'assets/img/watermelon.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Wassermelone",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.5,  0.5, 0.5, 1.0,   1.0, 1.0, 1.0,  1.0, 0.5, 0.0],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 0.0, 0.5]
}

foods['yellowplum'] = {
    'name': 'Mirabelle',
    'img': 'assets/img/yellow-plum.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Mirabelle",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 1.0, 1.0,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   1.0, 1.0, 1.0,  0.5, 0.0, 0.0]
}

foods['nectarine'] = {
    'name': 'Nektarine',
    'img': 'assets/img/nectarine.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Nektarine",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.5, 0.5, 0.5,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.5, 0.5, 1.0,   1.0, 1.0, 1.0,  0.0, 0.0, 0.0],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 0.5, 0.5]
}

foods['papaya'] = {
    'name': 'Papaya',
    'img': 'assets/img/papaya.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Papaya",
    'isCommon': 1,
    'type': 'fruit',
    'flightTransport'         : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0]
}

foods['passionfruit'] = {
    'name': 'Passionsfrucht',
    'img': 'assets/img/passion-fruit.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Passiflora_edulis",
    'isCommon': 1,
    'type': 'fruit',
    'flightTransport'         : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0]
}

foods['peach'] = {
    'name': 'Pfirsich',
    'img': 'assets/img/peach.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Pfirsich",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.5, 0.5, 0.5,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.5, 0.5, 1.0,   1.0, 1.0, 1.0,  0.0, 0.0, 0.0],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 0.5, 0.5]
}

foods['plum'] = {
    'name': 'Pflaume',
    'img': 'assets/img/plum.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Pflaume",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   1.0, 1.0, 1.0,  1.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 1.0,   1.0, 1.0, 1.0,  1.0, 0.0, 0.0]
}

foods['prune'] = {
    'name': 'Zwetschge',
    'img': 'assets/img/prune.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Zwetschge",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   1.0, 1.0, 1.0,  1.0, 0.0, 0.0],
}

foods['dragonfruit'] = {
    'name': 'Drachenfrucht',
    'img': 'assets/img/dragon-fruit.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Drachenfrucht",
    'isCommon': 1,
    'type': 'fruit',
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.0,   0.5, 0.5, 0.0,  0.0, 0.0, 0.5]
}

foods['quince'] = {
    'name': 'Quitte',
    'img': 'assets/img/quince.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Quitte",
    'isCommon': 0,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.5,  0.5, 0.5, 0.0]
}

foods['cherry'] = {
    'name': 'Kirsche',
    'img': 'assets/img/cherry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Vogel-Kirsche",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   1.0, 1.0, 0.5,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.5, 1.0,   1.0, 1.0, 0.5,  0.0, 0.0, 0.0]
}

foods['grapes'] = {
    'name': 'Traube',
    'img': 'assets/img/grapes.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Weintraube",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 1.0,  1.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   1.0, 1.0, 1.0,  1.0, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.0, 0.0, 0.0,  0.0, 0.5, 0.5]
}

foods['amla'] = {
    'name': 'Amla',
    'img': 'assets/img/amla.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Amlabaum",
    'isCommon': 0,
    'type': 'fruit',
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.0,   0.5, 0.5, 0.0,  0.0, 0.0, 0.5]
}

foods['orange'] = {
    'name': 'Orange',
    'img': 'assets/img/orange.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Orange_(Frucht)",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [1.0, 1.0, 1.0,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 0.5, 1.0],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['lemon'] = {
    'name': 'Zitrone',
    'img': 'assets/img/lemon.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Zitrone",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['lime'] = {
    'name': 'Limette',
    'img': 'assets/img/lime.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kulturapfel",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.3, 0.3, 0.3,  0.3, 0.3, 0.3,   0.3, 0.3, 0.3,  0.3, 0.3, 0.3],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['clementine'] = {
    'name': 'Clementine',
    'img': 'assets/img/clementine.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kulturapfel",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.5, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  0.5, 1.0, 1.0],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['honeymelon'] = {
    'name': 'Zuckermelonen',
    'img': 'assets/img/honey-melon.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Zuckermelone",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.5, 1.0,   1.0, 1.0, 1.0,  0.0, 0.0, 0.0],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['nashi'] = {
    'name': 'Nashi',
    'img': 'assets/img/nashi.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Nashi-Birne",
    'isCommon': 1,
    'type': 'fruit',
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['carob'] = {
    'name': 'Johannisbrot',
    'img': 'assets/img/carob.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Johannisbrotbaum",
    'isCommon': 0,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.5,  0.5, 0.5, 0.0]
}

foods['chestnut'] = {
    'name': 'Kastanie',
    'img': 'assets/img/chestnut.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Edelkastanie",
    'isCommon': 1,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.5,  1.0, 0.5, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  0.5, 0.5, 0.5]
}

foods['rosehip'] = {
    'name': 'Hagebutte',
    'img': 'assets/img/rosehip.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Hagebutte",
    'isCommon': 0,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  0.5, 0.5, 0.0]
}

foods['guava'] = {
    'name': 'Guave',
    'img': 'assets/img/guava.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Echte_Guave",
    'isCommon': 1,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  0.3, 0.3, 0.3],
    'flightTransport'         : [0.5, 0.0, 0.5,  0.5, 0.5, 0.5,   0.0, 0.0, 0.5,  0.5, 0.5, 0.5]
}

foods['wildstrawberry'] = {
    'name': 'Walderdbeere',
    'img': 'assets/img/wildstrawberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Wald-Erdbeere",
    'isCommon': 0,
    'type': 'fruit',
    'landTransport'           : [0.3, 0.0, 0.0,  0.0, 0.0, 0.0,   0.3, 0.3, 0.3,  0.0, 0.3, 0.3],
}

foods['sorb'] = {
    'name': 'Eberesche',
    'img': 'assets/img/sorb.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Vogelbeere",
    'isCommon': 0,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.3, 0.3,  0.3, 0.0, 0.0],
}

foods['cranberry'] = {
    'name': 'Cranberry',
    'img': 'assets/img/cranberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Gro%C3%9Ffr%C3%BCchtige_Moosbeere",
    'isCommon': 0,
    'type': 'fruit',
    'flightTransport'         : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.5,  0.5, 0.5, 0.5],
}

foods['cloudberry'] = {
    'name': 'Moltebeere',
    'img': 'assets/img/cloudberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Moltebeere",
    'isCommon': 0,
    'type': 'fruit',
    'landTransport'           : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.3, 0.3, 0.0,  0.0, 0.0, 0.0],
}

foods['lingonberry'] = {
    'name': 'Preiselbeere',
    'img': 'assets/img/lingonberry.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Preiselbeere",
    'isCommon': 0,
    'type': 'fruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.5, 0.5,  0.5, 0.0, 0.0],
}

foods['eggplant'] = {
    'name': 'Aubergine',
    'img': 'assets/img/eggplant.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Aubergine",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.5, 0.5,  0.5, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['batavia'] = {
    'name': 'Bataviasalat',
    'img': 'assets/img/batavia.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Eisbergsalat#Geschichte",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.5, 0.5,   0.5, 0.5, 0.0,  0.0, 0.0, 0.0]
}

foods['spinach'] = {
    'name': 'Spinat',
    'img': 'assets/img/spinach.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Spinat",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.5, 1.0,   1.0, 1.0, 1.0,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['celery-green'] = {
    'name': 'Staudensellerie',
    'img': 'assets/img/celery-green.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Echter_Sellerie#Staudensellerie",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   1.0, 1.0, 1.0,  1.0, 0.5, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['cauliflower'] = {
    'name': 'Blumenkohl',
    'img': 'assets/img/cauliflower.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Blumenkohl",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.5, 1.0,   1.0, 1.0, 1.0,  0.5, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['greenbeans'] = {
    'name': 'Bohnen',
    'img': 'assets/img/green-beans.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Gartenbohne",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.5, 1.0, 1.0,   1.0, 1.0, 0.5,  0.0, 0.0, 0.0],
}

foods['broccoli'] = {
    'name': 'Brokkoli',
    'img': 'assets/img/broccoli.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Brokkoli",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 1.0, 1.0,  0.5, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['champignon'] = {
    'name': 'Champignons',
    'img': 'assets/img/champignon.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Champignons",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['chicory'] = {
    'name': 'Chicorée',
    'img': 'assets/img/chicory.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Chicor%C3%A9e",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.5, 0.5, 0.5]
}

foods['iceberg'] = {
    'name': 'Eisbergsalat',
    'img': 'assets/img/iceberg-salad.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Eisbergsalat",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 1.0,   1.0, 1.0, 1.0,  0.0, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.0,   0.0, 0.0, 0.0,  0.0, 0.5, 0.5]
}

foods['endive'] = {
    'name': 'Endivie',
    'img': 'assets/img/endive-salad.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Endivie",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.0,   0.0, 0.0, 0.0,  0.0, 0.0, 0.5]
}

foods['fieldsalad'] = {
    'name': 'Feldsalat',
    'img': 'assets/img/field-salad.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Gew%C3%B6hnlicher_Feldsalat",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 0.0, 0.5]
}

foods['headlettuce'] = {
    'name': 'Kopfsalat',
    'img': 'assets/img/head-lettuce.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kopfsalat",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.0, 0.0]
}

foods['lollorossa'] = {
    'name': 'Lollo Rossa',
    'img': 'assets/img/lollo-rossa.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Schnittsalat",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 0.0, 0.5]
}

foods['radicchio'] = {
    'name': 'Radicchio',
    'img': 'assets/img/radicchio.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Radicchio",
    'isCommon': 1,
    'type': 'nonFruit',
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.0,   0.0, 0.0, 0.0,  0.5, 0.5, 0.5]
}

foods['chinesecabbage'] = {
    'name': 'Chinakohl',
    'img': 'assets/img/napa-cabbage.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Chinakohl",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['peas'] = {
    'name': 'Erbsen',
    'img': 'assets/img/peas.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Erbse",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   0.5, 0.5, 0.0,  0.0, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['fennel'] = {
    'name': 'Fenchel',
    'img': 'assets/img/fennel.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Fenchel",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 1.0, 1.0,  1.0, 0.5, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['greenonion'] = {
    'name': 'Grüne Zwiebeln',
    'img': 'assets/img/green-onion.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Winterzwiebel",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['sweetcorn'] = {
    'name': 'Mais',
    'img': 'assets/img/sweet-corn.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Mais",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.5, 0.5, 0.5,  0.5, 0.5, 0.0]
}

foods['greencabbage'] = {
    'name': 'Grünkohl',
    'img': 'assets/img/green-cabbage.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Gr%C3%BCnkohl",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [1.0, 1.0, 0.5,  0.0, 0.0, 0.0,   0.0, 0.0, 0.5,  1.0, 1.0, 1.0]
}

foods['cucumber'] = {
    'name': 'Gurken',
    'img': 'assets/img/cucumber.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Gurke",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 1.0, 1.0,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['potato'] = {
    'name': 'Kartoffel',
    'img': 'assets/img/potato.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kartoffel",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.5, 1.0,   1.0, 1.0, 1.0,  1.0, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'seaTransport'            : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['carrot'] = {
    'name': 'Karotte',
    'img': 'assets/img/carrot.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Karotte",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 0.5, 1.0,   1.0, 1.0, 1.0,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['celery'] = {
    'name': 'Knollensellerie',
    'img': 'assets/img/celery.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Echter_Sellerie#Knollensellerie",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['kohlrabi'] = {
    'name': 'Kohlrabi',
    'img': 'assets/img/kohlrabi.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Kohlrabi",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['leek'] = {
    'name': 'Lauch',
    'img': 'assets/img/leek.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Lauch",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['chard'] = {
    'name': 'Mangold',
    'img': 'assets/img/chard.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Mangold",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 0.0, 0.0]
}

foods['parsnip'] = {
    'name': 'Pastinake',
    'img': 'assets/img/parsnips.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Pastinak",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [1.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  0.0, 1.0, 1.0],
    'landTransport'           : [1.0, 0.0, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  1.0, 1.0, 1.0]
}

foods['smallradish'] = {
    'name': 'Radieschen',
    'img': 'assets/img/small-radish.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Radieschen",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.5, 0.5, 0.5,  0.5, 1.0, 1.0,   1.0, 0.5, 0.5,  0.5, 0.5, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['radish'] = {
    'name': 'Rettich',
    'img': 'assets/img/radish.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Rettiche",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['brusselssprouts'] = {
    'name': 'Rosenkohl',
    'img': 'assets/img/brussels-sprouts.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Rosenkohl",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [1.0, 0.5, 0.0,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  1.0, 1.0, 1.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.0, 0.0, 0.0,   0.0, 0.0, 0.0,  0.5, 0.5, 0.5]
}

foods['beetroot'] = {
    'name': 'Rote Bete',
    'img': 'assets/img/beetroot.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Rote_Bete",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [1.0, 1.0, 1.0,  0.5, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0]
}

foods['purplecabbage'] = {
    'name': 'Rotkohl',
    'img': 'assets/img/purple-cabbage.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Rotkohl",
    'isCommon': 1,
    'type': 'nonFruit',
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.5,   0.5, 0.5, 1.0,  1.0, 1.0, 1.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['asparagus'] = {
    'name': 'Spargel',
    'img': 'assets/img/asparagus.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Gem%C3%BCsespargel",
    'type': 'nonFruit',
    'isCommon': 1,
    'local'                   : [0.0, 0.0, 0.0,  1.0, 1.0, 1.0,   0.0, 0.0, 0.0,  0.0, 0.0, 0.0],
    'landTransport'           : [0.0, 0.0, 0.5,  0.5, 0.5, 0.5,   0.0, 0.0, 0.0,  0.0, 0.0, 0.0],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.0, 0.0, 0.0,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['pointedcabbage'] = {
    'name': 'Spitzkohl',
    'img': 'assets/img/pointed-cabbage.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Spitzkohl",
    'type': 'nonFruit',
    'isCommon': 1,
    'local'                   : [0.0, 0.0, 0.0,  0.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['tomato'] = {
    'name': 'Tomate',
    'img': 'assets/img/tomato.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Tomate",
    'type': 'fruit',
    'isCommon': 1,
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 0.0,   1.0, 1.0, 1.0,  1.0, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5],
    'flightTransport'         : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['whitecabbage'] = {
    'name': 'Weißkohl',
    'img': 'assets/img/white-cabbage.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Wei%C3%9Fkohl",
    'type': 'nonFruit',
    'isCommon': 1,
    'local'                   : [1.0, 1.0, 1.0,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 1.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['savoy'] = {
    'name': 'Wirsing',
    'img': 'assets/img/savoy.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Wirsing",
    'type': 'nonFruit',
    'isCommon': 1,
    'local'                   : [0.5, 0.5, 0.5,  1.0, 1.0, 1.0,   1.0, 1.0, 1.0,  1.0, 1.0, 0.5],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

foods['zucchini'] = {
    'name': 'Zucchini',
    'img': 'assets/img/zucchini.jpg',
    "infoURL": "https://de.wikipedia.org/wiki/Zucchini",
    'type': 'nonFruit',
    'isCommon': 1,
    'local'                   : [0.0, 0.0, 0.0,  0.0, 0.0, 1.0,   1.0, 1.0, 1.0,  1.0, 0.0, 0.0],
    'landTransport'           : [0.5, 0.5, 0.5,  0.5, 0.5, 0.5,   0.5, 0.5, 0.5,  0.5, 0.5, 0.5]
}

json.dump(foods, open("foods.json", "w"))